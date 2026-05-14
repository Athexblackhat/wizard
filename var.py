#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                     WIZARD FRAMEWORK - Variables & Constants              ║
║                          Version 3.0.0 - Phoenix                             ║
║                    Coded By: ATHEX BLACK HAT                                ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
from datetime import datetime

# ============================================================================
# FRAMEWORK INFORMATION
# ============================================================================

WIZARD_VERSION = "3.0.0"
WIZARD_CODENAME = "Phoenix"
WIZARD_AUTHOR = "ATHEX BLACK HAT"
WIZARD_DEBUG = False

# ============================================================================
# PATHS & DIRECTORIES
# ============================================================================

# Home and config directories
HOME_DIR = os.path.expanduser("~")
CONFIG_DIR = os.path.join(HOME_DIR, ".wizard")

# Data directories
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CURRENT_DIR, "data")
REPORTS_DIR = os.path.join(DATA_DIR, "reports")
WORDLISTS_DIR = os.path.join(DATA_DIR, "wordlists")
BACKUP_DIR = os.path.join(CONFIG_DIR, "backups")
PROFILES_DIR = os.path.join(CONFIG_DIR, "profiles")

# Config files
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
KEYS_FILE = os.path.join(CONFIG_DIR, "api_keys.enc")
ENV_FILE = os.path.join(CONFIG_DIR, ".env")
MASTER_KEY_FILE = os.path.join(CONFIG_DIR, ".master_key")

# ============================================================================
# HTTP & NETWORK SETTINGS
# ============================================================================

# User agents for rotation
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.43 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
]

# Request settings
DEFAULT_TIMEOUT = 10
MAX_RETRIES = 3
VERIFY_SSL = False
FOLLOW_REDIRECTS = True
MAX_THREADS = 20
REQUEST_DELAY = 0.1  # Delay between requests to avoid rate limiting

# ============================================================================
# COLOR SCHEMES (Rich Library)
# ============================================================================

class Colors:
    """Color constants for Rich library"""
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"
    BLUE = "blue"
    MAGENTA = "magenta"
    CYAN = "cyan"
    WHITE = "white"
    BLACK = "black"
    ORANGE = "orange1"
    PURPLE = "purple"
    PINK = "deep_pink"
    BRIGHT_RED = "bright_red"
    BRIGHT_GREEN = "bright_green"
    BRIGHT_YELLOW = "bright_yellow"
    BRIGHT_BLUE = "bright_blue"
    BRIGHT_MAGENTA = "bright_magenta"
    BRIGHT_CYAN = "bright_cyan"
    GREY = "grey"
    DIM = "dim"
    BOLD = "bold"
    BLINK = "blink"

# ============================================================================
# ANSI COLOR CODES (Terminal)
# ============================================================================

