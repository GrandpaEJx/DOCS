# ⚡ aiohttp - সম্পূর্ণ বাংলা গাইড

## 🌟 aiohttp কি?

aiohttp হলো Python এর একটি **asynchronous HTTP client/server library** যা দিয়ে আপনি অত্যন্ত দ্রুত ও efficient HTTP requests করতে পারেন।

### 🎯 **মূল বৈশিষ্ট্য:**
- ✅ **Async/await support** - Modern Python async programming
- ✅ **High performance** - Concurrent requests
- ✅ **Client ও Server** - Both HTTP client and server
- ✅ **WebSocket support** - Real-time communication
- ✅ **Session management** - Connection pooling
- ✅ **Streaming** - Large file handling

---

## 🚀 Installation ও Setup

### 📦 **Installation:**
```bash
# aiohttp install
pip install aiohttp>=3.9.0

# Additional dependencies
pip install aiofiles>=23.2.0    # Async file operations
pip install asyncio-mqtt>=0.16.0  # MQTT support (optional)
```

### ✅ **Installation Verify:**
```python
# test_aiohttp.py
import asyncio
import aiohttp

async def test_aiohttp():
    print("🧪 aiohttp installation test...")
    
    async with aiohttp.ClientSession() as session:
        async with session.get('https://httpbin.org/json') as response:
            data = await response.json()
            
            print(f"✅ Status: {response.status}")
            print(f"✅ Response: {data}")
            print("🎉 aiohttp working perfectly!")

# Run async function
asyncio.run(test_aiohttp())
```

---

## 🌐 Basic HTTP Requests

### 📥 **GET Requests:**
```python
import asyncio
import aiohttp
import time

async def get_requests():
    """Async GET request examples"""
    
    async with aiohttp.ClientSession() as session:
        # Simple GET request
        async with session.get('https://httpbin.org/json') as response:
            print(f"Status: {response.status}")
            print(f"Headers: {dict(response.headers)}")
            
            # Get JSON response
            data = await response.json()
            print(f"JSON data: {data}")
        
        # GET with parameters
        params = {
            'q': 'python programming',
            'page': 1,
            'per_page': 10
        }
        
        async with session.get('https://httpbin.org/get', params=params) as response:
            data = await response.json()
            print(f"URL with params: {data['url']}")
        
        # GET with custom headers
        headers = {
            'User-Agent': 'My Async Python App 1.0',
            'Accept': 'application/json',
            'Accept-Language': 'bn-BD,bn;q=0.9,en;q=0.8'
        }
        
        async with session.get('https://httpbin.org/headers', headers=headers) as response:
            data = await response.json()
            print(f"Custom headers sent: {data['headers']}")

asyncio.run(get_requests())
```

### 📤 **POST Requests:**
```python
async def post_requests():
    """Async POST request examples"""
    
    async with aiohttp.ClientSession() as session:
        # POST with form data
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Hello from async Python!'
        }
        
        async with session.post('https://httpbin.org/post', data=form_data) as response:
            data = await response.json()
            print(f"Form POST response: {data['form']}")
        
        # POST with JSON
        json_data = {
            'user': {
                'name': 'Jane Smith',
                'age': 25,
                'skills': ['Python', 'JavaScript', 'SQL']
            }
        }
        
        async with session.post('https://httpbin.org/post', json=json_data) as response:
            data = await response.json()
            print(f"JSON POST response: {data['json']}")
        
        # POST with files
        with open('test_file.txt', 'w') as f:
            f.write('This is a test file for async upload')
        
        with open('test_file.txt', 'rb') as f:
            files = {'file': f}
            async with session.post('https://httpbin.org/post', data=files) as response:
                data = await response.json()
                print(f"File upload: {data['files']}")

asyncio.run(post_requests())
```

### 🔄 **Other HTTP Methods:**
```python
async def other_methods():
    """PUT, DELETE, PATCH methods"""
    
    async with aiohttp.ClientSession() as session:
        # PUT request
        put_data = {'name': 'Updated Name', 'status': 'active'}
        async with session.put('https://httpbin.org/put', json=put_data) as response:
            print(f"PUT Status: {response.status}")
        
        # DELETE request
        async with session.delete('https://httpbin.org/delete') as response:
            print(f"DELETE Status: {response.status}")
        
        # PATCH request
        patch_data = {'status': 'inactive'}
        async with session.patch('https://httpbin.org/patch', json=patch_data) as response:
            print(f"PATCH Status: {response.status}")
        
        # HEAD request
        async with session.head('https://httpbin.org/get') as response:
            print(f"HEAD Headers: {dict(response.headers)}")

asyncio.run(other_methods())
```

