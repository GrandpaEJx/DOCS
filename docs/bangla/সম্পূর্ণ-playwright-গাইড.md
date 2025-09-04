# 🎭 সম্পূর্ণ Playwright গাইড - A-Z বাংলা টিউটোরিয়াল

## 🌟 স্বাগতম!

এটি বিশ্বের সবচেয়ে comprehensive **Playwright Web Scraping** গাইড - সম্পূর্ণ বাংলায়! এই গাইড দিয়ে আপনি **beginner থেকে expert** level এ পৌঁছাতে পারবেন।

### 🎯 **এই গাইডে কি আছে:**
- ✅ **2000+ lines** detailed tutorial
- ✅ **100+ practical examples**
- ✅ **Real-world projects**
- ✅ **Advanced techniques**
- ✅ **Production-ready code**

---

## 📚 সূচিপত্র

1. [Playwright পরিচয়](#playwright-পরিচয়)
2. [Installation ও Setup](#installation-ও-setup)
3. [Browser ও Page Management](#browser-ও-page-management)
4. [Element Selection Techniques](#element-selection-techniques)
5. [Data Extraction Methods](#data-extraction-methods)
6. [User Interactions](#user-interactions)
7. [Wait Strategies](#wait-strategies)
8. [Screenshots ও PDF](#screenshots-ও-pdf)
9. [Mobile Emulation](#mobile-emulation)
10. [Network Handling](#network-handling)
11. [Authentication ও Sessions](#authentication-ও-sessions)
12. [Advanced Techniques](#advanced-techniques)

---

## 🎭 Playwright পরিচয় {#playwright-পরিচয়}

### 🤔 **Playwright কি?**

Playwright হলো Microsoft এর তৈরি একটি **modern web automation library** যা দিয়ে আপনি:

- 🌐 **যেকোনো website** automatically browse করতে পারেন
- 🖱️ **Human-like interactions** করতে পারেন (click, type, scroll)
- 📊 **Data extract** করতে পারেন
- 📸 **Screenshots ও PDF** generate করতে পারেন
- 🤖 **Complete automation** তৈরি করতে পারেন

### 🆚 **অন্যান্য Tools এর তুলনা:**

| বৈশিষ্ট্য | Playwright | Selenium | Requests+BS4 | Scrapy |
|-----------|------------|----------|--------------|--------|
| **গতি** | ⚡ খুব দ্রুত | 🐌 ধীর | ⚡ দ্রুত | ⚡ দ্রুত |
| **JavaScript Support** | ✅ সম্পূর্ণ | ✅ সম্পূর্ণ | ❌ নেই | ❌ নেই |
| **Multiple Browsers** | ✅ Chrome, Firefox, Safari | ✅ Chrome, Firefox | ❌ নেই | ❌ নেই |
| **Mobile Emulation** | ✅ Perfect | ⚠️ Limited | ❌ নেই | ❌ নেই |
| **Setup Difficulty** | 🟢 সহজ | 🟡 মধ্যম | 🟢 সহজ | 🟡 মধ্যম |
| **Learning Curve** | 🟢 সহজ | 🟡 মধ্যম | 🟢 সহজ | 🔴 কঠিন |

### 🎯 **কখন Playwright ব্যবহার করবেন:**

#### ✅ **Perfect for:**
- **JavaScript-heavy websites** (React, Vue, Angular)
- **SPA (Single Page Applications)**
- **Login required sites**
- **Dynamic content loading**
- **AJAX/API calls dependent sites**
- **Mobile responsive testing**
- **Screenshot/PDF generation**

#### ❌ **Not ideal for:**
- **Simple static websites** (Requests+BS4 better)
- **Large scale crawling** (Scrapy better)
- **API-only data** (Direct API calls better)

### 🌟 **Playwright এর সুবিধা:**

#### **🚀 Performance:**
- **Auto-wait** - elements ready হওয়ার জন্য automatically wait
- **Parallel execution** - multiple browsers simultaneously
- **Fast execution** - optimized for speed

#### **🛡️ Reliability:**
- **Auto-retry** - failed actions automatically retry
- **Stable selectors** - intelligent element detection
- **Network interception** - requests/responses handle

#### **🔧 Developer Experience:**
- **Great documentation** - comprehensive guides
- **Debugging tools** - built-in debugging features
- **Code generation** - automatic code generation
- **Multiple languages** - Python, JavaScript, Java, C#

---

## 🔧 Installation ও Setup {#installation-ও-setup}

### 📋 **System Requirements:**

#### **Operating System:**
- ✅ **Windows** 10/11
- ✅ **macOS** 10.14+
- ✅ **Linux** (Ubuntu 18.04+, CentOS 7+)

#### **Python Version:**
- ✅ **Python 3.7+** (recommended: 3.9+)
- ✅ **pip** latest version

#### **Hardware:**
- **RAM:** 4GB+ (recommended: 8GB+)
- **Storage:** 2GB+ free space
- **Internet:** Stable connection for browser downloads

### 🚀 **Step-by-Step Installation:**

#### **Step 1: Virtual Environment তৈরি**
```bash
# নতুন project folder তৈরি করুন
mkdir my-playwright-project
cd my-playwright-project

# Virtual environment তৈরি করুন
python -m venv playwright-env

# Environment activate করুন
# Windows:
playwright-env\Scripts\activate
# Linux/Mac:
source playwright-env/bin/activate

# Activation verify করুন
python --version
pip --version
```

#### **Step 2: Playwright Installation**
```bash
# Pip upgrade করুন
python -m pip install --upgrade pip

# Playwright install করুন
pip install playwright

# Version check করুন
playwright --version
```

#### **Step 3: Browser Installation**
```bash
# সব browsers install করুন (recommended)
playwright install

# অথবা specific browsers
playwright install chromium    # Chrome/Chromium
playwright install firefox     # Firefox
playwright install webkit      # Safari

# Browser installation verify করুন
playwright install --dry-run
```

#### **Step 4: Additional Dependencies**
```bash
# Data processing এর জন্য
pip install pandas numpy

# Image processing এর জন্য
pip install Pillow

# HTTP requests এর জন্য
pip install requests

# Progress bars এর জন্য
pip install tqdm

# Colored output এর জন্য
pip install colorama
```

### ✅ **Installation Verification:**

#### **Basic Test:**
```python
# test_playwright.py
from playwright.sync_api import sync_playwright

def test_installation():
    print("🧪 Testing Playwright installation...")
    
    try:
        with sync_playwright() as p:
            # Browser launch test
            browser = p.chromium.launch(headless=True)
            print("✅ Browser launched successfully")
            
            # Page creation test
            page = browser.new_page()
            print("✅ Page created successfully")
            
            # Navigation test
            page.goto("https://google.com")
            print("✅ Navigation successful")
            
            # Title extraction test
            title = page.title()
            print(f"✅ Page title: {title}")
            
            # Cleanup
            browser.close()
            print("✅ Browser closed successfully")
            
            print("\n🎉 Playwright installation successful!")
            
    except Exception as e:
        print(f"❌ Installation test failed: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Check internet connection")
        print("2. Run: playwright install")
        print("3. Check virtual environment activation")

if __name__ == "__main__":
    test_installation()
```

```bash
python test_playwright.py
```

#### **Advanced Test:**
```python
# advanced_test.py
from playwright.sync_api import sync_playwright
import time

def advanced_test():
    print("🔬 Advanced Playwright testing...")
    
    with sync_playwright() as p:
        # Test all browsers
        browsers = [
            ("Chromium", p.chromium),
            ("Firefox", p.firefox),
            ("WebKit", p.webkit)
        ]
        
        for browser_name, browser_type in browsers:
            try:
                print(f"\n🌐 Testing {browser_name}...")
                
                browser = browser_type.launch(headless=True)
                page = browser.new_page()
                
                # Test navigation
                page.goto("https://httpbin.org/json")
                
                # Test JavaScript execution
                result = page.evaluate("() => ({ userAgent: navigator.userAgent })")
                print(f"✅ {browser_name}: JavaScript execution successful")
                
                # Test element interaction
                page.goto("https://httpbin.org/forms/post")
                page.fill("input[name='custname']", "Test User")
                print(f"✅ {browser_name}: Form interaction successful")
                
                browser.close()
                print(f"✅ {browser_name}: All tests passed")
                
            except Exception as e:
                print(f"❌ {browser_name}: Test failed - {e}")
        
        print("\n🎉 Advanced testing completed!")

if __name__ == "__main__":
    advanced_test()
```

### 🛠️ **IDE Setup (Optional):**

#### **VS Code Extensions:**
```json
// .vscode/extensions.json
{
    "recommendations": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-playwright.playwright"
    ]
}
```

#### **VS Code Settings:**
```json
// .vscode/settings.json
{
    "python.defaultInterpreterPath": "./playwright-env/bin/python",
    "python.terminal.activateEnvironment": true,
    "playwright.reuseBrowser": true,
    "playwright.showTrace": true
}
```

---

## 🌐 Browser ও Page Management {#browser-ও-page-management}

### 🚀 **Browser Launch Options:**

#### **Basic Browser Launch:**
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Different browsers
    chromium_browser = p.chromium.launch()
    firefox_browser = p.firefox.launch()
    webkit_browser = p.webkit.launch()
    
    # Basic page operations
    page = chromium_browser.new_page()
    page.goto("https://example.com")
    
    chromium_browser.close()
```

#### **Advanced Browser Configuration:**
```python
def launch_configured_browser():
    """Advanced browser configuration"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            # Visibility settings
            headless=False,              # Show browser window
            slow_mo=100,                # Slow down actions (debugging)
            
            # Browser arguments
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-web-security',
                '--allow-running-insecure-content',
                '--disable-features=TranslateUI',
                '--disable-ipc-flooding-protection'
            ],
            
            # Download settings
            downloads_path="./downloads",
            
            # Proxy settings (if needed)
            # proxy={
            #     "server": "http://proxy-server:8080",
            #     "username": "username",
            #     "password": "password"
            # }
        )
        
        return browser

# Usage
browser = launch_configured_browser()
page = browser.new_page()
page.goto("https://example.com")
browser.close()
```

### 📄 **Page Context Management:**

#### **Browser Context:**
```python
def context_management_example():
    """Browser context management"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        
        # Create context with specific settings
        context = browser.new_context(
            # Viewport settings
            viewport={'width': 1366, 'height': 768},
            
            # User agent
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            
            # Locale and timezone
            locale='bn-BD',
            timezone_id='Asia/Dhaka',
            
            # Permissions
            permissions=['geolocation', 'notifications'],
            
            # Extra HTTP headers
            extra_http_headers={
                'Accept-Language': 'bn-BD,bn;q=0.9,en;q=0.8'
            },
            
            # Ignore HTTPS errors
            ignore_https_errors=True
        )
        
        # Create multiple pages in same context
        page1 = context.new_page()
        page2 = context.new_page()
        
        # Pages share cookies and storage
        page1.goto("https://example.com/login")
        # ... login process
        
        page2.goto("https://example.com/dashboard")
        # page2 will have login session from page1
        
        context.close()
        browser.close()

context_management_example()
```

#### **Multiple Contexts:**
```python
def multiple_contexts_example():
    """Multiple isolated contexts"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        
        # Context 1: Regular user
        context1 = browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        
        # Context 2: Mobile user
        context2 = browser.new_context(
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)',
            viewport={'width': 375, 'height': 667},
            is_mobile=True,
            has_touch=True
        )
        
        # Each context is completely isolated
        page1 = context1.new_page()
        page2 = context2.new_page()
        
        page1.goto("https://example.com")  # Desktop version
        page2.goto("https://example.com")  # Mobile version
        
        print(f"Desktop title: {page1.title()}")
        print(f"Mobile title: {page2.title()}")
        
        context1.close()
        context2.close()
        browser.close()

multiple_contexts_example()
```

### 🔄 **Page Navigation:**

#### **Basic Navigation:**
```python
def navigation_examples():
    """Page navigation examples"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Basic navigation
        page.goto("https://example.com")
        print(f"Current URL: {page.url}")
        print(f"Page title: {page.title()}")
        
        # Navigation with options
        page.goto(
            "https://httpbin.org/delay/3",
            wait_until="networkidle",  # Wait for network to be idle
            timeout=30000             # 30 second timeout
        )
        
        # Navigation history
        page.goto("https://google.com")
        page.goto("https://github.com")
        
        page.go_back()    # Back to Google
        page.go_forward() # Forward to GitHub
        
        # Reload page
        page.reload()
        page.reload(wait_until="domcontentloaded")
        
        browser.close()

navigation_examples()
```

#### **Advanced Navigation:**
```python
def advanced_navigation():
    """Advanced navigation techniques"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Wait for specific events during navigation
        with page.expect_navigation():
            page.click("a[href='/next-page']")
        
        # Handle navigation with popup
        with page.expect_popup() as popup_info:
            page.click("a[target='_blank']")
        
        popup = popup_info.value
        print(f"Popup title: {popup.title()}")
        popup.close()
        
        # Handle navigation with download
        with page.expect_download() as download_info:
            page.click("a[download]")
        
        download = download_info.value
        download.save_as("./downloads/" + download.suggested_filename)
        
        browser.close()

advanced_navigation()
```

---

## 🎯 Element Selection Techniques {#element-selection-techniques}

### 🔍 **Locator Strategies:**

#### **CSS Selectors:**
```python
def css_selector_examples():
    """CSS selector techniques"""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")

        # Basic CSS selectors
        quotes = page.locator(".quote")                    # Class selector
        title = page.locator("#main-title")               # ID selector
        paragraphs = page.locator("p")                     # Tag selector

        # Attribute selectors
        links = page.locator("a[href]")                    # Has attribute
        external_links = page.locator("a[href^='http']")  # Starts with
        pdf_links = page.locator("a[href$='.pdf']")       # Ends with
        specific_link = page.locator("a[href*='github']") # Contains

        # Pseudo selectors
        first_quote = page.locator(".quote:first-child")
        last_quote = page.locator(".quote:last-child")
        even_quotes = page.locator(".quote:nth-child(even)")

        # Combination selectors
        quote_texts = page.locator(".quote .text")         # Descendant
        direct_children = page.locator(".quote > .text")   # Direct child
        next_sibling = page.locator("h1 + p")              # Adjacent sibling

        print(f"Total quotes: {quotes.count()}")
        print(f"External links: {external_links.count()}")

        browser.close()

css_selector_examples()
```

#### **Text-based Selection:**
```python
def text_based_selection():
    """Text-based element selection"""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")

        # Exact text match
        login_link = page.locator("text=Login")

        # Partial text match
        about_link = page.locator("text=About")

        # Case insensitive text match
        case_insensitive = page.locator("text=login >> i")

        # Text with regex
        regex_text = page.locator("text=/Log(in|out)/")

        # Text within specific element
        quote_with_text = page.locator(".quote:has-text('life')")

        # Multiple text conditions
        complex_text = page.locator("div:has-text('Albert Einstein'):has-text('imagination')")

        print(f"Login link exists: {login_link.count() > 0}")
        print(f"Quotes about life: {quote_with_text.count()}")

        browser.close()

text_based_selection()
```

#### **XPath Selectors:**
```python
def xpath_examples():
    """XPath selector examples"""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")

        # Basic XPath
        quotes = page.locator("xpath=//div[@class='quote']")

        # XPath with text
        login_link = page.locator("xpath=//a[text()='Login']")

        # XPath with contains
        quotes_with_life = page.locator("xpath=//div[contains(@class,'quote') and contains(.,'life')]")

        # XPath with position
        first_quote = page.locator("xpath=(//div[@class='quote'])[1]")
        last_quote = page.locator("xpath=(//div[@class='quote'])[last()]")

        # XPath with following/preceding
        next_element = page.locator("xpath=//h1/following-sibling::div[1]")

        # Complex XPath
        complex_xpath = page.locator("xpath=//div[@class='quote'][.//small[@class='author'][text()='Albert Einstein']]")

        print(f"XPath quotes count: {quotes.count()}")
        print(f"Einstein quotes: {complex_xpath.count()}")

        browser.close()

xpath_examples()
```

### 🎯 **Advanced Selection Techniques:**

#### **Chaining Locators:**
```python
def chaining_locators():
    """Chaining multiple locators"""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")

        # Chain locators for precise selection
        quote_container = page.locator(".quote")
        quote_text = quote_container.locator(".text")
        quote_author = quote_container.locator(".author")
        quote_tags = quote_container.locator(".tags .tag")

        # Get specific quote's information
        first_quote = page.locator(".quote").first
        first_text = first_quote.locator(".text").text_content()
        first_author = first_quote.locator(".author").text_content()
        first_tags = first_quote.locator(".tags .tag").all_text_contents()

        print(f"First quote: {first_text}")
        print(f"Author: {first_author}")
        print(f"Tags: {', '.join(first_tags)}")

        # Filter locators
        einstein_quotes = page.locator(".quote").filter(has_text="Einstein")
        print(f"Einstein quotes: {einstein_quotes.count()}")

        browser.close()

chaining_locators()
```

#### **Dynamic Element Selection:**
```python
def dynamic_selection():
    """Dynamic element selection techniques"""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")

        # Select elements based on content
        def find_quote_by_author(author_name):
            return page.locator(f".quote:has(.author:text('{author_name}'))")

        def find_quote_by_tag(tag_name):
            return page.locator(f".quote:has(.tag:text('{tag_name}'))")

        # Usage
        einstein_quotes = find_quote_by_author("Albert Einstein")
        love_quotes = find_quote_by_tag("love")

        print(f"Einstein quotes: {einstein_quotes.count()}")
        print(f"Love quotes: {love_quotes.count()}")

        # Dynamic attribute selection
        def find_elements_by_attribute(tag, attribute, value):
            return page.locator(f"{tag}[{attribute}='{value}']")

        # Select all links to specific domain
        github_links = find_elements_by_attribute("a", "href", "*github*")

        browser.close()

dynamic_selection()
```