class AnsiColors:
    """ANSI color codes for terminal output"""
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BLACK = "\033[30m"
    ORANGE = "\033[38;5;208m"
    PURPLE = "\033[38;5;129m"
    PINK = "\033[38;5;201m"
    GREY = "\033[37m"
    LIGHT_BLUE = "\033[36m"
    LIGHT_GREEN = "\033[92m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    BLINK = "\033[5m"
    UNDERLINE = "\033[4m"
    
    # Background colors
    BG_RED = "\033[101m"
    BG_GREEN = "\033[102m"
    BG_YELLOW = "\033[103m"
    BG_BLUE = "\033[104m"
    BG_MAGENTA = "\033[105m"
    BG_CYAN = "\033[106m"
    BG_WHITE = "\033[107m"

# ============================================================================
# SCAN TYPES & MENUS
# ============================================================================

SCAN_TYPES = {
    "0": {"name": "Basic Recon", "icon": "🔍", "description": "Site info, IP, CMS, Cloudflare, Robots.txt"},
    "1": {"name": "Whois Lookup", "icon": "📋", "description": "Domain registration information"},
    "2": {"name": "Geo-IP Lookup", "icon": "🗺️", "description": "Geographical location of server"},
    "3": {"name": "Banner Grabbing", "icon": "📡", "description": "Server headers and banners"},
    "4": {"name": "DNS Lookup", "icon": "🌐", "description": "DNS records enumeration"},
    "5": {"name": "Subnet Calculator", "icon": "🔢", "description": "Network subnet calculation"},
    "6": {"name": "Port Scanner", "icon": "🔍", "description": "Advanced Nmap port scanning"},
    "7": {"name": "Subdomain Finder", "icon": "🔎", "description": "Discover subdomains"},
    "8": {"name": "Reverse IP & CMS", "icon": "🔄", "description": "Reverse IP lookup + CMS detection"},
    "9": {"name": "SQLi Scanner", "icon": "💉", "description": "SQL injection vulnerability scanner"},
    "10": {"name": "XSS Scanner", "icon": "💥", "description": "Cross-site scripting scanner"},
    "11": {"name": "WordPress Scan", "icon": "🔵", "description": "WordPress specific vulnerability scan"},
    "12": {"name": "Directory Brute", "icon": "📁", "description": "Directory & file brute force"},
    "13": {"name": "MX Lookup", "icon": "📧", "description": "Mail server records"},
    "14": {"name": "SSL Analysis", "icon": "🔒", "description": "SSL/TLS security analysis"},
    "15": {"name": "Vulnerability Scan", "icon": "🔴", "description": "Comprehensive vulnerability assessment"},
}

# ============================================================================
# SQL INJECTION
# ============================================================================

SQLI_PAYLOADS = [
    "'",
    '"',
    "1'",
    '1"',
    "' OR '1'='1",
    '" OR "1"="1',
    "' OR '1'='1' --",
    '" OR "1"="1" --',
    "' OR '1'='1' #",
    '" OR "1"="1" #',
    "' OR '1'='1' /*",
    '" OR "1"="1" /*',
    "' UNION SELECT NULL--",
    '" UNION SELECT NULL--',
    "' UNION SELECT NULL,NULL--",
    '" UNION SELECT NULL,NULL--',
    "' UNION SELECT NULL,NULL,NULL--",
    "admin'--",
    "admin' #",
    "' OR 1=1--",
    "' OR 'x'='x",
    "' AND 1=1--",
    "' AND 'x'='x",
    "1' ORDER BY 1--",
    "1' ORDER BY 2--",
    "1' ORDER BY 3--",
]

SQLI_ERRORS = [
    "SQL syntax",
    "MySQL",
    "ORA-",
    "PostgreSQL",
    "Microsoft SQL",
    "ODBC Driver",
    "SQLite",
    "JDBC",
    "Oracle error",
    "Syntax error",
    "unclosed quotation",
    "SQL command not properly ended",
    "Warning: mysql_",
    "valid MySQL result",
    "PostgreSQL query failed",
    "Supplied argument is not a valid MySQL",
    "Microsoft OLE DB Provider for SQL Server",
    "Unclosed quotation mark",
    "SQLite3::query",
    "SQLSTATE",
    "You have an error in your SQL syntax",
    "Division by zero in",
    "Incorrect syntax near",
    "Unknown column",
    "Table '.*' doesn't exist",
    "mysqli_fetch_assoc()",
    "mysql_fetch_array()",
    "mysql_num_rows()",
    "pg_query()",
    "mysqli_query()",
    "sqlsrv_query()",
    "odbc_exec()",
]

# ============================================================================
# XSS PAYLOADS
# ============================================================================

XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "\"><script>alert('XSS')</script>",
    "'><script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg onload=alert('XSS')>",
    "javascript:alert('XSS')",
    "<body onload=alert('XSS')>",
    "<iframe src=javascript:alert('XSS')>",
    "<input onfocus=alert('XSS') autofocus>",
    "<select onfocus=alert('XSS') autofocus>",
    "<textarea onfocus=alert('XSS') autofocus>",
    "<keygen onfocus=alert('XSS') autofocus>",
    "<video><source onerror=alert('XSS')>",
    "<audio src=x onerror=alert('XSS')>",
    "<marquee onstart=alert('XSS')>",
    "<details open ontoggle=alert('XSS')>",
    "'-alert('XSS')-'",
    "\"-alert('XSS')-\"",
    "';alert('XSS');//",
    "\";alert('XSS');//",
    "<scr<script>ipt>alert('XSS')</scr</script>ipt>",
    "<img src=x onerror=&#97;lert('XSS')>",
    "<img src=x onerror=eval(atob('YWxlcnQoJ1hTUycp'))>",
]

