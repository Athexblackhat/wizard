#!/usr/bin/env python3
"""
                     WIZARD ULTIMATE FUNCTIONS LIBRARY                                         
          All Functions Enhanced with Maximum Power & Capabilities            

"""

import os
import sys
import re
import json
import time
import socket
import ssl
import hashlib
import base64
import random
import string
import threading
import subprocess
import ipaddress
from datetime import datetime
from urllib.parse import urlparse, urljoin, parse_qs, quote, unquote
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict, OrderedDict
from functools import lru_cache
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import WIZARD variables
from var import *

# ============================================================================
# AUTO-INSTALL DEPENDENCIES
# ============================================================================

def install_missing_modules():
    """Install missing third-party modules"""
    required_modules = {
        'requests': 'requests',
        'rich': 'rich',
        'colorama': 'colorama',
        'dnspython': 'dns',
        'whois': 'whois',
        'beautifulsoup4': 'bs4',
        'lxml': 'lxml',
        'Pillow': 'PIL',
        'exifread': 'exifread',
        'cryptography': 'cryptography',
        'python-nmap': 'nmap',
        'paramiko': 'paramiko',
        'scapy': 'scapy',
        'aiohttp': 'aiohttp',
    }
    
    missing = []
    for package, module in required_modules.items():
        try:
            __import__(module)
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"[!] Installing missing modules: {', '.join(missing)}")
        for package in missing:
            os.system(f"pip3 install {package} --quiet")
        print("[✓] Modules installed! Please restart WIZARD.\n")
        return True
    return False

# Check and install on first run
install_missing_modules()

# Now import third-party modules
import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.syntax import Syntax
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich import box
from rich.prompt import Prompt, Confirm
from colorama import Fore, Back, Style, init
import dns.resolver
import whois
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Optional imports (may not be available)
try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

try:
    import exifread
    EXIFREAD_AVAILABLE = True
except ImportError:
    EXIFREAD_AVAILABLE = False

try:
    import nmap
    NMAP_AVAILABLE = True
except ImportError:
    NMAP_AVAILABLE = False

try:
    import paramiko
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

try:
    from scapy.all import *
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

try:
    import aiohttp
    import asyncio
    AIOHTTP_AVAILABLE = True
except ImportError:
    AIOHTTP_AVAILABLE = False

# Initialize colorama
init(autoreset=True)

# Create console instance
console = Console()


