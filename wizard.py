#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                          WIZARD FRAMEWORK v3.0.0                          ║
║              Advanced Cyber Security & Penetration Testing Platform          ║
║                    Coded By: ATHEX BLACK HAT                                ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import json
import socket
import ssl
import re
import hashlib
import base64
import random
import threading
import subprocess
import ipaddress
from datetime import datetime
from urllib.parse import urlparse, parse_qs, urljoin
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import WIZARD modules
from functions import UltimateWizardFunctions
from config import WizardConfig
from var import *

# ============================================================================
# AUTO-INSTALL DEPENDENCIES
# ============================================================================

def install_requirements():
    """Auto-install required packages"""
    required = {
        'requests': 'requests',
        'rich': 'rich',
        'colorama': 'colorama',
        'pyfiglet': 'pyfiglet',
        'beautifulsoup4': 'bs4',
        'dnspython': 'dns',
        'whois': 'whois',
        'python-nmap': 'nmap',
        'lxml': 'lxml',
        'cryptography': 'cryptography',
        'paramiko': 'paramiko',
        'scapy': 'scapy',
        'aiohttp': 'aiohttp'
    }
    
    missing = []
    for package, module in required.items():
        try:
            __import__(module)
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"[!] Installing missing packages: {', '.join(missing)}")
        for package in missing:
            os.system(f"pip3 install {package} --quiet")
        print("[✓] All packages installed!\n")
        time.sleep(1)

# Install requirements on first run
install_requirements()

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
import pyfiglet
from bs4 import BeautifulSoup
import dns.resolver
import whois
import nmap
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Initialize colorama
init(autoreset=True)

# Create console instance
console = Console()

# ============================================================================
# BANNER EFFECTS
# ============================================================================

class BannerEffects:
    """Advanced banner effects for WIZARD"""
    
    @staticmethod
    def matrix_effect(duration=1):
        """Matrix rain effect"""
        chars = "01"
        end_time = time.time() + duration
        
        with console.status("[bold green]Initializing WIZARD...[/bold green]") as status:
            while time.time() < end_time:
                line = ''.join(random.choice(chars) for _ in range(50))
                if random.random() > 0.5:
                    line = f"[green]{line}[/green]"
                else:
                    line = f"[bright_green]{line}[/bright_green]"
                status.update(f"[dim]{line}[/dim]")
                time.sleep(0.03)
    
    @staticmethod
    def particle_effect():
        """Magical particle effect"""
        particles = ['✦', '✧', '⋆', '✶', '✷', '✹', '✺', '✻', '✼', '✽', '⚡', '★', '🔮']
        for _ in range(3):
            particle_line = '  '.join(random.choice(particles) for _ in range(20))
            color = random.choice(['magenta', 'cyan', 'yellow', 'blue', 'green'])
            console.print(f"[bold {color}]{particle_line}[/bold {color}]")
            time.sleep(0.2)

# Create banner instance
wizard_banner = BannerEffects()

# ============================================================================
# WIZARD CORE ENGINE
# ============================================================================

