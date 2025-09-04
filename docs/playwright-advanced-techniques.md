# 🚀 Playwright অ্যাডভান্স টেকনিক - Part 2

## 🎯 অ্যাডভান্স স্ক্র্যাপিং টেকনিক {#advanced-scraping}

### 🔄 Infinite Scroll Handling:

#### Basic Infinite Scroll:
```python
def scrape_infinite_scroll(page, max_items=100):
    """Infinite scroll page থেকে data scrape করা"""
    
    all_items = []
    previous_count = 0
    scroll_attempts = 0
    max_scroll_attempts = 10
    
    while len(all_items) < max_items and scroll_attempts < max_scroll_attempts:
        # Current items count
        current_items = page.locator('.item').all()
        current_count = len(current_items)
        
        # Extract new items
        for i in range(previous_count, current_count):
            try:
                item_data = {
                    'title': current_items[i].locator('.title').text_content(),
                    'description': current_items[i].locator('.description').text_content(),
                    'index': i
                }
                all_items.append(item_data)
            except:
                continue
        
        print(f"📊 Loaded {len(all_items)} items so far...")
        
        # Check if new items loaded
        if current_count == previous_count:
            scroll_attempts += 1
            print(f"⚠️ No new items loaded. Attempt {scroll_attempts}/{max_scroll_attempts}")
        else:
            scroll_attempts = 0  # Reset counter
        
        previous_count = current_count
        
        # Scroll to bottom
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        
        # Wait for new content
        page.wait_for_timeout(2000)
        
        # Alternative: Wait for loading indicator to disappear
        loading_indicator = page.locator('.loading')
        if loading_indicator.is_visible():
            loading_indicator.wait_for(state="hidden", timeout=5000)
    
    print(f"✅ Total items scraped: {len(all_items)}")
    return all_items

# Usage
page.goto("https://infinite-scroll-example.com")
items = scrape_infinite_scroll(page, max_items=200)
```

#### Advanced Infinite Scroll with Intersection Observer:
```python
def advanced_infinite_scroll(page):
    """Intersection Observer দিয়ে smart infinite scroll"""
    
    # Inject scroll detection script
    page.evaluate("""
        window.scrollData = {
            items: [],
            isLoading: false,
            hasMore: true
        };
        
        // Intersection Observer setup
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !window.scrollData.isLoading) {
                    window.scrollData.isLoading = true;
                    // Trigger scroll event
                    window.dispatchEvent(new CustomEvent('needMoreContent'));
                }
            });
        });
        
        // Observe the last item
        function observeLastItem() {
            const items = document.querySelectorAll('.item');
            if (items.length > 0) {
                observer.observe(items[items.length - 1]);
            }
        }
        
        // Initial observation
        setTimeout(observeLastItem, 1000);
    """)
    
    all_items = []
    
    while True:
        # Wait for scroll trigger or timeout
        try:
            page.wait_for_event('console', predicate=lambda msg: 'needMoreContent' in msg.text, timeout=5000)
        except:
            break
        
        # Extract current items
        items = page.locator('.item').all()
        
        for item in items[len(all_items):]:
            item_data = extract_item_data(item)
            all_items.append(item_data)
        
        # Check if more content available
        has_more = page.evaluate("window.scrollData.hasMore")
        if not has_more:
            break
        
        # Re-observe new last item
        page.evaluate("observeLastItem()")
        
        print(f"📊 Items loaded: {len(all_items)}")
    
    return all_items
```

### 🔄 Pagination Handling:

#### Simple Pagination:
```python
def scrape_paginated_content(page, base_url, max_pages=10):
    """Paginated content scrape করা"""
    
    all_data = []
    current_page = 1
    
    while current_page <= max_pages:
        # Navigate to page
        page_url = f"{base_url}?page={current_page}"
        page.goto(page_url)
        
        # Wait for content
        page.wait_for_selector('.content', timeout=10000)
        
        # Check if page has content
        items = page.locator('.item').all()
        if not items:
            print(f"❌ No content found on page {current_page}")
            break
        
        # Extract data
        page_data = []
        for item in items:
            item_data = {
                'title': item.locator('.title').text_content(),
                'content': item.locator('.content').text_content(),
                'page': current_page
            }
            page_data.append(item_data)
        
        all_data.extend(page_data)
        print(f"✅ Page {current_page}: {len(page_data)} items")
        
        # Check for next page button
        next_button = page.locator('.next-page')
        if not next_button.is_visible() or next_button.is_disabled():
            print("📄 Reached last page")
            break
        
        current_page += 1
        
        # Rate limiting
        page.wait_for_timeout(1000)
    
    return all_data
```

