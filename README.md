<div align="center">
    <img src="/logo.svg" alt="WIZARD Framework Logo" width="300" height="300">
</div>

# 🧙‍♂️ WIZARD FRAMEWORK

<div align="center">

**Advanced Cyber Security & Penetration Testing Platform**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://python.org)
[![Version](https://img.shields.io/badge/Version-3.0.0-red?style=for-the-badge)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)](https://docker.com)

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Configuration](#-configuration) • [API Integration](#-api-integration) • [Docker](#-docker-deployment) • [Reports](#-reports) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage Guide](#-usage-guide)
- [Configuration](#-configuration)
- [API Integration](#-api-integration)
- [Docker Deployment](#-docker-deployment)
- [Reports](#-reports)
- [Security](#-security)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Features

| Category | Feature | Status |
|---|---|---|
| **Reconnaissance** | Basic Recon (Title, IP, CMS, Cloudflare) | ✅ |
| | WHOIS Lookup | ✅ |
| | Geo-IP Location | ✅ |
| | DNS Records Enumeration | ✅ |
| | Subdomain Discovery | ✅ |
| | Reverse IP Lookup | ✅ |
| **Vulnerability** | SQL Injection Scanner | ✅ |
| | XSS Detection | ✅ |
| | WordPress Security Scan | ✅ |
| | Directory Brute Force | ✅ |
| | SSL/TLS Analysis | ✅ |
| **Network** | Port Scanner (Nmap) | ✅ |
| | Banner Grabbing | ✅ |
| | Subnet Calculator | ✅ |
| | MX Record Lookup | ✅ |
| **Reporting** | JSON Reports | ✅ |
| | HTML Reports | ✅ |
| | PDF Reports | ✅ |
| **Security** | AES-256 Encryption | ✅ |
| | TOR Support | ✅ |
| | Anonymous Mode | ✅ |
| **API Integration** | 15+ APIs Supported | ✅ |

---

## 📊 Architecture

WIZARD is organized into four core layers:

- **Input Layer** — Target URL, scan type, and configuration
- **Processing Layer** — URL validation, protocol selection, and scan execution
- **Analysis Layer** — Vulnerability checking, pattern matching, risk assessment, and score calculation
- **Output Layer** — Console display, JSON, HTML, and PDF reports

### Core Modules

| Module | Role |
|---|---|
| `wizard.py` | Main engine |
| `functions.py` | Utility functions |
| `config.py` | Configuration manager |
| `var.py` | Variables & constants |

### Scanner Modules

Basic Recon, WHOIS Lookup, Geo-IP Lookup, Banner Grabbing, DNS Lookup, Subnet Calculator, Port Scanner, Subdomain Finder, Reverse IP & CMS, SQLi Scanner, XSS Scanner, WordPress Scan, Directory Brute Force, MX Lookup, SSL Analysis, Vulnerability Scan, Full Scan.

---

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- pip3
- git *(optional)*
- nmap *(for port scanning)*

### Quick Install (One Command)

```bash
curl -sSL https://raw.githubusercontent.com/Athexblackhat/wizard/main/install.sh | bash
```

### Manual Installation

```bash
git clone https://github.com/Athexblackhat/wizard.git
cd wizard
chmod +x setup.sh
./setup.sh
# or manually:
pip3 install -r requirements.txt
python3 wizard.py
```

### Platform-Specific Instructions

<details>
<summary><b>🐧 Linux (Ubuntu/Debian)</b></summary>

```bash
sudo apt update
sudo apt install -y python3 python3-pip nmap git tor
git clone https://github.com/Athexblackhat/wizard.git
cd wizard
pip3 install -r requirements.txt
python3 wizard.py
```
</details>

<details>
<summary><b>🍎 macOS</b></summary>

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python3 nmap git tor
git clone https://github.com/Athexblackhat/wizard.git
cd wizard
pip3 install -r requirements.txt
python3 wizard.py
```
</details>

<details>
<summary><b>🪟 Windows</b></summary>

```powershell
# Install Python from python.org and nmap from nmap.org
git clone https://github.com/Athexblackhat/wizard.git
cd wizard
pip install -r requirements.txt
python wizard.py
```
</details>

<details>
<summary><b>🐳 Docker</b></summary>

```bash
docker build -t wizard-framework .
docker run -it --rm wizard-framework
# or with Docker Compose:
docker-compose up -d
docker-compose exec wizard bash
```
</details>

---

## 🚀 Quick Start

```bash
# Run WIZARD
python3 wizard.py

# Run configuration manager
python3 config.py

# Run functions test
python3 functions.py
```

### Interactive Commands

| Command | Description |
|---|---|
| `help` | Show help menu |
| `fix` | Install missing dependencies |
| `update` | Update WIZARD Framework |
| `config` | Open configuration manager |
| `exit` / `quit` / `q` | Exit WIZARD |

---

## 📖 Usage Guide

### Scan Types

#### 0. Basic Reconnaissance
```
📄 Site Title: Example Domain
🌐 IP Address: 93.184.216.34
🖥️ Web Server: ECS (dcb/7EC8)
📦 CMS: Unknown/None
☁️ Cloudflare: No Cloudflare
🤖 Robots.txt: Found (3 disallowed paths)
```

#### 1. WHOIS Lookup
```
Domain: EXAMPLE.COM
Registrar: RESERVED-Internet Assigned Numbers Authority
Creation Date: 1995-08-14
Expiration Date: 2025-08-13
```

#### 6. Port Scanner
```
PORT     STATE    SERVICE
22/tcp   filtered ssh
80/tcp   open     http
443/tcp  open     https
```

#### 9. SQLi Scanner
```
🚨 Found 2 potential SQLi vulnerabilities!
URL: http://example.com/page.php?id=1'
Parameter: id  |  Payload: '
Error: You have an error in your SQL syntax
```

#### A. Full Scan
Runs all 13 scans sequentially: Basic Recon → WHOIS → Geo-IP → Banner Grabbing → DNS → Port Scanner → Subdomain Finder → SQLi → XSS → WordPress → Directory Brute → MX Lookup → SSL Analysis.

### Advanced Usage

**Custom Timeout:**
```python
# In wizard.py
DEFAULT_TIMEOUT = 15
```

**TOR Anonymity:**
```bash
sudo service tor start
# Then in WIZARD: Settings > Anonymous Mode > Enable
#                 Settings > TOR Proxy > Enable
```

**Batch Scanning:**
```python
targets = ['example.com', 'test.com', 'demo.com']
for target in targets:
    wizard.target = target
    wizard.basic_recon()
    wizard.generate_report()
```

---

## 🔧 Configuration

### Configuration File Structure

```json
{
  "version": "3.0.0",
  "settings": {
    "theme": "dark",
    "timeout": 10,
    "max_threads": 20,
    "verify_ssl": false,
    "save_reports": true,
    "debug_mode": false
  },
  "api_keys": {
    "shodan": {
      "keys": {"api_key": "encrypted..."},
      "is_valid": true
    }
  }
}
```

### API Key Setup

```bash
# Method 1: Interactive configuration
python3 config.py

# Method 2: Environment variables
export WIZARD_SHODAN_API_KEY="your_key"
export WIZARD_MOZ_ACCESS_ID="your_id"
export WIZARD_MOZ_SECRET_KEY="your_secret"

# Method 3: Direct config edit
nano ~/.wizard/config.json
```

### Available Settings

| Setting | Type | Default | Description |
|---|---|---|---|
| `theme` | string | `dark` | UI theme (`dark`/`light`/`hacker`/`minimal`) |
| `timeout` | int | `10` | HTTP request timeout (seconds) |
| `max_threads` | int | `20` | Maximum concurrent threads |
| `verify_ssl` | bool | `false` | Verify SSL certificates |
| `save_reports` | bool | `true` | Auto-save scan reports |
| `debug_mode` | bool | `false` | Enable debug output |
| `anonymous_mode` | bool | `false` | Enable anonymous scanning |
| `tor_proxy` | bool | `false` | Route traffic through TOR |

---

## 📡 API Integration

### Free APIs

| API | Usage |
|---|---|
| HackerTarget | WHOIS, DNS Lookup, Port Scan, GeoIP |
| IP-API | Geolocation |
| crt.sh | Certificate Search |
| WPVulnDB | WordPress Vulnerabilities |

### Premium APIs

| API | Usage |
|---|---|
| Moz | Domain Authority, Page Authority |
| Shodan | Device Discovery, Service Detection |
| VirusTotal | URL Scan, File Analysis |
| Hunter.io | Email Finding |
| SecurityTrails | DNS History |

### Optional APIs

Censys, BinaryEdge, GreyNoise, AbuseIPDB, URLScan.io, BuiltWith, Wappalyzer.

### Usage Examples

```python
# Moz metrics
keys = config.get_moz_keys()
if keys:
    metrics = functions.get_moz_info_ultimate(target)

# Shodan
api_key = config.get_shodan_key()
if api_key:
    results = shodan.search(target)

# VirusTotal
api_key = config.get_virustotal_key()
if api_key:
    report = virustotal.scan_url(target)
```

---

## 🐳 Docker Deployment

```bash
# Build image
docker build -t wizard:latest .

# Run interactive
docker run -it --rm wizard

# Run with network access
docker run -it --rm --network host wizard

# Run specific scan
docker run -it --rm wizard python3 -c "
from wizard import WizardEngine
w = WizardEngine()
w.target = 'example.com'
w.protocol = 'https://'
w.basic_recon()
"

# Docker Compose
docker-compose up -d
docker-compose logs -f
docker-compose down
```

### Environment Variables

```bash
docker run -it --rm \
  -e WIZARD_DEBUG=true \
  -e WIZARD_SHODAN_API_KEY=your_key \
  -e WIZARD_MOZ_ACCESS_ID=your_id \
  -e WIZARD_MOZ_SECRET_KEY=your_secret \
  wizard
```

---

## 📊 Reports

### Formats

| Format | Method | Description |
|---|---|---|
| JSON | Auto-generated | Machine-readable, full data |
| HTML | `generate_html_report()` | Browser-viewable report |
| PDF | `generate_pdf_report()` | Professional document |

### Report Location

```
data/reports/
├── wizard_report_example_com_20240101_120000.json
├── wizard_report_example_com_20240101_120000.html
└── wizard_report_example_com_20240101_120000.pdf
```

### Sample Report Structure

```json
{
  "target": "https://example.com",
  "date": "2026-01-01T12:00:00",
  "version": "3.0.0",
  "results": {
    "basic_recon": {
      "title": "Example Domain",
      "ip": "93.184.216.34",
      "server": "ECS (dcb/7EC8)",
      "cms": "Unknown/None",
      "cloudflare": "No Cloudflare",
      "robots": "Found (3 disallowed paths)"
    },
    "whois": {},
    "geoip": {},
    "sqli": [],
    "xss": []
  }
}
```

---

## 🔒 Security

### Security Layers

- **Master Password** → AES-256 Encryption via PBKDF2 key derivation
- **Secure File Permissions** (600) enforced on all config and report files
- **TOR Proxy Support** for anonymous scanning
- **User-Agent Rotation** to avoid fingerprinting
- **Non-Root User** recommended for Docker deployments

### Best Practices

- Use a strong master password (12+ characters)
- Enable TOR for sensitive scans
- Rotate API keys regularly
- Review reports before sharing
- Keep WIZARD updated
- Run as non-root user in Docker

---

## ⚠️ Disclaimer

> **This tool is for EDUCATIONAL PURPOSES ONLY.**
>
> Always obtain proper authorization before scanning any target.
> Unauthorized scanning may violate laws and regulations.
> The authors assume no liability for misuse of this software.

---

## ❓ FAQ

<details>
<summary><b>Is WIZARD free to use?</b></summary>
Yes! WIZARD is completely free and open-source. Some advanced features require free API keys from third-party services.
</details>

<details>
<summary><b>What Python version do I need?</b></summary>
Python 3.8 or higher is required. Python 3.11+ is recommended for best performance.
</details>

<details>
<summary><b>How do I get API keys?</b></summary>
Run <code>python3 config.py</code> for interactive setup. Each API provider has a free tier — visit their websites to register and obtain keys.
</details>

<details>
<summary><b>Can I scan any website?</b></summary>
Only scan websites you own or have explicit permission to test. Unauthorized scanning is illegal in many jurisdictions.
</details>

<details>
<summary><b>How do I update WIZARD?</b></summary>

```bash
git pull origin main
pip3 install -r requirements.txt --upgrade
```
</details>

<details>
<summary><b>Where are reports saved?</b></summary>
Reports are saved in the <code>data/reports/</code> directory by default. This path is configurable in settings.
</details>

---

---

## 📄 License

```
MIT License

Copyright (c) 2026 ATHEX BLACK HAT

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

---

<div align="center">

🧙‍♂️ **WIZARD FRAMEWORK v3.0.0**

*"The Ultimate Cyber Security Platform"*

[⬆ Back to Top](#-wizard-framework-v300-phoenix)

</div>