---

## ⚡ Concurrent Requests

### 🚀 **Multiple Concurrent Requests:**
```python
async def concurrent_requests():
    """Multiple concurrent requests"""
    
    urls = [
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/3',
        'https://httpbin.org/delay/2'
    ]
    
    async def fetch_url(session, url):
        """Fetch single URL"""
        start_time = time.time()
        
        try:
            async with session.get(url) as response:
                data = await response.json()
                end_time = time.time()
                
                return {
                    'url': url,
                    'status': response.status,
                    'time_taken': round(end_time - start_time, 2),
                    'data': data
                }
        except Exception as e:
            return {
                'url': url,
                'error': str(e),
                'time_taken': round(time.time() - start_time, 2)
            }
    
    # Sequential requests (slow)
    print("🐌 Sequential requests:")
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        results = []
        for url in urls:
            result = await fetch_url(session, url)
            results.append(result)
    
    sequential_time = time.time() - start_time
    print(f"Sequential time: {sequential_time:.2f} seconds")
    
    # Concurrent requests (fast)
    print("\n⚡ Concurrent requests:")
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    concurrent_time = time.time() - start_time
    print(f"Concurrent time: {concurrent_time:.2f} seconds")
    print(f"Speed improvement: {sequential_time/concurrent_time:.1f}x faster")
    
    # Display results
    for result in results:
        if 'error' in result:
            print(f"❌ {result['url']}: {result['error']}")
        else:
            print(f"✅ {result['url']}: {result['status']} ({result['time_taken']}s)")

asyncio.run(concurrent_requests())
```

### 📊 **Rate Limited Concurrent Requests:**
```python
async def rate_limited_requests():
    """Rate limited concurrent requests"""
    
    # Create semaphore to limit concurrent requests
    semaphore = asyncio.Semaphore(3)  # Max 3 concurrent requests
    
    urls = [f'https://httpbin.org/delay/{i%3+1}' for i in range(10)]
    
    async def fetch_with_limit(session, url):
        """Fetch URL with rate limiting"""
        async with semaphore:  # Acquire semaphore
            print(f"🔄 Starting request to {url}")
            
            try:
                async with session.get(url) as response:
                    data = await response.json()
                    print(f"✅ Completed {url} - Status: {response.status}")
                    return data
                    
            except Exception as e:
                print(f"❌ Failed {url}: {e}")
                return None
    
    print("🚦 Rate limited concurrent requests (max 3 at a time):")
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_with_limit(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
    
    total_time = time.time() - start_time
    successful = sum(1 for r in results if r is not None and not isinstance(r, Exception))
    
    print(f"\n📊 Results:")
    print(f"Total time: {total_time:.2f} seconds")
    print(f"Successful requests: {successful}/{len(urls)}")

asyncio.run(rate_limited_requests())
```

---

## 🍪 Session Management

### 🔐 **Sessions ও Cookies:**
```python
async def session_management():
    """Session and cookie management"""
    
    # Create session with custom settings
    timeout = aiohttp.ClientTimeout(total=30)
    connector = aiohttp.TCPConnector(limit=100, limit_per_host=10)
    
    async with aiohttp.ClientSession(
        timeout=timeout,
        connector=connector,
        headers={'User-Agent': 'My Async App 1.0'}
    ) as session:
        
        # Set cookies
        session.cookie_jar.update_cookies({
            'session_id': 'abc123',
            'user_pref': 'dark_mode'
        })
        
        # Login simulation (cookies will be stored)
        login_data = {'username': 'testuser', 'password': 'testpass'}
        async with session.post('https://httpbin.org/cookies/set/sessionid/xyz789') as response:
            print(f"Login status: {response.status}")
        
        # Subsequent request will include cookies
        async with session.get('https://httpbin.org/cookies') as response:
            data = await response.json()
            print(f"Cookies: {data['cookies']}")
        
        # Manual cookie operations
        print(f"All cookies: {session.cookie_jar}")
        
        # Clear specific cookie
        session.cookie_jar.clear(lambda cookie: cookie.key == 'user_pref')

asyncio.run(session_management())
```