# ============================================================================
# CMS SIGNATURES
# ============================================================================

CMS_SIGNATURES = {
    "WordPress": {
        "paths": ["/wp-content/", "/wp-admin/", "/wp-includes/", "/xmlrpc.php"],
        "meta": "WordPress",
        "headers": ["X-Powered-By: WordPress"],
        "cookies": ["wp-settings-", "wordpress_logged_in"],
        "files": ["wp-login.php", "wp-config.php"],
    },
    "Joomla": {
        "paths": ["/components/com_", "/modules/mod_", "/templates/"],
        "meta": "Joomla",
        "headers": ["X-Content-Encoded-By: Joomla"],
        "cookies": ["joomla_user_state"],
        "files": ["administrator/index.php"],
    },
    "Drupal": {
        "paths": ["/sites/default/", "/misc/drupal.js", "/modules/"],
        "meta": "Drupal",
        "headers": ["X-Generator: Drupal"],
        "cookies": ["DRUPAL_UID"],
        "files": ["user/login", "node/"],
    },
    "Magento": {
        "paths": ["/skin/frontend/", "/media/catalog/"],
        "meta": "Magento",
        "cookies": ["frontend=", "adminhtml="],
        "files": ["admin/", "index.php/admin/"],
    },
    "Shopify": {
        "paths": ["/cdn.shopify.com", "myshopify.com"],
        "meta": "Shopify",
        "headers": ["X-Shopify-Stage"],
        "cookies": ["_shopify_"],
    },
    "Wix": {
        "paths": ["/wix.com", "_wix_"],
        "meta": "Wix.com",
        "headers": ["X-Wix-Request-Id"],
    },
    "Squarespace": {
        "paths": ["/squarespace.com", "static.squarespace.com"],
        "meta": "Squarespace",
    },
    "Blogger": {
        "paths": ["blogger.com", "blogspot.com"],
        "meta": "blogger",
    },
}

# ============================================================================
# COMMON DIRECTORIES FOR BRUTE FORCE
# ============================================================================

COMMON_DIRS = [
    # Admin panels
    "admin", "login", "administrator", "panel", "cpanel", "whm",
    "dashboard", "manage", "management", "moderator", "superadmin",
    
    # CMS specific
    "wp-admin", "wp-login.php", "wp-content", "wp-includes",
    "administrator/index.php", "user/login",
    
    # Configuration files
    "config", "configuration", "settings", "setup", "install",
    ".env", ".git", ".svn", ".htaccess",
    
    # Backup files
    "backup", "backups", "bak", "old", "archive",
    "wp-config.php.bak", "wp-config.php~", "config.php.bak",
    "database.sql", "db.sql", "dump.sql", "export.sql",
    
    # Development
    "dev", "development", "staging", "test", "testing",
    "debug", "phpinfo.php", "info.php", "test.php",
    
    # Common directories
    "css", "js", "images", "img", "assets", "static",
    "media", "files", "downloads", "upload", "uploads",
    "logs", "log", "tmp", "temp", "cache",
    
    # Email
    "webmail", "mail", "email", "squirrelmail", "roundcube",
    
    # Database
    "phpmyadmin", "phpPgAdmin", "adminer", "db", "database",
    
    # Files
    "robots.txt", "sitemap.xml", "crossdomain.xml",
    "README.md", "CHANGELOG.md", "LICENSE.txt",
    
    # API
    "api", "rest", "graphql", "soap", "wsdl",
    "swagger", "openapi", "docs", "documentation",
    
    # Security
    "security", "secure", "ssl", "private",
    
    # Other
    "forum", "blog", "news", "shop", "store",
    "members", "users", "profile", "account",
    "search", "sitemap", "feed", "rss",
]

