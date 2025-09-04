# 🌐 Requests - সম্পূর্ণ বাংলা গাইড

## 🌟 Requests কি?

Requests হলো Python এর সবচেয়ে জনপ্রিয় **HTTP library** যা দিয়ে আপনি সহজেই web APIs, websites এর সাথে communicate করতে পারেন।

### 🎯 **মূল বৈশিষ্ট্য:**
- ✅ **Simple API** - সহজ ব্যবহার
- ✅ **HTTP methods** - GET, POST, PUT, DELETE
- ✅ **Session management** - Cookies, headers persist
- ✅ **Authentication** - Basic, OAuth, custom auth
- ✅ **File uploads** - Multipart form data
- ✅ **SSL verification** - Secure connections

---

## 🚀 Installation ও Setup

### 📦 **Installation:**
```bash
# Requests install
pip install requests>=2.31.0

# Additional dependencies
pip install requests[security]  # Extra security features
```

### ✅ **Installation Verify:**
```python
# test_requests.py
import requests

def test_requests():
    print("🧪 Requests installation test...")
    
    try:
        response = requests.get('https://httpbin.org/json')
        
        print(f"✅ Status Code: {response.status_code}")
        print(f"✅ Response: {response.json()}")
        print("🎉 Requests working perfectly!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

test_requests()
```

---

## 🌐 Basic HTTP Requests

### 📥 **GET Requests:**
```python
import requests
import json

def get_requests():
    """GET request examples"""
    
    # Simple GET request
    response = requests.get('https://httpbin.org/json')
    
    print(f"Status Code: {response.status_code}")
    print(f"Headers: {response.headers}")
    print(f"Content: {response.text}")
    
    # JSON response
    if response.headers.get('content-type') == 'application/json':
        data = response.json()
        print(f"JSON Data: {data}")
    
    # GET with parameters
    params = {
        'q': 'python programming',
        'page': 1,
        'per_page': 10
    }
    
    response = requests.get('https://httpbin.org/get', params=params)
    print(f"URL with params: {response.url}")
    
    # GET with headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Accept': 'application/json',
        'Accept-Language': 'bn-BD,bn;q=0.9,en;q=0.8'
    }
    
    response = requests.get('https://httpbin.org/headers', headers=headers)
    print(f"Headers sent: {response.json()}")

get_requests()
```

### 📤 **POST Requests:**
```python
def post_requests():
    """POST request examples"""
    
    # Simple POST with data
    data = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'message': 'Hello from Python!'
    }
    
    response = requests.post('https://httpbin.org/post', data=data)
    print(f"POST Response: {response.json()}")
    
    # POST with JSON
    json_data = {
        'user': {
            'name': 'Jane Smith',
            'age': 25,
            'skills': ['Python', 'JavaScript', 'SQL']
        }
    }
    
    response = requests.post(
        'https://httpbin.org/post',
        json=json_data,
        headers={'Content-Type': 'application/json'}
    )
    
    print(f"JSON POST: {response.json()}")
    
    # POST with files
    files = {
        'file': ('test.txt', 'This is test file content', 'text/plain')
    }
    
    response = requests.post('https://httpbin.org/post', files=files)
    print(f"File upload: {response.json()}")

post_requests()
```

### 🔄 **Other HTTP Methods:**
```python
def other_methods():
    """PUT, DELETE, PATCH methods"""
    
    # PUT request
    put_data = {'name': 'Updated Name', 'status': 'active'}
    response = requests.put('https://httpbin.org/put', json=put_data)
    print(f"PUT Response: {response.status_code}")
    
    # DELETE request
    response = requests.delete('https://httpbin.org/delete')
    print(f"DELETE Response: {response.status_code}")
    
    # PATCH request
    patch_data = {'status': 'inactive'}
    response = requests.patch('https://httpbin.org/patch', json=patch_data)
    print(f"PATCH Response: {response.status_code}")
    
    # HEAD request (headers only)
    response = requests.head('https://httpbin.org/get')
    print(f"HEAD Headers: {response.headers}")
    
    # OPTIONS request
    response = requests.options('https://httpbin.org/get')
    print(f"OPTIONS: {response.headers.get('Allow')}")

other_methods()
```

---

## 🍪 Session Management

### 🔐 **Sessions ও Cookies:**
```python
def session_management():
    """Session ও cookie management"""
    
    # Create session
    session = requests.Session()
    
    # Set default headers for session
    session.headers.update({
        'User-Agent': 'My Python App 1.0',
        'Accept': 'application/json'
    })
    
    # Login simulation
    login_data = {
        'username': 'testuser',
        'password': 'testpass'
    }
    
    # Login request (cookies will be stored in session)
    login_response = session.post('https://httpbin.org/cookies/set/sessionid/abc123')
    print(f"Login Status: {login_response.status_code}")
    
    # Subsequent requests will include cookies
    profile_response = session.get('https://httpbin.org/cookies')
    print(f"Cookies: {profile_response.json()}")
    
    # Manual cookie setting
    session.cookies.set('custom_cookie', 'custom_value', domain='httpbin.org')
    
    # Check all cookies
    for cookie in session.cookies:
        print(f"Cookie: {cookie.name} = {cookie.value}")
    
    # Close session
    session.close()

session_management()
```