#### Smart Pagination with URL Pattern Detection:
```python
def smart_pagination_scraper(page, start_url):
    """URL pattern detect করে automatic pagination"""
    
    page.goto(start_url)
    
    # Detect pagination pattern
    pagination_info = page.evaluate("""
        () => {
            const nextBtn = document.querySelector('.next, .pagination .next, [aria-label*="next"]');
            const pageLinks = document.querySelectorAll('.pagination a, .page-numbers a');
            const currentPage = document.querySelector('.current, .active, .pagination .current');
            
            return {
                hasNextButton: !!nextBtn,
                nextButtonSelector: nextBtn ? nextBtn.className : null,
                totalPages: pageLinks.length,
                currentPageText: currentPage ? currentPage.textContent : '1'
            };
        }
    """)
    
    print(f"📊 Pagination info: {pagination_info}")
    
    all_data = []
    page_num = 1
    
    while True:
        # Extract current page data
        page_data = extract_page_data(page)
        all_data.extend(page_data)
        
        print(f"✅ Page {page_num}: {len(page_data)} items")
        
        # Try to go to next page
        if pagination_info['hasNextButton']:
            next_btn = page.locator('.next')
            if next_btn.is_visible() and next_btn.is_enabled():
                next_btn.click()
                page.wait_for_load_state('networkidle')
                page_num += 1
            else:
                break
        else:
            # Try URL pattern
            try:
                next_url = f"{start_url.split('?')[0]}?page={page_num + 1}"
                response = page.goto(next_url)
                if response.status == 404:
                    break
                page_num += 1
            except:
                break
    
    return all_data

def extract_page_data(page):
    """Extract data from current page"""
    items = page.locator('.item').all()
    data = []
    
    for item in items:
        try:
            item_data = {
                'title': item.locator('.title').text_content().strip(),
                'description': item.locator('.description').text_content().strip(),
                'url': item.locator('a').get_attribute('href')
            }
            data.append(item_data)
        except:
            continue
    
    return data
```

### 🎭 Dynamic Content Handling:

#### AJAX Content Loading:
```python
def wait_for_ajax_content(page, trigger_selector, content_selector):
    """AJAX content load হওয়ার জন্য অপেক্ষা"""
    
    # Initial content count
    initial_count = page.locator(content_selector).count()
    
    # Trigger AJAX call
    page.locator(trigger_selector).click()
    
    # Wait for new content
    page.wait_for_function(
        f"document.querySelectorAll('{content_selector}').length > {initial_count}",
        timeout=10000
    )
    
    # Wait for loading indicator to disappear
    loading = page.locator('.loading, .spinner')
    if loading.is_visible():
        loading.wait_for(state="hidden")
    
    print("✅ AJAX content loaded")

# Usage
wait_for_ajax_content(page, '.load-more-btn', '.product-item')
```

#### SPA (Single Page Application) Navigation:
```python
def scrape_spa_navigation(page, routes):
    """SPA routes navigate করে data scrape"""
    
    all_data = {}
    
    for route_name, route_path in routes.items():
        print(f"🔄 Navigating to {route_name}...")
        
        # Navigate using JavaScript (SPA style)
        page.evaluate(f"window.history.pushState({{}}, '', '{route_path}')")
        
        # Trigger route change event
        page.evaluate("window.dispatchEvent(new PopStateEvent('popstate'))")
        
        # Wait for route content
        page.wait_for_function(
            f"window.location.pathname === '{route_path}'",
            timeout=5000
        )
        
        # Wait for content to load
        page.wait_for_selector('[data-testid="content"]', timeout=10000)
        
        # Extract route-specific data
        route_data = extract_spa_data(page, route_name)
        all_data[route_name] = route_data
        
        print(f"✅ {route_name}: {len(route_data)} items")
    
    return all_data

def extract_spa_data(page, route_type):
    """SPA route থেকে data extract"""
    
    if route_type == 'products':
        return [
            {
                'name': item.locator('.name').text_content(),
                'price': item.locator('.price').text_content()
            }
            for item in page.locator('.product-card').all()
        ]
    elif route_type == 'users':
        return [
            {
                'username': item.locator('.username').text_content(),
                'email': item.locator('.email').text_content()
            }
            for item in page.locator('.user-card').all()
        ]
    
    return []

# Usage
spa_routes = {
    'products': '/products',
    'users': '/users',
    'orders': '/orders'
}

spa_data = scrape_spa_navigation(page, spa_routes)
```