# ============================================================================
# SUBDOMAINS FOR BRUTE FORCE
# ============================================================================

COMMON_SUBDOMAINS = [
    "www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "pop3",
    "ns1", "ns2", "ns3", "ns4",
    "webdisk", "cpanel", "whm", "autodiscover", "autoconfig",
    "m", "imap", "test", "ns", "blog", "dev", "www2", "admin",
    "forum", "news", "vpn", "mail2", "new", "mysql", "old",
    "lists", "support", "mobile", "mx", "static", "docs", "beta",
    "shop", "sql", "secure", "demo", "cp", "calendar", "wiki",
    "web", "media", "email", "images", "img", "download", "cdn",
    "api", "api2", "api3", "app", "apps", "auth", "backend",
    "board", "cdn2", "cdn3", "chat", "cloud", "community",
    "corp", "corporate", "crm", "data", "db", "design",
    "direct", "dns", "dns2", "edge", "en", "es", "fr", "de",
    "help", "host", "hosting", "intranet", "irc", "jabber",
    "jobs", "kb", "lab", "learn", "mssql", "music", "mysql",
    "net", "office", "online", "origin", "owa", "portal",
    "prod", "production", "proxy", "public", "remote", "root",
    "sandbox", "service", "services", "share", "sip", "stage",
    "stats", "status", "storage", "stream", "svn", "syslog",
    "training", "video", "voip", "webmin", "xen", "xmpp",
]

# ============================================================================
# CLOUDFLARE IP RANGES
# ============================================================================

CLOUDFLARE_IPS = [
    "103.21.244.0/22",
    "103.22.200.0/22",
    "103.31.4.0/22",
    "104.16.0.0/13",
    "104.24.0.0/14",
    "108.162.192.0/18",
    "131.0.72.0/22",
    "141.101.64.0/18",
    "162.158.0.0/15",
    "172.64.0.0/13",
    "173.245.48.0/20",
    "188.114.96.0/20",
    "190.93.240.0/20",
    "197.234.240.0/22",
    "198.41.128.0/17",
]

# ============================================================================
# SOCIAL MEDIA PLATFORMS
# ============================================================================

SOCIAL_PLATFORMS = {
    "Facebook": ["facebook.com", "fb.com", "fb.me", "messenger.com"],
    "Twitter": ["twitter.com", "t.co", "x.com"],
    "Instagram": ["instagram.com", "instagr.am"],
    "YouTube": ["youtube.com", "youtu.be", "yt.be"],
    "LinkedIn": ["linkedin.com", "lnkd.in"],
    "GitHub": ["github.com", "github.io"],
    "GitLab": ["gitlab.com"],
    "Bitbucket": ["bitbucket.org"],
    "Reddit": ["reddit.com", "redd.it"],
    "Tumblr": ["tumblr.com"],
    "Pinterest": ["pinterest.com", "pin.it"],
    "Flickr": ["flickr.com"],
    "Vimeo": ["vimeo.com"],
    "Dribbble": ["dribbble.com"],
    "Behance": ["behance.net"],
    "Medium": ["medium.com"],
    "Dev.to": ["dev.to"],
    "Stack Overflow": ["stackoverflow.com"],
    "WhatsApp": ["whatsapp.com", "wa.me"],
    "Telegram": ["telegram.org", "t.me"],
    "Discord": ["discord.com", "discord.gg"],
    "Slack": ["slack.com"],
    "Snapchat": ["snapchat.com"],
    "TikTok": ["tiktok.com"],
    "Twitch": ["twitch.tv"],
    "Spotify": ["spotify.com"],
    "SoundCloud": ["soundcloud.com"],
    "Bandcamp": ["bandcamp.com"],
    "Patreon": ["patreon.com"],
    "Ko-fi": ["ko-fi.com"],
    "Buy Me a Coffee": ["buymeacoffee.com"],
}