### 🔒 **Authentication:**
```python
from aiohttp import BasicAuth

async def authentication_examples():
    """Authentication examples"""
    
    async with aiohttp.ClientSession() as session:
        # Basic Authentication
        auth = BasicAuth('user', 'pass')
        async with session.get('https://httpbin.org/basic-auth/user/pass', auth=auth) as response:
            print(f"Basic Auth Status: {response.status}")
        
        # Bearer Token
        headers = {'Authorization': 'Bearer your-token-here'}
        async with session.get('https://httpbin.org/bearer', headers=headers) as response:
            print(f"Bearer Token Status: {response.status}")
        
        # API Key Authentication
        api_headers = {
            'X-API-Key': 'your-api-key-here',
            'Authorization': 'API-Key your-api-key-here'
        }
        
        async with session.get('https://httpbin.org/headers', headers=api_headers) as response:
            data = await response.json()
            print(f"API Key sent: {data['headers']}")

asyncio.run(authentication_examples())
```

---

## 📁 File Operations

### 📤 **File Upload:**
```python
import aiofiles

async def file_operations():
    """Async file operations"""
    
    # Create test file
    async with aiofiles.open('async_test.txt', 'w') as f:
        await f.write('This is an async test file')
    
    async with aiohttp.ClientSession() as session:
        # Single file upload
        async with aiofiles.open('async_test.txt', 'rb') as f:
            file_data = await f.read()
            
            data = aiohttp.FormData()
            data.add_field('file', file_data, filename='async_test.txt', content_type='text/plain')
            
            async with session.post('https://httpbin.org/post', data=data) as response:
                result = await response.json()
                print(f"File upload: {result['files']}")
        
        # Multiple files upload
        files_data = aiohttp.FormData()
        
        # Add multiple files
        for i in range(3):
            filename = f'file_{i}.txt'
            content = f'Content of file {i}'
            
            files_data.add_field('files', content.encode(), 
                               filename=filename, content_type='text/plain')
        
        async with session.post('https://httpbin.org/post', data=files_data) as response:
            result = await response.json()
            print(f"Multiple files: {len(result['files'])} files uploaded")

asyncio.run(file_operations())
```

### 📥 **File Download:**
```python
async def file_download():
    """Async file download"""
    
    async with aiohttp.ClientSession() as session:
        # Small file download
        async with session.get('https://httpbin.org/json') as response:
            content = await response.text()
            
            async with aiofiles.open('downloaded.json', 'w') as f:
                await f.write(content)
            
            print("✅ Small file downloaded")
        
        # Large file download with streaming
        url = 'https://httpbin.org/stream/100'
        
        async with session.get(url) as response:
            async with aiofiles.open('streamed_file.txt', 'wb') as f:
                async for chunk in response.content.iter_chunked(8192):
                    await f.write(chunk)
        
        print("✅ Large file downloaded with streaming")
        
        # Download with progress tracking
        async def download_with_progress(url, filename):
            async with session.get(url) as response:
                total_size = int(response.headers.get('content-length', 0))
                downloaded = 0
                
                async with aiofiles.open(filename, 'wb') as f:
                    async for chunk in response.content.iter_chunked(8192):
                        await f.write(chunk)
                        downloaded += len(chunk)
                        
                        if total_size > 0:
                            progress = (downloaded / total_size) * 100
                            print(f"\rDownload progress: {progress:.1f}%", end='')
                
                print(f"\n✅ Downloaded: {filename}")
        
        await download_with_progress('https://httpbin.org/json', 'progress_download.json')

asyncio.run(file_download())
```

---

## ⚠️ Error Handling

### 🛡️ **Exception Handling:**
```python
async def error_handling():
    """Error handling in async requests"""
    
    async with aiohttp.ClientSession() as session:
        # Timeout handling
        try:
            timeout = aiohttp.ClientTimeout(total=5)
            async with session.get('https://httpbin.org/delay/10', timeout=timeout) as response:
                data = await response.json()
                
        except asyncio.TimeoutError:
            print("❌ Request timeout")
        
        except aiohttp.ClientError as e:
            print(f"❌ Client error: {e}")
        
        # Connection error handling
        try:
            async with session.get('https://nonexistent-domain-12345.com') as response:
                data = await response.json()
                
        except aiohttp.ClientConnectorError:
            print("❌ Connection error - domain not found")
        
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        
        # Status code handling
        try:
            async with session.get('https://httpbin.org/status/404') as response:
                if response.status == 200:
                    data = await response.json()
                    print("✅ Success")
                elif response.status == 404:
                    print("⚠️ Not found")
                else:
                    print(f"❌ HTTP Error: {response.status}")
                    
        except Exception as e:
            print(f"❌ Request failed: {e}")

asyncio.run(error_handling())
```

