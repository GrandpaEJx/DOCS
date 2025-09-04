# 🍪 Cookies ও Session Management - Complete Guide

## 📚 সূচিপত্র
1. [Cookies কি এবং কেন?](#what-are-cookies)
2. [Playwright দিয়ে Cookie Management](#playwright-cookies)
3. [Requests দিয়ে Session Management](#requests-sessions)
4. [Aiohttp দিয়ে Async Sessions](#aiohttp-sessions)
5. [Advanced Cookie Techniques](#advanced-techniques)
6. [Real-World Examples](#real-world-examples)

---

## 🤔 Cookies কি এবং কেন? {#what-are-cookies}

### 🍪 Cookie কি?
**Cookie** হলো ছোট text files যা web browser এ store হয়। এগুলো দিয়ে:
- **Authentication:** Login state maintain করা
- **Personalization:** User preferences save করা
- **Tracking:** User behavior track করা
- **Shopping Cart:** E-commerce cart data রাখা

### 🔍 Cookie এর Structure:
```
Name=Value; Domain=example.com; Path=/; Expires=Wed, 09 Jun 2024 10:18:14 GMT; HttpOnly; Secure
```

**Components:**
- **Name=Value:** Cookie এর data
- **Domain:** কোন domain এর জন্য valid
- **Path:** কোন path এর জন্য valid
- **Expires/Max-Age:** কখন expire হবে
- **HttpOnly:** JavaScript access করতে পারবে না
- **Secure:** শুধু HTTPS এ send হবে
- **SameSite:** Cross-site request control

### 🎯 কেন Cookie Management গুরুত্বপূর্ণ?
- **Login Required Sites:** Authentication maintain করা
- **Personalized Content:** User-specific data access
- **Rate Limiting:** Same session এ multiple requests
- **E-commerce:** Shopping cart maintain করা

---

## 🎭 Playwright দিয়ে Cookie Management {#playwright-cookies}

### Basic Cookie Operations:
```python
from playwright.sync_api import sync_playwright
import json
import os

def basic_cookie_operations():
    """Playwright এ basic cookie operations"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Website এ যান
        page.goto("https://httpbin.org/cookies/set/test_cookie/hello_world")
        
        # Current cookies get করা
        cookies = context.cookies()
        print("🍪 Current Cookies:")
        for cookie in cookies:
            print(f"  {cookie['name']}: {cookie['value']}")
        
        # Specific cookie get করা
        test_cookie = context.cookies("https://httpbin.org")
        print(f"\n🎯 Specific site cookies: {len(test_cookie)}")
        
        browser.close()

basic_cookie_operations()
```

### Cookie Save ও Load:
```python
def save_and_load_cookies():
    """Cookies save করে পরে load করা"""
    
    cookie_file = "saved_cookies.json"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Login page এ যান
        page.goto("https://httpbin.org/cookies/set/session_id/abc123")
        page.goto("https://httpbin.org/cookies/set/user_pref/dark_mode")
        
        # Cookies save করা
        cookies = context.cookies()
        with open(cookie_file, 'w') as f:
            json.dump(cookies, f, indent=2)
        
        print(f"💾 Cookies saved to {cookie_file}")
        browser.close()
    
    # নতুন session এ cookies load করা
    print("\n🔄 Loading cookies in new session...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        
        # Saved cookies load করা
        if os.path.exists(cookie_file):
            with open(cookie_file, 'r') as f:
                saved_cookies = json.load(f)
            
            context.add_cookies(saved_cookies)
            print(f"✅ Loaded {len(saved_cookies)} cookies")
        
        page = context.new_page()
        
        # Cookies verify করা
        page.goto("https://httpbin.org/cookies")
        cookies_response = page.text_content("pre")
        print(f"🔍 Loaded cookies verification:\n{cookies_response}")
        
        browser.close()

save_and_load_cookies()
```

### Advanced Cookie Management:
```python
def advanced_cookie_management():
    """Advanced cookie operations"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Manual cookie add করা
        context.add_cookies([
            {
                'name': 'custom_session',
                'value': 'user_12345',
                'domain': 'httpbin.org',
                'path': '/',
                'expires': 1735689600,  # Unix timestamp
                'httpOnly': True,
                'secure': False,
                'sameSite': 'Lax'
            },
            {
                'name': 'theme',
                'value': 'dark',
                'domain': 'httpbin.org',
                'path': '/'
            }
        ])
        
        print("✅ Custom cookies added")
        
        # Website এ যান
        page.goto("https://httpbin.org/cookies")
        
        # Cookie modify করা (JavaScript দিয়ে)
        page.evaluate("""
            document.cookie = 'modified_cookie=new_value; path=/';
            document.cookie = 'temp_cookie=temporary; path=/; max-age=3600';
        """)
        
        # Updated cookies get করা
        updated_cookies = context.cookies()
        print(f"\n🔄 Updated cookies ({len(updated_cookies)}):")
        for cookie in updated_cookies:
            print(f"  {cookie['name']}: {cookie['value']}")
        
        # Specific cookie clear করা
        context.clear_cookies()
        print("\n🗑️ All cookies cleared")
        
        # Verify clearing
        final_cookies = context.cookies()
        print(f"Final cookie count: {len(final_cookies)}")
        
        browser.close()

advanced_cookie_management()
```

### Login Session Management:
```python
def login_session_management(username, password, login_url):
    """Complete login session management"""
    
    session_file = f"session_{username}.json"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Check if session exists
        if os.path.exists(session_file):
            print("🔍 Checking existing session...")
            
            with open(session_file, 'r') as f:
                saved_cookies = json.load(f)
            
            context.add_cookies(saved_cookies)
            
            # Test if session is still valid
            page.goto(login_url.replace('/login', '/dashboard'))  # Assume dashboard URL
            
            if page.locator('.dashboard, .profile, .logout').is_visible():
                print("✅ Existing session is valid!")
                return context, page
            else:
                print("⚠️ Session expired, logging in again...")
        
        # Perform fresh login
        print("🔐 Performing login...")
        page.goto(login_url)
        
        # Fill login form
        page.fill('input[name="username"], input[type="email"]', username)
        page.fill('input[name="password"], input[type="password"]', password)
        
        # Handle CSRF token if present
        csrf_input = page.locator('input[name="csrf_token"], input[name="_token"]')
        if csrf_input.is_visible():
            csrf_value = csrf_input.get_attribute('value')
            print(f"🛡️ CSRF Token found: {csrf_value[:20]}...")
        
        # Submit form
        page.click('button[type="submit"], input[type="submit"]')
        
        # Wait for login result
        try:
            page.wait_for_url('**/dashboard', timeout=10000)
            print("✅ Login successful!")
            
            # Save session cookies
            session_cookies = context.cookies()
            with open(session_file, 'w') as f:
                json.dump(session_cookies, f, indent=2)
            
            print(f"💾 Session saved with {len(session_cookies)} cookies")
            
            return context, page
            
        except:
            error_msg = page.locator('.error, .alert-danger').text_content()
            print(f"❌ Login failed: {error_msg}")
            return None, None
        
        finally:
            # Don't close browser here, return for further use
            pass

# Usage
# context, page = login_session_management("user@example.com", "password123", "https://example.com/login")
```

### Cookie-based Web Scraping:
```python
def cookie_based_scraping():
    """Cookie maintain করে data scraping"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Initial login
        page.goto("https://quotes.toscrape.com/login")
        page.fill('input[name="username"]', 'admin')
        page.fill('input[name="password"]', 'admin')
        page.click('input[type="submit"]')
        
        # Wait for login
        page.wait_for_url('**/quotes')
        print("✅ Logged in successfully")
        
        # Get session cookies
        session_cookies = context.cookies()
        print(f"🍪 Session has {len(session_cookies)} cookies")
        
        # Scrape multiple pages with same session
        all_quotes = []
        
        for page_num in range(1, 4):  # Pages 1-3
            page_url = f"https://quotes.toscrape.com/page/{page_num}/"
            page.goto(page_url)
            
            # Extract quotes
            quotes = page.locator('.quote').all()
            
            for quote in quotes:
                quote_data = {
                    'text': quote.locator('.text').text_content(),
                    'author': quote.locator('.author').text_content(),
                    'tags': [tag.text_content() for tag in quote.locator('.tag').all()],
                    'page': page_num
                }
                all_quotes.append(quote_data)
            
            print(f"📄 Page {page_num}: {len(quotes)} quotes")
        
        print(f"🎉 Total quotes scraped: {len(all_quotes)}")
        
        # Logout
        logout_btn = page.locator('a[href="/logout"]')
        if logout_btn.is_visible():
            logout_btn.click()
            print("👋 Logged out")
        
        browser.close()
        return all_quotes

# quotes = cookie_based_scraping()
```

---

## 🌐 Requests দিয়ে Session Management {#requests-sessions}

### Basic Session Usage:
```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def basic_requests_session():
    """Requests দিয়ে basic session management"""
    
    # Session তৈরি করা
    session = requests.Session()
    
    # Headers set করা
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    })
    
    # Retry strategy
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504]
    )
    
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    # Test requests
    response = session.get('https://httpbin.org/cookies/set/test/value')
    print(f"🍪 Cookies set: {response.cookies}")
    
    # Cookies automatically maintained
    response2 = session.get('https://httpbin.org/cookies')
    print(f"📋 Cookie verification: {response2.json()}")
    
    return session

session = basic_requests_session()
```

### Advanced Session with Cookie Persistence:
```python
import pickle
import os
from datetime import datetime

class PersistentSession:
    def __init__(self, cookie_file="session_cookies.pkl"):
        self.cookie_file = cookie_file
        self.session = requests.Session()
        self.setup_session()
        self.load_cookies()
    
    def setup_session(self):
        """Session configuration"""
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        # Retry strategy
        retry_strategy = Retry(total=3, backoff_factor=1)
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
    
    def load_cookies(self):
        """Saved cookies load করা"""
        if os.path.exists(self.cookie_file):
            try:
                with open(self.cookie_file, 'rb') as f:
                    cookies = pickle.load(f)
                    self.session.cookies.update(cookies)
                print(f"✅ Loaded cookies from {self.cookie_file}")
            except Exception as e:
                print(f"⚠️ Error loading cookies: {e}")
    
    def save_cookies(self):
        """Current cookies save করা"""
        try:
            with open(self.cookie_file, 'wb') as f:
                pickle.dump(self.session.cookies, f)
            print(f"💾 Cookies saved to {self.cookie_file}")
        except Exception as e:
            print(f"❌ Error saving cookies: {e}")
    
    def login(self, login_url, username, password):
        """Login with cookie persistence"""
        
        # Get login page
        response = self.session.get(login_url)
        
        # Extract CSRF token if present
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        csrf_token = None
        csrf_input = soup.find('input', {'name': ['csrf_token', '_token', 'authenticity_token']})
        if csrf_input:
            csrf_token = csrf_input.get('value')
            print(f"🛡️ CSRF Token: {csrf_token[:20]}...")
        
        # Prepare login data
        login_data = {
            'username': username,
            'password': password
        }
        
        if csrf_token:
            login_data['csrf_token'] = csrf_token
        
        # Submit login
        response = self.session.post(login_url, data=login_data)
        
        if response.status_code == 200:
            # Check if login successful
            if 'dashboard' in response.url or 'profile' in response.text.lower():
                print("✅ Login successful!")
                self.save_cookies()
                return True
            else:
                print("❌ Login failed - check credentials")
                return False
        else:
            print(f"❌ Login request failed: {response.status_code}")
            return False
    
    def get(self, url, **kwargs):
        """GET request with automatic cookie handling"""
        response = self.session.get(url, **kwargs)
        self.save_cookies()  # Save cookies after each request
        return response
    
    def post(self, url, **kwargs):
        """POST request with automatic cookie handling"""
        response = self.session.post(url, **kwargs)
        self.save_cookies()
        return response
    
    def close(self):
        """Session cleanup"""
        self.save_cookies()
        self.session.close()

# Usage
def use_persistent_session():
    """Persistent session ব্যবহার করা"""
    
    ps = PersistentSession("my_site_cookies.pkl")
    
    try:
        # Login (only needed first time)
        # ps.login("https://example.com/login", "username", "password")
        
        # Make requests (cookies automatically maintained)
        response1 = ps.get("https://httpbin.org/cookies/set/test/persistent")
        print(f"Response 1: {response1.status_code}")
        
        response2 = ps.get("https://httpbin.org/cookies")
        print(f"Cookies maintained: {response2.json()}")
        
    finally:
        ps.close()

use_persistent_session()
```

### Session-based Web Scraping:
```python
def session_based_scraping():
    """Session maintain করে web scraping"""
    
    session = requests.Session()
    
    # Headers setup
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    
    scraped_data = []
    
    try:
        # Login first
        login_url = "https://quotes.toscrape.com/login"
        login_page = session.get(login_url)
        
        # Parse login form
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(login_page.content, 'html.parser')
        
        # Get CSRF token
        csrf_input = soup.find('input', {'name': 'csrf_token'})
        csrf_token = csrf_input['value'] if csrf_input else None
        
        # Login data
        login_data = {
            'username': 'admin',
            'password': 'admin'
        }
        
        if csrf_token:
            login_data['csrf_token'] = csrf_token
        
        # Submit login
        login_response = session.post(login_url, data=login_data)
        
        if login_response.status_code == 200:
            print("✅ Login successful")
            
            # Scrape multiple pages
            for page_num in range(1, 4):
                page_url = f"https://quotes.toscrape.com/page/{page_num}/"
                response = session.get(page_url)
                
                soup = BeautifulSoup(response.content, 'html.parser')
                quotes = soup.find_all('div', class_='quote')
                
                for quote in quotes:
                    quote_data = {
                        'text': quote.find('span', class_='text').text,
                        'author': quote.find('small', class_='author').text,
                        'tags': [tag.text for tag in quote.find_all('a', class_='tag')],
                        'page': page_num
                    }
                    scraped_data.append(quote_data)
                
                print(f"📄 Page {page_num}: {len(quotes)} quotes")
        
        else:
            print("❌ Login failed")
    
    except Exception as e:
        print(f"❌ Error: {e}")
    
    finally:
        session.close()
    
    return scraped_data

# quotes = session_based_scraping()
```

---

## ⚡ Aiohttp দিয়ে Async Sessions {#aiohttp-sessions}

### Basic Async Session:
```python
import aiohttp
import asyncio
import json
import aiofiles

async def basic_aiohttp_session():
    """Aiohttp দিয়ে basic async session"""

    # Cookie jar তৈরি
    jar = aiohttp.CookieJar()

    async with aiohttp.ClientSession(cookie_jar=jar) as session:
        # Headers set করা
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

        # Cookie set করা
        async with session.get('https://httpbin.org/cookies/set/async_test/hello') as response:
            print(f"🍪 Cookie set: {response.status}")

        # Cookie verify করা
        async with session.get('https://httpbin.org/cookies') as response:
            data = await response.json()
            print(f"📋 Cookies: {data}")

        return session

# asyncio.run(basic_aiohttp_session())
```

### Persistent Async Session:
```python
class AsyncPersistentSession:
    def __init__(self, cookie_file="async_cookies.json"):
        self.cookie_file = cookie_file
        self.jar = aiohttp.CookieJar()
        self.session = None

    async def __aenter__(self):
        await self.load_cookies()
        self.session = aiohttp.ClientSession(
            cookie_jar=self.jar,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.save_cookies()
        if self.session:
            await self.session.close()

    async def load_cookies(self):
        """Saved cookies load করা"""
        try:
            if os.path.exists(self.cookie_file):
                async with aiofiles.open(self.cookie_file, 'r') as f:
                    content = await f.read()
                    cookies_data = json.loads(content)

                # Cookies restore করা
                for cookie_data in cookies_data:
                    self.jar.update_cookies([cookie_data])

                print(f"✅ Loaded {len(cookies_data)} cookies")
        except Exception as e:
            print(f"⚠️ Error loading cookies: {e}")

    async def save_cookies(self):
        """Current cookies save করা"""
        try:
            cookies_data = []
            for cookie in self.jar:
                cookies_data.append({
                    'name': cookie.key,
                    'value': cookie.value,
                    'domain': cookie['domain'],
                    'path': cookie['path']
                })

            async with aiofiles.open(self.cookie_file, 'w') as f:
                await f.write(json.dumps(cookies_data, indent=2))

            print(f"💾 Saved {len(cookies_data)} cookies")
        except Exception as e:
            print(f"❌ Error saving cookies: {e}")

    async def login(self, login_url, username, password):
        """Async login with cookie persistence"""

        try:
            # Get login page
            async with self.session.get(login_url) as response:
                html = await response.text()

            # Extract CSRF token
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, 'html.parser')
            csrf_input = soup.find('input', {'name': ['csrf_token', '_token']})
            csrf_token = csrf_input['value'] if csrf_input else None

            # Prepare login data
            login_data = {
                'username': username,
                'password': password
            }

            if csrf_token:
                login_data['csrf_token'] = csrf_token

            # Submit login
            async with self.session.post(login_url, data=login_data) as response:
                if response.status == 200:
                    response_text = await response.text()
                    if 'dashboard' in str(response.url) or 'profile' in response_text.lower():
                        print("✅ Async login successful!")
                        await self.save_cookies()
                        return True
                    else:
                        print("❌ Login failed")
                        return False
                else:
                    print(f"❌ Login request failed: {response.status}")
                    return False

        except Exception as e:
            print(f"❌ Login error: {e}")
            return False

# Usage
async def use_async_session():
    """Async session ব্যবহার করা"""

    async with AsyncPersistentSession("async_site_cookies.json") as session:
        # Login (if needed)
        # await session.login("https://example.com/login", "username", "password")

        # Make requests
        async with session.session.get("https://httpbin.org/cookies/set/async/working") as response:
            print(f"Response: {response.status}")

        async with session.session.get("https://httpbin.org/cookies") as response:
            data = await response.json()
            print(f"Cookies maintained: {data}")

# asyncio.run(use_async_session())
```

### Concurrent Scraping with Sessions:
```python
async def concurrent_scraping_with_cookies():
    """Multiple sites concurrent scraping with cookie management"""

    sites = [
        {"name": "site1", "url": "https://httpbin.org/cookies/set/site1/value1"},
        {"name": "site2", "url": "https://httpbin.org/cookies/set/site2/value2"},
        {"name": "site3", "url": "https://httpbin.org/cookies/set/site3/value3"}
    ]

    async def scrape_site(site_info):
        """Single site scrape করা"""

        jar = aiohttp.CookieJar()

        async with aiohttp.ClientSession(cookie_jar=jar) as session:
            try:
                # Set initial cookie
                async with session.get(site_info["url"]) as response:
                    print(f"🍪 {site_info['name']}: Cookie set ({response.status})")

                # Verify cookie
                async with session.get("https://httpbin.org/cookies") as response:
                    data = await response.json()
                    return {
                        "site": site_info["name"],
                        "cookies": data.get("cookies", {}),
                        "status": "success"
                    }

            except Exception as e:
                return {
                    "site": site_info["name"],
                    "error": str(e),
                    "status": "failed"
                }

    # Concurrent execution
    tasks = [scrape_site(site) for site in sites]
    results = await asyncio.gather(*tasks)

    # Process results
    for result in results:
        if result["status"] == "success":
            print(f"✅ {result['site']}: {result['cookies']}")
        else:
            print(f"❌ {result['site']}: {result['error']}")

    return results

# asyncio.run(concurrent_scraping_with_cookies())
```

---

## 🔧 Advanced Cookie Techniques {#advanced-techniques}

### Cookie Encryption ও Security:
```python
from cryptography.fernet import Fernet
import base64

class SecureCookieManager:
    def __init__(self, key=None):
        if key:
            self.key = key
        else:
            self.key = Fernet.generate_key()

        self.cipher = Fernet(self.key)

    def encrypt_cookies(self, cookies_dict):
        """Cookies encrypt করা"""
        try:
            cookies_json = json.dumps(cookies_dict)
            encrypted_data = self.cipher.encrypt(cookies_json.encode())
            return base64.b64encode(encrypted_data).decode()
        except Exception as e:
            print(f"❌ Encryption error: {e}")
            return None

    def decrypt_cookies(self, encrypted_data):
        """Cookies decrypt করা"""
        try:
            encrypted_bytes = base64.b64decode(encrypted_data.encode())
            decrypted_data = self.cipher.decrypt(encrypted_bytes)
            return json.loads(decrypted_data.decode())
        except Exception as e:
            print(f"❌ Decryption error: {e}")
            return {}

    def save_secure_cookies(self, cookies_dict, filename):
        """Encrypted cookies save করা"""
        encrypted_data = self.encrypt_cookies(cookies_dict)
        if encrypted_data:
            with open(filename, 'w') as f:
                f.write(encrypted_data)
            print(f"🔐 Secure cookies saved to {filename}")

    def load_secure_cookies(self, filename):
        """Encrypted cookies load করা"""
        try:
            with open(filename, 'r') as f:
                encrypted_data = f.read()
            return self.decrypt_cookies(encrypted_data)
        except Exception as e:
            print(f"❌ Error loading secure cookies: {e}")
            return {}

# Usage
def use_secure_cookies():
    """Secure cookie management"""

    # Create secure manager
    secure_manager = SecureCookieManager()

    # Sample cookies
    cookies = {
        "session_id": "abc123xyz",
        "user_token": "secret_token_here",
        "preferences": "dark_mode=true"
    }

    # Save securely
    secure_manager.save_secure_cookies(cookies, "secure_cookies.enc")

    # Load securely
    loaded_cookies = secure_manager.load_secure_cookies("secure_cookies.enc")
    print(f"🔓 Loaded secure cookies: {loaded_cookies}")

use_secure_cookies()
```

### Cookie Analytics ও Monitoring:
```python
from datetime import datetime, timedelta
import sqlite3

class CookieAnalytics:
    def __init__(self, db_file="cookie_analytics.db"):
        self.db_file = db_file
        self.init_database()

    def init_database(self):
        """Database initialize করা"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cookie_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                domain TEXT,
                cookie_name TEXT,
                cookie_value TEXT,
                timestamp DATETIME,
                action TEXT,
                session_id TEXT
            )
        ''')

        conn.commit()
        conn.close()

    def log_cookie_action(self, domain, cookie_name, cookie_value, action, session_id):
        """Cookie action log করা"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO cookie_logs (domain, cookie_name, cookie_value, timestamp, action, session_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (domain, cookie_name, cookie_value, datetime.now(), action, session_id))

        conn.commit()
        conn.close()

    def get_cookie_stats(self, domain=None, days=7):
        """Cookie statistics"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        since_date = datetime.now() - timedelta(days=days)

        if domain:
            cursor.execute('''
                SELECT action, COUNT(*) as count
                FROM cookie_logs
                WHERE domain = ? AND timestamp > ?
                GROUP BY action
            ''', (domain, since_date))
        else:
            cursor.execute('''
                SELECT domain, action, COUNT(*) as count
                FROM cookie_logs
                WHERE timestamp > ?
                GROUP BY domain, action
            ''', (since_date,))

        results = cursor.fetchall()
        conn.close()

        return results

    def monitor_cookies(self, session, session_id):
        """Session cookies monitor করা"""

        # Get current cookies
        if hasattr(session, 'cookies'):  # requests session
            for cookie in session.cookies:
                self.log_cookie_action(
                    cookie.domain,
                    cookie.name,
                    cookie.value[:50],  # First 50 chars only
                    "set",
                    session_id
                )

        print(f"📊 Cookie monitoring active for session: {session_id}")

# Usage
def monitor_session_cookies():
    """Session cookies monitor করা"""

    analytics = CookieAnalytics()
    session = requests.Session()
    session_id = f"session_{int(time.time())}"

    # Make some requests
    session.get("https://httpbin.org/cookies/set/test1/value1")
    analytics.monitor_cookies(session, session_id)

    session.get("https://httpbin.org/cookies/set/test2/value2")
    analytics.monitor_cookies(session, session_id)

    # Get statistics
    stats = analytics.get_cookie_stats()
    print(f"📈 Cookie statistics: {stats}")

# monitor_session_cookies()
```

---

## 🌟 Real-World Examples {#real-world-examples}

### E-commerce Session Management:
```python
class EcommerceSession:
    def __init__(self):
        self.session = requests.Session()
        self.cart_items = []
        self.user_info = {}

        # Setup session
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def login(self, email, password):
        """E-commerce site এ login"""

        login_url = "https://example-shop.com/login"

        # Get login page
        response = self.session.get(login_url)

        # Extract CSRF
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

        # Login
        login_data = {
            'email': email,
            'password': password,
            'csrf_token': csrf_token
        }

        response = self.session.post(login_url, data=login_data)

        if 'dashboard' in response.url:
            print("✅ E-commerce login successful")
            return True
        else:
            print("❌ Login failed")
            return False

    def add_to_cart(self, product_id, quantity=1):
        """Product cart এ add করা"""

        cart_url = "https://example-shop.com/cart/add"

        cart_data = {
            'product_id': product_id,
            'quantity': quantity
        }

        response = self.session.post(cart_url, data=cart_data)

        if response.status_code == 200:
            self.cart_items.append({'product_id': product_id, 'quantity': quantity})
            print(f"🛒 Added product {product_id} to cart")
            return True
        else:
            print(f"❌ Failed to add product to cart")
            return False

    def get_cart_total(self):
        """Cart total get করা"""

        cart_url = "https://example-shop.com/cart"
        response = self.session.get(cart_url)

        soup = BeautifulSoup(response.content, 'html.parser')
        total_element = soup.find('span', class_='cart-total')

        if total_element:
            return total_element.text.strip()
        else:
            return "0"

    def checkout(self, payment_info):
        """Checkout process"""

        checkout_url = "https://example-shop.com/checkout"

        checkout_data = {
            'payment_method': payment_info['method'],
            'billing_address': payment_info['address'],
            'card_number': payment_info.get('card_number', ''),
        }

        response = self.session.post(checkout_url, data=checkout_data)

        if 'order-confirmation' in response.url:
            print("✅ Order placed successfully")
            return True
        else:
            print("❌ Checkout failed")
            return False

# Usage
def ecommerce_automation():
    """Complete e-commerce automation"""

    shop = EcommerceSession()

    # Login
    if shop.login("user@example.com", "password123"):

        # Add products to cart
        shop.add_to_cart("PROD001", 2)
        shop.add_to_cart("PROD002", 1)

        # Check cart total
        total = shop.get_cart_total()
        print(f"💰 Cart total: {total}")

        # Checkout
        payment_info = {
            'method': 'credit_card',
            'address': '123 Main St, City, Country',
            'card_number': '1234-5678-9012-3456'
        }

        shop.checkout(payment_info)

# ecommerce_automation()
```

### Multi-Account Management:
```python
class MultiAccountManager:
    def __init__(self):
        self.accounts = {}
        self.active_sessions = {}

    def add_account(self, account_name, credentials):
        """Account add করা"""
        self.accounts[account_name] = credentials
        print(f"👤 Account added: {account_name}")

    def login_account(self, account_name, site_url):
        """Specific account login করা"""

        if account_name not in self.accounts:
            print(f"❌ Account not found: {account_name}")
            return None

        credentials = self.accounts[account_name]

        # Create session for this account
        session = requests.Session()
        session.headers.update({
            'User-Agent': f'Bot-{account_name}-Agent'
        })

        # Login process
        login_url = f"{site_url}/login"

        # Get login page
        response = session.get(login_url)

        # Login
        login_data = {
            'username': credentials['username'],
            'password': credentials['password']
        }

        response = session.post(login_url, data=login_data)

        if response.status_code == 200:
            self.active_sessions[account_name] = session
            print(f"✅ {account_name} logged in successfully")
            return session
        else:
            print(f"❌ {account_name} login failed")
            return None

    def perform_action_all_accounts(self, action_func, site_url):
        """সব accounts এ same action perform করা"""

        results = {}

        for account_name in self.accounts:
            session = self.login_account(account_name, site_url)

            if session:
                try:
                    result = action_func(session, account_name)
                    results[account_name] = result
                    print(f"✅ {account_name}: Action completed")
                except Exception as e:
                    results[account_name] = f"Error: {e}"
                    print(f"❌ {account_name}: {e}")

        return results

    def save_all_sessions(self):
        """সব sessions এর cookies save করা"""

        for account_name, session in self.active_sessions.items():
            cookie_file = f"cookies_{account_name}.pkl"

            with open(cookie_file, 'wb') as f:
                pickle.dump(session.cookies, f)

            print(f"💾 {account_name} cookies saved")

# Usage
def multi_account_automation():
    """Multi-account automation example"""

    manager = MultiAccountManager()

    # Add accounts
    manager.add_account("account1", {"username": "user1", "password": "pass1"})
    manager.add_account("account2", {"username": "user2", "password": "pass2"})
    manager.add_account("account3", {"username": "user3", "password": "pass3"})

    # Define action function
    def scrape_profile_data(session, account_name):
        """Profile data scrape করা"""

        profile_url = "https://example.com/profile"
        response = session.get(profile_url)

        soup = BeautifulSoup(response.content, 'html.parser')

        profile_data = {
            'name': soup.find('span', class_='username').text if soup.find('span', class_='username') else 'N/A',
            'email': soup.find('span', class_='email').text if soup.find('span', class_='email') else 'N/A',
            'posts': len(soup.find_all('div', class_='post'))
        }

        return profile_data

    # Perform action on all accounts
    results = manager.perform_action_all_accounts(scrape_profile_data, "https://example.com")

    # Print results
    for account, data in results.items():
        print(f"📊 {account}: {data}")

    # Save sessions
    manager.save_all_sessions()

# multi_account_automation()
```

---

## 🎉 সমাপনী

এই গাইডে আপনি শিখেছেন:

✅ **Cookie Basics:** কি, কেন, কিভাবে কাজ করে
✅ **Playwright Cookies:** Browser automation এ cookie management
✅ **Requests Sessions:** HTTP session ও cookie persistence
✅ **Aiohttp Async:** Async/await দিয়ে cookie handling
✅ **Security:** Cookie encryption ও secure storage
✅ **Analytics:** Cookie monitoring ও tracking
✅ **Real-World:** E-commerce ও multi-account automation

### 🔑 মূল বিষয়:
- **Always save cookies** for session persistence
- **Handle CSRF tokens** properly
- **Use secure storage** for sensitive cookies
- **Monitor cookie expiry** and refresh when needed
- **Respect rate limits** and website policies

**Happy Cookie Management! 🍪🚀**
```
