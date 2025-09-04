# 🎭 Playwright - সম্পূর্ণ বাংলা গাইড

## 🌟 Playwright কি?

Playwright হলো Microsoft এর তৈরি একটি **modern web automation library** যা দিয়ে আপনি যেকোনো website এ human-like interactions করতে পারেন।

### 🎯 **মূল বৈশিষ্ট্য:**
- ✅ **Multi-browser support** - Chrome, Firefox, Safari
- ✅ **Mobile emulation** - iOS, Android devices
- ✅ **JavaScript execution** - Dynamic content handling
- ✅ **Network interception** - API calls monitoring
- ✅ **Auto-wait** - Elements ready হওয়ার জন্য automatic wait
- ✅ **Screenshot/PDF** - Visual content generation

---

## 🚀 Installation ও Setup

### 📦 **Basic Installation:**
```bash
# Playwright install
pip install playwright>=1.40.0

# Browsers download (গুরুত্বপূর্ণ!)
playwright install

# Specific browser
playwright install chromium
playwright install firefox
playwright install webkit
```

### ✅ **Installation Verify:**
```python
# test_playwright.py
from playwright.sync_api import sync_playwright

def test_installation():
    print("🧪 Playwright installation test...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://google.com")
        
        title = page.title()
        print(f"✅ Page title: {title}")
        
        browser.close()
        print("🎉 Playwright working perfectly!")

test_installation()
```

---

## 🌐 Browser Management

### 🚀 **Browser Launch Options:**
```python
from playwright.sync_api import sync_playwright

def browser_examples():
    """বিভিন্ন browser launch options"""
    
    with sync_playwright() as p:
        # Basic launch
        browser = p.chromium.launch()
        
        # Visible browser (debugging এর জন্য)
        browser = p.chromium.launch(headless=False)
        
        # Slow motion (actions দেখার জন্য)
        browser = p.chromium.launch(
            headless=False,
            slow_mo=1000  # 1 second delay
        )
        
        # Advanced configuration
        browser = p.chromium.launch(
            headless=False,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--no-sandbox'
            ],
            downloads_path="./downloads"
        )
        
        # Different browsers
        chromium = p.chromium.launch()  # Chrome/Chromium
        firefox = p.firefox.launch()    # Firefox
        webkit = p.webkit.launch()      # Safari
        
        browser.close()

browser_examples()
```

### 📄 **Page Management:**
```python
def page_management():
    """Page creation ও management"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        # Basic page
        page = browser.new_page()
        
        # Page with custom settings
        context = browser.new_context(
            viewport={'width': 1366, 'height': 768},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            locale='bn-BD',
            timezone_id='Asia/Dhaka'
        )
        
        page = context.new_page()
        
        # Multiple pages
        page1 = browser.new_page()
        page2 = browser.new_page()
        
        # Page navigation
        page.goto("https://example.com")
        page.goto("https://google.com", wait_until="networkidle")
        
        # Page info
        print(f"Title: {page.title()}")
        print(f"URL: {page.url}")
        
        # Navigation history
        page.go_back()
        page.go_forward()
        page.reload()
        
        browser.close()

page_management()
```

---

## 🎯 Element Selection

### 🔍 **CSS Selectors:**
```python
def css_selectors():
    """CSS selector techniques"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")
        
        # Basic selectors
        quotes = page.locator(".quote")           # Class
        title = page.locator("#main")             # ID
        links = page.locator("a")                 # Tag
        
        # Attribute selectors
        external_links = page.locator("a[href^='http']")  # Starts with
        pdf_links = page.locator("a[href$='.pdf']")       # Ends with
        github_links = page.locator("a[href*='github']")  # Contains
        
        # Pseudo selectors
        first_quote = page.locator(".quote:first-child")
        last_quote = page.locator(".quote:last-child")
        even_quotes = page.locator(".quote:nth-child(even)")
        
        # Combination selectors
        quote_texts = page.locator(".quote .text")      # Descendant
        direct_child = page.locator(".quote > .text")   # Direct child
        
        print(f"Total quotes: {quotes.count()}")
        
        browser.close()

css_selectors()
```

### 📝 **Text-based Selection:**
```python
def text_selection():
    """Text দিয়ে element selection"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")
        
        # Exact text match
        login_link = page.locator("text=Login")
        
        # Partial text match
        about_link = page.locator("text=About")
        
        # Case insensitive
        case_insensitive = page.locator("text=login >> i")
        
        # Text with regex
        regex_text = page.locator("text=/Log(in|out)/")
        
        # Element with specific text
        einstein_quotes = page.locator(".quote:has-text('Einstein')")
        
        print(f"Einstein quotes: {einstein_quotes.count()}")
        
        browser.close()

text_selection()
```