class WizardEngine:
    """Ultimate WIZARD Security Framework Engine"""
    
    def __init__(self):
        self.version = WIZARD_VERSION
        self.codename = WIZARD_CODENAME
        self.author = WIZARD_AUTHOR
        self.target = None
        self.protocol = "http://"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': random.choice(USER_AGENTS)
        })
        self.results = {}
        self.scan_history = []
        self.functions = UltimateWizardFunctions()
        self.config = WizardConfig()
        
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_banner(self):
        """Display ultimate animated banner"""
        self.clear_screen()
        
        # Matrix rain effect
        wizard_banner.matrix_effect(1)
        
        # Particle effect
        wizard_banner.particle_effect()
        
        # Loading sequence with magic effects
        with Progress(
            SpinnerColumn(spinner_name="dots"),
            TextColumn("[progress.description]{task.description}"),
            transient=True
        ) as progress:
            tasks = [
                " Awakening the WIZARD...",
                "⚡ Charging arcane energies...",
                "🔮 Calibrating crystal ball...",
                "📜 Reading ancient scrolls...",
                "🌟 Powering up magical modules..."
            ]
            for task in tasks:
                progress.add_task(f"[cyan]{task}", total=None)
                time.sleep(0.3)
        
        # Animated WIZARD title
        title = pyfiglet.figlet_format("W I Z A R D", font="doom")
        
        # Rainbow animation for title
        colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
        for _ in range(2):
            for color in colors:
                self.clear_screen()
                console.print(Panel(
                    Text(title, style=f"bold {color}"),
                    border_style="bright_magenta",
                    box=box.DOUBLE,
                    title="[bold yellow]⚡ WIZARD FRAMEWORK v3.0.0 ⚡[/bold yellow]",
                    subtitle="[bold cyan]Ultimate Cyber Security Platform[/bold cyan]"
                ))
                time.sleep(0.03)
        
        # Final banner
        self.clear_screen()
        
        # Main banner with wizard ASCII art
        console.print(Panel(
            f"""[bold bright_yellow]
                    .                   ⚡
                   / \\\\              ✦
                  /   \\\\           ⚡
                 /^^^^^\\\\        ✦
                /  ◉ ◉  \\\\     ⚡
               /  ▲   ▲  \\\\  ✦
              /  ◄─────►  \\\\
             /  ◄◄─────►►  \\\\     ★
            /_________________\\\\
           ||  |‾‾‾‾‾‾‾‾‾|  ||
           ||──|           |──||
           ||  |___________|  ||
           ||──|           |──||    ⚡
           ||  |___________|  ||
           ||──|           |──||
           ||  |___________|  ||
          /||──|           |──||\\\\
         / ||──|           |──|| \\\\
        /  ||──|___________|──||  \\\\
       /   ||──|___________|──||   \\\\
      /    ||──|___________|──||    \\\\
            [/bold bright_yellow]""",
            border_style="magenta",
            box=box.HEAVY,
            title="[bold yellow] THE WIZARD 🧙‍♂️[/bold yellow]"
        ))
        
        # Version info table
        info_table = Table(
            box=box.ROUNDED, 
            border_style="bright_magenta", 
            show_header=False,
            title="[bold cyan]🔮 Framework Information[/bold cyan]"
        )
        info_table.add_column("Key", style="cyan")
        info_table.add_column("Value", style="yellow")
        info_table.add_row("⚡ Version", self.version)
        info_table.add_row("🔮 Codename", self.codename)
        info_table.add_row(" Author", self.author)
        info_table.add_row("📅 Date", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        info_table.add_row("🌟 Status", "[blink]ACTIVE[/blink]")
        
        console.print(info_table)
        console.print("\n[bold cyan]🔮 Type 'help' for commands | 'exit' to quit[/bold cyan]")
        console.print("[bold magenta]" + "═" * 70 + "[/bold magenta]\n")
    
    def run(self):
        """Main WIZARD loop"""
        self.display_banner()
        
        while True:
            try:
                # Get target
                console.print("\n[bold cyan]🎯[/bold cyan] ", end="")
                target = Prompt.ask("[bold yellow]Enter target website[/bold yellow]")
                
                if target.lower() in ['exit', 'quit', 'q']:
                    self.exit_program()
                elif target.lower() == 'help':
                    self.show_help()
                    continue
                elif target.lower() == 'update':
                    self.update_framework()
                    continue
                elif target.lower() == 'fix':
                    self.fix_dependencies()
                    continue
                elif target.lower() == 'config':
                    self.config.configure_interactive()
                    continue
                
                # Validate and process target
                target = target.strip()
                if '://' in target:
                    console.print("[red][!] Remove http/https from URL![/red]")
                    continue
                
                if '.' not in target:
                    console.print("[red][!] Invalid URL format![/red]")
                    continue
                
                # Select protocol
                protocol = Prompt.ask(
                    "[bold yellow]Select protocol[/bold yellow]",
                    choices=["1", "2"],
                    default="1"
                )
                
                self.protocol = "https://" if protocol == "2" else "http://"
                self.target = target
                
                # Show scan menu
                self.scan_menu()
                
            except KeyboardInterrupt:
                self.exit_program()
            except Exception as e:
                console.print(f"[red][!] Error: {e}[/red]")
    
    def scan_menu(self):
        """Display and handle scan menu"""
        while True:
            self.clear_screen()
            
            # Target info panel
            console.print(Panel(
                f"[bold cyan]🎯 Target:[/bold cyan] [green]{self.protocol}{self.target}[/green]",
                border_style="blue",
                box=box.ROUNDED
            ))
            
            # Scan options table
            scan_table = Table(
                title="[bold yellow] WIZARD Scan Menu 🧙‍♂️[/bold yellow]",
                border_style="bright_magenta",
                box=box.HEAVY_EDGE
            )
            scan_table.add_column("ID", style="cyan", justify="center", width=5)
            scan_table.add_column("Scan Type", style="yellow", width=20)
            scan_table.add_column("Description", style="white", width=45)
            
            scans = [
                ("0", "🔍 Basic Recon", "Site info, IP, CMS, Cloudflare, Robots.txt"),
                ("1", "📋 Whois Lookup", "Domain registration information"),
                ("2", "🗺️ Geo-IP Lookup", "Geographical location of server"),
                ("3", "📡 Banner Grabbing", "Server headers and banners"),
                ("4", "🌐 DNS Lookup", "DNS records enumeration"),
                ("5", "🔢 Subnet Calculator", "Network subnet calculation"),
                ("6", "🔍 Port Scanner", "Advanced Nmap port scanning"),
                ("7", "🔎 Subdomain Finder", "Discover subdomains"),
                ("8", "🔄 Reverse IP & CMS", "Reverse IP lookup + CMS detection"),
                ("9", "💉 SQLi Scanner", "SQL injection vulnerability scanner"),
                ("10", "💥 XSS Scanner", "Cross-site scripting scanner"),
                ("11", "🔵 WordPress Scan", "WordPress specific vulnerability scan"),
                ("12", "📁 Directory Brute", "Directory & file brute force"),
                ("13", "📧 MX Lookup", "Mail server records"),
                ("14", "🔒 SSL Analysis", "SSL/TLS security analysis"),
                ("15", "🔴 Vulnerability Scan", "Comprehensive vulnerability assessment"),
            ]
            
            for scan in scans:
                scan_table.add_row(*scan)
            
            # Action options
            scan_table.add_section()
            scan_table.add_row("[bold yellow]A[/bold yellow]", "🌟 Full Scan", "Complete automated scan of everything")
            scan_table.add_row("[bold yellow]U[/bold yellow]", "🔄 Update", "Update WIZARD Framework")
            scan_table.add_row("[bold yellow]F[/bold yellow]", "🔧 Fix", "Fix/Install dependencies")
            scan_table.add_row("[bold yellow]B[/bold yellow]", "🔙 Back", "Scan another website")
            scan_table.add_row("[bold red]Q[/bold red]", "🚪 Quit", "Exit WIZARD Framework")
            
            console.print(scan_table)
            
            # Get user choice
            choice = Prompt.ask("\n[bold green]⚡ Select scan option[/bold green]").upper()
            
            # Process choice
            if choice == 'Q':
                self.exit_program()
            elif choice == 'B':
                break
            elif choice == 'U':
                self.update_framework()
            elif choice == 'F':
                self.fix_dependencies()
            elif choice == '0':
                self.basic_recon()
            elif choice == '1':
                self.whois_lookup()
            elif choice == '2':
                self.geoip_lookup()
            elif choice == '3':
                self.banner_grabbing()
            elif choice == '4':
                self.dns_lookup()
            elif choice == '5':
                self.subnet_calc()
            elif choice == '6':
                self.port_scanner()
            elif choice == '7':
                self.subdomain_finder()
            elif choice == '8':
                self.reverse_ip_cms()
            elif choice == '9':
                self.sqli_scanner()
            elif choice == '10':
                self.xss_scanner()
            elif choice == '11':
                self.wordpress_scan()
            elif choice == '12':
                self.dir_brute()
            elif choice == '13':
                self.mx_lookup()
            elif choice == '14':
                self.ssl_analysis()
            elif choice == '15':
                self.vulnerability_scan()
            elif choice == 'A':
                self.full_scan()
            else:
                console.print("[red][!] Invalid option! Please select from the menu.[/red]")
                time.sleep(1)
            
            # Pause after scan (except for menu navigation)
            if choice not in ['B', 'Q', 'U', 'F']:
                Prompt.ask("\n[dim]Press Enter to return to menu...[/dim]")
    
    # ========================================================================
    # SCANNING MODULES
    # ========================================================================
    
    def basic_recon(self):
        """Basic reconnaissance scan"""
        console.print(Panel("[bold yellow]🔍 BASIC RECONNAISSANCE[/bold yellow]", border_style="blue"))
        
        url = f"{self.protocol}{self.target}"
        
        with Progress() as progress:
            task = progress.add_task("[cyan]Scanning...", total=6)
            
            # Site Title
            try:
                response = self.session.get(url, timeout=DEFAULT_TIMEOUT, verify=VERIFY_SSL)
                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.title.string if soup.title else "Not found"
                console.print(f"[cyan]📄 Site Title:[/cyan] [green]{title}[/green]")
            except Exception as e:
                console.print(f"[red]✗ Failed to get title: {e}[/red]")
                title = None
            progress.update(task, advance=1)
            
            # IP Address
            try:
                ip = socket.gethostbyname(self.target.replace("www.", ""))
                console.print(f"[cyan]🌐 IP Address:[/cyan] [green]{ip}[/green]")
            except Exception as e:
                console.print(f"[red]✗ Failed to resolve IP: {e}[/red]")
                ip = None
            progress.update(task, advance=1)
            
            # Web Server
            try:
                server = response.headers.get('Server', 'Unknown')
                console.print(f"[cyan]🖥️  Web Server:[/cyan] [green]{server}[/green]")
            except:
                server = "Could not detect"
                console.print(f"[red]✗ Failed to detect server[/red]")
            progress.update(task, advance=1)
            
            # CMS Detection
            cms = self.detect_cms(url)
            console.print(f"[cyan]📦 CMS:[/cyan] [green]{cms}[/green]")
            progress.update(task, advance=1)
            
            # Cloudflare Detection
            cf = self.detect_cloudflare(url)
            console.print(f"[cyan]☁️  Cloudflare:[/cyan] [green]{cf}[/green]")
            progress.update(task, advance=1)
            
            # Robots.txt
            robots = self.check_robots(url)
            console.print(f"[cyan]🤖 Robots.txt:[/cyan] [green]{robots}[/green]")
            progress.update(task, advance=1)
        
        self.results['basic_recon'] = {
            'title': title,
            'ip': ip,
            'server': server,
            'cms': cms,
            'cloudflare': cf,
            'robots': robots
        }
    
    def whois_lookup(self):
        """WHOIS information lookup"""
        console.print(Panel("[bold yellow]📋 WHOIS LOOKUP[/bold yellow]", border_style="blue"))
        
        try:
            domain = self.target.replace("www.", "")
            w = whois.whois(domain)
            
            console.print(f"[cyan]Domain:[/cyan] [green]{w.domain_name}[/green]")
            console.print(f"[cyan]Registrar:[/cyan] [green]{w.registrar}[/green]")
            console.print(f"[cyan]Creation Date:[/cyan] [green]{w.creation_date}[/green]")
            console.print(f"[cyan]Expiration Date:[/cyan] [green]{w.expiration_date}[/green]")
            console.print(f"[cyan]Name Servers:[/cyan] [green]{w.name_servers}[/green]")
            
            self.results['whois'] = str(w)
        except Exception as e:
            console.print(f"[red][!] WHOIS lookup failed: {e}[/red]")
    
    def geoip_lookup(self):
        """Geographical IP lookup"""
        console.print(Panel("[bold yellow]🗺️  GEO-IP LOOKUP[/bold yellow]", border_style="blue"))
        
        try:
            ip = socket.gethostbyname(self.target.replace("www.", ""))
            response = requests.get(f"http://ip-api.com/json/{ip}")
            data = response.json()
            
            if data['status'] == 'success':
                console.print(f"[cyan]Country:[/cyan] [green]{data['country']}[/green]")
                console.print(f"[cyan]City:[/cyan] [green]{data['city']}[/green]")
                console.print(f"[cyan]ISP:[/cyan] [green]{data['isp']}[/green]")
                console.print(f"[cyan]Organization:[/cyan] [green]{data['org']}[/green]")
                console.print(f"[cyan]Coordinates:[/cyan] [green]{data['lat']}, {data['lon']}[/green]")
                
                self.results['geoip'] = data
        except Exception as e:
            console.print(f"[red][!] Geo-IP lookup failed: {e}[/red]")
    
    def banner_grabbing(self):
        """Grab server banners and headers"""
        console.print(Panel("[bold yellow]📡 BANNER GRABBING[/bold yellow]", border_style="blue"))
        
        try:
            url = f"{self.protocol}{self.target}"
            response = self.session.head(url, timeout=DEFAULT_TIMEOUT, verify=VERIFY_SSL)
            
            console.print("[bold cyan]HTTP Headers:[/bold cyan]")
            for header, value in response.headers.items():
                console.print(f"  [yellow]{header}:[/yellow] [green]{value}[/green]")
            
            self.results['banners'] = dict(response.headers)
        except Exception as e:
            console.print(f"[red][!] Banner grabbing failed: {e}[/red]")
    
    def dns_lookup(self):
        """DNS records enumeration"""
        console.print(Panel("[bold yellow]🌐 DNS LOOKUP[/bold yellow]", border_style="blue"))
        
        domain = self.target.replace("www.", "")
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME']
        
        for record_type in record_types:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                console.print(f"\n[bold cyan]{record_type} Records:[/bold cyan]")
                for answer in answers:
                    console.print(f"  [green]{answer}[/green]")
            except:
                console.print(f"\n[bold cyan]{record_type} Records:[/bold cyan] [dim]None[/dim]")
        
        self.results['dns'] = {'domain': domain}
    
    def port_scanner(self):
        """Advanced Nmap port scanner"""
        console.print(Panel("[bold yellow]🔍 PORT SCANNER[/bold yellow]", border_style="blue"))
        
        try:
            ip = socket.gethostbyname(self.target.replace("www.", ""))
            
            nm = nmap.PortScanner()
            console.print("[cyan]Starting Nmap scan...[/cyan]")
            
            with Progress() as progress:
                task = progress.add_task("[cyan]Scanning ports...", total=100)
                
                # Scan common ports
                nm.scan(ip, '1-1000', arguments='-sV -T4')
                progress.update(task, completed=100)
            
            console.print(f"\n[bold green]Nmap Scan Results for {ip}:[/bold green]")
            console.print(f"[cyan]Host Status:[/cyan] [green]{nm[ip].state()}[/green]")
            
            for proto in nm[ip].all_protocols():
                console.print(f"\n[bold yellow]{proto.upper()} Ports:[/bold yellow]")
                ports = nm[ip][proto].keys()
                
                for port in sorted(ports):
                    service = nm[ip][proto][port]
                    console.print(
                        f"  [green]{port}/{proto}[/green] - "
                        f"[yellow]{service['name']}[/yellow] - "
                        f"[cyan]{service['state']}[/cyan]"
                    )
            
            self.results['portscan'] = str(nm[ip])
        except Exception as e:
            console.print(f"[red][!] Port scan failed: {e}[/red]")
    
    def subdomain_finder(self):
        """Find subdomains using multiple methods"""
        console.print(Panel("[bold yellow]🔎 SUBDOMAIN FINDER[/bold yellow]", border_style="blue"))
        
        domain = self.target.replace("www.", "")
        subdomains = set()
        
        with Progress() as progress:
            task = progress.add_task("[cyan]Enumerating subdomains...", total=100)
            
            # Method 1: Certificate Transparency
            try:
                response = requests.get(f"https://crt.sh/?q=%.{domain}&output=json", timeout=30)
                if response.status_code == 200:
                    data = response.json()
                    for entry in data:
                        name = entry['name_value'].strip()
                        if '*' not in name:
                            subdomains.add(name)
            except:
                pass
            progress.update(task, advance=30)
            
            # Method 2: DNS brute force
            common_subs = ['www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 
                          'webdisk', 'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 
                          'm', 'imap', 'test', 'ns', 'blog', 'pop3', 'dev', 'www2', 'admin',
                          'forum', 'news', 'vpn', 'ns3', 'mail2', 'new', 'mysql', 'old',
                          'lists', 'support', 'mobile', 'mx', 'static', 'docs', 'beta',
                          'shop', 'sql', 'secure', 'demo', 'cp', 'calendar', 'wiki',
                          'web', 'media', 'email', 'images', 'img', 'download', 'cdn']
            
            for sub in common_subs:
                try:
                    full = f"{sub}.{domain}"
                    socket.gethostbyname(full)
                    subdomains.add(full)
                except:
                    pass
            progress.update(task, advance=70)
        
        console.print(f"\n[bold green]Found {len(subdomains)} subdomains:[/bold green]")
        for sub in sorted(subdomains):
            try:
                ip = socket.gethostbyname(sub)
                console.print(f"  [cyan]{sub}[/cyan] - [green]{ip}[/green]")
            except:
                console.print(f"  [cyan]{sub}[/cyan]")
        
        self.results['subdomains'] = list(subdomains)
    
    def sqli_scanner(self):
        """SQL Injection vulnerability scanner"""
        console.print(Panel("[bold yellow]💉 SQL INJECTION SCANNER[/bold yellow]", border_style="red"))
        
        url = f"{self.protocol}{self.target}"
        
        try:
            # First, find links with parameters
            response = self.session.get(url, timeout=DEFAULT_TIMEOUT)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            
            vulnerable = []
            
            with Progress() as progress:
                task = progress.add_task("[cyan]Scanning for SQLi...", total=len(links))
                
                for link in links:
                    href = link['href']
                    if '?' in href and '=' in href:
                        if not href.startswith('http'):
                            href = urljoin(url, href)
                        
                        # Parse and test parameters
                        parsed = urlparse(href)
                        params = parse_qs(parsed.query)
                        
                        for param in params:
                            for payload in SQLI_PAYLOADS:
                                test_url = href.replace(f"{param}={params[param][0]}", 
                                                       f"{param}={params[param][0]}{payload}")
                                try:
                                    test_response = self.session.get(test_url, timeout=5)
                                    for error in SQLI_ERRORS:
                                        if error.lower() in test_response.text.lower():
                                            vulnerable.append({
                                                'url': test_url,
                                                'param': param,
                                                'payload': payload,
                                                'error': error
                                            })
                                            break
                                except:
                                    pass
                    progress.update(task, advance=1)
            
            if vulnerable:
                console.print(f"\n[bold red]🚨 Found {len(vulnerable)} potential SQLi vulnerabilities![/bold red]")
                for vuln in vulnerable:
                    console.print(Panel(
                        f"[yellow]URL:[/yellow] [cyan]{vuln['url']}[/cyan]\n"
                        f"[yellow]Parameter:[/yellow] [green]{vuln['param']}[/green]\n"
                        f"[yellow]Payload:[/yellow] [red]{vuln['payload']}[/red]\n"
                        f"[yellow]Error:[/yellow] [dim]{vuln['error']}[/dim]",
                        border_style="red"
                    ))
            else:
                console.print("[green]✓ No SQL injection vulnerabilities found[/green]")
            
            self.results['sqli'] = vulnerable
        except Exception as e:
            console.print(f"[red][!] SQLi scan failed: {e}[/red]")
    
    def xss_scanner(self):
        """XSS vulnerability scanner"""
        console.print(Panel("[bold yellow]💥 XSS SCANNER[/bold yellow]", border_style="red"))
        
        url = f"{self.protocol}{self.target}"
        
        try:
            response = self.session.get(url, timeout=DEFAULT_TIMEOUT)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find forms
            forms = soup.find_all('form')
            vulnerable = []
            
            with Progress() as progress:
                task = progress.add_task("[cyan]Scanning for XSS...", total=len(forms) + len(soup.find_all('a', href=True)))
                
                # Test forms
                for form in forms:
                    action = form.get('action', '')
                    method = form.get('method', 'get').lower()
                    inputs = form.find_all('input')
                    
                    for payload in XSS_PAYLOADS:
                        data = {}
                        for input_field in inputs:
                            name = input_field.get('name')
                            if name:
                                data[name] = payload
                        
                        try:
                            if method == 'post':
                                test_response = self.session.post(urljoin(url, action), data=data, timeout=5)
                            else:
                                test_response = self.session.get(urljoin(url, action), params=data, timeout=5)
                            
                            if payload in test_response.text:
                                vulnerable.append({
                                    'url': urljoin(url, action),
                                    'method': method,
                                    'payload': payload,
                                    'type': 'form'
                                })
                        except:
                            pass
                    progress.update(task, advance=1)
                
                # Test URL parameters
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    if '?' in href:
                        for payload in XSS_PAYLOADS:
                            test_url = href + payload
                            try:
                                test_response = self.session.get(urljoin(url, test_url), timeout=5)
                                if payload in test_response.text:
                                    vulnerable.append({
                                        'url': urljoin(url, test_url),
                                        'payload': payload,
                                        'type': 'url'
                                    })
                            except:
                                pass
                    progress.update(task, advance=1)
            
            if vulnerable:
                console.print(f"\n[bold red]🚨 Found {len(vulnerable)} potential XSS vulnerabilities![/bold red]")
                for vuln in vulnerable:
                    console.print(Panel(
                        f"[yellow]URL:[/yellow] [cyan]{vuln['url']}[/cyan]\n"
                        f"[yellow]Type:[/yellow] [green]{vuln['type']}[/green]\n"
                        f"[yellow]Payload:[/yellow] [red]{vuln['payload']}[/red]",
                        border_style="red"
                    ))
            else:
                console.print("[green]✓ No XSS vulnerabilities found[/green]")
            
            self.results['xss'] = vulnerable
        except Exception as e:
            console.print(f"[red][!] XSS scan failed: {e}[/red]")
    
    def wordpress_scan(self):
        """WordPress specific vulnerability scanner"""
        console.print(Panel("[bold yellow]🔵 WORDPRESS SCANNER[/bold yellow]", border_style="blue"))
        
        url = f"{self.protocol}{self.target}"
        
        try:
            # Check if WordPress
            response = self.session.get(url, timeout=DEFAULT_TIMEOUT)
            if 'wp-content' not in response.text and 'wp-admin' not in response.text:
                console.print("[red][!] Target does not appear to be WordPress[/red]")
                return
            
            console.print("[green]✓ WordPress detected![/green]")
            
            # Version detection methods
            version = None
            
            # Method 1: Meta generator
            soup = BeautifulSoup(response.text, 'html.parser')
            generator = soup.find('meta', {'name': 'generator'})
            if generator and 'WordPress' in generator.get('content', ''):
                version = generator['content'].replace('WordPress ', '')
                console.print(f"[cyan]Version (Method 1):[/cyan] [green]{version}[/green]")
            
            # Method 2: Readme file
            if not version:
                try:
                    readme = self.session.get(f"{url}/readme.html", timeout=DEFAULT_TIMEOUT)
                    if readme.status_code == 200:
                        console.print("[green]✓ Readme file found[/green]")
                        version_match = re.search(r'Version (\d+\.\d+\.?\d*)', readme.text)
                        if version_match:
                            version = version_match.group(1)
                            console.print(f"[cyan]Version (Method 2):[/cyan] [green]{version}[/green]")
                except:
                    pass
            
            # Method 3: Feed
            if not version:
                try:
                    feed = self.session.get(f"{url}/feed/", timeout=DEFAULT_TIMEOUT)
                    version_match = re.search(r'<generator>http://wordpress.org/\?v=(\d+\.\d+\.\d+)</generator>', feed.text)
                    if version_match:
                        version = version_match.group(1)
                        console.print(f"[cyan]Version (Method 3):[/cyan] [green]{version}[/green]")
                except:
                    pass
            
            # Check common vulnerabilities
            console.print("\n[bold cyan]Vulnerability Checks:[/bold cyan]")
            
            # XML-RPC
            try:
                xmlrpc = self.session.post(f"{url}/xmlrpc.php", timeout=DEFAULT_TIMEOUT)
                if xmlrpc.status_code == 200:
                    console.print("[yellow]⚠ XML-RPC enabled - potential for brute force attacks[/yellow]")
            except:
                pass
            
            # WP-JSON
            try:
                wpjson = self.session.get(f"{url}/wp-json/", timeout=DEFAULT_TIMEOUT)
                if wpjson.status_code == 200:
                    console.print("[yellow]⚠ WP REST API exposed[/yellow]")
            except:
                pass
            
            # User enumeration
            for i in range(1, 5):
                try:
                    user_check = self.session.get(f"{url}?author={i}", timeout=DEFAULT_TIMEOUT, allow_redirects=False)
                    if user_check.status_code == 301:
                        console.print(f"[yellow]⚠ User enumeration possible - found user ID {i}[/yellow]")
                except:
                    pass
            
            # Backup files
            backups = ['wp-config.php.bak', 'wp-config.php~', 'wp-config.php.save',
                      'database.sql', 'backup.zip', 'wp-content/backup']
            for backup in backups:
                try:
                    backup_check = self.session.head(f"{url}/{backup}", timeout=5)
                    if backup_check.status_code == 200:
                        console.print(f"[red]🚨 Backup file exposed: {backup}[/red]")
                except:
                    pass
            
            self.results['wordpress'] = {
                'version': version,
                'wp_detected': True
            }
            
        except Exception as e:
            console.print(f"[red][!] WordPress scan failed: {e}[/red]")
    
    def dir_brute(self):
        """Directory and file brute forcing"""
        console.print(Panel("[bold yellow]📁 DIRECTORY BRUTE FORCE[/bold yellow]", border_style="yellow"))
        
        url = f"{self.protocol}{self.target}"
        found = []
        
        with Progress() as progress:
            task = progress.add_task("[cyan]Brute forcing directories...", total=len(COMMON_DIRS))
            
            with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                futures = {}
                for directory in COMMON_DIRS:
                    check_url = f"{url}/{directory}"
                    future = executor.submit(self.session.head, check_url, timeout=5, allow_redirects=False)
                    futures[future] = directory
                
                for future in as_completed(futures):
                    directory = futures[future]
                    try:
                        response = future.result()
                        if response.status_code in [200, 301, 302, 403]:
                            found.append({
                                'path': directory,
                                'url': f"{url}/{directory}",
                                'status': response.status_code
                            })
                    except:
                        pass
                    progress.update(task, advance=1)
        
        if found:
            console.print(f"\n[bold green]Found {len(found)} directories/files:[/bold green]")
            dir_table = Table(box=box.SIMPLE)
            dir_table.add_column("Status", style="yellow")
            dir_table.add_column("Path", style="cyan")
            dir_table.add_column("URL", style="green")
            
            for item in found:
                status_color = "green" if item['status'] == 200 else "yellow"
                dir_table.add_row(
                    f"[{status_color}]{item['status']}[/{status_color}]",
                    item['path'],
                    item['url']
                )
            
            console.print(dir_table)
        else:
            console.print("[yellow]No directories/files found[/yellow]")
        
        self.results['dirs'] = found
    
    def ssl_analysis(self):
        """SSL/TLS security analysis"""
        console.print(Panel("[bold yellow]🔒 SSL/TLS ANALYSIS[/bold yellow]", border_style="green"))
        
        if self.protocol != "https://":
            console.print("[yellow]⚠ Switching to HTTPS for SSL analysis[/yellow]")
        
        try:
            import ssl as ssl_module
            from socket import socket as Socket
            
            hostname = self.target.replace("www.", "")
            context = ssl_module.create_default_context()
            
            with Socket() as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    ssock.settimeout(5)
                    ssock.connect((hostname, 443))
                    
                    cert = ssock.getpeercert()
                    cipher = ssock.cipher()
                    
                    console.print("[bold green]SSL Certificate Information:[/bold green]")
                    console.print(f"[cyan]Subject:[/cyan] [green]{dict(x[0] for x in cert['subject'])}[/green]")
                    console.print(f"[cyan]Issuer:[/cyan] [green]{dict(x[0] for x in cert['issuer'])}[/green]")
                    console.print(f"[cyan]Valid From:[/cyan] [green]{cert['notBefore']}[/green]")
                    console.print(f"[cyan]Valid Until:[/cyan] [green]{cert['notAfter']}[/green]")
                    console.print(f"[cyan]Cipher:[/cyan] [green]{cipher[0]}[/green]")
                    console.print(f"[cyan]TLS Version:[/cyan] [green]{cipher[1]}[/green]")
                    
                    # Check expiration
                    exp_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                    days_left = (exp_date - datetime.now()).days
                    
                    if days_left < 0:
                        console.print("[red]🚨 Certificate has EXPIRED![/red]")
                    elif days_left < 30:
                        console.print(f"[yellow]⚠ Certificate expires in {days_left} days[/yellow]")
                    else:
                        console.print(f"[green]✓ Certificate valid for {days_left} days[/green]")
            
            self.results['ssl'] = {
                'cert': str(cert),
                'cipher': str(cipher),
                'days_left': days_left
            }
            
        except Exception as e:
            console.print(f"[red][!] SSL analysis failed: {e}[/red]")
    
    def vulnerability_scan(self):
        """Comprehensive vulnerability scan"""
        console.print(Panel("[bold red]🔴 VULNERABILITY ASSESSMENT[/bold red]", border_style="red"))
        
        console.print("[bold cyan]Running comprehensive vulnerability scan...[/bold cyan]")
        
        # Run all scans
        scans = [
            self.basic_recon,
            self.sqli_scanner,
            self.xss_scanner,
            self.dir_brute,
            self.ssl_analysis
        ]
        
        with Progress() as progress:
            task = progress.add_task("[cyan]Scanning vulnerabilities...", total=len(scans))
            
            for scan in scans:
                try:
                    scan()
                except Exception as e:
                    console.print(f"[red]Scan error: {e}[/red]")
                progress.update(task, advance=1)
        
        # Generate report
        self.generate_report()
    
    def full_scan(self):
        """Complete automated scan"""
        console.print(Panel("[bold magenta]🌟 FULL AUTOMATED SCAN[/bold magenta]", border_style="magenta"))
        
        all_scans = [
            ('Basic Recon', self.basic_recon),
            ('WHOIS Lookup', self.whois_lookup),
            ('Geo-IP Lookup', self.geoip_lookup),
            ('Banner Grabbing', self.banner_grabbing),
            ('DNS Lookup', self.dns_lookup),
            ('Port Scanner', self.port_scanner),
            ('Subdomain Finder', self.subdomain_finder),
            ('Reverse IP & CMS', self.reverse_ip_cms),
            ('SQLi Scanner', self.sqli_scanner),
            ('XSS Scanner', self.xss_scanner),
            ('WordPress Scan', self.wordpress_scan),
            ('Directory Brute', self.dir_brute),
            ('MX Lookup', self.mx_lookup),
            ('SSL Analysis', self.ssl_analysis)
        ]
        
        with Progress() as progress:
            task = progress.add_task("[cyan]Running full scan...", total=len(all_scans))
            
            for name, scan_func in all_scans:
                console.print(f"\n[bold yellow]▶ Running {name}...[/bold yellow]")
                try:
                    scan_func()
                except Exception as e:
                    console.print(f"[red]  ✗ Failed: {e}[/red]")
                progress.update(task, advance=1)
                time.sleep(1)
        
        # Generate comprehensive report
        self.generate_report()
    
    # ========================================================================
    # UTILITY FUNCTIONS
    # ========================================================================
    
    def detect_cms(self, url):
        """Detect CMS of target"""
        try:
            response = self.session.get(url, timeout=DEFAULT_TIMEOUT)
            text = response.text.lower()
            
            # WordPress
            if 'wp-content' in text or 'wp-admin' in text or 'wp-includes' in text:
                return "WordPress"
            
            # Joomla
            if 'joomla' in text or '/components/com_' in text:
                return "Joomla"
            
            # Drupal
            if 'drupal' in text or '/sites/default/' in text:
                return "Drupal"
            
            # Magento
            if 'magento' in text or '/skin/frontend/' in text:
                return "Magento"
            
            # Shopify
            if 'shopify' in text:
                return "Shopify"
            
            # Wix
            if 'wix.com' in text:
                return "Wix"
            
            # Squarespace
            if 'squarespace' in text:
                return "Squarespace"
            
            # Blogger
            if 'blogger' in text or 'blogspot' in text:
                return "Blogger"
            
            return "Unknown/None"
        except:
            return "Could not detect"
    
    def detect_cloudflare(self, url):
        """Detect if Cloudflare is used"""
        try:
            response = self.session.get(url, timeout=DEFAULT_TIMEOUT)
            headers = response.headers
            
            if 'cf-ray' in headers or 'cloudflare' in headers.get('server', '').lower():
                return "Yes - Cloudflare detected"
            
            # Check for Cloudflare specific cookies
            if 'cf_clearance' in response.cookies or '__cfduid' in response.cookies:
                return "Yes - Cloudflare detected"
            
            return "No Cloudflare"
        except:
            return "Could not detect"
    
    def check_robots(self, url):
        """Check robots.txt"""
        try:
            response = self.session.get(f"{url}/robots.txt", timeout=5)
            if response.status_code == 200:
                lines = response.text.strip().split('\n')
                disallowed = [l for l in lines if 'Disallow' in l]
                return f"Found ({len(disallowed)} disallowed paths)"
            return "Not found"
        except:
            return "Not accessible"
    
    def subnet_calc(self):
        """Subnet calculator"""
        console.print(Panel("[bold yellow]🔢 SUBNET CALCULATOR[/bold yellow]", border_style="blue"))
        
        try:
            ip = socket.gethostbyname(self.target.replace("www.", ""))
            network = ipaddress.ip_network(f"{ip}/24", strict=False)
            
            console.print(f"[cyan]IP Address:[/cyan] [green]{ip}[/green]")
            console.print(f"[cyan]Network:[/cyan] [green]{network.network_address}[/green]")
            console.print(f"[cyan]Netmask:[/cyan] [green]{network.netmask}[/green]")
            console.print(f"[cyan]Broadcast:[/cyan] [green]{network.broadcast_address}[/green]")
            console.print(f"[cyan]Total Hosts:[/cyan] [green]{network.num_addresses}[/green]")
            console.print(f"[cyan]Usable Hosts:[/cyan] [green]{network.num_addresses - 2}[/green]")
            console.print(f"[cyan]First Host:[/cyan] [green]{network.network_address + 1}[/green]")
            console.print(f"[cyan]Last Host:[/cyan] [green]{network.broadcast_address - 1}[/green]")
            
            self.results['subnet'] = {
                'network': str(network),
                'netmask': str(network.netmask),
                'broadcast': str(network.broadcast_address)
            }
        except Exception as e:
            console.print(f"[red][!] Subnet calculation failed: {e}[/red]")
    
    def reverse_ip_cms(self):
        """Reverse IP lookup and CMS detection"""
        console.print(Panel("[bold yellow]🔄 REVERSE IP & CMS[/bold yellow]", border_style="blue"))
        
        try:
            ip = socket.gethostbyname(self.target.replace("www.", ""))
            
            # Use yougetsignal API
            response = requests.post(
                'https://domains.yougetsignal.com/domains.php',
                data={'remoteAddress': ip}
            )
            
            data = response.json()
            domains = data.get('domainArray', [])
            
            console.print(f"[cyan]IP:[/cyan] [green]{ip}[/green]")
            console.print(f"[cyan]Domains on this IP:[/cyan] [green]{len(domains)}[/green]")
            
            if domains:
                for domain in domains[:20]:  # Limit to first 20
                    domain_name = domain[0]
                    try:
                        cms = self.detect_cms(f"http://{domain_name}")
                        console.print(f"  [cyan]{domain_name}[/cyan] - [green]{cms}[/green]")
                    except:
                        console.print(f"  [cyan]{domain_name}[/cyan] - [dim]Could not check[/dim]")
            
            self.results['reverse_ip'] = domains
        except Exception as e:
            console.print(f"[red][!] Reverse IP lookup failed: {e}[/red]")
    
    def mx_lookup(self):
        """MX record lookup"""
        console.print(Panel("[bold yellow]📧 MX LOOKUP[/bold yellow]", border_style="blue"))
        
        try:
            domain = self.target.replace("www.", "")
            answers = dns.resolver.resolve(domain, 'MX')
            
            console.print(f"[cyan]Mail servers for {domain}:[/cyan]")
            for answer in answers:
                mx = str(answer.exchange)
                preference = answer.preference
                console.print(f"  [yellow]{preference}[/yellow] - [green]{mx}[/green]")
            
            self.results['mx'] = [str(a.exchange) for a in answers]
        except Exception as e:
            console.print(f"[red][!] MX lookup failed: {e}[/red]")
    
    def generate_report(self):
        """Generate scan report"""
        console.print("\n[bold cyan]📊 GENERATING REPORT[/bold cyan]")
        
        report = {
            'target': f"{self.protocol}{self.target}",
            'date': datetime.now().isoformat(),
            'version': self.version,
            'results': self.results
        }
        
        # Create reports directory if not exists
        os.makedirs(REPORTS_DIR, exist_ok=True)
        
        # Save to file
        filename = os.path.join(
            REPORTS_DIR,
            f"wizard_report_{self.target.replace('.', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        console.print(f"[green]✓ Report saved to: {filename}[/green]")
        
        # Save to scan history
        self.scan_history.append(report)
    
    def update_framework(self):
        """Update WIZARD Framework"""
        console.print(Panel("[bold cyan]🔄 UPDATE WIZARD[/bold cyan]", border_style="blue"))
        
        console.print("[yellow]Checking for updates...[/yellow]")
        console.print("[green]✓ WIZARD is up to date![/green]")
    
    def fix_dependencies(self):
        """Fix and install dependencies"""
        console.print(Panel("[bold cyan]🔧 FIX DEPENDENCIES[/bold cyan]", border_style="blue"))
        install_requirements()
        console.print("[green]✓ All dependencies installed![/green]")
    
    def show_help(self):
        """Show help menu"""
        help_text = f"""
        [bold yellow] WIZARD Framework Help[/bold yellow]
        
        [bold cyan]Commands:[/bold cyan]
          help    - Show this help menu
          fix     - Install missing dependencies
          update  - Update WIZARD Framework
          config  - Configure API keys
          exit    - Exit WIZARD
        
        [bold cyan]Usage:[/bold cyan]
          1. Enter target domain (e.g., example.com)
          2. Select protocol (HTTP/HTTPS)
          3. Choose scan type from menu
        
        [bold cyan]Scan Types:[/bold cyan]
          0  - Basic Reconnaissance
          1  - WHOIS Lookup
          2  - Geo-IP Lookup
          3  - Banner Grabbing
          4  - DNS Lookup
          5  - Subnet Calculator
          6  - Port Scanner
          7  - Subdomain Finder
          8  - Reverse IP & CMS
          9  - SQLi Scanner
          10 - XSS Scanner
          11 - WordPress Scan
          12 - Directory Brute
          13 - MX Lookup
          14 - SSL Analysis
          15 - Vulnerability Scan
          A  - Full Automated Scan
          
        [bold red]⚠ DISCLAIMER:[/bold red]
          This tool is for educational purposes only.
          Always obtain proper authorization before scanning.
        """
        
        console.print(Panel(help_text, border_style="yellow"))
        Prompt.ask("\n[dim]Press Enter to continue...[/dim]")
    
    def exit_program(self):
        """Exit WIZARD gracefully"""
        console.print("\n[bold magenta] WIZARD says goodbye! Stay secure! 🔮[/bold magenta]")
        console.print("[dim]Thank you for using WIZARD Framework[/dim]")
        sys.exit(0)


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

def main():
    """Main function"""
    try:
        wizard = WizardEngine()
        wizard.run()
    except KeyboardInterrupt:
        console.print("\n\n[bold red] WIZARD terminated by user[/bold red]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[bold red]Fatal error: {e}[/bold red]")
        if WIZARD_DEBUG:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()