# ============================================================================
# SECURITY HEADERS
# ============================================================================

SECURITY_HEADERS = {
    "Strict-Transport-Security": {
        "recommended": "max-age=31536000; includeSubDomains",
        "weight": 10,
    },
    "Content-Security-Policy": {
        "recommended": "default-src 'self'",
        "weight": 10,
    },
    "X-Frame-Options": {
        "recommended": "DENY",
        "weight": 10,
    },
    "X-Content-Type-Options": {
        "recommended": "nosniff",
        "weight": 10,
    },
    "X-XSS-Protection": {
        "recommended": "1; mode=block",
        "weight": 10,
    },
    "Referrer-Policy": {
        "recommended": "strict-origin-when-cross-origin",
        "weight": 5,
    },
    "Permissions-Policy": {
        "recommended": "geolocation=(), microphone=()",
        "weight": 5,
    },
}

# ============================================================================
# INTERESTING FILES TO CHECK
# ============================================================================

INTERESTING_FILES = [
    # Version control
    ".git/config", ".git/HEAD", ".svn/entries",
    
    # Configuration
    ".env", ".env.local", ".env.production", ".env.development",
    "config.php", "config.yml", "config.yaml", "config.json",
    "wp-config.php", "wp-config.php.bak", "wp-config.php~",
    "settings.py", "settings.php",
    
    # Database
    "database.sql", "db.sql", "dump.sql", "backup.sql",
    "export.sql", "mysql.sql",
    
    # Backup files
    "backup.zip", "backup.tar.gz", "backup.rar",
    "site.zip", "www.zip", "web.zip",
    
    # Log files
    "error.log", "access.log", "debug.log",
    "php_error.log", "mysql_error.log",
    
    # Other
    "phpinfo.php", "info.php", "test.php",
    "robots.txt", "sitemap.xml", "crossdomain.xml",
    "README.md", "CHANGELOG.md", "LICENSE",
]

# ============================================================================
# API ENDPOINTS
# ============================================================================

API_ENDPOINTS = {
    # HackerTarget APIs
    "hackertarget_whois": "http://api.hackertarget.com/whois/?q=",
    "hackertarget_geoip": "http://api.hackertarget.com/geoip/?q=",
    "hackertarget_dns": "http://api.hackertarget.com/dnslookup/?q=",
    "hackertarget_subnet": "http://api.hackertarget.com/subnetcalc/?q=",
    "hackertarget_nmap": "http://api.hackertarget.com/nmap/?q=",
    "hackertarget_hostsearch": "http://api.hackertarget.com/hostsearch/?q=",
    "hackertarget_headers": "http://api.hackertarget.com/httpheaders/?q=",
    
    # Other APIs
    "alexa_rank": "http://data.alexa.com/data?cli=10&url=",
    "ip_api": "http://ip-api.com/json/",
    "crt_sh": "https://crt.sh/?q=",
    "wpvulndb": "https://wpvulndb.com/api/v2/wordpresses/",
    "yougetsignal": "https://domains.yougetsignal.com/domains.php",
}

# ============================================================================
# DNS RECORD TYPES
# ============================================================================

DNS_RECORD_TYPES = [
    "A",
    "AAAA",
    "MX",
    "NS",
    "TXT",
    "SOA",
    "CNAME",
    "PTR",
    "SRV",
    "CAA",
    "DNSKEY",
    "DS",
    "NAPTR",
    "SMIMEA",
    "SSHFP",
    "TLSA",
]

# ============================================================================
# FILE SIGNATURES (Magic Bytes)
# ============================================================================

