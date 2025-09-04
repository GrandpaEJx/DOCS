# 🎭 Playwright দিয়ে ওয়েব স্ক্র্যাপিং - A to Z সম্পূর্ণ গাইড 🇧🇩

## 📚 সূচিপত্র
1. [Playwright কি এবং কেন?](#what-is-playwright)
2. [ইনস্টলেশন ও সেটআপ](#installation-setup)
3. [ডেভেলপার টুলস (DevTools) মাস্টারি](#devtools-mastery)
4. [নেটওয়ার্ক ট্যাব মনিটরিং](#network-monitoring)
5. [HTML/CSS সিলেক্টর এক্সপার্ট](#selectors-expert)
6. [Playwright বেসিক - Browser ও Page](#playwright-basics)
7. [Element Interaction - Click, Type, Fill](#element-interaction)
8. [অ্যাডভান্স স্ক্র্যাপিং টেকনিক](#advanced-scraping)
9. [JavaScript Execution ও Evaluation](#javascript-execution)
10. [Request/Response Interception](#request-interception)
11. [Mobile ও Multi-Browser Testing](#mobile-multi-browser)
12. [Performance ও Optimization](#performance-optimization)
13. [Error Handling ও Debugging](#error-handling)
14. [Real-World প্রজেক্ট](#real-world-projects)
15. [Best Practices ও Security](#best-practices)

---

## 🎭 Playwright কি এবং কেন? {#what-is-playwright}

### 🤔 Playwright কি?
**Playwright** হলো Microsoft এর তৈরি একটি শক্তিশালী browser automation library যা দিয়ে আপনি:
- **Real Browser Control:** Chrome, Firefox, Safari নিয়ন্ত্রণ করতে পারেন
- **JavaScript Rendering:** Dynamic content load করতে পারেন
- **User Interaction:** Click, type, scroll করতে পারেন
- **Mobile Testing:** Mobile device emulate করতে পারেন

### 🚀 কেন Playwright ব্যবহার করবেন?

#### ✅ **Playwright এর সুবিধা:**
- **Fast & Reliable:** অন্যান্য tools থেকে দ্রুত
- **Multi-Browser:** Chrome, Firefox, Safari support
- **Mobile Support:** iOS/Android emulation
- **Network Control:** Request/Response intercept করতে পারেন
- **Screenshot/PDF:** Page capture করতে পারেন
- **Headless/Headed:** দুটো mode এ কাজ করে

#### ❌ **অন্যান্য Tools এর সমস্যা:**
- **Requests + BeautifulSoup:** JavaScript render করে না
- **Selenium:** ধীর এবং unstable
- **Puppeteer:** শুধু Chrome support

### 🎯 কখন Playwright ব্যবহার করবেন?
- ✅ **Dynamic Content:** JavaScript দিয়ে load হওয়া content
- ✅ **User Interaction:** Form fill, button click প্রয়োজন
- ✅ **SPA (Single Page Apps):** React, Vue, Angular sites
- ✅ **Authentication:** Login করে data নিতে হবে
- ✅ **Complex Navigation:** Multi-step process

---

## 🛠️ ইনস্টলেশন ও সেটআপ {#installation-setup}

### 📋 প্রয়োজনীয় সফটওয়্যার:
1. **Python 3.8+** (অবশ্যই প্রয়োজন)
2. **VS Code** বা যেকোনো code editor
3. **Terminal/Command Prompt**

### 🐍 Playwright ইনস্টল করুন:
```bash
# Playwright Python package install
pip install playwright

# Browser binaries install (গুরুত্বপূর্ণ!)
playwright install

# Specific browser install করতে চাইলে
playwright install chromium
playwright install firefox
playwright install webkit
```

### ✅ ইনস্টলেশন টেস্ট:
```python
# test_installation.py
from playwright.sync_api import sync_playwright

def test_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")
        print(f"Page title: {page.title()}")
        browser.close()
        print("✅ Playwright successfully installed!")

if __name__ == "__main__":
    test_playwright()
```

### 🚀 প্রথম Playwright প্রোগ্রাম:
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Browser launch করুন
    browser = p.chromium.launch(headless=False)  # headless=True করলে browser দেখা যাবে না

    # নতুন page তৈরি করুন
    page = browser.new_page()

    # Website এ যান
    page.goto("https://example.com")

    # Page title print করুন
    print(f"Title: {page.title()}")

    # Browser বন্ধ করুন
    browser.close()
```

---

## 🔧 ডেভেলপার টুলস (DevTools) মাস্টারি {#devtools-mastery}

### 🖱️ DevTools খোলার উপায়:
- **Windows/Linux:** `F12` বা `Ctrl+Shift+I`
- **Mac:** `Cmd+Option+I`
- **Right Click:** "Inspect Element"
- **Playwright থেকে:** `args=["--auto-open-devtools-for-tabs"]`

### 📱 DevTools এর প্রধান ট্যাবসমূহ:

#### 1️⃣ **Elements Tab** (HTML/CSS Analysis)
```html
<!-- এভাবে HTML structure দেখতে পাবেন -->
<div class="product" data-id="123">
    <h2 class="title">পণ্যের নাম</h2>
    <span class="price" data-currency="BDT">৫০০ টাকা</span>
    <button class="add-to-cart" onclick="addToCart(123)">Add to Cart</button>
</div>
```

**🎯 Advanced Element Inspection:**
- **Element select:** `Ctrl+Shift+C` (Windows) / `Cmd+Shift+C` (Mac)
- **CSS properties:** Right panel এ "Styles", "Computed", "Layout"
- **Selector copy:** Right click → Copy → Copy selector/XPath/JS path
- **Event listeners:** "Event Listeners" tab এ click events দেখুন
- **Accessibility:** "Accessibility" tab এ screen reader info

#### 2️⃣ **Console Tab** (JavaScript Testing Ground)
```javascript
// Console এ এই advanced কমান্ডগুলো চালিয়ে দেখুন

// Basic DOM queries
document.title                           // পেজের টাইটেল
document.querySelector('h1')             // প্রথম h1 element
document.querySelectorAll('.price')      // সব price class elements
document.getElementById('main-content')   // ID দিয়ে element

// Advanced queries
$('h1')                                  // jQuery-style selector (Chrome DevTools)
$$('.product')                           // সব .product elements (Chrome DevTools)
$x('//div[@class="product"]')            // XPath selector

// Element properties
let element = document.querySelector('.price');
element.textContent                      // Text content
element.innerHTML                        // HTML content
element.getAttribute('data-currency')    // Attribute value
element.style.color = 'red'             // Style change

// Page manipulation
window.scrollTo(0, document.body.scrollHeight)  // Scroll to bottom
localStorage.getItem('user_data')        // Local storage data
sessionStorage.setItem('test', 'value')  // Session storage
document.cookie                          // All cookies

// Network and performance
performance.now()                        // Current timestamp
navigator.userAgent                      // Browser info
window.location.href                     // Current URL
```

#### 3️⃣ **Sources Tab** (JavaScript Debugging)
- **File explorer:** সব JavaScript, CSS files
- **Breakpoints:** Code execution থামানোর জন্য
- **Watch expressions:** Variable values monitor করা
- **Call stack:** Function call hierarchy
- **Scope:** Current scope এর variables

**🔍 Debugging টিপস:**
```javascript
// Console এ debugging commands
debugger;                    // Code এ breakpoint set করা
console.log('Debug info');   // Simple logging
console.table(data);         // Table format এ data
console.time('operation');   // Performance timing start
console.timeEnd('operation'); // Performance timing end
```

---

## 📡 নেটওয়ার্ক ট্যাব মনিটরিং {#network-monitoring}

### 🌐 Network Tab কেন অত্যন্ত গুরুত্বপূর্ণ?
Network Tab হলো web scraping এর **সবচেয়ে শক্তিশালী টুল**। এখানে আপনি দেখতে পাবেন:
- 🔍 **API Endpoints:** Hidden API calls
- 📡 **AJAX Requests:** Dynamic content loading
- 🍪 **Cookies & Headers:** Authentication info
- 📊 **Response Data:** Raw JSON/XML data
- ⏱️ **Timing Info:** Performance metrics

### 🔍 Network Tab Advanced ব্যবহার:

#### ধাপ ১: Network Tab Setup
```javascript
// DevTools খোলার পর Console এ এই command চালান
// Network requests clear করতে
console.clear();

// অথবা Playwright দিয়ে auto-open
```

```python
# Playwright এ DevTools auto-open
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=["--auto-open-devtools-for-tabs"]
    )
    page = browser.new_page()
    page.goto("https://example.com")
```

#### ধাপ ২: Request Types ও Filtering
```
🎯 Advanced Filter Options:
- All: সব requests (default)
- Fetch/XHR: API calls এবং AJAX requests
- JS: JavaScript files
- CSS: Stylesheet files
- Img: Images (PNG, JPG, SVG)
- Media: Videos, Audio files
- Font: Web fonts (WOFF, TTF)
- Doc: HTML documents
- WS: WebSocket connections
- Manifest: PWA manifest files
```

#### ধাপ ৩: Request Analysis (বিস্তারিত)
একটি request এ ক্লিক করলে এই tabs পাবেন:

**📋 Headers Tab:**
```
General:
- Request URL: https://api.example.com/products
- Request Method: GET/POST/PUT/DELETE
- Status Code: 200 OK / 404 Not Found
- Remote Address: 192.168.1.1:443

Request Headers:
- User-Agent: Browser information
- Accept: Content types accepted
- Authorization: Bearer token/API key
- Cookie: Session cookies
- Referer: Previous page URL

Response Headers:
- Content-Type: application/json
- Set-Cookie: New cookies
- Access-Control-Allow-Origin: CORS settings
- Cache-Control: Caching rules
```

**👁️ Preview Tab:**
- JSON data এর formatted view
- Images এর preview
- HTML content এর rendered view

**📄 Response Tab:**
- Raw response data
- JSON, XML, HTML source code
- Binary data (images, files)

**⏱️ Timing Tab:**
```
Request timing breakdown:
- Queueing: Request queue time
- Stalled: Network stack delay
- DNS Lookup: Domain resolution
- Initial Connection: TCP handshake
- SSL: SSL/TLS negotiation
- Request Sent: Upload time
- Waiting (TTFB): Time to First Byte
- Content Download: Download time
```

### 🎯 Playwright দিয়ে Network Monitoring:

#### Request/Response Interception:
```python
from playwright.sync_api import sync_playwright

def monitor_network():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # All network requests capture করা
        requests_log = []

        def handle_request(request):
            requests_log.append({
                'url': request.url,
                'method': request.method,
                'headers': request.headers,
                'post_data': request.post_data
            })
            print(f"📤 Request: {request.method} {request.url}")

        def handle_response(response):
            print(f"📥 Response: {response.status} {response.url}")

            # JSON response parse করা
            if 'application/json' in response.headers.get('content-type', ''):
                try:
                    json_data = response.json()
                    print(f"📊 JSON Data: {json_data}")
                except:
                    pass

        # Event listeners attach করা
        page.on('request', handle_request)
        page.on('response', handle_response)

        # Website navigate করা
        page.goto("https://example.com")
        page.wait_for_load_state('networkidle')

        # Captured requests analysis
        print(f"\n📋 Total Requests: {len(requests_log)}")
        for req in requests_log:
            if 'api' in req['url']:
                print(f"🔍 API Found: {req['url']}")

        browser.close()

monitor_network()
```

### 💡 Real-World Network Analysis Example:
```python
def find_hidden_apis():
    """E-commerce site এর hidden API খুঁজে বের করা"""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        api_endpoints = []

        def capture_api_calls(response):
            url = response.url

            # API patterns খুঁজে বের করা
            api_patterns = ['/api/', '/ajax/', '.json', '/graphql', '/rest/']

            if any(pattern in url for pattern in api_patterns):
                api_info = {
                    'url': url,
                    'status': response.status,
                    'method': response.request.method,
                    'headers': dict(response.headers)
                }

                # Response data capture করা
                try:
                    if response.headers.get('content-type', '').startswith('application/json'):
                        api_info['data'] = response.json()
                except:
                    pass

                api_endpoints.append(api_info)
                print(f"🎯 API Found: {url}")

        page.on('response', capture_api_calls)

        # E-commerce site navigate করা
        page.goto("https://example-shop.com")

        # Product search করা (API calls trigger করার জন্য)
        search_box = page.locator('input[type="search"]')
        if search_box.is_visible():
            search_box.fill('laptop')
            search_box.press('Enter')
            page.wait_for_load_state('networkidle')

        # Results analysis
        print(f"\n🔍 Found {len(api_endpoints)} API endpoints:")
        for api in api_endpoints:
            print(f"  📡 {api['method']} {api['url']} - Status: {api['status']}")

        browser.close()
        return api_endpoints

# Function call করা
apis = find_hidden_apis()
```

---

## 🎯 HTML/CSS সিলেক্টর এক্সপার্ট {#selectors-expert}

### 📝 HTML Structure Deep Dive:
```html
<!DOCTYPE html>
<html lang="bn">
<head>
    <title>E-commerce Product Page</title>
    <meta charset="UTF-8">
</head>
<body>
    <nav class="navbar" id="main-nav">
        <ul class="nav-links">
            <li><a href="/home" class="nav-link active">Home</a></li>
            <li><a href="/products" class="nav-link">Products</a></li>
        </ul>
    </nav>

    <main class="container">
        <section class="product-section" data-category="electronics">
            <h1 id="product-title" class="title main-title">iPhone 15 Pro</h1>
            <div class="product-info">
                <span class="price" data-currency="BDT" data-amount="120000">১,২০,০০০ টাকা</span>
                <div class="rating" data-rating="4.5">
                    <span class="stars">★★★★☆</span>
                    <span class="rating-text">(4.5/5)</span>
                </div>
            </div>

            <ul class="features-list">
                <li class="feature-item" data-feature="camera">48MP Camera</li>
                <li class="feature-item" data-feature="storage">256GB Storage</li>
                <li class="feature-item" data-feature="display">6.1" Display</li>
            </ul>

            <form class="purchase-form" id="buy-form">
                <input type="number" name="quantity" value="1" min="1" class="quantity-input">
                <button type="submit" class="btn btn-primary add-to-cart" data-product-id="12345">
                    Add to Cart
                </button>
            </form>
        </section>

        <aside class="sidebar">
            <div class="related-products">
                <h3>Related Products</h3>
                <div class="product-card" data-id="67890">
                    <img src="product2.jpg" alt="iPhone 14" class="product-image">
                    <h4 class="product-name">iPhone 14</h4>
                    <span class="product-price">৯৫,০০০ টাকা</span>
                </div>
            </div>
        </aside>
    </main>

    <footer class="footer">
        <p>&copy; 2024 My Shop</p>
    </footer>
</body>
</html>
```

### 🎯 CSS Selectors - Complete Guide:

#### 1️⃣ **বেসিক সিলেক্টর:**
```css
/* Element/Tag Selector */
h1                  → সব h1 elements
div                 → সব div elements
span                → সব span elements

/* Class Selector */
.container          → class="container"
.product-info       → class="product-info"
.btn.btn-primary    → class="btn btn-primary" (multiple classes)

/* ID Selector */
#product-title      → id="product-title"
#main-nav           → id="main-nav"

/* Universal Selector */
*                   → সব elements
```

#### 2️⃣ **Attribute Selectors:**
```css
/* Attribute exists */
[data-category]     → data-category attribute আছে
[href]              → href attribute আছে

/* Attribute equals */
[data-currency="BDT"]     → data-currency="BDT"
[type="submit"]           → type="submit"

/* Attribute contains */
[class*="btn"]            → class এ "btn" আছে
[data-feature*="camera"]  → data-feature এ "camera" আছে

/* Attribute starts with */
[class^="product"]        → class "product" দিয়ে শুরু
[href^="https"]           → href "https" দিয়ে শুরু

/* Attribute ends with */
[class$="primary"]        → class "primary" দিয়ে শেষ
[src$=".jpg"]             → src ".jpg" দিয়ে শেষ
```

#### 3️⃣ **Combinators (সম্পর্ক নির্দেশক):**
```css
/* Descendant (বংশধর) */
.container h1             → container এর ভিতরের যেকোনো h1
.product-section span     → product-section এর ভিতরের যেকোনো span

/* Child (সন্তান) */
.container > h1           → container এর direct child h1
.nav-links > li           → nav-links এর direct child li

/* Adjacent Sibling (পাশের ভাই) */
h1 + div                  → h1 এর ঠিক পরের div
.price + .rating          → price এর ঠিক পরের rating

/* General Sibling (সব ভাই) */
h1 ~ div                  → h1 এর পরের সব div
.price ~ span             → price এর পরের সব span
```

#### 4️⃣ **Pseudo Selectors:**
```css
/* Structural Pseudo-classes */
li:first-child            → প্রথম li
li:last-child             → শেষ li
li:nth-child(2)           → ২য় li
li:nth-child(odd)         → বিজোড় position এর li
li:nth-child(even)        → জোড় position এর li
li:nth-child(3n+1)        → ৩n+১ position এর li

/* State Pseudo-classes */
a:hover                   → mouse hover করলে
input:focus               → input field focus করলে
button:disabled           → disabled button
input:checked             → checked checkbox/radio

/* Content Pseudo-classes */
p:empty                   → খালি p elements
div:not(.sidebar)         → sidebar class নেই এমন div
```

#### 5️⃣ **Advanced Selectors:**
```css
/* Multiple Selectors */
h1, h2, h3                → সব h1, h2, h3
.price, .rating           → price অথবা rating class

/* Complex Combinations */
.product-section .price:not(.discount)    → product-section এর ভিতরের price class যার discount class নেই
.container > .product-info span[data-currency] → container এর direct child product-info এর span যার data-currency আছে

/* Case-insensitive Attribute */
[data-feature="CAMERA" i] → case-insensitive matching
```

### 🎭 Playwright এ Selector ব্যবহার:

#### Text-based Selectors (Playwright Special):
```python
# Text content দিয়ে select করা
page.locator('text="Add to Cart"')           # Exact text match
page.locator('text=/Add.*Cart/i')            # Regex match (case-insensitive)
page.locator('"Add to Cart"')                # Shorthand for exact text

# Partial text match
page.locator('text="Add"')                   # "Add" text আছে এমন element

# Role-based selectors (Accessibility)
page.locator('role=button[name="Add to Cart"]')  # Button role with name
page.locator('role=textbox[name="Search"]')      # Textbox role
page.locator('role=link[name="Home"]')           # Link role
```

#### XPath Selectors:
```python
# XPath দিয়ে complex selection
page.locator('xpath=//div[@class="product-info"]//span[@data-currency="BDT"]')
page.locator('xpath=//button[contains(text(), "Add")]')
page.locator('xpath=//li[position()=2]')     # ২য় li element
page.locator('xpath=//div[following-sibling::span[@class="price"]]')  # price class এর আগের div
```

### 💡 Selector Testing ও Debugging:

#### DevTools Console এ Test করা:
```javascript
// CSS Selector test
document.querySelector('.product-info .price')
document.querySelectorAll('.feature-item')

// XPath test
$x('//div[@class="product-info"]//span[@data-currency="BDT"]')

// Playwright-style text selector simulation
document.evaluate('//button[contains(text(), "Add to Cart")]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue
```

#### Playwright এ Selector Debugging:
```python
# Selector highlight করা
page.locator('.price').highlight()

# Element count check করা
count = page.locator('.feature-item').count()
print(f"Found {count} feature items")

# Wait for selector
page.wait_for_selector('.product-info', timeout=5000)

# Check if selector exists
if page.locator('.add-to-cart').is_visible():
    print("Add to cart button is visible")
```

---

## 🎭 Playwright বেসিক - Browser ও Page {#playwright-basics}

### 🚀 Browser Launch Options:

#### Basic Browser Launch:
```python
from playwright.sync_api import sync_playwright

# সবচেয়ে সিম্পল way
with sync_playwright() as p:
    browser = p.chromium.launch()  # Headless mode (default)
    page = browser.new_page()
    page.goto("https://example.com")
    print(page.title())
    browser.close()
```

#### Advanced Browser Configuration:
```python
def advanced_browser_setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,                    # Browser দেখা যাবে
            slow_mo=1000,                      # প্রতিটি action এ 1 সেকেন্ড delay
            devtools=True,                     # DevTools auto open
            args=[
                "--start-maximized",           # Full screen
                "--disable-blink-features=AutomationControlled",  # Bot detection এড়ানো
                "--disable-web-security",      # CORS disable
                "--disable-features=VizDisplayCompositor",
                "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            ]
        )

        # Browser context with custom settings
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            locale='bn-BD',                    # Bengali locale
            timezone_id='Asia/Dhaka',          # Dhaka timezone
            permissions=['geolocation'],       # Location permission
            geolocation={'latitude': 23.8103, 'longitude': 90.4125}  # Dhaka coordinates
        )

        page = context.new_page()
        return browser, context, page

browser, context, page = advanced_browser_setup()
```

### 🌐 Page Navigation ও Loading:

#### Basic Navigation:
```python
# URL এ যাওয়া
page.goto("https://example.com")

# Wait strategies
page.wait_for_load_state("load")          # HTML load complete
page.wait_for_load_state("domcontentloaded")  # DOM ready
page.wait_for_load_state("networkidle")   # Network idle (recommended)

# Page info
print(f"Title: {page.title()}")
print(f"URL: {page.url}")
print(f"Content: {page.content()[:100]}...")  # First 100 chars
```

#### Advanced Navigation:
```python
def smart_navigation(page, url, max_retries=3):
    """Smart navigation with retry logic"""

    for attempt in range(max_retries):
        try:
            # Navigate with timeout
            response = page.goto(url, timeout=30000, wait_until="networkidle")

            # Check response status
            if response.status >= 400:
                print(f"❌ HTTP Error: {response.status}")
                continue

            # Wait for critical elements
            page.wait_for_selector('body', timeout=10000)

            # Check if page loaded properly
            if page.locator('body').is_visible():
                print(f"✅ Successfully loaded: {url}")
                return True

        except Exception as e:
            print(f"⚠️ Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                page.wait_for_timeout(2000)  # Wait before retry
                continue

    print(f"❌ Failed to load {url} after {max_retries} attempts")
    return False

# Usage
success = smart_navigation(page, "https://example.com")
```

### 🔍 Element Location ও Selection:

#### Modern Locator API:
```python
# Modern way (recommended)
title = page.locator("h1")                    # CSS selector
price = page.locator(".price")                # Class selector
button = page.locator("#submit-btn")          # ID selector

# Text-based locators
add_button = page.locator('text="Add to Cart"')
link = page.locator('text=/Home|হোম/i')       # Regex with Bengali

# Role-based locators (Accessibility)
search_box = page.locator('role=textbox[name="Search"]')
nav_links = page.locator('role=link')

# Attribute-based locators
product = page.locator('[data-product-id="123"]')
images = page.locator('img[alt*="product"]')
```

#### Legacy Selectors (still useful):
```python
# Old way (still works)
title_element = page.query_selector("h1")
all_links = page.query_selector_all("a")

# XPath
xpath_element = page.locator('xpath=//div[@class="product"]//span[@class="price"]')
```

### 📊 Element Information Extraction:

#### Text Content:
```python
# Text content নেওয়া
title_text = page.locator("h1").text_content()
price_text = page.locator(".price").text_content()

# Inner text (visible text only)
visible_text = page.locator(".description").inner_text()

# Inner HTML
html_content = page.locator(".product-info").inner_html()

# All text contents (multiple elements)
all_prices = page.locator(".price").all_text_contents()
print(f"All prices: {all_prices}")
```

#### Attributes:
```python
# Single attribute
link_href = page.locator("a").get_attribute("href")
image_src = page.locator("img").get_attribute("src")
data_id = page.locator(".product").get_attribute("data-id")

# Multiple attributes
element = page.locator(".product-card")
attributes = {
    'id': element.get_attribute('id'),
    'class': element.get_attribute('class'),
    'data-price': element.get_attribute('data-price')
}
print(attributes)
```

#### Element Properties:
```python
# Element visibility
is_visible = page.locator(".popup").is_visible()
is_hidden = page.locator(".loading").is_hidden()

# Element state
is_enabled = page.locator("button").is_enabled()
is_disabled = page.locator("input").is_disabled()
is_checked = page.locator("checkbox").is_checked()

# Element count
product_count = page.locator(".product-card").count()
print(f"Found {product_count} products")
```

### 🎯 Multiple Elements Handling:

#### Working with Lists:
```python
# Get all matching elements
products = page.locator(".product-card").all()

# Loop through elements
for i, product in enumerate(products):
    name = product.locator(".product-name").text_content()
    price = product.locator(".product-price").text_content()
    print(f"{i+1}. {name} - {price}")

# Nth element
first_product = page.locator(".product-card").nth(0)  # First
last_product = page.locator(".product-card").nth(-1)  # Last
second_product = page.locator(".product-card").nth(1) # Second

# Filter elements
expensive_products = page.locator(".product-card").filter(has_text="৫০,০০০")
available_products = page.locator(".product-card").filter(has=page.locator(".in-stock"))
```

#### Advanced Element Queries:
```python
def extract_product_data(page):
    """Extract all product data from a page"""

    products = []
    product_cards = page.locator(".product-card").all()

    for card in product_cards:
        try:
            product_data = {
                'name': card.locator(".product-name").text_content().strip(),
                'price': card.locator(".product-price").text_content().strip(),
                'rating': card.locator(".rating").text_content().strip() if card.locator(".rating").is_visible() else "No rating",
                'image_url': card.locator("img").get_attribute("src"),
                'product_url': card.locator("a").get_attribute("href"),
                'availability': "In Stock" if card.locator(".in-stock").is_visible() else "Out of Stock"
            }
            products.append(product_data)

        except Exception as e:
            print(f"Error extracting product data: {e}")
            continue

    return products

# Usage
products = extract_product_data(page)
print(f"Extracted {len(products)} products")
```

---

## 🖱️ Element Interaction - Click, Type, Fill {#element-interaction}

### 🎯 Click Operations:

#### Basic Clicking:
```python
# Simple click
page.locator("button").click()
page.locator("#submit-btn").click()
page.locator('text="Add to Cart"').click()

# Click with options
page.locator("button").click(
    button="left",           # left, right, middle
    click_count=1,           # Single click (default)
    delay=100,               # Delay between mousedown and mouseup
    force=True,              # Force click even if element is not visible
    no_wait_after=False,     # Wait for navigation after click
    timeout=30000            # Timeout in milliseconds
)

# Double click
page.locator(".file-item").dblclick()

# Right click (context menu)
page.locator(".item").click(button="right")
```

#### Advanced Click Scenarios:
```python
def smart_click(page, selector, max_attempts=3):
    """Smart clicking with retry logic"""

    for attempt in range(max_attempts):
        try:
            element = page.locator(selector)

            # Wait for element to be visible and enabled
            element.wait_for(state="visible", timeout=10000)

            # Scroll into view if needed
            element.scroll_into_view_if_needed()

            # Check if clickable
            if element.is_enabled():
                element.click()
                print(f"✅ Successfully clicked: {selector}")
                return True
            else:
                print(f"⚠️ Element not enabled: {selector}")

        except Exception as e:
            print(f"❌ Click attempt {attempt + 1} failed: {e}")
            if attempt < max_attempts - 1:
                page.wait_for_timeout(1000)
                continue

    return False

# Usage
success = smart_click(page, ".add-to-cart-btn")
```

### ⌨️ Text Input Operations:

#### Basic Text Input:
```python
# Fill input field (clears first, then types)
page.locator('input[name="username"]').fill("my_username")
page.locator('#password').fill("my_password")
page.locator('textarea').fill("This is a long text message")

# Type text (simulates human typing)
page.locator('input[type="search"]').type("laptop computer", delay=100)

# Clear input
page.locator('input').clear()

# Press specific keys
page.locator('input').press("Enter")
page.locator('input').press("Tab")
page.locator('input').press("Escape")
page.locator('input').press("Control+A")  # Select all
```

#### Advanced Text Input:
```python
def fill_form_data(page, form_data):
    """Fill multiple form fields"""

    for field_name, value in form_data.items():
        try:
            # Try different selector patterns
            selectors = [
                f'input[name="{field_name}"]',
                f'#{field_name}',
                f'.{field_name}',
                f'input[placeholder*="{field_name}"]'
            ]

            element_found = False
            for selector in selectors:
                element = page.locator(selector)
                if element.is_visible():
                    element.fill(str(value))
                    print(f"✅ Filled {field_name}: {value}")
                    element_found = True
                    break

            if not element_found:
                print(f"❌ Field not found: {field_name}")

        except Exception as e:
            print(f"❌ Error filling {field_name}: {e}")

# Usage
form_data = {
    "username": "john_doe",
    "email": "john@example.com",
    "phone": "01712345678",
    "address": "Dhaka, Bangladesh"
}

fill_form_data(page, form_data)
```

### 📋 Form Interactions:

#### Dropdown/Select Operations:
```python
# Select by value
page.locator('select[name="country"]').select_option("BD")

# Select by label
page.locator('select').select_option(label="Bangladesh")

# Select by index
page.locator('select').select_option(index=2)

# Multiple selections
page.locator('select[multiple]').select_option(["option1", "option2"])

# Get selected value
selected = page.locator('select').input_value()
print(f"Selected: {selected}")
```

#### Checkbox and Radio Operations:
```python
# Check checkbox
page.locator('input[type="checkbox"]').check()

# Uncheck checkbox
page.locator('input[type="checkbox"]').uncheck()

# Set checkbox state
page.locator('input[type="checkbox"]').set_checked(True)

# Radio button selection
page.locator('input[value="male"]').check()

# Check if checked
is_checked = page.locator('input[type="checkbox"]').is_checked()
print(f"Checkbox is checked: {is_checked}")
```

#### File Upload:
```python
# Single file upload
page.locator('input[type="file"]').set_input_files("path/to/file.pdf")

# Multiple files upload
page.locator('input[type="file"]').set_input_files([
    "file1.jpg",
    "file2.png",
    "document.pdf"
])

# Remove files
page.locator('input[type="file"]').set_input_files([])
```

### 🖱️ Mouse Operations:

#### Hover and Mouse Events:
```python
# Hover over element
page.locator(".menu-item").hover()

# Hover with custom position
page.locator(".element").hover(position={"x": 50, "y": 50})

# Mouse down and up
page.locator(".draggable").mouse_down()
page.locator(".drop-zone").mouse_up()

# Drag and drop
page.locator(".source").drag_to(page.locator(".target"))
```

### ⏱️ Wait Strategies:

#### Element-based Waits:
```python
# Wait for element to be visible
page.locator(".loading").wait_for(state="visible")

# Wait for element to be hidden
page.locator(".popup").wait_for(state="hidden")

# Wait for element to be attached to DOM
page.locator(".dynamic-content").wait_for(state="attached")

# Wait for element to be detached from DOM
page.locator(".temporary-element").wait_for(state="detached")

# Wait with timeout
try:
    page.locator(".slow-element").wait_for(state="visible", timeout=5000)
except TimeoutError:
    print("Element did not appear within 5 seconds")
```

#### Custom Wait Conditions:
```python
def wait_for_element_count(page, selector, expected_count, timeout=10000):
    """Wait until element count matches expected"""

    def check_count():
        actual_count = page.locator(selector).count()
        return actual_count == expected_count

    page.wait_for_function(
        f"() => document.querySelectorAll('{selector}').length === {expected_count}",
        timeout=timeout
    )

# Wait for specific text to appear
def wait_for_text(page, selector, expected_text, timeout=10000):
    """Wait for element to contain specific text"""

    page.wait_for_function(
        f"""() => {{
            const element = document.querySelector('{selector}');
            return element && element.textContent.includes('{expected_text}');
        }}""",
        timeout=timeout
    )

# Usage
wait_for_element_count(page, ".product-card", 20)
wait_for_text(page, ".status", "Loading complete")
```

### 🎯 Complex Interaction Scenarios:

#### Login Automation:
```python
def automated_login(page, username, password):
    """Automated login with error handling"""

    try:
        # Navigate to login page
        page.goto("https://example.com/login")

        # Wait for login form
        page.wait_for_selector('form', timeout=10000)

        # Fill credentials
        page.locator('input[name="username"]').fill(username)
        page.locator('input[name="password"]').fill(password)

        # Submit form
        page.locator('button[type="submit"]').click()

        # Wait for navigation or error message
        try:
            # Success: wait for dashboard
            page.wait_for_url("**/dashboard", timeout=5000)
            print("✅ Login successful!")
            return True

        except:
            # Check for error message
            error_element = page.locator('.error-message')
            if error_element.is_visible():
                error_text = error_element.text_content()
                print(f"❌ Login failed: {error_text}")
            else:
                print("❌ Login failed: Unknown error")
            return False

    except Exception as e:
        print(f"❌ Login error: {e}")
        return False

# Usage
success = automated_login(page, "my_username", "my_password")
```

#### Search and Filter:
```python
def search_and_filter(page, search_term, filters=None):
    """Search with filters and return results"""

    # Perform search
    search_box = page.locator('input[type="search"]')
    search_box.fill(search_term)
    search_box.press("Enter")

    # Wait for results
    page.wait_for_selector('.search-results', timeout=10000)

    # Apply filters if provided
    if filters:
        for filter_type, filter_value in filters.items():
            filter_selector = f'select[name="{filter_type}"]'
            if page.locator(filter_selector).is_visible():
                page.locator(filter_selector).select_option(filter_value)
                page.wait_for_load_state('networkidle')

    # Extract results
    results = []
    result_elements = page.locator('.search-result').all()

    for element in result_elements:
        result_data = {
            'title': element.locator('.title').text_content(),
            'description': element.locator('.description').text_content(),
            'url': element.locator('a').get_attribute('href')
        }
        results.append(result_data)

    return results

# Usage
filters = {"category": "electronics", "price_range": "10000-50000"}
results = search_and_filter(page, "smartphone", filters)
print(f"Found {len(results)} results")
```
```

### 📚 Requests + BeautifulSoup (বেসিক):

#### সিম্পল স্ক্র্যাপিং:
```python
import requests
from bs4 import BeautifulSoup
import time

def scrape_basic_site():
    url = "https://quotes.toscrape.com/"
    
    # Headers যোগ করা (bot detection এড়ানোর জন্য)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # সব quotes সংগ্রহ
        quotes = soup.find_all('div', class_='quote')
        
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            
            print(f"Quote: {text}")
            print(f"Author: {author}")
            print(f"Tags: {', '.join(tags)}")
            print("-" * 50)
    
    else:
        print(f"Error: {response.status_code}")

# ফাংশন চালানো
scrape_basic_site()
```

#### Multiple Pages স্ক্র্যাপিং:
```python
def scrape_multiple_pages():
    base_url = "https://quotes.toscrape.com/page/{}"
    all_quotes = []
    
    for page in range(1, 6):  # ১-৫ পেজ
        url = base_url.format(page)
        print(f"Scraping page {page}...")
        
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        quotes = soup.find_all('div', class_='quote')
        
        if not quotes:  # আর কোন quote নেই
            break
            
        for quote in quotes:
            quote_data = {
                'text': quote.find('span', class_='text').text,
                'author': quote.find('small', class_='author').text,
                'tags': [tag.text for tag in quote.find_all('a', class_='tag')]
            }
            all_quotes.append(quote_data)
        
        # সাইটের উপর চাপ কমানোর জন্য delay
        time.sleep(1)
    
    return all_quotes

quotes = scrape_multiple_pages()
print(f"Total quotes collected: {len(quotes)}")
```

### 🔄 Session ব্যবহার (Login সহ):
```python
import requests
from bs4 import BeautifulSoup

def login_and_scrape():
    session = requests.Session()

    # Login page থেকে CSRF token নেওয়া
    login_url = "https://example.com/login"
    login_page = session.get(login_url)
    soup = BeautifulSoup(login_page.content, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

    # Login data
    login_data = {
        'username': 'your_username',
        'password': 'your_password',
        'csrf_token': csrf_token
    }

    # Login করা
    session.post(login_url, data=login_data)

    # Protected page access
    protected_url = "https://example.com/protected"
    response = session.get(protected_url)

    if "dashboard" in response.text.lower():
        print("Successfully logged in!")
        # এখন scraping করুন
    else:
        print("Login failed!")

login_and_scrape()
```

### 📊 Error Handling ও Retry Logic:
```python
import requests
from bs4 import BeautifulSoup
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def create_session_with_retries():
    session = requests.Session()

    # Retry strategy
    retry_strategy = Retry(
        total=3,                    # মোট ৩ বার চেষ্টা
        backoff_factor=1,           # প্রতিবার ১ সেকেন্ড বেশি অপেক্ষা
        status_forcelist=[429, 500, 502, 503, 504],  # এই status codes এ retry
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session

def robust_scraping():
    session = create_session_with_retries()

    urls = [
        "https://example1.com",
        "https://example2.com",
        "https://example3.com"
    ]

    for url in urls:
        try:
            response = session.get(url, timeout=10)
            response.raise_for_status()  # HTTP error থাকলে exception raise করবে

            soup = BeautifulSoup(response.content, 'html.parser')
            # Scraping logic here

        except requests.exceptions.RequestException as e:
            print(f"Error scraping {url}: {e}")
            continue

        time.sleep(2)  # Rate limiting

robust_scraping()
```

---

## 🎭 Playwright দিয়ে অ্যাডভান্স স্ক্র্যাপিং {#playwright-advanced}

### 🚀 Playwright কেন ব্যবহার করবেন?
- **JavaScript রেন্ডারিং:** Dynamic content load হয়
- **User Interaction:** Click, scroll, form fill করতে পারেন
- **Multiple Browsers:** Chrome, Firefox, Safari support
- **Mobile Emulation:** Mobile device simulate করতে পারেন

### 🎯 বেসিক Playwright Setup:
```python
from playwright.sync_api import sync_playwright
import time

def basic_playwright_scraping():
    with sync_playwright() as p:
        # Browser launch (headless=False মানে browser দেখা যাবে)
        browser = p.chromium.launch(
            headless=False,
            args=["--auto-open-devtools-for-tabs"]
        )

        # New page create
        page = browser.new_page()

        # URL এ যাওয়া
        page.goto("https://example.com")

        # Page load হওয়ার জন্য অপেক্ষা
        page.wait_for_load_state("networkidle")

        # Title print
        print(f"Page title: {page.title()}")

        # Element থেকে text নেওয়া
        heading = page.locator("h1").text_content()
        print(f"Main heading: {heading}")

        # Screenshot নেওয়া
        page.screenshot(path="screenshot.png")

        browser.close()

basic_playwright_scraping()
```

### 🖱️ User Interactions:
```python
def interactive_scraping():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://example.com/search")

        # Search box এ text type করা
        page.fill('input[name="search"]', 'Python programming')

        # Search button এ click
        page.click('button[type="submit"]')

        # Results load হওয়ার জন্য অপেক্ষা
        page.wait_for_selector('.search-results')

        # Results scrape করা
        results = page.locator('.search-result').all()

        for i, result in enumerate(results):
            title = result.locator('.title').text_content()
            link = result.locator('a').get_attribute('href')
            print(f"{i+1}. {title} - {link}")

        browser.close()

interactive_scraping()
```

### 📱 Mobile Device Emulation:
```python
def mobile_scraping():
    with sync_playwright() as p:
        # Mobile device emulate করা
        iphone = p.devices['iPhone 12']
        browser = p.chromium.launch()
        context = browser.new_context(**iphone)
        page = context.new_page()

        page.goto("https://example.com")

        # Mobile specific elements scrape করা
        mobile_menu = page.locator('.mobile-menu')
        if mobile_menu.is_visible():
            mobile_menu.click()

        browser.close()

mobile_scraping()
```

### 🔄 Infinite Scroll Handling:
```python
def scrape_infinite_scroll():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://example.com/infinite-scroll")

        # Initial items count
        previous_count = 0

        while True:
            # Current items count
            current_count = page.locator('.item').count()

            if current_count == previous_count:
                print("No more items to load")
                break

            print(f"Loaded {current_count} items")
            previous_count = current_count

            # Scroll to bottom
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

            # Wait for new content
            page.wait_for_timeout(2000)

        # Scrape all items
        items = page.locator('.item').all()
        for item in items:
            title = item.locator('.title').text_content()
            print(title)

        browser.close()

scrape_infinite_scroll()
```

### 🍪 Cookies ও Local Storage:
```python
def handle_cookies_storage():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Cookie set করা
        context.add_cookies([{
            'name': 'session_id',
            'value': 'abc123',
            'domain': 'example.com',
            'path': '/'
        }])

        page.goto("https://example.com")

        # Local storage এ data set করা
        page.evaluate("""
            localStorage.setItem('user_preference', 'dark_mode');
        """)

        # Cookie read করা
        cookies = context.cookies()
        for cookie in cookies:
            print(f"{cookie['name']}: {cookie['value']}")

        # Local storage read করা
        user_pref = page.evaluate("localStorage.getItem('user_preference')")
        print(f"User preference: {user_pref}")

        browser.close()

handle_cookies_storage()
```

### 🚫 Request Blocking (Ad Block):
```python
def block_ads_and_trackers():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Block করার domain list
        blocked_domains = [
            "doubleclick.net",
            "googlesyndication.com",
            "googletagmanager.com",
            "facebook.com/tr",
            "google-analytics.com"
        ]

        def handle_route(route, request):
            # Check if request URL contains blocked domains
            if any(domain in request.url for domain in blocked_domains):
                print(f"Blocked: {request.url}")
                route.abort()
            else:
                route.continue_()

        # All requests intercept করা
        page.route("**/*", handle_route)

        page.goto("https://example.com")

        # Page content scrape করা (ads ছাড়া)
        content = page.locator('.main-content').text_content()
        print(content)

        browser.close()

block_ads_and_trackers()
```

---

## 💾 ডেটা সংরক্ষণ ও প্রসেসিং {#data-processing}

### 📊 CSV ফাইলে সেভ করা:
```python
import csv
import pandas as pd

def save_to_csv(data, filename):
    """
    data: list of dictionaries
    filename: CSV file name
    """
    if not data:
        print("No data to save!")
        return

    # CSV writer ব্যবহার করে
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

    print(f"Data saved to {filename}")

# Example usage
scraped_data = [
    {'name': 'Product 1', 'price': '৫০০ টাকা', 'rating': '4.5'},
    {'name': 'Product 2', 'price': '৭০০ টাকা', 'rating': '4.2'},
]

save_to_csv(scraped_data, 'products.csv')
```

### 🐼 Pandas দিয়ে ডেটা প্রসেসিং:
```python
import pandas as pd
import numpy as np

def process_scraped_data():
    # CSV থেকে data load করা
    df = pd.read_csv('products.csv')

    # Data cleaning
    df['price_numeric'] = df['price'].str.extract('(\d+)').astype(int)
    df['rating_numeric'] = df['rating'].astype(float)

    # Data analysis
    print("=== Data Summary ===")
    print(f"Total products: {len(df)}")
    print(f"Average price: {df['price_numeric'].mean():.2f} টাকা")
    print(f"Average rating: {df['rating_numeric'].mean():.2f}")

    # Filter high-rated products
    high_rated = df[df['rating_numeric'] >= 4.0]
    print(f"High-rated products: {len(high_rated)}")

    # Save processed data
    df.to_csv('processed_products.csv', index=False)

    return df

processed_df = process_scraped_data()
```

### 🗄️ Database এ সেভ করা (SQLite):
```python
import sqlite3
import pandas as pd

def save_to_database(data, db_name='scraped_data.db'):
    # Database connection
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Table create করা
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price TEXT,
            rating REAL,
            scraped_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Data insert করা
    for item in data:
        cursor.execute('''
            INSERT INTO products (name, price, rating)
            VALUES (?, ?, ?)
        ''', (item['name'], item['price'], float(item['rating'])))

    conn.commit()
    conn.close()
    print(f"Data saved to database: {db_name}")

# Database থেকে data read করা
def read_from_database(db_name='scraped_data.db'):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query("SELECT * FROM products", conn)
    conn.close()
    return df

# Usage
scraped_data = [
    {'name': 'Product 1', 'price': '৫০০ টাকা', 'rating': '4.5'},
    {'name': 'Product 2', 'price': '৭০০ টাকা', 'rating': '4.2'},
]

save_to_database(scraped_data)
db_data = read_from_database()
print(db_data)
```

### 📈 ডেটা ভিজুয়ালাইজেশন:
```python
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(df):
    # Set Bengali font (if available)
    plt.rcParams['font.family'] = ['DejaVu Sans']

    # Price distribution
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.hist(df['price_numeric'], bins=20, alpha=0.7)
    plt.title('Price Distribution')
    plt.xlabel('Price (Taka)')
    plt.ylabel('Frequency')

    # Rating distribution
    plt.subplot(2, 2, 2)
    plt.hist(df['rating_numeric'], bins=10, alpha=0.7, color='orange')
    plt.title('Rating Distribution')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')

    # Price vs Rating scatter plot
    plt.subplot(2, 2, 3)
    plt.scatter(df['price_numeric'], df['rating_numeric'], alpha=0.6)
    plt.title('Price vs Rating')
    plt.xlabel('Price (Taka)')
    plt.ylabel('Rating')

    # Top 10 products by rating
    plt.subplot(2, 2, 4)
    top_products = df.nlargest(10, 'rating_numeric')
    plt.barh(range(len(top_products)), top_products['rating_numeric'])
    plt.title('Top 10 Products by Rating')
    plt.xlabel('Rating')

    plt.tight_layout()
    plt.savefig('data_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

# Usage
df = pd.read_csv('processed_products.csv')
visualize_data(df)
```

---

## 🔧 সমস্যা সমাধান ও টিপস {#troubleshooting}

### 🚫 সাধারণ সমস্যা ও সমাধান:

#### ১. **Bot Detection এড়ানো:**
```python
import random
import time
from fake_useragent import UserAgent

def avoid_bot_detection():
    ua = UserAgent()

    headers = {
        'User-Agent': ua.random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    # Random delay between requests
    delay = random.uniform(1, 3)
    time.sleep(delay)

    return headers

# Playwright এ User-Agent change করা
def playwright_avoid_detection():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        page = context.new_page()

        # Additional headers
        page.set_extra_http_headers({
            'Accept-Language': 'en-US,en;q=0.9',
        })

        page.goto("https://example.com")
        browser.close()
```

#### ২. **CAPTCHA সমাধান:**
```python
# Manual CAPTCHA solving
def handle_captcha_manually():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False রাখুন
        page = browser.new_page()

        page.goto("https://example.com")

        # CAPTCHA আছে কিনা check করা
        if page.locator('.captcha').is_visible():
            print("CAPTCHA detected! Please solve it manually...")

            # User এর CAPTCHA solve করার জন্য অপেক্ষা
            page.wait_for_selector('.captcha', state='hidden', timeout=60000)
            print("CAPTCHA solved! Continuing...")

        # Continue scraping
        browser.close()
```

#### ৩. **Rate Limiting Handle করা:**
```python
import time
from datetime import datetime, timedelta

class RateLimiter:
    def __init__(self, max_requests=10, time_window=60):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = []

    def wait_if_needed(self):
        now = datetime.now()

        # Remove old requests
        self.requests = [req_time for req_time in self.requests
                        if now - req_time < timedelta(seconds=self.time_window)]

        # Check if we need to wait
        if len(self.requests) >= self.max_requests:
            sleep_time = self.time_window - (now - self.requests[0]).seconds
            print(f"Rate limit reached. Waiting {sleep_time} seconds...")
            time.sleep(sleep_time)

        self.requests.append(now)

# Usage
rate_limiter = RateLimiter(max_requests=5, time_window=60)

def scrape_with_rate_limit(urls):
    for url in urls:
        rate_limiter.wait_if_needed()

        # Your scraping code here
        response = requests.get(url)
        print(f"Scraped: {url}")
```

#### ৪. **Dynamic Content Loading:**
```python
def wait_for_dynamic_content():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://example.com")

        # Method 1: Wait for specific element
        page.wait_for_selector('.dynamic-content', timeout=10000)

        # Method 2: Wait for network to be idle
        page.wait_for_load_state('networkidle')

        # Method 3: Wait for JavaScript to complete
        page.wait_for_function("document.readyState === 'complete'")

        # Method 4: Custom wait condition
        page.wait_for_function("""
            () => document.querySelectorAll('.item').length > 10
        """)

        browser.close()
```

### 💡 **Performance Optimization টিপস:**

#### ১. **Concurrent Scraping:**
```python
import asyncio
from playwright.async_api import async_playwright

async def scrape_page(url, semaphore):
    async with semaphore:  # Limit concurrent requests
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()

            await page.goto(url)
            title = await page.title()

            await browser.close()
            return {'url': url, 'title': title}

async def concurrent_scraping():
    urls = [
        "https://example1.com",
        "https://example2.com",
        "https://example3.com",
    ]

    # Maximum 3 concurrent requests
    semaphore = asyncio.Semaphore(3)

    tasks = [scrape_page(url, semaphore) for url in urls]
    results = await asyncio.gather(*tasks)

    return results

# Run async function
results = asyncio.run(concurrent_scraping())
print(results)
```

#### ২. **Memory Management:**
```python
def memory_efficient_scraping():
    with sync_playwright() as p:
        browser = p.chromium.launch()

        for i in range(100):  # Many pages
            page = browser.new_page()

            try:
                page.goto(f"https://example.com/page/{i}")
                # Scraping logic

            finally:
                page.close()  # Important: Close page to free memory

        browser.close()
```

---

## ⚖️ আইনি ও নৈতিক বিষয় {#legal-ethics}

### 📋 **স্ক্র্যাপিং এর নিয়মকানুন:**

#### ✅ **যা করতে পারেন:**
- **Public Data:** সবার জন্য উন্মুক্ত তথ্য সংগ্রহ
- **Personal Use:** নিজের গবেষণা বা শেখার জন্য
- **robots.txt মেনে চলা:** সাইটের নিয়ম অনুসরণ
- **Rate Limiting:** সাইটের উপর চাপ কম দেওয়া

#### ❌ **যা করবেন না:**
- **Copyright Content:** কপিরাইট সুরক্ষিত কন্টেন্ট চুরি
- **Personal Information:** ব্যক্তিগত তথ্য সংগ্রহ
- **Commercial Misuse:** অনুমতি ছাড়া ব্যবসায়িক ব্যবহার
- **Server Overload:** সাইট ক্র্যাশ করানো

### 🤖 **robots.txt চেক করা:**
```python
import requests
from urllib.robotparser import RobotFileParser

def check_robots_txt(url, user_agent='*'):
    """
    Check if scraping is allowed according to robots.txt
    """
    try:
        robots_url = f"{url.rstrip('/')}/robots.txt"

        rp = RobotFileParser()
        rp.set_url(robots_url)
        rp.read()

        # Check if URL can be fetched
        can_fetch = rp.can_fetch(user_agent, url)

        print(f"Can scrape {url}: {can_fetch}")

        # Get crawl delay
        crawl_delay = rp.crawl_delay(user_agent)
        if crawl_delay:
            print(f"Recommended delay: {crawl_delay} seconds")

        return can_fetch, crawl_delay

    except Exception as e:
        print(f"Error checking robots.txt: {e}")
        return True, None  # If can't check, assume allowed

# Usage
can_scrape, delay = check_robots_txt("https://example.com")
if can_scrape:
    print("Scraping is allowed!")
else:
    print("Scraping is not allowed by robots.txt")
```

### 📜 **Terms of Service চেক করা:**
```python
def ethical_scraping_guidelines():
    guidelines = """
    🔍 নৈতিক স্ক্র্যাপিং গাইডলাইন:

    1. 📖 Terms of Service পড়ুন
    2. 🤖 robots.txt মেনে চলুন
    3. ⏱️ Request এর মধ্যে delay রাখুন
    4. 🔒 Personal data সংগ্রহ করবেন না
    5. 💰 Commercial use এর আগে permission নিন
    6. 📊 Data এর source credit দিন
    7. 🔄 Reasonable frequency তে scrape করুন
    8. 🚫 Site এর functionality ক্ষতি করবেন না
    """
    print(guidelines)

ethical_scraping_guidelines()
```

---

## 🏗️ প্রজেক্ট স্ট্রাকচার ও বেস্ট প্র্যাকটিস

### 📁 **Recommended Project Structure:**
```
web_scraping_project/
│
├── src/
│   ├── __init__.py
│   ├── scrapers/
│   │   ├── __init__.py
│   │   ├── base_scraper.py
│   │   ├── ecommerce_scraper.py
│   │   └── news_scraper.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── helpers.py
│   │   └── data_processor.py
│   └── config/
│       ├── __init__.py
│       └── settings.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── exports/
│
├── tests/
│   ├── __init__.py
│   └── test_scrapers.py
│
├── logs/
├── requirements.txt
├── README.md
└── main.py
```

### 🔧 **Base Scraper Class:**
```python
# src/scrapers/base_scraper.py
import logging
import time
import random
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseScraper(ABC):
    def __init__(self, base_url: str, delay_range: tuple = (1, 3)):
        self.base_url = base_url
        self.delay_range = delay_range
        self.session = None
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('logs/scraper.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(self.__class__.__name__)

    def random_delay(self):
        """Random delay between requests"""
        delay = random.uniform(*self.delay_range)
        time.sleep(delay)

    @abstractmethod
    def scrape(self) -> List[Dict[str, Any]]:
        """Main scraping method - must be implemented by subclasses"""
        pass

    def save_data(self, data: List[Dict], filename: str):
        """Save scraped data to file"""
        import json
        with open(f'data/raw/{filename}', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        self.logger.info(f"Data saved to {filename}")

# Example implementation
class EcommerceScraper(BaseScraper):
    def scrape(self) -> List[Dict[str, Any]]:
        products = []

        # Your scraping logic here
        self.logger.info("Starting e-commerce scraping...")

        # Example data
        products.append({
            'name': 'Sample Product',
            'price': '৫০০ টাকা',
            'rating': 4.5
        })

        return products
```

### ⚙️ **Configuration Management:**
```python
# src/config/settings.py
import os
from dataclasses import dataclass
from typing import List

@dataclass
class ScrapingConfig:
    # Browser settings
    headless: bool = True
    browser_timeout: int = 30000

    # Request settings
    max_retries: int = 3
    delay_range: tuple = (1, 3)
    concurrent_requests: int = 5

    # Data settings
    output_format: str = 'json'  # json, csv, xlsx
    data_dir: str = 'data'

    # Logging
    log_level: str = 'INFO'
    log_file: str = 'logs/scraper.log'

    # User agents
    user_agents: List[str] = None

    def __post_init__(self):
        if self.user_agents is None:
            self.user_agents = [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
            ]

# Load config from environment
def load_config():
    return ScrapingConfig(
        headless=os.getenv('HEADLESS', 'true').lower() == 'true',
        max_retries=int(os.getenv('MAX_RETRIES', '3')),
        concurrent_requests=int(os.getenv('CONCURRENT_REQUESTS', '5'))
    )
```

### 🧪 **Testing:**
```python
# tests/test_scrapers.py
import unittest
from unittest.mock import Mock, patch
from src.scrapers.ecommerce_scraper import EcommerceScraper

class TestEcommerceScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = EcommerceScraper("https://example.com")

    def test_scraper_initialization(self):
        self.assertEqual(self.scraper.base_url, "https://example.com")
        self.assertIsNotNone(self.scraper.logger)

    @patch('requests.get')
    def test_scrape_method(self, mock_get):
        # Mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = "<html><body>Test</body></html>"
        mock_get.return_value = mock_response

        # Test scraping
        result = self.scraper.scrape()
        self.assertIsInstance(result, list)

    def test_random_delay(self):
        import time
        start_time = time.time()
        self.scraper.random_delay()
        end_time = time.time()

        # Check if delay was applied
        self.assertGreater(end_time - start_time, 0.5)

if __name__ == '__main__':
    unittest.main()
```

---

## 🌟 রিয়েল-ওয়ার্ল্ড প্রজেক্ট উদাহরণ

### 🛒 **E-commerce Price Monitor:**
```python
# main.py - E-commerce price monitoring system
import schedule
import time
from datetime import datetime
from src.scrapers.ecommerce_scraper import EcommerceScraper
from src.utils.data_processor import DataProcessor
from src.utils.helpers import send_notification

class PriceMonitor:
    def __init__(self):
        self.scraper = EcommerceScraper("https://example-shop.com")
        self.processor = DataProcessor()
        self.target_products = [
            {'name': 'iPhone 15', 'target_price': 80000},
            {'name': 'Samsung Galaxy S24', 'target_price': 70000}
        ]

    def monitor_prices(self):
        print(f"🔍 Price monitoring started at {datetime.now()}")

        # Scrape current prices
        current_data = self.scraper.scrape()

        # Process and compare with targets
        for product in current_data:
            for target in self.target_products:
                if target['name'].lower() in product['name'].lower():
                    current_price = self.extract_price(product['price'])

                    if current_price <= target['target_price']:
                        message = f"🎉 Price Alert! {product['name']} is now {current_price} টাকা"
                        send_notification(message)
                        print(message)

        # Save data with timestamp
        filename = f"price_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        self.scraper.save_data(current_data, filename)

    def extract_price(self, price_text):
        import re
        # Extract numeric price from text like "৫০,০০০ টাকা"
        numbers = re.findall(r'[\d,]+', price_text)
        if numbers:
            return int(numbers[0].replace(',', ''))
        return 0

    def start_monitoring(self):
        # Schedule monitoring every hour
        schedule.every().hour.do(self.monitor_prices)

        print("📊 Price monitoring system started!")
        print("Press Ctrl+C to stop...")

        try:
            while True:
                schedule.run_pending()
                time.sleep(60)
        except KeyboardInterrupt:
            print("\n🛑 Monitoring stopped!")

if __name__ == "__main__":
    monitor = PriceMonitor()
    monitor.start_monitoring()
```

### 📰 **News Aggregator:**
```python
# news_aggregator.py
from playwright.sync_api import sync_playwright
import json
from datetime import datetime

class NewsAggregator:
    def __init__(self):
        self.news_sources = [
            {
                'name': 'Prothom Alo',
                'url': 'https://www.prothomalo.com',
                'title_selector': '.story-card__title',
                'link_selector': '.story-card__title a'
            },
            {
                'name': 'The Daily Star',
                'url': 'https://www.thedailystar.net',
                'title_selector': '.title',
                'link_selector': '.title a'
            }
        ]

    def scrape_news_source(self, source):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            try:
                page.goto(source['url'])
                page.wait_for_load_state('networkidle')

                # Get all news titles and links
                titles = page.locator(source['title_selector']).all()
                links = page.locator(source['link_selector']).all()

                news_items = []
                for i, title in enumerate(titles[:10]):  # Top 10 news
                    try:
                        title_text = title.text_content().strip()
                        link_href = links[i].get_attribute('href') if i < len(links) else ''

                        # Make absolute URL
                        if link_href.startswith('/'):
                            link_href = source['url'] + link_href

                        news_items.append({
                            'title': title_text,
                            'link': link_href,
                            'source': source['name'],
                            'scraped_at': datetime.now().isoformat()
                        })
                    except Exception as e:
                        print(f"Error processing item {i}: {e}")
                        continue

                return news_items

            except Exception as e:
                print(f"Error scraping {source['name']}: {e}")
                return []

            finally:
                browser.close()

    def aggregate_all_news(self):
        all_news = []

        for source in self.news_sources:
            print(f"📰 Scraping {source['name']}...")
            news_items = self.scrape_news_source(source)
            all_news.extend(news_items)

            # Delay between sources
            import time
            time.sleep(2)

        # Save aggregated news
        filename = f"news_aggregated_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(f'data/raw/{filename}', 'w', encoding='utf-8') as f:
            json.dump(all_news, f, ensure_ascii=False, indent=2)

        print(f"✅ Total {len(all_news)} news items collected!")
        return all_news

# Usage
if __name__ == "__main__":
    aggregator = NewsAggregator()
    news = aggregator.aggregate_all_news()

    # Print top 5 news
    for i, item in enumerate(news[:5]):
        print(f"{i+1}. {item['title']} - {item['source']}")
```

### 🏢 **Job Listings Scraper:**
```python
# job_scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

class JobScraper:
    def __init__(self):
        self.base_url = "https://jobs.example.com"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def scrape_jobs(self, keyword="python developer", location="dhaka"):
        jobs = []
        page = 1

        while page <= 5:  # Scrape first 5 pages
            print(f"🔍 Scraping page {page}...")

            params = {
                'q': keyword,
                'l': location,
                'p': page
            }

            response = requests.get(f"{self.base_url}/search",
                                  params=params, headers=self.headers)

            if response.status_code != 200:
                print(f"Error: {response.status_code}")
                break

            soup = BeautifulSoup(response.content, 'html.parser')
            job_cards = soup.find_all('div', class_='job-card')

            if not job_cards:
                print("No more jobs found!")
                break

            for card in job_cards:
                try:
                    job_data = {
                        'title': card.find('h3', class_='job-title').text.strip(),
                        'company': card.find('span', class_='company-name').text.strip(),
                        'location': card.find('span', class_='job-location').text.strip(),
                        'salary': self.extract_salary(card),
                        'posted_date': card.find('span', class_='posted-date').text.strip(),
                        'job_url': self.base_url + card.find('a')['href'],
                        'scraped_at': datetime.now().isoformat()
                    }
                    jobs.append(job_data)

                except Exception as e:
                    print(f"Error parsing job card: {e}")
                    continue

            page += 1
            import time
            time.sleep(2)  # Be respectful

        return jobs

    def extract_salary(self, card):
        salary_elem = card.find('span', class_='salary')
        if salary_elem:
            return salary_elem.text.strip()
        return "Not specified"

    def save_to_excel(self, jobs, filename):
        df = pd.DataFrame(jobs)

        # Data cleaning
        df['salary_numeric'] = df['salary'].str.extract('(\d+)').astype(float)

        # Save to Excel with multiple sheets
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='All Jobs', index=False)

            # High salary jobs (if salary info available)
            high_salary = df[df['salary_numeric'] > 50000]
            if not high_salary.empty:
                high_salary.to_excel(writer, sheet_name='High Salary', index=False)

            # Jobs by company
            company_summary = df.groupby('company').size().reset_index(name='job_count')
            company_summary.to_excel(writer, sheet_name='Company Summary', index=False)

        print(f"📊 Data saved to {filename}")

# Usage
if __name__ == "__main__":
    scraper = JobScraper()

    # Scrape Python developer jobs in Dhaka
    jobs = scraper.scrape_jobs("python developer", "dhaka")

    if jobs:
        filename = f"jobs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        scraper.save_to_excel(jobs, filename)

        print(f"✅ Found {len(jobs)} jobs!")

        # Show top 5 jobs
        for i, job in enumerate(jobs[:5]):
            print(f"{i+1}. {job['title']} at {job['company']} - {job['location']}")
    else:
        print("❌ No jobs found!")
```

---

## 🎓 শেখার পথ ও পরবর্তী ধাপ

### 📚 **শিক্ষানবিস থেকে এক্সপার্ট হওয়ার রোডম্যাপ:**

#### 🥉 **Level 1: Beginner (১-২ মাস)**
- [ ] HTML/CSS বেসিক শিখুন
- [ ] Python বেসিক শিখুন
- [ ] requests + BeautifulSoup দিয়ে সিম্পল স্ক্র্যাপিং
- [ ] CSV ফাইলে ডেটা সেভ করা
- [ ] DevTools ব্যবহার করা

#### 🥈 **Level 2: Intermediate (২-৪ মাস)**
- [ ] Playwright/Selenium শিখুন
- [ ] JavaScript rendering handle করা
- [ ] Form submission ও login
- [ ] Database এ ডেটা সেভ করা
- [ ] Error handling ও retry logic
- [ ] Basic data analysis with Pandas

#### 🥇 **Level 3: Advanced (৪-৬ মাস)**
- [ ] Async/concurrent scraping
- [ ] API reverse engineering
- [ ] CAPTCHA solving
- [ ] Proxy rotation
- [ ] Distributed scraping
- [ ] Machine learning for data extraction

#### 🏆 **Level 4: Expert (৬+ মাস)**
- [ ] Custom browser automation
- [ ] Anti-detection techniques
- [ ] Large-scale data pipelines
- [ ] Real-time monitoring systems
- [ ] Cloud deployment (AWS/GCP)
- [ ] Contributing to open-source projects

### 🔗 **দরকারী রিসোর্স:**

#### 📖 **বই:**
- "Web Scraping with Python" by Ryan Mitchell
- "Automate the Boring Stuff with Python" by Al Sweigart

#### 🌐 **ওয়েবসাইট:**
- [Scrapy Documentation](https://scrapy.org/)
- [Playwright Documentation](https://playwright.dev/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/)

#### 🎥 **YouTube Channels:**
- Corey Schafer (Python tutorials)
- Tech With Tim (Web scraping tutorials)

#### 💬 **কমিউনিটি:**
- Reddit: r/webscraping
- Stack Overflow
- GitHub (open source projects)

---

## 🎯 সমাপনী

এই গাইডে আমরা ওয়েব স্ক্র্যাপিং এর A-Z সব কিছু কভার করেছি। মনে রাখবেন:

### ✅ **মূল বিষয়গুলো:**
1. **ধৈর্য রাখুন:** স্ক্র্যাপিং শেখা একটি প্রক্রিয়া
2. **নৈতিকতা মেনে চলুন:** robots.txt ও ToS respect করুন
3. **প্র্যাকটিস করুন:** ছোট প্রজেক্ট দিয়ে শুরু করুন
4. **আপডেট থাকুন:** ওয়েবসাইট পরিবর্তন হয়, কোডও আপডেট করুন

### 🚀 **পরবর্তী পদক্ষেপ:**
1. এই গাইডের উদাহরণগুলো চালিয়ে দেখুন
2. নিজের একটি প্রজেক্ট শুরু করুন
3. GitHub এ কোড শেয়ার করুন
4. কমিউনিটিতে যোগ দিন

### 💡 **মনে রাখুন:**
> "The best way to learn web scraping is by doing it!"

**Happy Scraping! 🕷️🇧🇩**

---

*এই ডকুমেন্টেশন নিয়মিত আপডেট করা হবে। নতুন টুলস ও টেকনিক যোগ করা হবে।*
```
```
```
```