### 🔐 Authentication & Session Management:

#### Cookie-based Authentication:
```python
def login_with_cookies(page, login_url, credentials, cookie_file=None):
    """Cookie দিয়ে authentication"""
    
    # Load existing cookies if available
    if cookie_file and os.path.exists(cookie_file):
        with open(cookie_file, 'r') as f:
            cookies = json.load(f)
            page.context.add_cookies(cookies)
        
        # Test if still logged in
        page.goto(login_url)
        if page.locator('.dashboard, .profile').is_visible():
            print("✅ Already logged in with saved cookies")
            return True
    
    # Perform login
    page.goto(login_url)
    
    # Fill login form
    page.locator('input[name="username"]').fill(credentials['username'])
    page.locator('input[name="password"]').fill(credentials['password'])
    
    # Handle CSRF token if present
    csrf_token = page.locator('input[name="csrf_token"]')
    if csrf_token.is_visible():
        token_value = csrf_token.get_attribute('value')
        print(f"🔐 CSRF Token: {token_value}")
    
    # Submit login
    page.locator('button[type="submit"]').click()
    
    # Wait for login result
    try:
        page.wait_for_url('**/dashboard', timeout=5000)
        print("✅ Login successful")
        
        # Save cookies for future use
        if cookie_file:
            cookies = page.context.cookies()
            with open(cookie_file, 'w') as f:
                json.dump(cookies, f)
            print(f"💾 Cookies saved to {cookie_file}")
        
        return True
        
    except:
        error_msg = page.locator('.error, .alert-danger').text_content()
        print(f"❌ Login failed: {error_msg}")
        return False

# Usage
credentials = {'username': 'myuser', 'password': 'mypass'}
success = login_with_cookies(page, 'https://example.com/login', credentials, 'cookies.json')
```

---

## 🧠 JavaScript Execution ও Evaluation {#javascript-execution}

### 🎯 Basic JavaScript Execution:

#### Simple JavaScript Commands:
```python
# Basic JavaScript execution
page_title = page.evaluate("document.title")
page_url = page.evaluate("window.location.href")
scroll_position = page.evaluate("window.pageYOffset")

# DOM manipulation
page.evaluate("document.body.style.backgroundColor = 'lightblue'")
page.evaluate("document.querySelector('h1').style.color = 'red'")

# Get element properties
element_text = page.evaluate("document.querySelector('.price').textContent")
element_html = page.evaluate("document.querySelector('.content').innerHTML")

# Array of elements
all_links = page.evaluate("""
    Array.from(document.querySelectorAll('a')).map(link => ({
        text: link.textContent,
        href: link.href
    }))
""")

print(f"Found {len(all_links)} links")
```