### 🎯 **XPath Selectors:**
```python
def xpath_selectors():
    """XPath selector examples"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")
        
        # Basic XPath
        quotes = page.locator("xpath=//div[@class='quote']")
        
        # XPath with text
        login = page.locator("xpath=//a[text()='Login']")
        
        # XPath with contains
        life_quotes = page.locator("xpath=//div[contains(.,'life')]")
        
        # XPath with position
        first_quote = page.locator("xpath=(//div[@class='quote'])[1]")
        last_quote = page.locator("xpath=(//div[@class='quote'])[last()]")
        
        # Complex XPath
        einstein = page.locator("xpath=//div[@class='quote'][.//small[text()='Albert Einstein']]")
        
        print(f"XPath quotes: {quotes.count()}")
        
        browser.close()

xpath_selectors()
```

---

## 📊 Data Extraction

### 📖 **Text Content:**
```python
def text_extraction():
    """Text content extraction"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")
        
        # Single element text
        first_quote = page.locator(".quote .text").first.text_content()
        print(f"First quote: {first_quote}")
        
        # Multiple elements text
        all_authors = page.locator(".quote .author").all_text_contents()
        print(f"Authors: {all_authors}")
        
        # Inner text (visible only)
        visible_text = page.locator(".quote").first.inner_text()
        
        # Text with processing
        quotes = page.locator(".quote").all()
        
        for i, quote in enumerate(quotes, 1):
            text = quote.locator(".text").text_content().strip().strip('"')
            author = quote.locator(".author").text_content().strip()
            tags = quote.locator(".tags .tag").all_text_contents()
            
            print(f"\nQuote {i}:")
            print(f"  Text: {text}")
            print(f"  Author: {author}")
            print(f"  Tags: {', '.join(tags)}")
        
        browser.close()

text_extraction()
```

### 🔗 **Attributes ও Links:**
```python
def attribute_extraction():
    """Attribute ও link extraction"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")
        
        # Link attributes
        links = page.locator("a[href]").all()
        
        for link in links:
            href = link.get_attribute('href')
            text = link.text_content().strip()
            title = link.get_attribute('title')
            
            if text:  # Only links with text
                print(f"Link: {text} -> {href}")
        
        # Image attributes (if any)
        images = page.locator("img").all()
        for img in images:
            src = img.get_attribute('src')
            alt = img.get_attribute('alt')
            print(f"Image: {alt} -> {src}")
        
        # Form elements
        inputs = page.locator("input").all()
        for input_elem in inputs:
            name = input_elem.get_attribute('name')
            type_attr = input_elem.get_attribute('type')
            placeholder = input_elem.get_attribute('placeholder')
            
            print(f"Input: {name} ({type_attr}) - {placeholder}")
        
        browser.close()

attribute_extraction()
```

### 🏷️ **HTML Content:**
```python
def html_extraction():
    """HTML content extraction"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")
        
        # Inner HTML
        first_quote_html = page.locator(".quote").first.inner_html()
        print("Inner HTML:")
        print(first_quote_html)
        
        # Outer HTML
        full_html = page.locator(".quote").first.outer_html()
        print("\nOuter HTML:")
        print(full_html)
        
        # JavaScript evaluation
        quote_info = page.locator(".quote").first.evaluate("""
            element => {
                return {
                    tagName: element.tagName,
                    className: element.className,
                    childCount: element.childElementCount,
                    textLength: element.textContent.length
                };
            }
        """)
        
        print(f"\nQuote info: {quote_info}")
        
        browser.close()

html_extraction()
```

---

## 🖱️ User Interactions

### 👆 **Click Actions:**
```python
def click_actions():
    """বিভিন্ন click operations"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")
        
        # Simple click
        login_link = page.locator("a[href='/login']")
        if login_link.count() > 0:
            login_link.click()
            page.wait_for_load_state("networkidle")
        
        # Click with options
        page.goto("https://quotes.toscrape.com")
        
        # Right click
        page.locator(".quote").first.click(button="right")
        
        # Double click
        page.locator(".quote").first.click(click_count=2)
        
        # Click with modifier keys
        page.locator("a").first.click(modifiers=["Control"])
        
        # Force click (even if not visible)
        page.locator("button").click(force=True)
        
        # Click at specific position
        page.locator(".quote").first.click(position={"x": 10, "y": 10})
        
        browser.close()

click_actions()
```

### ⌨️ **Typing ও Form Filling:**
```python
def typing_forms():
    """Typing ও form handling"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://httpbin.org/forms/post")
        
        # Text input
        page.locator("input[name='custname']").fill("John Doe")
        
        # Type with delay
        page.locator("input[name='custtel']").type("01712345678", delay=100)
        
        # Clear and type
        page.locator("input[name='custemail']").clear()
        page.locator("input[name='custemail']").fill("john@example.com")
        
        # Textarea
        page.locator("textarea[name='comments']").fill("This is a test comment")
        
        # Dropdown selection
        page.locator("select[name='size']").select_option("large")
        
        # Radio button
        page.locator("input[value='bacon']").check()
        
        # Checkbox
        page.locator("input[name='topping'][value='cheese']").check()
        
        # Press keys
        page.locator("input[name='custname']").press("Control+A")
        page.locator("input[name='custname']").press("Delete")
        
        # Submit form
        page.locator("input[type='submit']").click()
        
        browser.close()

typing_forms()
```
