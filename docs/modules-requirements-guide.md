# 📦 Modules ও Requirements - Complete Guide

## 📚 সূচিপত্র
1. [Core Requirements](#core-requirements)
2. [Module Installation Guide](#installation-guide)
3. [Async Programming (asyncio, aiohttp, aiofiles)](#async-programming)
4. [Web Scraping Modules](#web-scraping)
5. [Data Processing Modules](#data-processing)
6. [Utility Modules](#utility-modules)

---

## 🎯 Core Requirements {#core-requirements}

### Essential Requirements File:
```txt
# requirements.txt

# Core Web Scraping
playwright>=1.40.0
requests>=2.31.0
beautifulsoup4>=4.12.0
lxml>=4.9.0
selenium>=4.15.0

# Async Programming
aiohttp>=3.9.0
aiofiles>=23.2.0
asyncio-mqtt>=0.16.0

# Data Processing
pandas>=2.1.0
numpy>=1.24.0
openpyxl>=3.1.0
xlsxwriter>=3.1.0

# Image/PDF Processing
Pillow>=10.0.0
reportlab>=4.0.0
img2pdf>=0.5.0
PyPDF2>=3.0.0
opencv-python>=4.8.0

# QR Code & Image Generation
qrcode[pil]>=7.4.0
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.17.0

# Database
sqlite3  # Built-in
sqlalchemy>=2.0.0
pymongo>=4.5.0

# API & Networking
flask>=3.0.0
fastapi>=0.104.0
uvicorn>=0.24.0
websockets>=12.0

# Utilities
schedule>=1.2.0
python-dotenv>=1.0.0
colorama>=0.4.6
tqdm>=4.66.0
click>=8.1.0

# Cryptography & Security
cryptography>=41.0.0
hashlib  # Built-in
hmac  # Built-in

# Email & Notifications
smtplib  # Built-in
email  # Built-in
python-telegram-bot>=20.6

# File Processing
pathlib  # Built-in
zipfile  # Built-in
tarfile  # Built-in
shutil  # Built-in

# JSON & XML
json  # Built-in
xmltodict>=0.13.0
jsonpath-ng>=1.6.0

# Testing
pytest>=7.4.0
pytest-asyncio>=0.21.0
pytest-playwright>=0.4.0

# Development
black>=23.9.0
flake8>=6.1.0
mypy>=1.6.0
```

### Optional Advanced Requirements:
```txt
# requirements-advanced.txt

# AI & Machine Learning
openai>=1.3.0
transformers>=4.35.0
torch>=2.1.0
scikit-learn>=1.3.0
tensorflow>=2.14.0

# Advanced Data Processing
polars>=0.19.0
dask>=2023.10.0
apache-airflow>=2.7.0

# Advanced Visualization
bokeh>=3.3.0
altair>=5.1.0
streamlit>=1.28.0
dash>=2.14.0

# Cloud & Storage
boto3>=1.29.0
google-cloud-storage>=2.10.0
azure-storage-blob>=12.19.0

# Advanced Networking
httpx>=0.25.0
websocket-client>=1.6.0
paho-mqtt>=1.6.0

# Performance
numba>=0.58.0
cython>=3.0.0
uvloop>=0.19.0  # Linux/Mac only

# Monitoring & Logging
prometheus-client>=0.18.0
structlog>=23.2.0
sentry-sdk>=1.38.0
```

---

## 🚀 Module Installation Guide {#installation-guide}

### Step-by-Step Installation:

#### 1. Python Environment Setup:
```bash
# Create virtual environment
python -m venv playwright-env

# Activate environment
# Windows:
playwright-env\Scripts\activate
# Linux/Mac:
source playwright-env/bin/activate

# Upgrade pip
python -m pip install --upgrade pip
```

#### 2. Core Modules Installation:
```bash
# Install basic requirements
pip install -r requirements.txt

# Install Playwright browsers (IMPORTANT!)
playwright install

# Install specific browsers only
playwright install chromium
playwright install firefox
playwright install webkit
```

#### 3. Verify Installation:
```python
# test_installation.py
import sys

def test_imports():
    """Test all important module imports"""
    
    modules_to_test = [
        # Core web scraping
        ('playwright', 'playwright.sync_api'),
        ('requests', 'requests'),
        ('bs4', 'BeautifulSoup'),
        ('lxml', 'lxml'),
        
        # Async programming
        ('aiohttp', 'aiohttp'),
        ('aiofiles', 'aiofiles'),
        ('asyncio', 'asyncio'),
        
        # Data processing
        ('pandas', 'pd'),
        ('numpy', 'np'),
        ('openpyxl', 'openpyxl'),
        
        # Image/PDF
        ('PIL', 'Image'),
        ('reportlab', 'reportlab'),
        ('cv2', 'cv2'),
        
        # Utilities
        ('schedule', 'schedule'),
        ('tqdm', 'tqdm'),
        ('colorama', 'colorama')
    ]
    
    print("🧪 Testing module imports...")
    
    for module_name, import_name in modules_to_test:
        try:
            if import_name == 'playwright.sync_api':
                from playwright.sync_api import sync_playwright
                print(f"✅ {module_name}: OK")
            elif import_name == 'BeautifulSoup':
                from bs4 import BeautifulSoup
                print(f"✅ {module_name}: OK")
            elif import_name == 'Image':
                from PIL import Image
                print(f"✅ {module_name}: OK")
            elif import_name == 'pd':
                import pandas as pd
                print(f"✅ {module_name}: OK")
            elif import_name == 'np':
                import numpy as np
                print(f"✅ {module_name}: OK")
            else:
                exec(f"import {import_name}")
                print(f"✅ {module_name}: OK")
                
        except ImportError as e:
            print(f"❌ {module_name}: FAILED - {e}")
    
    print("\n🎉 Import test completed!")

if __name__ == "__main__":
    test_imports()
```

#### 4. Run Installation Test:
```bash
python test_installation.py
```

---

## ⚡ Async Programming (asyncio, aiohttp, aiofiles) {#async-programming}

### Asyncio Fundamentals:
```python
import asyncio
import time
from datetime import datetime

# Basic async function
async def basic_async_example():
    """Basic asyncio example"""
    
    print(f"🚀 Started at {datetime.now()}")
    
    # Simulate async work
    await asyncio.sleep(2)
    
    print(f"✅ Completed at {datetime.now()}")
    return "Task completed"

# Running async functions
def run_basic_async():
    """Run basic async example"""
    
    # Method 1: asyncio.run() (Python 3.7+)
    result = asyncio.run(basic_async_example())
    print(f"Result: {result}")
    
    # Method 2: Event loop (older Python versions)
    # loop = asyncio.get_event_loop()
    # result = loop.run_until_complete(basic_async_example())

# Concurrent execution
async def concurrent_tasks():
    """Run multiple tasks concurrently"""
    
    async def task(name, delay):
        print(f"🔄 Task {name} started")
        await asyncio.sleep(delay)
        print(f"✅ Task {name} completed")
        return f"Result from {name}"
    
    # Create tasks
    tasks = [
        task("A", 2),
        task("B", 1),
        task("C", 3)
    ]
    
    # Run concurrently
    start_time = time.time()
    results = await asyncio.gather(*tasks)
    end_time = time.time()
    
    print(f"⏱️ All tasks completed in {end_time - start_time:.2f} seconds")
    print(f"📊 Results: {results}")

# asyncio.run(concurrent_tasks())
```

### Aiohttp - Async HTTP Client:
```python
import aiohttp
import asyncio
import json

class AsyncHTTPClient:
    def __init__(self):
        self.session = None
    
    async def __aenter__(self):
        """Async context manager entry"""
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=30),
            headers={
                'User-Agent': 'AsyncHTTPClient/1.0'
            }
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        if self.session:
            await self.session.close()
    
    async def get(self, url, **kwargs):
        """Async GET request"""
        
        try:
            async with self.session.get(url, **kwargs) as response:
                print(f"📥 GET {url} - Status: {response.status}")
                
                # Handle different content types
                content_type = response.headers.get('content-type', '')
                
                if 'application/json' in content_type:
                    return await response.json()
                else:
                    return await response.text()
                    
        except Exception as e:
            print(f"❌ Error fetching {url}: {e}")
            return None
    
    async def post(self, url, data=None, json_data=None, **kwargs):
        """Async POST request"""
        
        try:
            async with self.session.post(
                url, 
                data=data, 
                json=json_data, 
                **kwargs
            ) as response:
                print(f"📤 POST {url} - Status: {response.status}")
                return await response.json()
                
        except Exception as e:
            print(f"❌ Error posting to {url}: {e}")
            return None
    
    async def download_file(self, url, filename):
        """Download file asynchronously"""
        
        try:
            async with self.session.get(url) as response:
                if response.status == 200:
                    # Use aiofiles for async file writing
                    import aiofiles
                    
                    async with aiofiles.open(filename, 'wb') as f:
                        async for chunk in response.content.iter_chunked(8192):
                            await f.write(chunk)
                    
                    print(f"📁 Downloaded: {filename}")
                    return True
                else:
                    print(f"❌ Download failed: {response.status}")
                    return False
                    
        except Exception as e:
            print(f"❌ Download error: {e}")
            return False

# Usage examples
async def aiohttp_examples():
    """Aiohttp usage examples"""
    
    async with AsyncHTTPClient() as client:
        # Single request
        data = await client.get('https://jsonplaceholder.typicode.com/posts/1')
        print(f"📊 Single request result: {data}")
        
        # Multiple concurrent requests
        urls = [
            'https://jsonplaceholder.typicode.com/posts/1',
            'https://jsonplaceholder.typicode.com/posts/2',
            'https://jsonplaceholder.typicode.com/posts/3'
        ]
        
        tasks = [client.get(url) for url in urls]
        results = await asyncio.gather(*tasks)
        
        print(f"📊 Concurrent requests: {len(results)} results")
        
        # File download
        await client.download_file(
            'https://httpbin.org/json',
            'downloaded_data.json'
        )

# asyncio.run(aiohttp_examples())
```

### Aiofiles - Async File Operations:
```python
import aiofiles
import asyncio
import json
from pathlib import Path

class AsyncFileProcessor:
    def __init__(self):
        self.processed_files = []
    
    async def read_text_file(self, filepath):
        """Read text file asynchronously"""
        
        try:
            async with aiofiles.open(filepath, 'r', encoding='utf-8') as f:
                content = await f.read()
                print(f"📖 Read file: {filepath} ({len(content)} chars)")
                return content
                
        except Exception as e:
            print(f"❌ Error reading {filepath}: {e}")
            return None
    
    async def write_text_file(self, filepath, content):
        """Write text file asynchronously"""
        
        try:
            async with aiofiles.open(filepath, 'w', encoding='utf-8') as f:
                await f.write(content)
                print(f"💾 Written file: {filepath}")
                return True
                
        except Exception as e:
            print(f"❌ Error writing {filepath}: {e}")
            return False
    
    async def read_json_file(self, filepath):
        """Read JSON file asynchronously"""
        
        try:
            async with aiofiles.open(filepath, 'r', encoding='utf-8') as f:
                content = await f.read()
                data = json.loads(content)
                print(f"📊 Read JSON: {filepath} ({len(data)} items)")
                return data
                
        except Exception as e:
            print(f"❌ Error reading JSON {filepath}: {e}")
            return None
    
    async def write_json_file(self, filepath, data):
        """Write JSON file asynchronously"""
        
        try:
            json_content = json.dumps(data, indent=2, ensure_ascii=False)
            
            async with aiofiles.open(filepath, 'w', encoding='utf-8') as f:
                await f.write(json_content)
                print(f"💾 Written JSON: {filepath}")
                return True
                
        except Exception as e:
            print(f"❌ Error writing JSON {filepath}: {e}")
            return False
    
    async def process_multiple_files(self, file_paths):
        """Process multiple files concurrently"""
        
        async def process_single_file(filepath):
            """Process single file"""
            
            try:
                # Read file
                content = await self.read_text_file(filepath)
                
                if content:
                    # Process content (example: count lines)
                    line_count = len(content.split('\n'))
                    
                    # Create result
                    result = {
                        'filepath': str(filepath),
                        'size': len(content),
                        'lines': line_count,
                        'processed_at': asyncio.get_event_loop().time()
                    }
                    
                    return result
                
                return None
                
            except Exception as e:
                print(f"❌ Error processing {filepath}: {e}")
                return None
        
        # Process all files concurrently
        tasks = [process_single_file(fp) for fp in file_paths]
        results = await asyncio.gather(*tasks)
        
        # Filter successful results
        successful_results = [r for r in results if r is not None]
        
        print(f"📊 Processed {len(successful_results)}/{len(file_paths)} files")
        return successful_results
    
    async def batch_file_operations(self, operations):
        """Batch file operations"""
        
        async def execute_operation(operation):
            """Execute single file operation"""
            
            op_type = operation['type']
            
            if op_type == 'read':
                return await self.read_text_file(operation['filepath'])
            
            elif op_type == 'write':
                return await self.write_text_file(
                    operation['filepath'], 
                    operation['content']
                )
            
            elif op_type == 'read_json':
                return await self.read_json_file(operation['filepath'])
            
            elif op_type == 'write_json':
                return await self.write_json_file(
                    operation['filepath'], 
                    operation['data']
                )
        
        # Execute all operations concurrently
        tasks = [execute_operation(op) for op in operations]
        results = await asyncio.gather(*tasks)
        
        return results

# Usage examples
async def aiofiles_examples():
    """Aiofiles usage examples"""
    
    processor = AsyncFileProcessor()
    
    # Single file operations
    await processor.write_text_file('test_async.txt', 'Hello Async World!')
    content = await processor.read_text_file('test_async.txt')
    
    # JSON operations
    test_data = {'name': 'Async Test', 'items': [1, 2, 3, 4, 5]}
    await processor.write_json_file('test_async.json', test_data)
    loaded_data = await processor.read_json_file('test_async.json')
    
    # Multiple file processing
    file_paths = ['file1.txt', 'file2.txt', 'file3.txt']
    
    # Create test files first
    for i, filepath in enumerate(file_paths):
        await processor.write_text_file(filepath, f'Test content for file {i+1}\nLine 2\nLine 3')
    
    # Process multiple files
    results = await processor.process_multiple_files(file_paths)
    print(f"📊 Processing results: {results}")
    
    # Batch operations
    batch_operations = [
        {'type': 'write', 'filepath': 'batch1.txt', 'content': 'Batch content 1'},
        {'type': 'write', 'filepath': 'batch2.txt', 'content': 'Batch content 2'},
        {'type': 'write_json', 'filepath': 'batch.json', 'data': {'batch': True}},
    ]
    
    batch_results = await processor.batch_file_operations(batch_operations)
    print(f"📦 Batch results: {batch_results}")

# asyncio.run(aiofiles_examples())
```

---

## 🕷️ Web Scraping Modules {#web-scraping}

### Playwright Module Deep Dive:
```python
from playwright.sync_api import sync_playwright, expect
from playwright.async_api import async_playwright
import asyncio

class PlaywrightMaster:
    def __init__(self):
        self.browsers = {}
        self.contexts = {}

    def setup_browser_options(self):
        """Browser launch options"""

        return {
            'headless': False,  # Set True for production
            'slow_mo': 100,     # Slow down for debugging
            'args': [
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-web-security',
                '--allow-running-insecure-content'
            ]
        }

    def setup_context_options(self):
        """Browser context options"""

        return {
            'viewport': {'width': 1366, 'height': 768},
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'locale': 'en-US',
            'timezone_id': 'America/New_York',
            'permissions': ['geolocation', 'notifications'],
            'extra_http_headers': {
                'Accept-Language': 'en-US,en;q=0.9'
            }
        }

    def mobile_device_emulation(self):
        """Mobile device emulation examples"""

        devices = {
            'iPhone 13': {
                'viewport': {'width': 390, 'height': 844},
                'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15',
                'device_scale_factor': 3,
                'is_mobile': True,
                'has_touch': True
            },
            'iPad': {
                'viewport': {'width': 820, 'height': 1180},
                'user_agent': 'Mozilla/5.0 (iPad; CPU OS 15_0 like Mac OS X) AppleWebKit/605.1.15',
                'device_scale_factor': 2,
                'is_mobile': True,
                'has_touch': True
            },
            'Android': {
                'viewport': {'width': 412, 'height': 915},
                'user_agent': 'Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36',
                'device_scale_factor': 2.625,
                'is_mobile': True,
                'has_touch': True
            }
        }

        return devices

# Usage example
def playwright_advanced_usage():
    """Advanced Playwright usage"""

    master = PlaywrightMaster()

    with sync_playwright() as p:
        # Launch browser with options
        browser = p.chromium.launch(**master.setup_browser_options())

        # Create context with mobile emulation
        devices = master.mobile_device_emulation()
        context = browser.new_context(**devices['iPhone 13'])

        page = context.new_page()

        # Advanced page interactions
        page.goto('https://example.com')

        # Wait for specific conditions
        page.wait_for_load_state('networkidle')
        page.wait_for_selector('.content', timeout=10000)

        # Advanced element interactions
        element = page.locator('.button')
        expect(element).to_be_visible()
        element.click()

        # Handle dialogs
        page.on('dialog', lambda dialog: dialog.accept())

        # Network interception
        def handle_route(route):
            if 'ads' in route.request.url:
                route.abort()
            else:
                route.continue_()

        page.route('**/*', handle_route)

        browser.close()

# playwright_advanced_usage()
```

### Requests Module Advanced Usage:
```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time

class AdvancedRequestsClient:
    def __init__(self):
        self.session = requests.Session()
        self.setup_session()

    def setup_session(self):
        """Setup advanced session configuration"""

        # Retry strategy
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS", "POST"]
        )

        # Mount adapter with retry strategy
        adapter = HTTPAdapter(max_retries=retry_strategy, pool_connections=20, pool_maxsize=20)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        # Default headers
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })

    def get_with_proxy(self, url, proxy_list=None):
        """GET request with proxy rotation"""

        if proxy_list:
            import random
            proxy = random.choice(proxy_list)
            proxies = {
                'http': proxy,
                'https': proxy
            }
        else:
            proxies = None

        try:
            response = self.session.get(url, proxies=proxies, timeout=30)
            response.raise_for_status()
            return response

        except Exception as e:
            print(f"❌ Request failed: {e}")
            return None

    def handle_rate_limiting(self, url, max_requests_per_minute=60):
        """Handle rate limiting"""

        request_times = []

        def make_request():
            nonlocal request_times

            # Clean old timestamps
            current_time = time.time()
            request_times = [t for t in request_times if current_time - t < 60]

            # Check rate limit
            if len(request_times) >= max_requests_per_minute:
                sleep_time = 60 - (current_time - request_times[0])
                print(f"⏱️ Rate limiting: sleeping {sleep_time:.2f} seconds")
                time.sleep(sleep_time)

            # Make request
            request_times.append(current_time)
            return self.session.get(url)

        return make_request()

# Usage
def requests_advanced_usage():
    """Advanced requests usage"""

    client = AdvancedRequestsClient()

    # Proxy list example
    proxy_list = [
        'http://proxy1:8080',
        'http://proxy2:8080',
        'socks5://proxy3:1080'
    ]

    # Make request with proxy
    response = client.get_with_proxy('https://httpbin.org/ip', proxy_list)

    if response:
        print(f"Response: {response.json()}")

# requests_advanced_usage()
```

### BeautifulSoup Advanced Parsing:
```python
from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import re

class AdvancedSoupParser:
    def __init__(self):
        self.soup = None
        self.parsed_data = {}

    def parse_html(self, html_content, parser='lxml'):
        """Parse HTML with different parsers"""

        # Available parsers: 'html.parser', 'lxml', 'xml', 'html5lib'
        self.soup = BeautifulSoup(html_content, parser)
        return self.soup

    def advanced_selectors(self):
        """Advanced CSS selectors and methods"""

        if not self.soup:
            return None

        examples = {
            # CSS Selectors
            'by_class': self.soup.select('.class-name'),
            'by_id': self.soup.select('#element-id'),
            'by_attribute': self.soup.select('[data-value="specific"]'),
            'descendant': self.soup.select('div p'),  # p inside div
            'child': self.soup.select('div > p'),     # direct child
            'sibling': self.soup.select('h1 + p'),    # next sibling
            'nth_child': self.soup.select('tr:nth-child(2n)'),  # even rows
            'contains_text': self.soup.select('a:contains("Click")'),

            # Method-based finding
            'find_by_text': self.soup.find(text=re.compile('pattern')),
            'find_by_attrs': self.soup.find('div', {'class': 'specific', 'id': 'unique'}),
            'find_all_links': self.soup.find_all('a', href=True),
            'find_by_function': self.soup.find_all(lambda tag: tag.name == 'p' and len(tag.text) > 100)
        }

        return examples

    def extract_structured_data(self):
        """Extract structured data from common patterns"""

        if not self.soup:
            return None

        structured_data = {}

        # Extract tables
        tables = self.soup.find_all('table')
        for i, table in enumerate(tables):
            table_data = []
            rows = table.find_all('tr')

            for row in rows:
                cells = row.find_all(['td', 'th'])
                row_data = [cell.get_text(strip=True) for cell in cells]
                if row_data:
                    table_data.append(row_data)

            structured_data[f'table_{i}'] = table_data

        # Extract lists
        lists = self.soup.find_all(['ul', 'ol'])
        for i, list_elem in enumerate(lists):
            items = list_elem.find_all('li')
            list_data = [item.get_text(strip=True) for item in items]
            structured_data[f'list_{i}'] = list_data

        # Extract forms
        forms = self.soup.find_all('form')
        for i, form in enumerate(forms):
            form_data = {
                'action': form.get('action'),
                'method': form.get('method', 'GET'),
                'fields': []
            }

            inputs = form.find_all(['input', 'select', 'textarea'])
            for input_elem in inputs:
                field_data = {
                    'name': input_elem.get('name'),
                    'type': input_elem.get('type'),
                    'value': input_elem.get('value'),
                    'required': input_elem.has_attr('required')
                }
                form_data['fields'].append(field_data)

            structured_data[f'form_{i}'] = form_data

        return structured_data

    def clean_text_content(self, element):
        """Clean and normalize text content"""

        if isinstance(element, NavigableString):
            text = str(element)
        elif isinstance(element, Tag):
            text = element.get_text()
        else:
            text = str(element)

        # Clean text
        text = re.sub(r'\s+', ' ', text)  # Multiple whitespace to single
        text = text.strip()
        text = re.sub(r'[^\w\s\-.,!?]', '', text)  # Remove special chars

        return text

    def extract_metadata(self):
        """Extract page metadata"""

        if not self.soup:
            return None

        metadata = {}

        # Title
        title_tag = self.soup.find('title')
        metadata['title'] = title_tag.get_text(strip=True) if title_tag else None

        # Meta tags
        meta_tags = self.soup.find_all('meta')
        for meta in meta_tags:
            name = meta.get('name') or meta.get('property') or meta.get('http-equiv')
            content = meta.get('content')

            if name and content:
                metadata[name] = content

        # Links
        links = self.soup.find_all('link')
        metadata['links'] = []
        for link in links:
            link_data = {
                'rel': link.get('rel'),
                'href': link.get('href'),
                'type': link.get('type')
            }
            metadata['links'].append(link_data)

        return metadata

# Usage example
def beautifulsoup_advanced_usage():
    """Advanced BeautifulSoup usage"""

    # Sample HTML
    html_content = """
    <html>
    <head>
        <title>Test Page</title>
        <meta name="description" content="Test description">
    </head>
    <body>
        <div class="container">
            <h1>Main Title</h1>
            <p class="intro">Introduction paragraph</p>
            <table>
                <tr><th>Name</th><th>Age</th></tr>
                <tr><td>John</td><td>25</td></tr>
                <tr><td>Jane</td><td>30</td></tr>
            </table>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
            </ul>
        </div>
    </body>
    </html>
    """

    parser = AdvancedSoupParser()
    soup = parser.parse_html(html_content)

    # Advanced selectors
    selectors = parser.advanced_selectors()
    print(f"🔍 Advanced selectors: {len(selectors)} examples")

    # Extract structured data
    structured = parser.extract_structured_data()
    print(f"📊 Structured data: {structured}")

    # Extract metadata
    metadata = parser.extract_metadata()
    print(f"📋 Metadata: {metadata}")

# beautifulsoup_advanced_usage()
```

---

## 📊 Data Processing Modules {#data-processing}

### Pandas Advanced Operations:
```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class PandasMaster:
    def __init__(self):
        self.dataframes = {}

    def create_sample_data(self):
        """Create sample data for examples"""

        np.random.seed(42)

        # Sample sales data
        dates = pd.date_range('2023-01-01', periods=1000, freq='D')

        sales_data = pd.DataFrame({
            'date': np.random.choice(dates, 1000),
            'product': np.random.choice(['A', 'B', 'C', 'D', 'E'], 1000),
            'category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home'], 1000),
            'sales': np.random.normal(1000, 300, 1000),
            'quantity': np.random.poisson(5, 1000),
            'customer_id': np.random.randint(1, 101, 1000),
            'region': np.random.choice(['North', 'South', 'East', 'West'], 1000)
        })

        # Ensure positive sales
        sales_data['sales'] = np.abs(sales_data['sales'])

        return sales_data

    def advanced_data_manipulation(self, df):
        """Advanced pandas operations"""

        # Group operations
        grouped_stats = df.groupby(['category', 'region']).agg({
            'sales': ['sum', 'mean', 'std', 'count'],
            'quantity': ['sum', 'mean'],
            'customer_id': 'nunique'
        }).round(2)

        # Pivot tables
        pivot_table = pd.pivot_table(
            df,
            values='sales',
            index='category',
            columns='region',
            aggfunc=['sum', 'mean'],
            fill_value=0
        )

        # Time series operations
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)

        # Resample by month
        monthly_sales = df.resample('M')['sales'].agg(['sum', 'mean', 'count'])

        # Rolling statistics
        df['sales_7day_avg'] = df['sales'].rolling(window=7).mean()
        df['sales_30day_avg'] = df['sales'].rolling(window=30).mean()

        # Percentage change
        monthly_sales['sales_pct_change'] = monthly_sales['sum'].pct_change()

        return {
            'grouped_stats': grouped_stats,
            'pivot_table': pivot_table,
            'monthly_sales': monthly_sales,
            'processed_df': df
        }

    def data_quality_checks(self, df):
        """Comprehensive data quality checks"""

        quality_report = {}

        # Basic info
        quality_report['shape'] = df.shape
        quality_report['memory_usage'] = df.memory_usage(deep=True).sum() / 1024**2  # MB

        # Missing values
        missing_data = df.isnull().sum()
        quality_report['missing_values'] = missing_data[missing_data > 0].to_dict()

        # Duplicates
        quality_report['duplicate_rows'] = df.duplicated().sum()

        # Data types
        quality_report['data_types'] = df.dtypes.to_dict()

        # Numeric columns statistics
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        quality_report['numeric_stats'] = df[numeric_cols].describe().to_dict()

        # Categorical columns
        categorical_cols = df.select_dtypes(include=['object']).columns
        quality_report['categorical_info'] = {}

        for col in categorical_cols:
            quality_report['categorical_info'][col] = {
                'unique_count': df[col].nunique(),
                'top_values': df[col].value_counts().head().to_dict()
            }

        return quality_report

    def advanced_filtering_and_selection(self, df):
        """Advanced filtering techniques"""

        examples = {}

        # Query method
        examples['high_sales'] = df.query('sales > 1200 and quantity > 3')

        # Multiple conditions
        examples['complex_filter'] = df[
            (df['sales'] > df['sales'].quantile(0.75)) &
            (df['category'].isin(['Electronics', 'Books'])) &
            (df['region'] != 'South')
        ]

        # String operations
        if 'product' in df.columns:
            examples['string_filter'] = df[df['product'].str.contains('A|B')]

        # Date filtering
        if 'date' in df.columns or df.index.name == 'date':
            date_col = df.index if df.index.name == 'date' else df['date']
            examples['recent_data'] = df[date_col >= '2023-06-01']

        # Statistical filtering
        examples['outliers'] = df[
            np.abs(df['sales'] - df['sales'].mean()) > 2 * df['sales'].std()
        ]

        return examples

# Usage example
def pandas_advanced_usage():
    """Advanced pandas usage examples"""

    master = PandasMaster()

    # Create sample data
    df = master.create_sample_data()
    print(f"📊 Created sample data: {df.shape}")

    # Advanced manipulations
    results = master.advanced_data_manipulation(df.copy())
    print(f"📈 Grouped stats shape: {results['grouped_stats'].shape}")
    print(f"📊 Monthly sales: {len(results['monthly_sales'])} months")

    # Data quality checks
    quality = master.data_quality_checks(df)
    print(f"🔍 Data quality report: {len(quality)} metrics")

    # Advanced filtering
    filters = master.advanced_filtering_and_selection(df)
    print(f"🎯 Filter examples: {len(filters)} types")

# pandas_advanced_usage()
```

---

## 🔧 Utility Modules {#utility-modules}

### Schedule - Task Scheduling:
```python
import schedule
import time
import threading
from datetime import datetime

class TaskScheduler:
    def __init__(self):
        self.jobs = []
        self.running = False
        self.scheduler_thread = None

    def add_daily_task(self, time_str, func, *args, **kwargs):
        """Add daily scheduled task"""

        job = schedule.every().day.at(time_str).do(func, *args, **kwargs)
        self.jobs.append(job)
        print(f"📅 Daily task scheduled at {time_str}: {func.__name__}")
        return job

    def add_interval_task(self, interval, unit, func, *args, **kwargs):
        """Add interval-based task"""

        if unit == 'seconds':
            job = schedule.every(interval).seconds.do(func, *args, **kwargs)
        elif unit == 'minutes':
            job = schedule.every(interval).minutes.do(func, *args, **kwargs)
        elif unit == 'hours':
            job = schedule.every(interval).hours.do(func, *args, **kwargs)

        self.jobs.append(job)
        print(f"⏰ Interval task scheduled every {interval} {unit}: {func.__name__}")
        return job

    def add_weekly_task(self, day, time_str, func, *args, **kwargs):
        """Add weekly scheduled task"""

        day_methods = {
            'monday': schedule.every().monday,
            'tuesday': schedule.every().tuesday,
            'wednesday': schedule.every().wednesday,
            'thursday': schedule.every().thursday,
            'friday': schedule.every().friday,
            'saturday': schedule.every().saturday,
            'sunday': schedule.every().sunday
        }

        if day.lower() in day_methods:
            job = day_methods[day.lower()].at(time_str).do(func, *args, **kwargs)
            self.jobs.append(job)
            print(f"📆 Weekly task scheduled on {day} at {time_str}: {func.__name__}")
            return job

    def start_scheduler(self):
        """Start the scheduler in a separate thread"""

        if self.running:
            print("⚠️ Scheduler is already running")
            return

        self.running = True

        def run_scheduler():
            print("🚀 Task scheduler started")
            while self.running:
                schedule.run_pending()
                time.sleep(1)
            print("🛑 Task scheduler stopped")

        self.scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
        self.scheduler_thread.start()

    def stop_scheduler(self):
        """Stop the scheduler"""
        self.running = False
        if self.scheduler_thread:
            self.scheduler_thread.join(timeout=5)

# Example scheduled functions
def backup_task():
    print(f"💾 Running backup at {datetime.now()}")

def health_check():
    print(f"🔍 Health check at {datetime.now()}")

def cleanup_task():
    print(f"🧹 Cleanup task at {datetime.now()}")

# Usage
def schedule_usage_example():
    """Schedule module usage example"""

    scheduler = TaskScheduler()

    # Add various scheduled tasks
    scheduler.add_daily_task("02:00", backup_task)
    scheduler.add_interval_task(30, "minutes", health_check)
    scheduler.add_weekly_task("sunday", "01:00", cleanup_task)

    # Start scheduler
    scheduler.start_scheduler()

    # Run for demo (in real usage, this would run indefinitely)
    time.sleep(10)
    scheduler.stop_scheduler()

# schedule_usage_example()
```

### TQDM - Progress Bars:
```python
from tqdm import tqdm, trange
import time
import requests
import threading

class ProgressTracker:
    def __init__(self):
        self.progress_bars = {}

    def basic_progress_bar(self, items):
        """Basic progress bar for iterations"""

        results = []

        # Simple progress bar
        for item in tqdm(items, desc="Processing items"):
            # Simulate work
            time.sleep(0.1)
            results.append(item * 2)

        return results

    def download_with_progress(self, url, filename):
        """Download file with progress bar"""

        try:
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))

            with open(filename, 'wb') as f:
                with tqdm(
                    total=total_size,
                    unit='B',
                    unit_scale=True,
                    desc=filename
                ) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            pbar.update(len(chunk))

            print(f"✅ Downloaded: {filename}")
            return True

        except Exception as e:
            print(f"❌ Download failed: {e}")
            return False

    def nested_progress_bars(self, outer_items, inner_items):
        """Nested progress bars"""

        results = []

        # Outer progress bar
        outer_pbar = tqdm(outer_items, desc="Outer loop", position=0)

        for outer_item in outer_pbar:
            inner_results = []

            # Inner progress bar
            inner_pbar = tqdm(
                inner_items,
                desc=f"Inner {outer_item}",
                position=1,
                leave=False
            )

            for inner_item in inner_pbar:
                # Simulate work
                time.sleep(0.01)
                inner_results.append(inner_item)

            results.append(inner_results)
            inner_pbar.close()

        outer_pbar.close()
        return results

    def manual_progress_control(self, total_steps):
        """Manual progress bar control"""

        pbar = tqdm(total=total_steps, desc="Manual progress")

        for i in range(total_steps):
            # Simulate variable work
            work_time = 0.1 + (i % 3) * 0.05
            time.sleep(work_time)

            # Update progress
            pbar.update(1)
            pbar.set_postfix({
                'step': i+1,
                'time': f'{work_time:.2f}s'
            })

        pbar.close()

    def concurrent_progress_tracking(self, tasks):
        """Track progress of concurrent tasks"""

        def worker_task(task_id, iterations):
            """Worker function with progress tracking"""

            pbar = tqdm(
                range(iterations),
                desc=f"Task {task_id}",
                position=task_id
            )

            for i in pbar:
                # Simulate work
                time.sleep(0.1)
                pbar.set_postfix({'iteration': i+1})

            pbar.close()
            return f"Task {task_id} completed"

        # Start concurrent tasks
        threads = []

        for task_id, iterations in enumerate(tasks):
            thread = threading.Thread(
                target=worker_task,
                args=(task_id, iterations)
            )
            threads.append(thread)
            thread.start()

        # Wait for all tasks to complete
        for thread in threads:
            thread.join()

        print("🎉 All concurrent tasks completed")

# Usage examples
def tqdm_usage_examples():
    """TQDM usage examples"""

    tracker = ProgressTracker()

    # Basic progress bar
    items = list(range(50))
    results = tracker.basic_progress_bar(items)
    print(f"📊 Processed {len(results)} items")

    # Download with progress (example URL)
    # tracker.download_with_progress('https://httpbin.org/json', 'test_download.json')

    # Nested progress bars
    outer = ['A', 'B', 'C']
    inner = list(range(10))
    nested_results = tracker.nested_progress_bars(outer, inner)
    print(f"🔄 Nested processing: {len(nested_results)} outer items")

    # Manual progress control
    tracker.manual_progress_control(20)

    # Concurrent progress tracking
    concurrent_tasks = [15, 20, 10, 25]  # Different iteration counts
    tracker.concurrent_progress_tracking(concurrent_tasks)

# tqdm_usage_examples()
```

### Colorama - Colored Terminal Output:
```python
from colorama import init, Fore, Back, Style
import sys

# Initialize colorama
init(autoreset=True)

class ColoredLogger:
    def __init__(self):
        self.colors = {
            'info': Fore.BLUE,
            'success': Fore.GREEN,
            'warning': Fore.YELLOW,
            'error': Fore.RED,
            'critical': Fore.MAGENTA,
            'debug': Fore.CYAN
        }

        self.backgrounds = {
            'highlight': Back.YELLOW,
            'error_bg': Back.RED,
            'success_bg': Back.GREEN
        }

    def info(self, message):
        """Info message in blue"""
        print(f"{self.colors['info']}ℹ️  INFO: {message}")

    def success(self, message):
        """Success message in green"""
        print(f"{self.colors['success']}✅ SUCCESS: {message}")

    def warning(self, message):
        """Warning message in yellow"""
        print(f"{self.colors['warning']}⚠️  WARNING: {message}")

    def error(self, message):
        """Error message in red"""
        print(f"{self.colors['error']}❌ ERROR: {message}")

    def critical(self, message):
        """Critical message in magenta with background"""
        print(f"{self.backgrounds['error_bg']}{Fore.WHITE}🚨 CRITICAL: {message}")

    def debug(self, message):
        """Debug message in cyan"""
        print(f"{self.colors['debug']}🐛 DEBUG: {message}")

    def highlight(self, message):
        """Highlighted message"""
        print(f"{self.backgrounds['highlight']}{Fore.BLACK}🌟 {message}")

    def progress_indicator(self, current, total, message="Progress"):
        """Colored progress indicator"""

        percentage = (current / total) * 100

        if percentage < 30:
            color = Fore.RED
        elif percentage < 70:
            color = Fore.YELLOW
        else:
            color = Fore.GREEN

        bar_length = 20
        filled_length = int(bar_length * current // total)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)

        print(f"\r{color}{message}: |{bar}| {percentage:.1f}% ({current}/{total})", end='')

        if current == total:
            print()  # New line when complete

    def table_output(self, headers, rows):
        """Colored table output"""

        # Print headers
        header_line = " | ".join(f"{Fore.CYAN}{Style.BRIGHT}{header:<15}" for header in headers)
        print(header_line)
        print("-" * len(header_line.replace(Fore.CYAN + Style.BRIGHT, "")))

        # Print rows
        for i, row in enumerate(rows):
            row_color = Fore.WHITE if i % 2 == 0 else Fore.LIGHTBLACK_EX
            row_line = " | ".join(f"{row_color}{str(cell):<15}" for cell in row)
            print(row_line)

# Usage examples
def colorama_usage_examples():
    """Colorama usage examples"""

    logger = ColoredLogger()

    # Different log levels
    logger.info("This is an info message")
    logger.success("Operation completed successfully")
    logger.warning("This is a warning message")
    logger.error("An error occurred")
    logger.critical("Critical system error")
    logger.debug("Debug information")
    logger.highlight("Important highlighted message")

    print()  # Spacing

    # Progress indicator
    print("Progress indicator example:")
    for i in range(101):
        logger.progress_indicator(i, 100, "Loading")
        time.sleep(0.02)

    print()  # Spacing

    # Table output
    headers = ['Name', 'Age', 'City']
    rows = [
        ['John Doe', '25', 'New York'],
        ['Jane Smith', '30', 'Los Angeles'],
        ['Bob Johnson', '35', 'Chicago']
    ]

    print("Colored table example:")
    logger.table_output(headers, rows)

# colorama_usage_examples()
```

---

## 🎯 Complete Integration Example {#complete-example}

### Real-World Project: E-commerce Data Scraper
```python
import asyncio
import aiohttp
import aiofiles
from playwright.async_api import async_playwright
import pandas as pd
from tqdm.asyncio import tqdm
from colorama import Fore, init
import json
from datetime import datetime
import schedule
import threading

init(autoreset=True)

class EcommerceDataScraper:
    def __init__(self):
        self.session = None
        self.browser = None
        self.context = None
        self.scraped_data = []
        self.logger = ColoredLogger()

    async def __aenter__(self):
        """Async context manager entry"""

        # Initialize aiohttp session
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=30)
        )

        # Initialize Playwright
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.context = await self.browser.new_context(
            viewport={'width': 1366, 'height': 768},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )

        self.logger.success("Scraper initialized successfully")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""

        if self.session:
            await self.session.close()

        if self.context:
            await self.context.close()

        if self.browser:
            await self.browser.close()

        if hasattr(self, 'playwright'):
            await self.playwright.stop()

        self.logger.info("Scraper cleanup completed")

    async def scrape_product_data(self, product_urls):
        """Scrape product data from multiple URLs"""

        self.logger.info(f"Starting to scrape {len(product_urls)} products")

        # Create semaphore for rate limiting
        semaphore = asyncio.Semaphore(5)  # Max 5 concurrent requests

        async def scrape_single_product(url):
            async with semaphore:
                try:
                    page = await self.context.new_page()
                    await page.goto(url)
                    await page.wait_for_load_state('networkidle')

                    # Extract product data
                    product_data = await page.evaluate("""
                        () => {
                            return {
                                title: document.querySelector('h1')?.textContent?.trim(),
                                price: document.querySelector('.price')?.textContent?.trim(),
                                description: document.querySelector('.description')?.textContent?.trim(),
                                rating: document.querySelector('.rating')?.textContent?.trim(),
                                availability: document.querySelector('.availability')?.textContent?.trim(),
                                url: window.location.href
                            };
                        }
                    """)

                    await page.close()
                    return product_data

                except Exception as e:
                    self.logger.error(f"Error scraping {url}: {e}")
                    return None

        # Execute scraping with progress bar
        tasks = [scrape_single_product(url) for url in product_urls]
        results = []

        for coro in tqdm.as_completed(tasks, desc="Scraping products"):
            result = await coro
            if result:
                results.append(result)

        self.scraped_data.extend(results)
        self.logger.success(f"Scraped {len(results)} products successfully")

        return results

    async def save_data_async(self, data, filename):
        """Save data asynchronously using aiofiles"""

        try:
            # Save as JSON
            json_filename = f"{filename}.json"
            async with aiofiles.open(json_filename, 'w', encoding='utf-8') as f:
                await f.write(json.dumps(data, indent=2, ensure_ascii=False))

            # Save as CSV using pandas
            df = pd.DataFrame(data)
            csv_filename = f"{filename}.csv"
            df.to_csv(csv_filename, index=False)

            self.logger.success(f"Data saved to {json_filename} and {csv_filename}")
            return True

        except Exception as e:
            self.logger.error(f"Error saving data: {e}")
            return False

    def analyze_scraped_data(self):
        """Analyze scraped data using pandas"""

        if not self.scraped_data:
            self.logger.warning("No data to analyze")
            return None

        df = pd.DataFrame(self.scraped_data)

        # Clean price data
        if 'price' in df.columns:
            df['price_numeric'] = df['price'].str.extract(r'(\d+\.?\d*)').astype(float)

        # Basic analysis
        analysis = {
            'total_products': len(df),
            'average_price': df['price_numeric'].mean() if 'price_numeric' in df.columns else None,
            'price_range': {
                'min': df['price_numeric'].min() if 'price_numeric' in df.columns else None,
                'max': df['price_numeric'].max() if 'price_numeric' in df.columns else None
            },
            'availability_stats': df['availability'].value_counts().to_dict() if 'availability' in df.columns else None
        }

        self.logger.info(f"Analysis completed: {analysis}")
        return analysis

    def schedule_scraping_job(self, product_urls, schedule_time="02:00"):
        """Schedule regular scraping job"""

        def run_scraping_job():
            """Wrapper function for scheduled scraping"""

            async def async_scraping_job():
                async with EcommerceDataScraper() as scraper:
                    await scraper.scrape_product_data(product_urls)

                    # Save data with timestamp
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    await scraper.save_data_async(
                        scraper.scraped_data,
                        f"scraped_data_{timestamp}"
                    )

                    # Analyze data
                    analysis = scraper.analyze_scraped_data()

                    # Save analysis
                    if analysis:
                        async with aiofiles.open(
                            f"analysis_{timestamp}.json",
                            'w',
                            encoding='utf-8'
                        ) as f:
                            await f.write(json.dumps(analysis, indent=2))

            # Run async function
            asyncio.run(async_scraping_job())

        # Schedule the job
        schedule.every().day.at(schedule_time).do(run_scraping_job)

        self.logger.success(f"Scraping job scheduled for {schedule_time} daily")

        # Start scheduler in background thread
        def run_scheduler():
            while True:
                schedule.run_pending()
                time.sleep(60)

        scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
        scheduler_thread.start()

# Usage example
async def complete_scraping_example():
    """Complete scraping workflow example"""

    # Sample product URLs (replace with real URLs)
    product_urls = [
        "https://example-shop.com/product/1",
        "https://example-shop.com/product/2",
        "https://example-shop.com/product/3",
        # Add more URLs...
    ]

    async with EcommerceDataScraper() as scraper:
        # Scrape product data
        products = await scraper.scrape_product_data(product_urls)

        # Save data
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        await scraper.save_data_async(products, f"products_{timestamp}")

        # Analyze data
        analysis = scraper.analyze_scraped_data()

        # Schedule regular scraping
        scraper.schedule_scraping_job(product_urls, "02:00")

        print(f"🎉 Scraping workflow completed!")
        print(f"📊 Scraped {len(products)} products")
        print(f"📈 Analysis: {analysis}")

# Run the complete example
# asyncio.run(complete_scraping_example())
```

---

## 🎉 সমাপনী

এই Modules ও Requirements গাইডে আপনি পেয়েছেন:

✅ **Complete Requirements List:** সব প্রয়োজনীয় modules
✅ **Installation Guide:** Step-by-step setup process
✅ **Async Programming:** asyncio, aiohttp, aiofiles mastery
✅ **Web Scraping Modules:** Playwright, Requests, BeautifulSoup
✅ **Data Processing:** Pandas advanced operations
✅ **Utility Modules:** Schedule, TQDM, Colorama
✅ **Complete Integration:** Real-world project example

### 🚀 Key Takeaways:

1. **Always use virtual environments** for project isolation
2. **Install Playwright browsers** after installing the package
3. **Use async programming** for better performance
4. **Combine multiple modules** for powerful solutions
5. **Test your installation** before starting projects

### 📦 Quick Installation Commands:
```bash
# Create environment
python -m venv myproject-env
source myproject-env/bin/activate  # Linux/Mac
# myproject-env\Scripts\activate  # Windows

# Install requirements
pip install -r requirements.txt
playwright install

# Test installation
python test_installation.py
```

**Happy Module Mastery! 📦🚀**
```
```