#### Advanced JavaScript Functions:
```python
def inject_helper_functions(page):
    """Useful JavaScript functions inject করা"""

    page.evaluate("""
        // Helper functions
        window.scrapeHelpers = {
            // Get all text content from elements
            getAllText: (selector) => {
                return Array.from(document.querySelectorAll(selector))
                    .map(el => el.textContent.trim())
                    .filter(text => text.length > 0);
            },

            // Get element with all attributes
            getElementData: (selector) => {
                const element = document.querySelector(selector);
                if (!element) return null;

                const attributes = {};
                for (let attr of element.attributes) {
                    attributes[attr.name] = attr.value;
                }

                return {
                    tagName: element.tagName,
                    textContent: element.textContent.trim(),
                    innerHTML: element.innerHTML,
                    attributes: attributes,
                    boundingRect: element.getBoundingClientRect()
                };
            },

            // Wait for element with custom condition
            waitForCondition: (condition, timeout = 5000) => {
                return new Promise((resolve, reject) => {
                    const startTime = Date.now();

                    function check() {
                        if (condition()) {
                            resolve(true);
                        } else if (Date.now() - startTime > timeout) {
                            reject(new Error('Timeout waiting for condition'));
                        } else {
                            setTimeout(check, 100);
                        }
                    }

                    check();
                });
            },

            // Scroll to element smoothly
            scrollToElement: (selector) => {
                const element = document.querySelector(selector);
                if (element) {
                    element.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    return true;
                }
                return false;
            }
        };
    """)

# Usage
inject_helper_functions(page)

# Use helper functions
all_prices = page.evaluate("window.scrapeHelpers.getAllText('.price')")
product_data = page.evaluate("window.scrapeHelpers.getElementData('.product-main')")
```

### 🔄 Asynchronous JavaScript:

#### Promise-based Operations:
```python
def execute_async_js(page):
    """Async JavaScript operations"""

    # Fetch API call
    api_data = page.evaluate("""
        async () => {
            try {
                const response = await fetch('/api/products');
                const data = await response.json();
                return data;
            } catch (error) {
                return { error: error.message };
            }
        }
    """)

    # Wait for animation to complete
    page.evaluate("""
        async () => {
            const element = document.querySelector('.animated');
            if (element) {
                // Wait for CSS animation to end
                await new Promise(resolve => {
                    element.addEventListener('animationend', resolve, { once: true });
                });
            }
        }
    """)

    # Custom async operation
    result = page.evaluate("""
        async () => {
            // Simulate async data loading
            await new Promise(resolve => setTimeout(resolve, 2000));

            // Process data
            const elements = document.querySelectorAll('.item');
            const processedData = [];

            for (let element of elements) {
                // Simulate processing delay
                await new Promise(resolve => setTimeout(resolve, 100));

                processedData.push({
                    text: element.textContent,
                    visible: element.offsetParent !== null
                });
            }

            return processedData;
        }
    """)

    return result
```

### 🎨 DOM Manipulation:

#### Dynamic Content Creation:
```python
def create_extraction_ui(page):
    """Page এ data extraction UI তৈরি করা"""

    page.evaluate("""
        // Create extraction panel
        const panel = document.createElement('div');
        panel.id = 'extraction-panel';
        panel.style.cssText = `
            position: fixed;
            top: 10px;
            right: 10px;
            width: 300px;
            background: white;
            border: 2px solid #333;
            padding: 10px;
            z-index: 10000;
            font-family: Arial, sans-serif;
        `;

        panel.innerHTML = `
            <h3>Data Extraction Panel</h3>
            <button id="extract-products">Extract Products</button>
            <button id="extract-links">Extract Links</button>
            <div id="results"></div>
        `;

        document.body.appendChild(panel);

        // Add event listeners
        document.getElementById('extract-products').onclick = () => {
            const products = Array.from(document.querySelectorAll('.product')).map(p => ({
                name: p.querySelector('.name')?.textContent || 'N/A',
                price: p.querySelector('.price')?.textContent || 'N/A'
            }));

            document.getElementById('results').innerHTML =
                '<pre>' + JSON.stringify(products, null, 2) + '</pre>';
        };

        document.getElementById('extract-links').onclick = () => {
            const links = Array.from(document.querySelectorAll('a')).map(a => ({
                text: a.textContent.trim(),
                href: a.href
            }));

            document.getElementById('results').innerHTML =
                '<pre>' + JSON.stringify(links, null, 2) + '</pre>';
        };
    """)

# Usage
create_extraction_ui(page)
```

---

## 🌐 Request/Response Interception {#request-interception}

### 🔍 Basic Request Monitoring:

#### Simple Request Logging:
```python
def setup_request_logging(page):
    """সব network requests log করা"""

    requests_log = []

    def log_request(request):
        request_data = {
            'url': request.url,
            'method': request.method,
            'headers': dict(request.headers),
            'post_data': request.post_data,
            'timestamp': time.time()
        }
        requests_log.append(request_data)
        print(f"📤 {request.method} {request.url}")

    def log_response(response):
        print(f"📥 {response.status} {response.url}")

        # Log API responses
        if 'api' in response.url or response.headers.get('content-type', '').startswith('application/json'):
            try:
                json_data = response.json()
                print(f"📊 API Response: {json_data}")
            except:
                pass

    # Attach event listeners
    page.on('request', log_request)
    page.on('response', log_response)

    return requests_log

# Usage
requests_log = setup_request_logging(page)
page.goto("https://example.com")
print(f"Total requests: {len(requests_log)}")
```

### 🚫 Request Blocking & Modification:

#### Advanced Request Blocking:
```python
def setup_smart_blocking(page):
    """Smart request blocking system"""

    # Define blocking rules
    blocking_rules = {
        'ads': [
            'doubleclick.net', 'googlesyndication.com', 'googletagmanager.com',
            'facebook.com/tr', 'google-analytics.com', 'hotjar.com'
        ],
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'],
        'fonts': ['.woff', '.woff2', '.ttf', '.otf'],
        'media': ['.mp4', '.mp3', '.avi', '.mov'],
        'tracking': ['analytics', 'tracking', 'pixel', 'beacon']
    }

    blocked_count = {'ads': 0, 'images': 0, 'fonts': 0, 'media': 0, 'tracking': 0}

    def handle_route(route, request):
        url = request.url.lower()
        resource_type = request.resource_type

        # Check blocking rules
        for category, patterns in blocking_rules.items():
            if any(pattern in url for pattern in patterns):
                blocked_count[category] += 1
                print(f"🚫 Blocked {category}: {url}")
                route.abort()
                return

        # Block by resource type
        if resource_type in ['image', 'font', 'media']:
            blocked_count[resource_type] = blocked_count.get(resource_type, 0) + 1
            route.abort()
            return

        # Allow request
        route.continue_()

    # Setup route interception
    page.route("**/*", handle_route)

    return blocked_count

# Usage
blocked_stats = setup_smart_blocking(page)
page.goto("https://example.com")
print(f"Blocking stats: {blocked_stats}")
```

#### Request Modification:
```python
def setup_request_modification(page):
    """Request headers এবং data modify করা"""

    def modify_request(route, request):
        # Custom headers add করা
        headers = {
            **request.headers,
            'X-Custom-Header': 'Playwright-Scraper',
            'Accept-Language': 'bn-BD,bn;q=0.9,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        # API requests modify করা
        if '/api/' in request.url:
            # Add authentication header
            headers['Authorization'] = 'Bearer your-token-here'

            # Modify POST data
            if request.method == 'POST' and request.post_data:
                try:
                    post_data = json.loads(request.post_data)
                    post_data['modified_by'] = 'playwright'
                    modified_data = json.dumps(post_data)

                    route.continue_(
                        headers=headers,
                        post_data=modified_data
                    )
                    return
                except:
                    pass

        # Continue with modified headers
        route.continue_(headers=headers)

    page.route("**/*", modify_request)

# Usage
setup_request_modification(page)
```

### 📡 Response Interception:

#### Response Data Capture:
```python
def capture_api_responses(page):
    """API responses capture এবং analyze করা"""

    api_responses = {}

    def handle_response(response):
        url = response.url

        # Only capture API responses
        if '/api/' in url or response.headers.get('content-type', '').startswith('application/json'):
            try:
                response_data = {
                    'url': url,
                    'status': response.status,
                    'headers': dict(response.headers),
                    'data': response.json(),
                    'timestamp': time.time()
                }

                # Store by endpoint
                endpoint = url.split('/api/')[-1].split('?')[0]
                api_responses[endpoint] = response_data

                print(f"📊 Captured API: {endpoint}")

            except Exception as e:
                print(f"❌ Error capturing response: {e}")

    page.on('response', handle_response)
    return api_responses

# Usage
api_data = capture_api_responses(page)
page.goto("https://spa-example.com")

# Analyze captured data
for endpoint, data in api_data.items():
    print(f"🔍 {endpoint}: {len(data['data'])} items")
```
```