class UltimateWizardFunctions:
    """
     ULTIMATE WIZARD FUNCTIONS
    
    All functions enhanced with:
    - Multi-threading support
    - Advanced error handling
    - LRU Caching for performance
    - Beautiful Rich output formatting
    - Extended functionality beyond original
    """
    
    def __init__(self):
        """Initialize with session and settings"""
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': random.choice(USER_AGENTS)
        })
        self.session.verify = VERIFY_SSL
        self.cache = {}
        self.results = defaultdict(dict)
        self.console = Console()
        
    def _random_user_agent(self):
        """Generate random user agent from list"""
        return random.choice(USER_AGENTS)
    
    def _rotate_user_agent(self):
        """Rotate user agent for session"""
        self.session.headers.update({
            'User-Agent': self._random_user_agent()
        })
    
    # ========================================================================
    # TITLE EXTRACTION
    # ========================================================================
    
    @lru_cache(maxsize=100)
    def get_title(self, url):
        """
        Extract page title with multiple fallback methods
        
        Args:
            url: Target URL
            
        Returns:
            str: Page title or error message
        """
        methods = []
        
        try:
            response = self.session.get(url, timeout=DEFAULT_TIMEOUT, verify=VERIFY_SSL)
            html = response.text
            
            # Method 1: HTML title tag
            soup = BeautifulSoup(html, 'html.parser')
            if soup.title and soup.title.string:
                title = soup.title.string.strip()
                if title:
                    methods.append(('HTML Title', title))
            
            # Method 2: Open Graph title
            og_title = soup.find('meta', property='og:title')
            if og_title and og_title.get('content'):
                methods.append(('OG Title', og_title['content'].strip()))
            
            # Method 3: Twitter card title
            twitter_title = soup.find('meta', attrs={'name': 'twitter:title'})
            if twitter_title and twitter_title.get('content'):
                methods.append(('Twitter Title', twitter_title['content'].strip()))
            
            # Method 4: H1 tag
            h1 = soup.find('h1')
            if h1:
                h1_text = h1.get_text().strip()
                if h1_text:
                    methods.append(('H1 Title', h1_text))
            
            # Method 5: Regex fallback
            if not methods:
                regex_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
                if regex_match:
                    methods.append(('Regex Title', regex_match.group(1).strip()))
            
            if methods:
                return methods[0][1]
            
            return "No title found"
            
        except requests.exceptions.Timeout:
            return "Timeout - Site may be slow"
        except requests.exceptions.ConnectionError:
            return "Connection failed"
        except Exception as e:
            return f"Error: {str(e)[:50]}"
    
    def get_title_advanced(self, url):
        """
        Advanced title extraction with confidence scoring
        
        Args:
            url: Target URL
            
        Returns:
            dict: Title information with confidence scores
        """
        result = {
            'url': url,
            'titles': [],
            'best_title': None,
            'confidence': 0
        }
        
        try:
            response = self.session.get(url, timeout=DEFAULT_TIMEOUT, verify=VERIFY_SSL)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            
            titles = []
            
            # HTML Title (highest confidence)
            if soup.title and soup.title.string:
                titles.append(('html_title', soup.title.string.strip(), 100))
            
            # Meta titles (high confidence)
            meta_titles = [
                ('og:title', 'property'),
                ('twitter:title', 'name'),
            ]
            
            for meta_name, attr in meta_titles:
                meta = soup.find('meta', attrs={attr: meta_name})
                if meta and meta.get('content'):
                    titles.append((meta_name, meta['content'].strip(), 80))
            
            # H1 title (medium confidence)
            h1 = soup.find('h1')
            if h1:
                h1_text = h1.get_text().strip()
                if h1_text:
                    titles.append(('h1', h1_text, 60))
            
            # Sort by confidence (highest first)
            titles.sort(key=lambda x: x[2], reverse=True)
            
            result['titles'] = [
                {'source': t[0], 'title': t[1], 'confidence': t[2]} 
                for t in titles
            ]
            result['best_title'] = titles[0][1] if titles else "No title found"
            result['confidence'] = titles[0][2] if titles else 0
            
            return result
            
        except Exception as e:
            result['error'] = str(e)
            return result
    
    # ========================================================================
    # WEB SERVER DETECTION
    # ========================================================================
    
    def detect_web_server(self, url):
        """
        Detect web server with multiple techniques
        
        Args:
            url: Target URL
            
        Returns:
            dict: Server information
        """
        results = {
            'server': None,
            'powered_by': None,
            'technology': [],
            'confidence': 0
        }
        
        try:
            response = self.session.get(url, timeout=DEFAULT_TIMEOUT, verify=VERIFY_SSL)
            headers = response.headers
            
            # Method 1: Server header
            server = headers.get('Server', '')
            if server:
                results['server'] = server
                results['confidence'] += 40
            
            # Method 2: X-Powered-By header
            powered_by = headers.get('X-Powered-By', '')
            if powered_by:
                results['powered_by'] = powered_by
                results['confidence'] += 30
            
            # Method 3: Cookie analysis
            cookies = response.cookies
            tech_indicators = {
                'PHPSESSID': 'PHP',
                'JSESSIONID': 'Java/Tomcat',
                'ASP.NET_SessionId': 'ASP.NET',
                'laravel_session': 'Laravel',
                'wp-settings': 'WordPress'
            }
            
            for cookie_name, technology in tech_indicators.items():
                if cookie_name in cookies:
                    if technology not in results['technology']:
                        results['technology'].append(technology)
                        results['confidence'] += 10
            
            # Method 4: Header pattern analysis
            header_patterns = {
                'nginx': ['nginx', 'NGINX'],
                'apache': ['Apache', 'apache'],
                'iis': ['IIS', 'Microsoft-IIS'],
                'cloudflare': ['cloudflare', 'Cloudflare'],
                'varnish': ['Varnish', 'varnish'],
                'litespeed': ['LiteSpeed', 'litespeed']
            }
            
            headers_str = str(headers).lower()
            for tech, patterns in header_patterns.items():
                for pattern in patterns:
                    if pattern.lower() in headers_str:
                        if tech not in results['technology']:
                            results['technology'].append(tech)
                            results['confidence'] += 15
                            break
            
            # Method 5: HTML fingerprinting
            html = response.text[:2000].lower()
            tech_fingerprints = {
                'nginx': ['nginx', 'nginx/'],
                'apache': ['apache', 'apache/'],
                'iis': ['microsoft-iis', 'iis/'],
                'tomcat': ['apache tomcat', 'tomcat/'],
                'jetty': ['jetty', 'jetty/']
            }
            
            for tech, fingerprints in tech_fingerprints.items():
                for fp in fingerprints:
                    if fp in html:
                        if tech not in results['technology']:
                            results['technology'].append(tech)
                            results['confidence'] += 10
                            break
            
            if not results['server'] and not results['technology']:
                results['server'] = "Could not detect"
            
            return results
            
        except Exception as e:
            return {'error': str(e), 'server': 'Detection failed'}
    
    # ========================================================================
    # CLOUDFLARE DETECTION
    # ========================================================================
    
    def detect_cloudflare(self, url):
        """
        Multi-method Cloudflare detection
        
        Args:
            url: Target URL
            
        Returns:
            dict: Detection results with methods used
        """
        detection_methods = []
        is_cloudflare = False
        
        try:
            response = self.session.get(url, timeout=DEFAULT_TIMEOUT, verify=VERIFY_SSL)
            headers = response.headers
            html = response.text[:5000].lower()
            
            # Method 1: CF-Ray header (most reliable)
            if 'cf-ray' in headers:
                detection_methods.append('CF-Ray header')
                is_cloudflare = True
            
            # Method 2: Server header
            if 'cloudflare' in headers.get('Server', '').lower():
                detection_methods.append('Server header')
                is_cloudflare = True
            
            # Method 3: CF-Cache-Status
            if 'cf-cache-status' in headers:
                detection_methods.append('CF-Cache-Status header')
                is_cloudflare = True
            
            # Method 4: Cloudflare cookies
            cf_cookies = ['__cfduid', 'cf_clearance', '__cf_bm', '__cflb']
            for cookie in cf_cookies:
                if cookie in response.cookies:
                    detection_methods.append(f'Cookie: {cookie}')
                    is_cloudflare = True
                    break
            
            # Method 5: HTML fingerprints
            cf_fingerprints = [
                'cloudflare',
                'cf-browser-verification',
                'cf-chl-bypass',
                'cf-error-code',
                'cf-ray',
                'jschl-answer',
                'attention required! | cloudflare'
            ]
            for fp in cf_fingerprints:
                if fp in html:
                    detection_methods.append(f'HTML: {fp}')
                    is_cloudflare = True
                    break
            
            # Method 6: IP range check
            if not is_cloudflare:
                try:
                    domain = url.replace('http://', '').replace('https://', '').split('/')[0]
                    ip = socket.gethostbyname(domain)
                    for cf_range in CLOUDFLARE_IPS:
                        if ipaddress.ip_address(ip) in ipaddress.ip_network(cf_range):
                            detection_methods.append(f'IP Range: {cf_range}')
                            is_cloudflare = True
                            break
                except:
                    pass
            
            # Method 7: SSL certificate check
            if not is_cloudflare and url.startswith('https'):
                try:
                    domain = url.split('/')[2]
                    cert = ssl.get_server_certificate((domain, 443))
                    if 'Cloudflare' in cert or 'cloudflare' in cert.lower():
                        detection_methods.append('SSL Certificate')
                        is_cloudflare = True
                except:
                    pass
            
            return {
                'detected': is_cloudflare,
                'methods': detection_methods,
                'confidence': min(len(detection_methods) * 15, 100) if is_cloudflare else 0
            }
            
        except Exception as e:
            return {'detected': False, 'error': str(e)[:100]}
    
    # ========================================================================
    # CMS DETECTION
    # ========================================================================
    
    def detect_cms(self, url):
        """
        Simple CMS detection (used by wizard.py)
        
        Args:
            url: Target URL
            
        Returns:
            str: CMS name
        """
        try:
            response = self.session.get(url, timeout=DEFAULT_TIMEOUT, verify=VERIFY_SSL)
            text = response.text.lower()
            
            # WordPress
            if 'wp-content' in text or 'wp-admin' in text or 'wp-includes' in text:
                return "WordPress"
            
            # Joomla
            if 'joomla' in text or '/components/com_' in text:
                return "Joomla"
            
            # Drupal
            if 'drupal' in text or '/sites/default/' in text or '/misc/drupal.js' in text:
                return "Drupal"
            
            # Magento
            if 'magento' in text or '/skin/frontend/' in text:
                return "Magento"
            
            # Shopify
            if 'shopify' in text or 'myshopify.com' in text:
                return "Shopify"
            
            # Wix
            if 'wix.com' in text or '_wix' in text:
                return "Wix"
            
            # Squarespace
            if 'squarespace' in text:
                return "Squarespace"
            
            # Blogger
            if 'blogger' in text or 'blogspot' in text:
                return "Blogger"
            
            # Ghost
            if 'ghost' in text or 'ghost.org' in text:
                return "Ghost"
            
            return "Unknown/None"
            
        except:
            return "Could not detect"
    
    def detect_cms_ultimate(self, url):
        """
        Advanced CMS detection with confidence scoring
        
        Args:
            url: Target URL
            
        Returns:
            dict: Detailed CMS detection results
        """
        cms_signatures = {
            'WordPress': {
                'paths': ['/wp-content/', '/wp-admin/', '/wp-includes/'],
                'meta': ['generator', 'WordPress'],
                'headers': ['X-Powered-By: WordPress'],
                'cookies': ['wp-settings-', 'wordpress_logged_in'],
                'files': ['wp-login.php', 'xmlrpc.php'],
                'weight': 0
            },
            'Joomla': {
                'paths': ['/components/com_', '/modules/mod_', '/templates/'],
                'meta': ['generator', 'Joomla'],
                'headers': ['X-Content-Encoded-By: Joomla'],
                'cookies': ['joomla_user_state'],
                'files': ['administrator/index.php'],
                'weight': 0
            },
            'Drupal': {
                'paths': ['/sites/default/', '/misc/drupal.js', '/modules/'],
                'meta': ['generator', 'Drupal'],
                'headers': ['X-Generator: Drupal'],
                'cookies': ['DRUPAL_UID'],
                'files': ['user/login'],
                'weight': 0
            },
            'Magento': {
                'paths': ['/skin/frontend/', '/media/catalog/'],
                'meta': ['generator', 'Magento'],
                'cookies': ['frontend=', 'adminhtml='],
                'files': ['admin/'],
                'weight': 0
            },
            'Shopify': {
                'paths': ['cdn.shopify.com', 'myshopify.com'],
                'meta': ['generator', 'Shopify'],
                'headers': ['X-Shopify-Stage'],
                'cookies': ['_shopify_'],
                'weight': 0
            },
            'Wix': {
                'paths': ['wix.com', '_wix_'],
                'meta': ['generator', 'Wix.com'],
                'headers': ['X-Wix-Request-Id'],
                'weight': 0
            },
            'Squarespace': {
                'paths': ['squarespace.com', 'static.squarespace.com'],
                'meta': ['generator', 'Squarespace'],
                'weight': 0
            },
            'Laravel': {
                'cookies': ['laravel_session'],
                'weight': 0
            },
            'Django': {
                'cookies': ['csrftoken', 'sessionid'],
                'weight': 0
            },
            'ASP.NET': {
                'headers': ['X-AspNet-Version', 'X-Powered-By: ASP.NET'],
                'cookies': ['ASP.NET_SessionId', '.ASPXAUTH'],
                'weight': 0
            }
        }
        
        try:
            response = self.session.get(url, timeout=DEFAULT_TIMEOUT, verify=VERIFY_SSL)
            html = response.text
            headers = response.headers
            cookies = response.cookies
            
            # Check each CMS
            for cms_name, signature in cms_signatures.items():
                weight = 0
                
                # Check paths in HTML
                if 'paths' in signature:
                    for path in signature['paths']:
                        if path in html:
                            weight += 30
                
                # Check meta tags
                if 'meta' in signature:
                    meta_name, meta_content = signature['meta']
                    if f'name="{meta_name}"' in html.lower() and meta_content.lower() in html.lower():
                        weight += 40
                
                # Check headers
                if 'headers' in signature:
                    for header_pattern in signature['headers']:
                        if ': ' in header_pattern:
                            header_key, header_value = header_pattern.split(': ', 1)
                            if header_key in headers and header_value.lower() in str(headers[header_key]).lower():
                                weight += 25
                
                # Check cookies
                if 'cookies' in signature:
                    cookies_str = str(cookies).lower()
                    for cookie_pattern in signature['cookies']:
                        if cookie_pattern.lower() in cookies_str:
                            weight += 20
                
                # Check specific files
                if 'files' in signature:
                    for file_path in signature['files']:
                        try:
                            file_url = urljoin(url, file_path)
                            file_response = self.session.head(file_url, timeout=5, verify=VERIFY_SSL)
                            if file_response.status_code == 200:
                                weight += 15
                        except:
                            pass
                
                signature['weight'] = weight
            
            # Find best match
            detected_cms = []
            for cms_name, signature in cms_signatures.items():
                if signature['weight'] > 0:
                    detected_cms.append((cms_name, signature['weight']))
            
            detected_cms.sort(key=lambda x: x[1], reverse=True)
            
            if detected_cms and detected_cms[0][1] >= 30:
                return {
                    'cms': detected_cms[0][0],
                    'confidence': detected_cms[0][1],
                    'all_detected': detected_cms[:3],
                    'version': self._detect_cms_version(url, detected_cms[0][0], html)
                }
            
            return {'cms': 'Unknown/Custom', 'confidence': 0, 'all_detected': []}
            
        except Exception as e:
            return {'cms': 'Detection failed', 'error': str(e)[:100]}
    
    def _detect_cms_version(self, url, cms_name, html):
        """Detect version for specific CMS"""
        version = None
        
        try:
            if cms_name == 'WordPress':
                # Method 1: Meta generator
                match = re.search(r'<meta name="generator" content="WordPress (\d+\.\d+\.?\d*)"', html)
                if match:
                    version = match.group(1)
                
                # Method 2: Readme file
                if not version:
                    try:
                        readme = self.session.get(f"{url}/readme.html", timeout=5)
                        match = re.search(r'Version (\d+\.\d+\.?\d*)', readme.text)
                        if match:
                            version = match.group(1)
                    except:
                        pass
                
                # Method 3: RSS feed
                if not version:
                    try:
                        feed = self.session.get(f"{url}/feed/", timeout=5)
                        match = re.search(r'<generator>http://wordpress.org/\?v=(\d+\.\d+\.?\d*)</generator>', feed.text)
                        if match:
                            version = match.group(1)
                    except:
                        pass
            
            elif cms_name == 'Joomla':
                match = re.search(r'<meta name="generator" content="Joomla! (\d+\.\d+\.?\d*)"', html)
                if match:
                    version = match.group(1)
            
            elif cms_name == 'Drupal':
                match = re.search(r'<meta name="generator" content="Drupal (\d+\.\d+\.?\d*)"', html)
                if match:
                    version = match.group(1)
        
        except:
            pass
        
        return version
    
    # ========================================================================
    # ROBOTS.TXT ANALYZER
    # ========================================================================
    
    def check_robots(self, url):
        """
        Simple robots.txt check (used by wizard.py)
        
        Args:
            url: Target URL
            
        Returns:
            str: Status message
        """
        try:
            robots_url = urljoin(url, '/robots.txt')
            response = self.session.get(robots_url, timeout=5, verify=VERIFY_SSL)
            
            if response.status_code == 200:
                lines = response.text.strip().split('\n')
                disallowed = [l for l in lines if 'Disallow' in l]
                if disallowed:
                    return f"Found ({len(disallowed)} disallowed paths)"
                return "Found (empty)"
            return "Not found"
        except:
            return "Not accessible"
    
    def check_robots_txt(self, url):
        """
        Advanced robots.txt analysis
        
        Args:
            url: Target URL
            
        Returns:
            dict: Detailed robots.txt analysis
        """
        result = {
            'exists': False,
            'status_code': None,
            'content': None,
            'disallowed': [],
            'allowed': [],
            'sitemaps': [],
            'crawl_delay': None,
            'user_agents': [],
            'analysis': {}
        }
        
        try:
            robots_url = urljoin(url, '/robots.txt')
            response = self.session.get(robots_url, timeout=DEFAULT_TIMEOUT, verify=VERIFY_SSL)
            
            result['status_code'] = response.status_code
            
            if response.status_code == 200:
                result['exists'] = True
                content = response.text
                result['content'] = content
                
                if not content.strip():
                    result['analysis']['warning'] = 'Robots.txt exists but is empty'
                    return result
                
                # Parse robots.txt
                current_agent = None
                for line in content.split('\n'):
                    line = line.strip()
                    
                    if line.lower().startswith('user-agent:'):
                        current_agent = line.split(':', 1)[1].strip()
                        if current_agent not in result['user_agents']:
                            result['user_agents'].append(current_agent)
                    
                    elif line.lower().startswith('disallow:') and current_agent:
                        path = line.split(':', 1)[1].strip()
                        if path:
                            result['disallowed'].append({
                                'agent': current_agent,
                                'path': path
                            })
                    
                    elif line.lower().startswith('allow:') and current_agent:
                        path = line.split(':', 1)[1].strip()
                        if path:
                            result['allowed'].append({
                                'agent': current_agent,
                                'path': path
                            })
                    
                    elif line.lower().startswith('sitemap:'):
                        sitemap_url = line.split(':', 1)[1].strip()
                        result['sitemaps'].append(sitemap_url)
                    
                    elif line.lower().startswith('crawl-delay:'):
                        try:
                            result['crawl_delay'] = float(line.split(':', 1)[1].strip())
                        except:
                            pass
                
                # Analysis
                result['analysis']['total_disallowed'] = len(result['disallowed'])
                result['analysis']['total_sitemaps'] = len(result['sitemaps'])
                
                # Check for sensitive paths
                sensitive_paths = [
                    '/admin', '/wp-admin', '/administrator',
                    '/login', '/config', '/backup', '/db'
                ]
                found_sensitive = []
                for disallowed in result['disallowed']:
                    for sensitive in sensitive_paths:
                        if sensitive in disallowed['path'].lower():
                            found_sensitive.append(disallowed['path'])
                
                if found_sensitive:
                    result['analysis']['sensitive_paths'] = found_sensitive
                
                # Check if all search engines are blocked
                if '*' in result['user_agents']:
                    all_disallowed = [
                        d['path'] for d in result['disallowed'] 
                        if d['agent'] == '*'
                    ]
                    if '/' in all_disallowed:
                        result['analysis']['warning'] = 'All search engines are blocked from entire site!'
            
            elif response.status_code == 404:
                result['analysis']['warning'] = 'No robots.txt file found'
            else:
                result['analysis']['warning'] = f'Unexpected status code: {response.status_code}'
            
            return result
            
        except Exception as e:
            result['error'] = str(e)[:100]
            return result
    
    # ========================================================================
    # SOCIAL MEDIA EXTRACTOR
    # ========================================================================
    
    def extract_social_links(self, url):
        """
        Extract social media links from page
        
        Args:
            url: Target URL
            
        Returns:
            dict: Social media links by platform
        """
        results = {platform: [] for platform in SOCIAL_PLATFORMS}
        total_links = 0
        
        try:
            response = self.session.get(url, timeout=DEFAULT_TIMEOUT, verify=VERIFY_SSL)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all links
            for element in soup.find_all(['a', 'link', 'script', 'iframe', 'img']):
                link = ''
                if element.name == 'a':
                    link = element.get('href', '')
                elif element.name in ['link', 'script', 'iframe']:
                    link = element.get('src', '')
                elif element.name == 'img':
                    link = element.get('src', '') or element.get('data-src', '')
                
                if link:
                    link_lower = link.lower()
                    for platform, domains in SOCIAL_PLATFORMS.items():
                        for domain in domains:
                            if domain in link_lower:
                                if link not in results[platform]:
                                    results[platform].append(link)
                                    total_links += 1
                                break
            
            return {
                'total_links': total_links,
                'platforms': {k: v for k, v in results.items() if v},
                'platform_count': len([k for k, v in results.items() if v])
            }
            
        except Exception as e:
            return {'error': str(e)[:100], 'total_links': 0}
    
    # ========================================================================
    # LINK EXTRACTOR
    # ========================================================================
    
    def extract_links(self, url):
        """
        Extract and categorize all links from page
        
        Args:
            url: Target URL
            
        Returns:
            dict: Categorized links
        """
        result = {
            'internal': [],
            'external': [],
            'subdomains': [],
            'emails': [],
            'phones': [],
            'files': [],
            'javascript': [],
            'css': [],
            'images': [],
            'total': 0
        }
        
        try:
            domain = urlparse(url).netloc.replace('www.', '')
            
            response = self.session.get(url, timeout=DEFAULT_TIMEOUT, verify=VERIFY_SSL)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract all types of links
            for tag in soup.find_all(['a', 'link', 'script', 'img', 'iframe']):
                if tag.name == 'a':
                    href = tag.get('href', '')
                    if href and not href.startswith('#') and not href.startswith('javascript:'):
                        result['total'] += 1
                        absolute_url = urljoin(url, href)
                        
                        if domain in absolute_url:
                            result['internal'].append(absolute_url)
                        else:
                            result['external'].append(absolute_url)
                        
                        parsed = urlparse(absolute_url)
                        if parsed.netloc.endswith(domain) and parsed.netloc != domain:
                            result['subdomains'].append(absolute_url)
                
                elif tag.name == 'script':
                    src = tag.get('src', '')
                    if src:
                        result['javascript'].append(urljoin(url, src))
                        result['total'] += 1
                
                elif tag.name == 'link':
                    href = tag.get('href', '')
                    rel = tag.get('rel', [])
                    if href and 'stylesheet' in rel:
                        result['css'].append(urljoin(url, href))
                        result['total'] += 1
                
                elif tag.name == 'img':
                    src = tag.get('src', '') or tag.get('data-src', '')
                    if src:
                        result['images'].append(urljoin(url, src))
                        result['total'] += 1
            
            # Remove duplicates
            for key in ['internal', 'external', 'subdomains', 'javascript', 'css', 'images']:
                result[key] = list(set(result[key]))
            
            # Extract emails
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            result['emails'] = list(set(re.findall(email_pattern, response.text)))
            
            # Extract phone numbers
            phone_pattern = r'\+?[\d]{1,3}[-.\s]?\(?[\d]{1,4}\)?[-.\s]?[\d]{1,4}[-.\s]?[\d]{1,9}'
            result['phones'] = list(set(re.findall(phone_pattern, response.text)))
            
            # Find file downloads
            file_extensions = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', 
                             '.zip', '.tar', '.gz', '.sql', '.bak']
            for link in result['internal'] + result['external']:
                for ext in file_extensions:
                    if link.lower().endswith(ext):
                        result['files'].append(link)
                        break
            
            result['files'] = list(set(result['files']))
            
            return result
            
        except Exception as e:
            return {'error': str(e)[:100], 'total': 0}
    
    # ========================================================================
    # MX LOOKUP
    # ========================================================================
    
    def mx_lookup(self, domain):
        """
        MX record lookup with security analysis
        
        Args:
            domain: Target domain
            
        Returns:
            dict: MX records and security info
        """
        result = {
            'mx_records': [],
            'spf_record': None,
            'dmarc_record': None,
            'security_score': 0
        }
        
        domain = domain.replace('www.', '').replace('http://', '').replace('https://', '').split('/')[0]
        
        try:
            # MX Records
            try:
                mx_records = dns.resolver.resolve(domain, 'MX')
                for mx in mx_records:
                    mx_host = str(mx.exchange).rstrip('.')
                    try:
                        mx_ip = socket.gethostbyname(mx_host)
                    except:
                        mx_ip = 'Unknown'
                    
                    result['mx_records'].append({
                        'hostname': mx_host,
                        'preference': mx.preference,
                        'ip': mx_ip
                    })
            except:
                pass
            
            # SPF Record
            try:
                txt_records = dns.resolver.resolve(domain, 'TXT')
                for txt in txt_records:
                    txt_str = str(txt).strip('"')
                    if 'v=spf1' in txt_str:
                        result['spf_record'] = txt_str
                        break
            except:
                pass
            
            # DMARC Record
            try:
                dmarc_records = dns.resolver.resolve(f'_dmarc.{domain}', 'TXT')
                for dmarc in dmarc_records:
                    dmarc_str = str(dmarc).strip('"')
                    if 'v=DMARC1' in dmarc_str:
                        result['dmarc_record'] = dmarc_str
                        break
            except:
                pass
            
            # Calculate security score
            score = 0
            if result['spf_record']:
                score += 40
                if '-all' in result['spf_record']:
                    score += 10  # Hard fail is more secure
            if result['dmarc_record']:
                score += 50
            
            result['security_score'] = min(score, 100)
            
            return result
            
        except Exception as e:
            return {'error': str(e)[:100]}
    
    # ========================================================================
    # CONTENT READER
    # ========================================================================
    
    def read_contents(self, url):
        """
        Read URL contents with multiple fallback methods
        
        Args:
            url: Target URL
            
        Returns:
            str: Page content or None
        """
        # Method 1: requests with SSL verification disabled
        try:
            response = self.session.get(url, timeout=DEFAULT_TIMEOUT, verify=False)
            if response.status_code == 200:
                return response.text
        except:
            pass
        
        # Method 2: requests with SSL verification
        try:
            response = requests.get(url, timeout=DEFAULT_TIMEOUT, verify=True)
            if response.status_code == 200:
                return response.text
        except:
            pass
        
        # Method 3: urllib
        try:
            from urllib.request import urlopen, Request
            req = Request(url, headers={'User-Agent': self._random_user_agent()})
            response = urlopen(req, timeout=DEFAULT_TIMEOUT)
            return response.read().decode('utf-8', errors='ignore')
        except:
            pass
        
        # Method 4: curl command
        try:
            result = subprocess.run(
                ['curl', '-s', '-L', '--insecure', '-m', str(DEFAULT_TIMEOUT), url],
                capture_output=True, text=True, timeout=DEFAULT_TIMEOUT + 5
            )
            if result.returncode == 0 and result.stdout:
                return result.stdout
        except:
            pass
        
        return None
    
    # ========================================================================
    # HTTP HEADERS ANALYZER
    # ========================================================================
    
    def get_http_headers(self, url):
        """
        Get and analyze HTTP headers
        
        Args:
            url: Target URL
            
        Returns:
            dict: Headers with security analysis
        """
        result = {
            'headers': {},
            'security_headers': {},
            'security_score': 0,
            'recommendations': []
        }
        
        try:
            response = self.session.get(url, timeout=DEFAULT_TIMEOUT, verify=VERIFY_SSL)
            result['headers'] = dict(response.headers)
            
            # Check security headers
            for header_name, header_info in SECURITY_HEADERS.items():
                value = response.headers.get(header_name, 'Missing')
                result['security_headers'][header_name] = {
                    'value': value,
                    'recommended': header_info['recommended'],
                    'weight': header_info['weight']
                }
                
                if value != 'Missing':
                    result['security_score'] += header_info['weight']
            
            # Generate recommendations
            if result['security_score'] < 30:
                result['recommendations'].append('Critical: Implement security headers immediately')
            if result['security_headers'].get('Strict-Transport-Security', {}).get('value') == 'Missing':
                result['recommendations'].append('Add HSTS header for HTTPS enforcement')
            if result['security_headers'].get('Content-Security-Policy', {}).get('value') == 'Missing':
                result['recommendations'].append('Implement Content Security Policy')
            if result['security_headers'].get('X-Frame-Options', {}).get('value') == 'Missing':
                result['recommendations'].append('Add X-Frame-Options to prevent clickjacking')
            
            return result
            
        except Exception as e:
            return {'error': str(e)[:100]}
    
    # ========================================================================
    # NETWORK UTILITIES
    # ========================================================================
    
    def get_ip(self, domain):
        """Resolve domain to IP"""
        try:
            return socket.gethostbyname(domain.replace('www.', ''))
        except:
            return None
    
    def is_port_open(self, host, port, timeout=2):
        """Check if a port is open"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            sock.close()
            return result == 0
        except:
            return False
    
    def get_geolocation(self, ip):
        """Get geolocation for an IP address"""
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
            data = response.json()
            if data.get('status') == 'success':
                return {
                    'country': data.get('country'),
                    'city': data.get('city'),
                    'isp': data.get('isp'),
                    'org': data.get('org'),
                    'lat': data.get('lat'),
                    'lon': data.get('lon')
                }
        except:
            pass
        return None
    
    # ========================================================================
    # SECURITY FUNCTIONS
    # ========================================================================
    
    def calculate_hash(self, data, algorithm='sha256'):
        """Calculate hash of data"""
        algorithms = {
            'md5': hashlib.md5,
            'sha1': hashlib.sha1,
            'sha256': hashlib.sha256,
            'sha512': hashlib.sha512
        }
        
        if algorithm in algorithms:
            return algorithms[algorithm](data.encode()).hexdigest()
        return None
    
    def generate_password(self, length=16, complexity='high'):
        """Generate secure password"""
        if complexity == 'low':
            chars = string.ascii_letters + string.digits
        elif complexity == 'medium':
            chars = string.ascii_letters + string.digits + '!@#$%^&*'
        else:
            chars = string.ascii_letters + string.digits + string.punctuation
        
        # Ensure at least one of each type
        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice('!@#$%^&*')
        ]
        
        password += [random.choice(chars) for _ in range(length - 4)]
        random.shuffle(password)
        
        return ''.join(password)
    
    def encode_base64(self, data):
        """Encode data to base64"""
        try:
            return base64.b64encode(data.encode()).decode()
        except:
            return None
    
    def decode_base64(self, data):
        """Decode base64 data"""
        try:
            return base64.b64decode(data.encode()).decode()
        except:
            return None
    
    # ========================================================================
    # REPORT GENERATION
    # ========================================================================
    
    def generate_json_report(self, results, filename=None):
        """Generate JSON report"""
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"wizard_report_{timestamp}.json"
        
        os.makedirs(REPORTS_DIR, exist_ok=True)
        filepath = os.path.join(REPORTS_DIR, filename)
        
        with open(filepath, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        return filepath
    
    def generate_html_report(self, results, filename=None):
        """Generate HTML report"""
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"wizard_report_{timestamp}.html"
        
        os.makedirs(REPORTS_DIR, exist_ok=True)
        filepath = os.path.join(REPORTS_DIR, filename)
        
        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>WIZARD Scan Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background: #1a1a2e; color: #eee; }}
        .header {{ background: #16213e; padding: 20px; border-radius: 10px; text-align: center; }}
        .section {{ background: #0f3460; padding: 15px; margin: 10px 0; border-radius: 5px; }}
        .finding {{ background: #533483; padding: 10px; margin: 5px 0; border-left: 4px solid #e94560; }}
        h1 {{ color: #e94560; }}
        h2 {{ color: #f0a500; }}
        .success {{ color: #00ff00; }}
        .warning {{ color: #ffaa00; }}
        .danger {{ color: #ff0000; }}
        pre {{ background: #1a1a2e; padding: 10px; border-radius: 5px; overflow-x: auto; font-size: 12px; }}
        .footer {{ text-align: center; margin-top: 20px; color: #666; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>WIZARD Framework Scan Report</h1>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p>Version: {WIZARD_VERSION}</p>
    </div>
"""
        
        for section, data in results.items():
            if section != 'target':
                html += f"""
    <div class="section">
        <h2>{section.replace('_', ' ').title()}</h2>
        <pre>{json.dumps(data, indent=2, default=str)}</pre>
    </div>"""
        
        html += """
    <div class="footer">
        <p>Generated by WIZARD Framework - The Ultimate Security Platform</p>
    </div>
</body>
</html>"""
        
        with open(filepath, 'w') as f:
            f.write(html)
        
        return filepath
    
    # ========================================================================
    # DISPLAY UTILITIES
    # ========================================================================
    
    def display_table(self, title, columns, rows):
        """Display data in a formatted table"""
        table = Table(
            title=f"[bold yellow]{title}[/bold yellow]",
            border_style="bright_magenta",
            box=box.ROUNDED
        )
        
        for col in columns:
            table.add_column(col, style="cyan")
        
        for row in rows:
            table.add_row(*[str(item) for item in row])
        
        console.print(table)
    
    def display_success(self, message):
        """Display success message"""
        console.print(f"[bold green]✓ {message}[/bold green]")
    
    def display_error(self, message):
        """Display error message"""
        console.print(f"[bold red]✗ {message}[/bold red]")
    
    def display_warning(self, message):
        """Display warning message"""
        console.print(f"[bold yellow]⚠ {message}[/bold yellow]")
    
    def display_info(self, message):
        """Display info message"""
        console.print(f"[bold cyan]ℹ {message}[/bold cyan]")


# ============================================================================
# CREATE SINGLETON INSTANCE
# ============================================================================

wizard_funcs = UltimateWizardFunctions()

# ============================================================================
# EXPORT LIST
# ============================================================================

__all__ = [
    'UltimateWizardFunctions',
    'wizard_funcs',
]

# ============================================================================
# TEST (if run directly)
# ============================================================================

if __name__ == "__main__":
    console.print("[bold magenta] WIZARD Functions Library[/bold magenta]")
    console.print(f"[cyan]Version: {WIZARD_VERSION}[/cyan]")
    console.print(f"[cyan]Available functions: {len([m for m in dir(UltimateWizardFunctions) if not m.startswith('_')])}[/cyan]")
    console.print("[green]✓ Library loaded successfully![/green]")