FILE_SIGNATURES = {
    "FFD8FF": "JPEG Image",
    "89504E47": "PNG Image",
    "47494638": "GIF Image",
    "25504446": "PDF Document",
    "504B0304": "ZIP Archive",
    "52617221": "RAR Archive",
    "1F8B08": "GZIP Archive",
    "4D5A": "Windows Executable",
    "7F454C46": "Linux Executable",
    "CAFEBABE": "Java Class File",
    "D0CF11E0": "MS Office Document",
}

# ============================================================================
# COMMON PORTS & SERVICES
# ============================================================================

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    111: "RPC",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    993: "IMAPS",
    995: "POP3S",
    1723: "PPTP",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP-Proxy",
    8443: "HTTPS-Alt",
    27017: "MongoDB",
}

# ============================================================================
# WIZARD ASCII ART
# ============================================================================

WIZARD_ASCII_ART = """
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
"""

# ============================================================================
# BANNER FRAMES (For animation)
# ============================================================================

BANNER_FRAMES = [
    "⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"
]

PARTICLES = [
    "✦", "✧", "⋆", "✶", "✷", "✹", "✺", "✻", "✼", "✽", "⚡", "★", "🔮", "🌟", "✨"
]

# ============================================================================
# WIZARD FEATURES LIST
# ============================================================================

WIZARD_FEATURES = [
    "🔮 Advanced Reconnaissance & Information Gathering",
    "⚡ Real-time Vulnerability Assessment",
    "🌟 Automated Exploitation Framework",
    "🛡️ Intelligent Defense Evasion",
    "📡 Network Traffic Analysis",
    "💉 Advanced SQL Injection Testing",
    "🔐 Cryptography & Hash Cracking",
    "🌐 Web Application Firewall Bypass",
    "🎯 Zero-Day Exploit Development",
    "🧬 AI-Powered Threat Detection",
    "📊 Professional Report Generation",
    "🔍 Deep Web & Dark Web Scanning",
    "📱 Mobile Application Security Testing",
    "☁️ Cloud Security Assessment",
    "🔗 API Security Testing",
]

# ============================================================================
# ERROR MESSAGES
# ============================================================================

ERROR_MESSAGES = {
    "invalid_url": "Invalid URL format! Please enter a valid domain.",
    "connection_failed": "Failed to connect to target! Check the URL and try again.",
    "timeout": "Request timed out! Target may be slow or unreachable.",
    "dns_failed": "DNS resolution failed! Domain may not exist.",
    "permission_denied": "Permission denied! Some features require root/admin privileges.",
    "module_missing": "Required module is missing! Run 'fix' to install dependencies.",
    "api_key_missing": "API key not configured! Use 'config' to set up API keys.",
}

# ============================================================================
# SUCCESS MESSAGES
# ============================================================================

SUCCESS_MESSAGES = {
    "scan_complete": "Scan completed successfully!",
    "report_saved": "Report saved successfully!",
    "update_complete": "WIZARD is up to date!",
    "fix_complete": "All dependencies installed successfully!",
    "config_saved": "Configuration saved successfully!",
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_timestamp():
    """Get current timestamp"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_file_timestamp():
    """Get timestamp for filenames"""
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def create_directories():
    """Create all required directories"""
    directories = [
        CONFIG_DIR,
        DATA_DIR,
        REPORTS_DIR,
        WORDLISTS_DIR,
        BACKUP_DIR,
        PROFILES_DIR,
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    return True

# Create directories on import
create_directories()

# ============================================================================
# DEBUG MODE
# ============================================================================

if WIZARD_DEBUG:
    print(f"{AnsiColors.CYAN}[DEBUG] WIZARD Framework v{WIZARD_VERSION}{AnsiColors.RESET}")
    print(f"{AnsiColors.CYAN}[DEBUG] Config Dir: {CONFIG_DIR}{AnsiColors.RESET}")
    print(f"{AnsiColors.CYAN}[DEBUG] Data Dir: {DATA_DIR}{AnsiColors.RESET}")
    print(f"{AnsiColors.CYAN}[DEBUG] All directories created successfully{AnsiColors.RESET}")

# ============================================================================
# END OF VARIABLES
# ============================================================================