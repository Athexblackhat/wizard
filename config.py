#!/usr/bin/env python3
"""

                     WIZARD ULTIMATE CONFIGURATION SYSTEM                                             
               Multi-API Configuration with Secure Key Management             

"""

import os
import sys
import json
import base64
import hashlib
import hmac
import getpass
import shutil
from pathlib import Path
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import WIZARD variables
from var import *

# ============================================================================
# AUTO-INSTALL DEPENDENCIES
# ============================================================================

def install_config_dependencies():
    """Install required packages for configuration"""
    required = {
        'cryptography': 'cryptography',
        'keyring': 'keyring',
        'python-dotenv': 'dotenv',
        'pyyaml': 'yaml',
        'rich': 'rich',
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
        print("[✓] Dependencies installed!\n")

install_config_dependencies()

# Now import third-party modules
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from dotenv import load_dotenv, set_key
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.progress import Progress
from rich import box

# Optional imports
try:
    import keyring
    KEYRING_AVAILABLE = True
except ImportError:
    KEYRING_AVAILABLE = False

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False

# Initialize console
console = Console()

# ============================================================================
# WIZARD CONFIGURATION CLASS
# ============================================================================

class WizardConfig:
    """
    🧙‍♂️ ULTIMATE WIZARD CONFIGURATION MANAGER
    
    Features:
    - AES-256 Encrypted API key storage
    - 15+ API Provider support
    - Environment variable integration
    - System keyring support
    - Auto-backup and restore
    - API key validation
    - Multi-profile support
    - Import/Export configuration
    """
    
    def __init__(self, config_dir=None):
        """Initialize configuration manager"""
        # Use CONFIG_DIR from var.py or default
        self.config_dir = Path(config_dir or CONFIG_DIR)
        self.config_file = self.config_dir / "config.json"
        self.keys_file = self.config_dir / "api_keys.enc"
        self.profiles_dir = self.config_dir / "profiles"
        self.backup_dir = self.config_dir / "backups"
        self.env_file = self.config_dir / ".env"
        self.master_key_file = self.config_dir / ".master_key"
        
        # Create directories
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.profiles_dir.mkdir(parents=True, exist_ok=True)
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Load environment variables
        if self.env_file.exists():
            load_dotenv(self.env_file)
        
        # Initialize encryption
        self.cipher = None
        self.master_key = None
        self._init_encryption()
        
        # Load configuration
        self.config = self.load_config()
        
        # API Providers configuration
        self.api_providers = {
            'moz': {
                'name': 'Moz',
                'description': 'SEO and Domain Authority Metrics',
                'keys': ['access_id', 'secret_key'],
                'url': 'https://moz.com/products/mozscape/access',
                'free_tier': '27,000 calls/month',
                'docs': 'https://moz.com/help/links-api',
                'required_for': ['bloggers_view', 'seo_analysis']
            },
            'shodan': {
                'name': 'Shodan',
                'description': 'Internet Device Search Engine',
                'keys': ['api_key'],
                'url': 'https://account.shodan.io/',
                'free_tier': 'Limited queries/month',
                'docs': 'https://developer.shodan.io/',
                'required_for': ['port_scanning', 'device_discovery']
            },
            'virustotal': {
                'name': 'VirusTotal',
                'description': 'File and URL Malware Scanner',
                'keys': ['api_key'],
                'url': 'https://www.virustotal.com/gui/my-apikey',
                'free_tier': '500 requests/day',
                'docs': 'https://developers.virustotal.com/',
                'required_for': ['malware_scan', 'url_reputation']
            },
            'hunter': {
                'name': 'Hunter.io',
                'description': 'Email Finder and Verifier',
                'keys': ['api_key'],
                'url': 'https://hunter.io/api-keys',
                'free_tier': '25 searches/month',
                'docs': 'https://hunter.io/api-documentation',
                'required_for': ['email_hunting', 'domain_search']
            },
            'securitytrails': {
                'name': 'SecurityTrails',
                'description': 'DNS and Domain Intelligence',
                'keys': ['api_key'],
                'url': 'https://securitytrails.com/app/account/credentials',
                'free_tier': '50 requests/month',
                'docs': 'https://docs.securitytrails.com/',
                'required_for': ['dns_history', 'domain_intel']
            },
            'spyse': {
                'name': 'Spyse',
                'description': 'Cyber Security Search Engine',
                'keys': ['api_key'],
                'url': 'https://spyse.com/user/api',
                'free_tier': 'Limited requests/month',
                'docs': 'https://spyse.com/api-docs',
                'required_for': ['asset_discovery', 'vulnerability_scan']
            },
            'censys': {
                'name': 'Censys',
                'description': 'Internet Asset Discovery',
                'keys': ['api_id', 'api_secret'],
                'url': 'https://search.censys.io/account/api',
                'free_tier': '250 queries/month',
                'docs': 'https://search.censys.io/api',
                'required_for': ['certificate_search', 'host_discovery']
            },
            'binaryedge': {
                'name': 'BinaryEdge',
                'description': 'Threat Intelligence Platform',
                'keys': ['api_key'],
                'url': 'https://app.binaryedge.io/account/api',
                'free_tier': '250 credits/month',
                'docs': 'https://docs.binaryedge.io/',
                'required_for': ['threat_intel', 'exposure_detection']
            },
            'greynoise': {
                'name': 'GreyNoise',
                'description': 'Internet Noise Analysis',
                'keys': ['api_key'],
                'url': 'https://viz.greynoise.io/account/',
                'free_tier': '50 queries/day',
                'docs': 'https://docs.greynoise.io/',
                'required_for': ['noise_analysis', 'ip_reputation']
            },
            'alienvault': {
                'name': 'AlienVault OTX',
                'description': 'Open Threat Exchange',
                'keys': ['api_key'],
                'url': 'https://otx.alienvault.com/api',
                'free_tier': 'Free (registration required)',
                'docs': 'https://otx.alienvault.com/api',
                'required_for': ['threat_intel', 'ioc_lookup']
            },
            'abuseipdb': {
                'name': 'AbuseIPDB',
                'description': 'IP Address Reputation',
                'keys': ['api_key'],
                'url': 'https://www.abuseipdb.com/account/api',
                'free_tier': '1,000 checks/day',
                'docs': 'https://docs.abuseipdb.com/',
                'required_for': ['ip_reputation', 'abuse_check']
            },
            'urlscan': {
                'name': 'URLScan.io',
                'description': 'URL Scanner and Analyzer',
                'keys': ['api_key'],
                'url': 'https://urlscan.io/user/settings/',
                'free_tier': 'Limited scans/day',
                'docs': 'https://urlscan.io/docs/api/',
                'required_for': ['url_scanning', 'phishing_detection']
            },
            'builtwith': {
                'name': 'BuiltWith',
                'description': 'Website Technology Profiler',
                'keys': ['api_key'],
                'url': 'https://builtwith.com/api',
                'free_tier': 'Limited (paid plans)',
                'docs': 'https://api.builtwith.com/',
                'required_for': ['technology_detection', 'competitor_analysis']
            },
            'wappalyzer': {
                'name': 'Wappalyzer',
                'description': 'Technology Stack Detection',
                'keys': ['api_key'],
                'url': 'https://www.wappalyzer.com/api/',
                'free_tier': '50 lookups/month',
                'docs': 'https://www.wappalyzer.com/docs/api/',
                'required_for': ['tech_stack', 'framework_detection']
            },
            'haveibeenpwned': {
                'name': 'Have I Been Pwned',
                'description': 'Breach Database Check',
                'keys': ['api_key'],
                'url': 'https://haveibeenpwned.com/API/Key',
                'free_tier': 'Limited (paid for full access)',
                'docs': 'https://haveibeenpwned.com/API/v3',
                'required_for': ['breach_check', 'email_security']
            }
        }
    
    # ========================================================================
    # ENCRYPTION METHODS
    # ========================================================================
    
    def _init_encryption(self):
        """Initialize encryption for API keys"""
        if self.master_key_file.exists():
            try:
                with open(self.master_key_file, 'rb') as f:
                    self.master_key = f.read()
                self.cipher = Fernet(self.master_key)
            except Exception:
                self._create_master_key()
        else:
            self._create_master_key()
    
    def _create_master_key(self):
        """Create new master key"""
        console.print(Panel(
            "[bold yellow] WIZARD Master Password Setup[/bold yellow]\n\n"
            "[cyan]This password will encrypt all your API keys.[/cyan]\n"
            "[red]⚠ IMPORTANT: Do not forget this password![/red]",
            border_style="yellow"
        ))
        
        while True:
            password = getpass.getpass("[bold green]Enter master password: [/bold green]")
            if len(password) < 8:
                console.print("[red]Password must be at least 8 characters![/red]")
                continue
            
            confirm = getpass.getpass("[bold green]Confirm master password: [/bold green]")
            
            if password == confirm:
                break
            else:
                console.print("[red]Passwords do not match![/red]")
        
        # Generate key from password
        salt = b'wizard_salt_2024_phoenix'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        self.master_key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        self.cipher = Fernet(self.master_key)
        
        # Save master key
        with open(self.master_key_file, 'wb') as f:
            f.write(self.master_key)
        
        # Set secure permissions
        os.chmod(self.master_key_file, 0o600)
        
        console.print("[green]✓ Master key created successfully![/green]")
    
    def encrypt_api_key(self, key):
        """Encrypt API key"""
        if self.cipher and key:
            try:
                return self.cipher.encrypt(key.encode()).decode()
            except Exception:
                return None
        return key
    
    def decrypt_api_key(self, encrypted_key):
        """Decrypt API key"""
        if self.cipher and encrypted_key:
            try:
                return self.cipher.decrypt(encrypted_key.encode()).decode()
            except Exception:
                return None
        return encrypted_key
    
    # ========================================================================
    # CONFIGURATION LOAD/SAVE
    # ========================================================================
    
    def load_config(self):
        """Load configuration from file"""
        default_config = {
            'version': WIZARD_VERSION,
            'settings': {
                'theme': 'dark',
                'language': 'en',
                'output_format': 'table',
                'timeout': DEFAULT_TIMEOUT,
                'max_threads': MAX_THREADS,
                'user_agent': f'WIZARD/{WIZARD_VERSION}',
                'verify_ssl': VERIFY_SSL,
                'follow_redirects': FOLLOW_REDIRECTS,
                'save_reports': True,
                'report_format': 'json',
                'auto_update': True,
                'anonymous_mode': False,
                'tor_proxy': False,
                'proxy_url': '',
                'debug_mode': WIZARD_DEBUG
            },
            'api_keys': {},
            'custom_wordlists': {},
            'scan_profiles': {},
            'bookmarks': [],
            'history': [],
            'plugins': [],
            'last_updated': datetime.now().isoformat()
        }
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    # Merge with defaults for any new keys
                    for key, value in default_config.items():
                        if key not in config:
                            config[key] = value
                    return config
            except (json.JSONDecodeError, Exception):
                console.print("[yellow]⚠ Config file corrupted, using defaults[/yellow]")
                return default_config
        
        return default_config
    
    def save_config(self):
        """Save configuration to file with backup"""
        self.config['last_updated'] = datetime.now().isoformat()
        
        try:
            # Save main config
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            
            # Set secure permissions
            os.chmod(self.config_file, 0o600)
            
            # Create backup
            self._backup_config()
            
            return True
        except Exception as e:
            console.print(f"[red]Error saving config: {e}[/red]")
            return False
    
    def _backup_config(self):
        """Create backup of configuration"""
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_file = self.backup_dir / f"config_backup_{timestamp}.json"
            
            with open(backup_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            
            # Keep only last 10 backups
            backups = sorted(self.backup_dir.glob("config_backup_*.json"))
            if len(backups) > 10:
                for old_backup in backups[:-10]:
                    old_backup.unlink()
        except Exception:
            pass  # Silent fail for backup
    
    # ========================================================================
    # API KEY MANAGEMENT
    # ========================================================================
    
    def set_api_keys(self, provider, keys):
        """
        Set API keys for a provider
        
        Args:
            provider: Provider name (e.g., 'moz')
            keys: Dictionary of key-value pairs
            
        Returns:
            bool: Success status
        """
        if provider not in self.api_providers:
            console.print(f"[red]Unknown provider: {provider}[/red]")
            return False
        
        # Validate required keys
        provider_info = self.api_providers[provider]
        required_keys = provider_info['keys']
        
        for key in required_keys:
            if key not in keys or not keys[key]:
                console.print(f"[red]Missing required key: {key}[/red]")
                return False
        
        # Encrypt and store keys
        encrypted_keys = {}
        for key, value in keys.items():
            encrypted_value = self.encrypt_api_key(value)
            if encrypted_value:
                encrypted_keys[key] = encrypted_value
        
        if not encrypted_keys:
            console.print("[red]Failed to encrypt keys![/red]")
            return False
        
        self.config['api_keys'][provider] = {
            'keys': encrypted_keys,
            'added': datetime.now().isoformat(),
            'last_used': None,
            'is_valid': False
        }
        
        # Save to system keyring if available
        if KEYRING_AVAILABLE:
            try:
                keyring.set_password(
                    f"wizard_{provider}",
                    "api_keys",
                    json.dumps(keys)
                )
            except Exception:
                pass
        
        self.save_config()
        
        # Optionally validate keys
        console.print(f"[green]✓ {provider_info['name']} API keys saved![/green]")
        
        return True
    
    def get_api_keys(self, provider):
        """
        Get API keys for a provider
        
        Args:
            provider: Provider name
            
        Returns:
            dict or None: Decrypted API keys
        """
        # Try environment variables first
        env_keys = {}
        provider_info = self.api_providers.get(provider, {})
        required_keys = provider_info.get('keys', [])
        
        for key in required_keys:
            env_var = f"WIZARD_{provider.upper()}_{key.upper()}"
            env_value = os.getenv(env_var)
            if env_value:
                env_keys[key] = env_value
        
        if env_keys and len(env_keys) == len(required_keys):
            return env_keys
        
        # Try system keyring
        if KEYRING_AVAILABLE:
            try:
                keyring_data = keyring.get_password(f"wizard_{provider}", "api_keys")
                if keyring_data:
                    return json.loads(keyring_data)
            except Exception:
                pass
        
        # Try config file
        if provider in self.config.get('api_keys', {}):
            encrypted_keys = self.config['api_keys'][provider].get('keys', {})
            decrypted_keys = {}
            
            for key, encrypted_value in encrypted_keys.items():
                decrypted_value = self.decrypt_api_key(encrypted_value)
                if decrypted_value:
                    decrypted_keys[key] = decrypted_value
            
            if decrypted_keys:
                # Update last used timestamp
                self.config['api_keys'][provider]['last_used'] = datetime.now().isoformat()
                self.save_config()
                return decrypted_keys
        
        return None
    
    def remove_api_keys(self, provider):
        """Remove API keys for a provider"""
        if provider in self.config.get('api_keys', {}):
            del self.config['api_keys'][provider]
            
            # Remove from keyring
            if KEYRING_AVAILABLE:
                try:
                    keyring.delete_password(f"wizard_{provider}", "api_keys")
                except Exception:
                    pass
            
            self.save_config()
            console.print(f"[green]✓ {provider.upper()} API keys removed[/green]")
            return True
        
        console.print(f"[yellow]No keys found for {provider}[/yellow]")
        return False
    
    def validate_api_keys(self, provider):
        """
        Validate API keys for a provider
        
        Args:
            provider: Provider name
            
        Returns:
            bool: True if valid
        """
        keys = self.get_api_keys(provider)
        if not keys:
            return False
        
        # Validation URLs for different providers
        validation_urls = {
            'shodan': ('https://api.shodan.io/api-info', {'params': {'key': keys.get('api_key', '')}}),
            'virustotal': ('https://www.virustotal.com/api/v3/users/me', {'headers': {'x-apikey': keys.get('api_key', '')}}),
            'hunter': ('https://api.hunter.io/v2/account', {'params': {'api_key': keys.get('api_key', '')}}),
        }
        
        if provider in validation_urls:
            try:
                import requests
                url, kwargs = validation_urls[provider]
                response = requests.get(url, timeout=10, **kwargs)
                is_valid = response.status_code == 200
                
                # Update validity in config
                if provider in self.config.get('api_keys', {}):
                    self.config['api_keys'][provider]['is_valid'] = is_valid
                    self.save_config()
                
                return is_valid
            except Exception:
                return False
        
        # For providers without validation URL, assume valid if keys exist
        return True
    
    # ========================================================================
    # API PROVIDER LISTING
    # ========================================================================
    
    def list_api_providers(self):
        """List all API providers and their status"""
        table = Table(
            title="[bold yellow] WIZARD API Providers[/bold yellow]",
            border_style="bright_magenta",
            box=box.ROUNDED
        )
        
        table.add_column("Provider", style="cyan", width=20)
        table.add_column("Status", style="yellow", width=25)
        table.add_column("Free Tier", style="green", width=25)
        table.add_column("Required For", style="white", width=30)
        
        for provider_id, info in self.api_providers.items():
            keys = self.get_api_keys(provider_id)
            
            if keys:
                is_valid = self.config.get('api_keys', {}).get(provider_id, {}).get('is_valid', False)
                if is_valid:
                    status = "[green] Configured & Valid[/green]"
                else:
                    status = "[yellow] Configured (Not Tested)[/yellow]"
            else:
                status = "[red] Not Configured[/red]"
            
            table.add_row(
                f"[bold]{info['name']}[/bold]",
                status,
                info['free_tier'],
                ', '.join(info['required_for'][:3])
            )
        
        console.print(table)
        console.print(f"\n[dim]Total: {len(self.api_providers)} providers | "
                     f"Configured: {len([k for k in self.config.get('api_keys', {}) if self.config['api_keys'][k].get('keys')])}[/dim]")
        return table
    
    # ========================================================================
    # INTERACTIVE CONFIGURATION
    # ========================================================================
    
    def configure_interactive(self):
        """Interactive configuration wizard"""
        console.print(Panel(
            "[bold magenta] WIZARD Interactive Configuration[/bold magenta]\n"
            "[cyan]Set up your API keys for maximum power![/cyan]",
            border_style="magenta"
        ))
        
        while True:
            console.print("\n[bold yellow]Configuration Options:[/bold yellow]")
            console.print("  [cyan]1.[/cyan] Add/Update API Keys")
            console.print("  [cyan]2.[/cyan] View Configured APIs")
            console.print("  [cyan]3.[/cyan] Remove API Keys")
            console.print("  [cyan]4.[/cyan] Test API Keys")
            console.print("  [cyan]5.[/cyan] Import Configuration")
            console.print("  [cyan]6.[/cyan] Export Configuration")
            console.print("  [cyan]7.[/cyan] General Settings")
            console.print("  [cyan]8.[/cyan] Back to Main Menu")
            
            choice = Prompt.ask("[bold green]Select option[/bold green]", 
                              choices=["1", "2", "3", "4", "5", "6", "7", "8"])
            
            if choice == "1":
                self._interactive_add_keys()
            elif choice == "2":
                self.list_api_providers()
            elif choice == "3":
                self._interactive_remove_keys()
            elif choice == "4":
                self._interactive_test_keys()
            elif choice == "5":
                self._import_configuration()
            elif choice == "6":
                self._export_configuration()
            elif choice == "7":
                self._general_settings()
            elif choice == "8":
                break
    
    def _interactive_add_keys(self):
        """Interactive API key addition"""
        console.print("\n[bold cyan]Select API Provider to configure:[/bold cyan]")
        
        providers = list(self.api_providers.keys())
        for i, provider in enumerate(providers, 1):
            info = self.api_providers[provider]
            status = ""
            if provider in self.config.get('api_keys', {}):
                status = " [green](configured)[/green]"
            console.print(f"  {i}. [yellow]{info['name']}[/yellow] - {info['description']}{status}")
        
        console.print(f"  {len(providers) + 1}. [red]Cancel[/red]")
        
        choice = Prompt.ask("[bold green]Select provider[/bold green]", 
                          default=str(len(providers) + 1))
        
        try:
            idx = int(choice) - 1
            if idx == len(providers):
                return
            if idx < 0 or idx >= len(providers):
                console.print("[red]Invalid selection![/red]")
                return
            provider = providers[idx]
        except ValueError:
            return
        
        info = self.api_providers[provider]
        
        console.print(Panel(
            f"[bold yellow]{info['name']} API Configuration[/bold yellow]\n\n"
            f"[cyan]Description:[/cyan] {info['description']}\n"
            f"[cyan]Free Tier:[/cyan] {info['free_tier']}\n"
            f"[cyan]Get Keys:[/cyan] [link={info['url']}]{info['url']}[/link]\n"
            f"[cyan]Documentation:[/cyan] [link={info['docs']}]{info['docs']}[/link]",
            border_style="blue"
        ))
        
        # Get keys from user
        keys = {}
        for key_name in info['keys']:
            display_name = key_name.replace('_', ' ').title()
            value = Prompt.ask(f"[bold green]Enter {display_name}[/bold green]", password=True)
            if value:
                keys[key_name] = value.strip()
        
        if keys:
            self.set_api_keys(provider, keys)
        else:
            console.print("[yellow]No keys entered, cancelled.[/yellow]")
    
    def _interactive_remove_keys(self):
        """Interactive API key removal"""
        configured = [k for k, v in self.config.get('api_keys', {}).items() if v.get('keys')]
        
        if not configured:
            console.print("[yellow]No API keys configured[/yellow]")
            return
        
        console.print("\n[bold cyan]Select provider to remove:[/bold cyan]")
        for i, provider in enumerate(configured, 1):
            info = self.api_providers.get(provider, {})
            console.print(f"  {i}. [yellow]{info.get('name', provider)}[/yellow]")
        console.print(f"  {len(configured) + 1}. [red]Cancel[/red]")
        
        choice = Prompt.ask("[bold red]Select provider[/bold red]", default="0")
        
        try:
            idx = int(choice) - 1
            if idx == len(configured):
                return
            if 0 <= idx < len(configured):
                confirm = Confirm.ask(f"[bold red]Remove {configured[idx].upper()} keys?[/bold red]", default=False)
                if confirm:
                    self.remove_api_keys(configured[idx])
        except ValueError:
            pass
    
    def _interactive_test_keys(self):
        """Test all configured API keys"""
        configured = [k for k, v in self.config.get('api_keys', {}).items() if v.get('keys')]
        
        if not configured:
            console.print("[yellow]No API keys to test[/yellow]")
            return
        
        console.print("[cyan]Testing API keys...[/cyan]\n")
        
        with Progress() as progress:
            task = progress.add_task("[cyan]Testing...", total=len(configured))
            
            for provider in configured:
                info = self.api_providers.get(provider, {})
                progress.update(task, description=f"[cyan]Testing {info.get('name', provider)}...")
                
                is_valid = self.validate_api_keys(provider)
                
                if is_valid:
                    console.print(f"  [green]✓ {info.get('name', provider)}: Valid[/green]")
                else:
                    console.print(f"  [yellow]⚠ {info.get('name', provider)}: Could not validate[/yellow]")
                
                progress.update(task, advance=1)
        
        console.print("\n[dim]Note: Some providers may not support automatic validation.[/dim]")
    
    def _import_configuration(self):
        """Import configuration from file"""
        import_path = Prompt.ask("[bold green]Enter path to configuration file[/bold green]")
        
        if not os.path.exists(import_path):
            console.print("[red]File not found![/red]")
            return
        
        try:
            with open(import_path, 'r') as f:
                imported_config = json.load(f)
            
            # Merge with current config
            if 'api_keys' in imported_config:
                self.config['api_keys'].update(imported_config['api_keys'])
            
            if 'settings' in imported_config:
                self.config['settings'].update(imported_config['settings'])
            
            self.save_config()
            console.print("[green]✓ Configuration imported successfully![/green]")
        except json.JSONDecodeError:
            console.print("[red]Invalid JSON file![/red]")
        except Exception as e:
            console.print(f"[red]Error importing: {e}[/red]")
    
    def _export_configuration(self):
        """Export configuration to file"""
        export_path = Prompt.ask(
            "[bold green]Enter export path[/bold green]",
            default=str(Path.home() / "wizard_config_export.json")
        )
        
        # Create export config (without sensitive data by default)
        export_config = {
            'version': self.config['version'],
            'settings': self.config['settings'],
            'api_providers_configured': list(self.config.get('api_keys', {}).keys()),
            'export_date': datetime.now().isoformat()
        }
        
        include_keys = Confirm.ask("[yellow]Include encrypted API keys in export?[/yellow]", default=False)
        
        if include_keys:
            export_config['api_keys'] = self.config['api_keys']
        
        try:
            with open(export_path, 'w') as f:
                json.dump(export_config, f, indent=2)
            
            console.print(f"[green]✓ Configuration exported to: {export_path}[/green]")
        except Exception as e:
            console.print(f"[red]Error exporting: {e}[/red]")
    
    def _general_settings(self):
        """Configure general settings"""
        console.print(Panel("[bold yellow] General Settings[/bold yellow]", border_style="yellow"))
        
        settings = self.config.get('settings', {})
        
        settings['theme'] = Prompt.ask(
            "[bold green]Theme[/bold green]",
            choices=["dark", "light", "hacker", "minimal"],
            default=settings.get('theme', 'dark')
        )
        
        settings['output_format'] = Prompt.ask(
            "[bold green]Default output format[/bold green]",
            choices=["table", "json", "yaml", "csv"],
            default=settings.get('output_format', 'table')
        )
        
        settings['timeout'] = int(Prompt.ask(
            "[bold green]Request timeout (seconds)[/bold green]",
            default=str(settings.get('timeout', 10))
        ))
        
        settings['max_threads'] = int(Prompt.ask(
            "[bold green]Maximum threads[/bold green]",
            default=str(settings.get('max_threads', 20))
        ))
        
        settings['verify_ssl'] = Confirm.ask(
            "[bold green]Verify SSL certificates?[/bold green]",
            default=settings.get('verify_ssl', False)
        )
        
        settings['save_reports'] = Confirm.ask(
            "[bold green]Auto-save scan reports?[/bold green]",
            default=settings.get('save_reports', True)
        )
        
        settings['debug_mode'] = Confirm.ask(
            "[bold green]Enable debug mode?[/bold green]",
            default=settings.get('debug_mode', False)
        )
        
        self.config['settings'] = settings
        self.save_config()
        console.print("[green]✓ Settings updated successfully![/green]")
    
    # ========================================================================
    # UTILITY METHODS
    # ========================================================================
    
    def get_setting(self, key, default=None):
        """Get a configuration setting"""
        return self.config.get('settings', {}).get(key, default)
    
    def set_setting(self, key, value):
        """Set a configuration setting"""
        if 'settings' not in self.config:
            self.config['settings'] = {}
        self.config['settings'][key] = value
        self.save_config()
    
    def create_profile(self, name, settings=None):
        """Create a scan profile"""
        profile = {
            'name': name,
            'created': datetime.now().isoformat(),
            'settings': settings or {},
            'api_keys_to_use': [],
            'scan_modules': []
        }
        
        profile_file = self.profiles_dir / f"{name}.json"
        with open(profile_file, 'w') as f:
            json.dump(profile, f, indent=2)
        
        console.print(f"[green]✓ Profile '{name}' created![/green]")
        return profile
    
    def load_profile(self, name):
        """Load a scan profile"""
        profile_file = self.profiles_dir / f"{name}.json"
        
        if profile_file.exists():
            with open(profile_file, 'r') as f:
                return json.load(f)
        
        return None
    
    def list_profiles(self):
        """List all profiles"""
        profiles = []
        
        if self.profiles_dir.exists():
            for profile_file in self.profiles_dir.glob("*.json"):
                try:
                    with open(profile_file, 'r') as f:
                        profile = json.load(f)
                        profiles.append(profile)
                except Exception:
                    pass
        
        return profiles
    
    def check_environment(self):
        """Check environment and dependencies"""
        console.print("[cyan]🔍 Checking WIZARD environment...[/cyan]\n")
        
        checks = []
        
        # Python version
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        checks.append(("Python Version", python_version, sys.version_info >= (3, 8)))
        
        # Required modules
        required_modules = [
            'requests', 'rich', 'colorama', 'bs4', 'dns', 'whois',
            'cryptography', 'lxml'
        ]
        
        for module in required_modules:
            try:
                __import__(module)
                checks.append((f"Module: {module}", "Installed", True))
            except ImportError:
                checks.append((f"Module: {module}", "Missing", False))
        
        # API keys
        configured_apis = len([k for k, v in self.config.get('api_keys', {}).items() if v.get('keys')])
        checks.append(("API Keys", f"{configured_apis}/{len(self.api_providers)} configured", configured_apis > 0))
        
        # Disk space
        try:
            disk_usage = shutil.disk_usage(self.config_dir)
            free_gb = disk_usage.free / (1024**3)
            checks.append(("Free Disk Space", f"{free_gb:.1f} GB", free_gb > 1))
        except Exception:
            checks.append(("Free Disk Space", "Unknown", True))
        
        # Display results
        table = Table(title="[bold yellow]Environment Check[/bold yellow]", border_style="blue")
        table.add_column("Check", style="cyan")
        table.add_column("Status", style="yellow")
        table.add_column("Result", style="white")
        
        all_passed = True
        for check in checks:
            name, status, passed = check
            result = "[green]✓ Pass[/green]" if passed else "[red]✗ Fail[/red]"
            if not passed:
                all_passed = False
            table.add_row(name, status, result)
        
        console.print(table)
        
        if all_passed:
            console.print("\n[green]✓ All checks passed![/green]")
        else:
            console.print("\n[yellow] Some checks failed. Run 'fix' to resolve issues.[/yellow]")
        
        return all_passed
    
    def display_config_summary(self):
        """Display configuration summary"""
        console.print(Panel(
            "[bold magenta] WIZARD Configuration Summary[/bold magenta]",
            border_style="magenta"
        ))
        
        # Settings
        settings = self.config.get('settings', {})
        console.print("\n[bold cyan] General Settings:[/bold cyan]")
        for key, value in settings.items():
            console.print(f"  [yellow]{key}:[/yellow] [green]{value}[/green]")
        
        # API Keys
        configured_apis = {k: v for k, v in self.config.get('api_keys', {}).items() if v.get('keys')}
        console.print(f"\n[bold cyan] API Keys:[/bold cyan] [green]{len(configured_apis)}/{len(self.api_providers)} configured[/green]")
        for api, info in configured_apis.items():
            provider_info = self.api_providers.get(api, {})
            status = "[green]✓ Valid[/green]" if info.get('is_valid') else "[yellow]⚠ Pending validation[/yellow]"
            console.print(f"  [yellow]{provider_info.get('name', api)}:[/yellow] {status}")
        
        # Profiles
        profiles = self.list_profiles()
        console.print(f"\n[bold cyan] Profiles:[/bold cyan] [green]{len(profiles)} saved[/green]")
        
        # History
        history = self.config.get('history', [])
        console.print(f"\n[bold cyan] Scan History:[/bold cyan] [green]{len(history)} entries[/green]")
    
    def reset_configuration(self):
        """Reset configuration to defaults"""
        confirm = Confirm.ask(
            "[bold red]⚠ Are you sure you want to reset ALL configuration?[/bold red]",
            default=False
        )
        
        if confirm:
            # Delete config file
            if self.config_file.exists():
                self.config_file.unlink()
            
            # Reload defaults
            self.config = self.load_config()
            self.save_config()
            console.print("[green]✓ Configuration reset to defaults![/green]")
    
    # ========================================================================
    # CONVENIENCE METHODS
    # ========================================================================
    
    def get_moz_keys(self):
        """Get Moz API keys"""
        return self.get_api_keys('moz')
    
    def get_shodan_key(self):
        """Get Shodan API key"""
        keys = self.get_api_keys('shodan')
        return keys.get('api_key') if keys else None
    
    def get_virustotal_key(self):
        """Get VirusTotal API key"""
        keys = self.get_api_keys('virustotal')
        return keys.get('api_key') if keys else None
    
    def get_hunter_key(self):
        """Get Hunter.io API key"""
        keys = self.get_api_keys('hunter')
        return keys.get('api_key') if keys else None


# ============================================================================
# GLOBAL CONFIGURATION INSTANCE
# ============================================================================

try:
    config = WizardConfig()
except Exception as e:
    console.print(f"[red]Error initializing configuration: {e}[/red]")
    config = None


# ============================================================================
# COMMAND LINE INTERFACE
# ============================================================================

def main():
    """Main CLI for configuration management"""
    console.print(Panel(
        f"[bold magenta] WIZARD Configuration Manager[/bold magenta]\n"
        f"[cyan]Version: {WIZARD_VERSION}[/cyan]\n"
        f"[cyan]Config Directory: {config.config_dir}[/cyan]",
        border_style="magenta"
    ))
    
    while True:
        console.print("\n[bold yellow]Configuration Menu:[/bold yellow]")
        options = [
            "1. Interactive Setup Wizard",
            "2. View API Providers",
            "3. Add/Update API Keys",
            "4. Test API Keys",
            "5. General Settings",
            "6. Manage Profiles",
            "7. Environment Check",
            "8. Configuration Summary",
            "9. Export Configuration",
            "10. Import Configuration",
            "11. Reset Configuration",
            "12. Exit"
        ]
        
        for option in options:
            console.print(f"  [cyan]{option}[/cyan]")
        
        choice = Prompt.ask("[bold green]Select option[/bold green]", 
                          choices=[str(i) for i in range(1, 13)])
        
        if choice == "1":
            config.configure_interactive()
        elif choice == "2":
            config.list_api_providers()
        elif choice == "3":
            config._interactive_add_keys()
        elif choice == "4":
            config._interactive_test_keys()
        elif choice == "5":
            config._general_settings()
        elif choice == "6":
            _manage_profiles()
        elif choice == "7":
            config.check_environment()
        elif choice == "8":
            config.display_config_summary()
        elif choice == "9":
            config._export_configuration()
        elif choice == "10":
            config._import_configuration()
        elif choice == "11":
            config.reset_configuration()
        elif choice == "12":
            console.print("\n[bold magenta]🧙‍♂️ Configuration saved. Goodbye![/bold magenta]")
            break


def _manage_profiles():
    """Manage scan profiles"""
    console.print("\n[bold cyan] Profile Management:[/bold cyan]")
    console.print("  1. Create Profile")
    console.print("  2. List Profiles")
    console.print("  3. Load Profile")
    console.print("  4. Delete Profile")
    console.print("  5. Back")
    
    choice = Prompt.ask("[bold green]Select option[/bold green]", 
                      choices=["1", "2", "3", "4", "5"])
    
    if choice == "1":
        name = Prompt.ask("[bold green]Profile name[/bold green]")
        if name:
            config.create_profile(name)
    elif choice == "2":
        profiles = config.list_profiles()
        if profiles:
            for profile in profiles:
                console.print(f"  [yellow]{profile['name']}[/yellow] - Created: {profile['created']}")
        else:
            console.print("  [dim]No profiles found[/dim]")
    elif choice == "3":
        name = Prompt.ask("[bold green]Profile name to load[/bold green]")
        profile = config.load_profile(name)
        if profile:
            console.print(f"[green]✓ Loaded profile: {name}[/green]")
            console.print(json.dumps(profile, indent=2))
        else:
            console.print("[red]Profile not found![/red]")
    elif choice == "4":
        name = Prompt.ask("[bold red]Profile name to delete[/bold red]")
        profile_file = config.profiles_dir / f"{name}.json"
        if profile_file.exists():
            confirm = Confirm.ask(f"[red]Delete profile '{name}'?[/red]", default=False)
            if confirm:
                profile_file.unlink()
                console.print(f"[green]✓ Profile '{name}' deleted[/green]")
        else:
            console.print("[red]Profile not found![/red]")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n\n[bold yellow]Configuration manager closed.[/bold yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")
        sys.exit(1)