### 🔄 **Retry Mechanism:**
```python
async def retry_mechanism():
    """Retry mechanism for failed requests"""
    
    async def fetch_with_retry(session, url, max_retries=3, delay=1):
        """Fetch URL with retry logic"""
        
        for attempt in range(max_retries + 1):
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        raise aiohttp.ClientResponseError(
                            request_info=response.request_info,
                            history=response.history,
                            status=response.status
                        )
                        
            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                if attempt == max_retries:
                    print(f"❌ Failed after {max_retries + 1} attempts: {e}")
                    return None
                
                print(f"⚠️ Attempt {attempt + 1} failed, retrying in {delay}s...")
                await asyncio.sleep(delay)
                delay *= 2  # Exponential backoff
        
        return None
    
    async with aiohttp.ClientSession() as session:
        # Test with unreliable endpoint
        result = await fetch_with_retry(session, 'https://httpbin.org/status/500')
        
        if result:
            print(f"✅ Success: {result}")
        else:
            print("❌ All retry attempts failed")

asyncio.run(retry_mechanism())
```

---

## 🎯 Real-World Examples

### 🕷️ **Web Scraping:**
```python
from bs4 import BeautifulSoup

async def async_web_scraping():
    """Async web scraping example"""
    
    urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
        'https://quotes.toscrape.com/page/3/'
    ]
    
    async def scrape_quotes_page(session, url):
        """Scrape quotes from a single page"""
        try:
            async with session.get(url) as response:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                
                quotes = []
                for quote in soup.find_all('div', class_='quote'):
                    text = quote.find('span', class_='text').text
                    author = quote.find('small', class_='author').text
                    tags = [tag.text for tag in quote.find_all('a', class_='tag')]
                    
                    quotes.append({
                        'text': text.strip().strip('"'),
                        'author': author,
                        'tags': tags,
                        'page_url': url
                    })
                
                return quotes
                
        except Exception as e:
            print(f"❌ Error scraping {url}: {e}")
            return []
    
    print("🕷️ Async web scraping started...")
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        tasks = [scrape_quotes_page(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    # Flatten results
    all_quotes = []
    for page_quotes in results:
        all_quotes.extend(page_quotes)
    
    scraping_time = time.time() - start_time
    
    print(f"✅ Scraped {len(all_quotes)} quotes in {scraping_time:.2f} seconds")
    
    # Display first few quotes
    for i, quote in enumerate(all_quotes[:3], 1):
        print(f"\nQuote {i}:")
        print(f"  Text: {quote['text']}")
        print(f"  Author: {quote['author']}")
        print(f"  Tags: {', '.join(quote['tags'])}")

asyncio.run(async_web_scraping())
```

### 📊 **API Data Collection:**
```python
async def api_data_collection():
    """Collect data from multiple APIs"""
    
    # Simulate multiple API endpoints
    api_endpoints = [
        'https://httpbin.org/json',
        'https://httpbin.org/uuid',
        'https://httpbin.org/ip',
        'https://httpbin.org/user-agent'
    ]
    
    async def fetch_api_data(session, endpoint):
        """Fetch data from API endpoint"""
        try:
            async with session.get(endpoint) as response:
                data = await response.json()
                return {
                    'endpoint': endpoint,
                    'status': response.status,
                    'data': data,
                    'timestamp': time.time()
                }
                
        except Exception as e:
            return {
                'endpoint': endpoint,
                'error': str(e),
                'timestamp': time.time()
            }
    
    print("📊 Collecting data from multiple APIs...")
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_api_data(session, endpoint) for endpoint in api_endpoints]
        results = await asyncio.gather(*tasks)
    
    # Process results
    successful = 0
    failed = 0
    
    for result in results:
        if 'error' in result:
            print(f"❌ {result['endpoint']}: {result['error']}")
            failed += 1
        else:
            print(f"✅ {result['endpoint']}: Status {result['status']}")
            successful += 1
    
    print(f"\n📈 Summary: {successful} successful, {failed} failed")

asyncio.run(api_data_collection())
```

---

## 🎉 সমাপনী

### ✅ **aiohttp এ আপনি শিখেছেন:**
- Async HTTP requests (GET, POST, PUT, DELETE)
- Concurrent request handling
- Session management ও cookies
- Authentication methods
- File upload ও download
- Error handling ও retry mechanisms
- Real-world async web scraping

### 🚀 **Next Steps:**
- **aiofiles** দিয়ে async file operations
- **asyncio** advanced patterns
- **WebSocket** real-time communication
- **FastAPI** async web development

**aiohttp mastery সম্পন্ন! ⚡🇧🇩**