### 🔒 **Authentication:**
```python
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

def authentication_examples():
    """বিভিন্ন authentication methods"""
    
    # Basic Authentication
    response = requests.get(
        'https://httpbin.org/basic-auth/user/pass',
        auth=HTTPBasicAuth('user', 'pass')
    )
    print(f"Basic Auth: {response.status_code}")
    
    # Shorthand basic auth
    response = requests.get(
        'https://httpbin.org/basic-auth/user/pass',
        auth=('user', 'pass')
    )
    print(f"Basic Auth (shorthand): {response.status_code}")
    
    # Digest Authentication
    response = requests.get(
        'https://httpbin.org/digest-auth/auth/user/pass',
        auth=HTTPDigestAuth('user', 'pass')
    )
    print(f"Digest Auth: {response.status_code}")
    
    # Bearer Token Authentication
    headers = {
        'Authorization': 'Bearer your-token-here'
    }
    
    response = requests.get('https://httpbin.org/bearer', headers=headers)
    print(f"Bearer Token: {response.status_code}")
    
    # API Key Authentication
    api_headers = {
        'X-API-Key': 'your-api-key-here',
        'Authorization': 'API-Key your-api-key-here'
    }
    
    response = requests.get('https://httpbin.org/headers', headers=api_headers)
    print(f"API Key sent: {response.json()}")

authentication_examples()
```

---

## 📁 File Operations

### 📤 **File Upload:**
```python
def file_operations():
    """File upload ও download"""
    
    # Single file upload
    with open('test.txt', 'w') as f:
        f.write('This is a test file for upload')
    
    with open('test.txt', 'rb') as f:
        files = {'file': f}
        response = requests.post('https://httpbin.org/post', files=files)
        print(f"File upload: {response.json()['files']}")
    
    # Multiple files upload
    files = {
        'file1': ('file1.txt', 'Content of file 1', 'text/plain'),
        'file2': ('file2.txt', 'Content of file 2', 'text/plain')
    }
    
    response = requests.post('https://httpbin.org/post', files=files)
    print(f"Multiple files: {len(response.json()['files'])} files uploaded")
    
    # File upload with additional data
    files = {'file': ('data.txt', 'File content', 'text/plain')}
    data = {'description': 'Test file upload', 'category': 'documents'}
    
    response = requests.post('https://httpbin.org/post', files=files, data=data)
    print(f"File with data: {response.json()['form']}")

file_operations()
```

### 📥 **File Download:**
```python
def file_download():
    """File download examples"""
    
    # Small file download
    response = requests.get('https://httpbin.org/json')
    
    with open('downloaded.json', 'w') as f:
        f.write(response.text)
    
    print("✅ Small file downloaded")
    
    # Large file download with streaming
    url = 'https://httpbin.org/stream/1000'
    
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        
        with open('large_file.txt', 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    
    print("✅ Large file downloaded with streaming")
    
    # Download with progress
    def download_with_progress(url, filename):
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        
        with open(filename, 'wb') as f:
            downloaded = 0
            
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    
                    if total_size > 0:
                        progress = (downloaded / total_size) * 100
                        print(f"\rDownload progress: {progress:.1f}%", end='')
        
        print(f"\n✅ Downloaded: {filename}")
    
    download_with_progress('https://httpbin.org/json', 'progress_download.json')

file_download()
```

---

## ⚡ Advanced Features

### 🔄 **Retry Mechanism:**
```python
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def retry_mechanism():
    """Automatic retry mechanism"""
    
    # Create session with retry strategy
    session = requests.Session()
    
    retry_strategy = Retry(
        total=3,                    # Total retries
        backoff_factor=1,           # Wait time between retries
        status_forcelist=[429, 500, 502, 503, 504],  # Status codes to retry
        allowed_methods=["HEAD", "GET", "OPTIONS", "POST"]
    )
    
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    try:
        # This will retry on failure
        response = session.get('https://httpbin.org/status/500', timeout=5)
        print(f"Response: {response.status_code}")
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed after retries: {e}")
    
    session.close()

retry_mechanism()
```

### ⏱️ **Timeout ও Error Handling:**
```python
def timeout_error_handling():
    """Timeout ও error handling"""
    
    try:
        # Connection timeout: 5 seconds, Read timeout: 10 seconds
        response = requests.get('https://httpbin.org/delay/3', timeout=(5, 10))
        print(f"Success: {response.status_code}")
        
    except requests.exceptions.ConnectTimeout:
        print("❌ Connection timeout")
        
    except requests.exceptions.ReadTimeout:
        print("❌ Read timeout")
        
    except requests.exceptions.Timeout:
        print("❌ General timeout")
        
    except requests.exceptions.ConnectionError:
        print("❌ Connection error")
        
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error: {e}")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ General request error: {e}")
    
    # Check status code
    response = requests.get('https://httpbin.org/status/404')
    
    if response.status_code == 200:
        print("✅ Success")
    elif response.status_code == 404:
        print("⚠️ Not found")
    else:
        print(f"❌ Error: {response.status_code}")
    
    # Raise exception for bad status codes
    try:
        response = requests.get('https://httpbin.org/status/500')
        response.raise_for_status()  # Raises HTTPError for bad responses
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")

timeout_error_handling()
```

### 🌐 **Proxy ও SSL:**
```python
def proxy_ssl_examples():
    """Proxy ও SSL configuration"""
    
    # Proxy configuration
    proxies = {
        'http': 'http://proxy-server:8080',
        'https': 'https://proxy-server:8080'
    }
    
    # With authentication
    proxies_with_auth = {
        'http': 'http://username:password@proxy-server:8080',
        'https': 'https://username:password@proxy-server:8080'
    }
    
    try:
        # Use proxy (will fail without real proxy)
        # response = requests.get('https://httpbin.org/ip', proxies=proxies)
        # print(f"IP through proxy: {response.json()}")
        pass
        
    except requests.exceptions.RequestException as e:
        print(f"Proxy error: {e}")
    
    # SSL verification
    # Disable SSL verification (not recommended for production)
    response = requests.get('https://httpbin.org/get', verify=False)
    print(f"SSL disabled: {response.status_code}")
    
    # Custom SSL certificate
    # response = requests.get('https://example.com', verify='/path/to/cert.pem')
    
    # SSL with custom headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    
    response = requests.get('https://httpbin.org/headers', headers=headers, verify=True)
    print(f"SSL verified: {response.status_code}")

proxy_ssl_examples()
```

---

## 🎯 Real-World Examples

### 📰 **API Integration:**
```python
def api_integration():
    """Real API integration example"""
    
    # GitHub API example
    def get_github_user(username):
        url = f'https://api.github.com/users/{username}'
        
        headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Python-Requests-App'
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            user_data = response.json()
            return {
                'name': user_data.get('name'),
                'bio': user_data.get('bio'),
                'public_repos': user_data.get('public_repos'),
                'followers': user_data.get('followers'),
                'following': user_data.get('following')
            }
        else:
            return None
    
    # Usage
    user_info = get_github_user('octocat')
    if user_info:
        print(f"GitHub User: {user_info}")
    
    # Weather API example (hypothetical)
    def get_weather(city):
        api_key = 'your-api-key-here'
        url = f'https://api.openweathermap.org/data/2.5/weather'
        
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            weather_data = response.json()
            return {
                'city': weather_data['name'],
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'humidity': weather_data['main']['humidity']
            }
            
        except requests.exceptions.RequestException as e:
            print(f"Weather API error: {e}")
            return None
    
    # Note: Need real API key to work
    # weather = get_weather('Dhaka')

api_integration()
```

### 🕷️ **Web Scraping:**
```python
def web_scraping_example():
    """Simple web scraping with requests"""
    
    # Get webpage
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    response = requests.get('https://quotes.toscrape.com', headers=headers)
    
    if response.status_code == 200:
        print(f"✅ Page loaded: {len(response.text)} characters")
        print(f"Content type: {response.headers.get('content-type')}")
        
        # Save HTML for further processing
        with open('scraped_page.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        print("✅ HTML saved for processing")
    
    # Rate limiting for scraping
    import time
    
    def scrape_with_delay(urls, delay=1):
        results = []
        
        for url in urls:
            try:
                response = requests.get(url, headers=headers)
                results.append({
                    'url': url,
                    'status': response.status_code,
                    'size': len(response.text)
                })
                
                print(f"Scraped: {url} ({response.status_code})")
                time.sleep(delay)  # Be respectful to servers
                
            except requests.exceptions.RequestException as e:
                print(f"Error scraping {url}: {e}")
        
        return results
    
    # Example URLs
    urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/'
    ]
    
    results = scrape_with_delay(urls, delay=2)
    print(f"Scraped {len(results)} pages")

web_scraping_example()
```

---

## 🎉 সমাপনী

### ✅ **Requests এ আপনি শিখেছেন:**
- Basic HTTP requests (GET, POST, PUT, DELETE)
- Session management ও cookies
- Authentication methods
- File upload ও download
- Error handling ও timeouts
- Retry mechanisms
- Proxy ও SSL configuration
- Real-world API integration

### 🚀 **Next Steps:**
- **BeautifulSoup** দিয়ে HTML parsing
- **Async requests** with aiohttp
- **Advanced scraping** with Playwright
- **API development** with Flask/FastAPI

**Requests mastery সম্পন্ন! 🌐🇧🇩**
