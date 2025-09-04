# 🎭 Playwright কুইক রেফারেন্স - চিট শিট

## 🔧 সেটআপ কমান্ড

```bash
# Playwright install
pip install playwright

# Browser binaries install (গুরুত্বপূর্ণ!)
playwright install

# Specific browsers
playwright install chromium
playwright install firefox
playwright install webkit
```

## 🎯 CSS Selectors চিট শিট

| Selector | Example | বর্ণনা |
|----------|---------|---------|
| `tag` | `div` | সব div element |
| `.class` | `.product` | class="product" |
| `#id` | `#main` | id="main" |
| `[attr]` | `[href]` | href attribute আছে |
| `[attr=value]` | `[type="text"]` | type="text" |
| `parent child` | `div p` | div এর ভিতরের p |
| `parent > child` | `div > p` | div এর direct child p |
| `:first-child` | `li:first-child` | প্রথম li |
| `:nth-child(n)` | `li:nth-child(2)` | ২য় li |
| `:contains()` | `p:contains("text")` | "text" আছে এমন p |

## 🐍 BeautifulSoup Quick Commands

```python
from bs4 import BeautifulSoup
import requests

# Basic setup
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Finding elements
soup.find('tag')                    # প্রথম element
soup.find_all('tag')               # সব elements
soup.select('css-selector')        # CSS selector
soup.select_one('css-selector')    # প্রথম match

# Getting data
element.text                       # Text content
element.get_text()                # Clean text
element['attribute']              # Attribute value
element.get('attribute')          # Safe attribute get

# Navigation
element.parent                    # Parent element
element.children                  # Child elements
element.siblings                  # Sibling elements
```

## 🎭 Playwright Quick Commands

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Navigation
    page.goto(url)
    page.wait_for_load_state("networkidle")
    
    # Finding elements
    page.locator("selector")              # Modern way
    page.query_selector("selector")       # Single element
    page.query_selector_all("selector")   # All elements
    
    # Getting data
    page.locator("h1").text_content()     # Text
    page.locator("a").get_attribute("href") # Attribute
    page.title()                          # Page title
    
    # Interactions
    page.click("button")                  # Click
    page.fill("input", "text")           # Fill input
    page.type("input", "text")           # Type text
    page.select_option("select", "value") # Select option
    
    # Waiting
    page.wait_for_selector("selector")    # Wait for element
    page.wait_for_timeout(5000)          # Wait 5 seconds
    
    # Screenshots
    page.screenshot(path="screenshot.png")
    
    browser.close()
```

## 📊 Data Processing Quick Commands

```python
import pandas as pd
import json

# Save to CSV
df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)

# Save to JSON
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Save to Excel
df.to_excel('data.xlsx', index=False)

# Data cleaning
df['price'] = df['price'].str.extract('(\d+)').astype(int)
df.dropna()                           # Remove null values
df.drop_duplicates()                  # Remove duplicates
```

## 🛡️ Error Handling Template

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time

def create_session():
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def safe_scrape(url):
    session = create_session()
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
```

## 🤖 Bot Detection এড়ানোর টিপস

```python
import random
import time
from fake_useragent import UserAgent

# Random User Agent
ua = UserAgent()
headers = {'User-Agent': ua.random}

# Random delays
time.sleep(random.uniform(1, 3))

# Playwright এ
context = browser.new_context(
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
)

# Request blocking
def handle_route(route, request):
    if 'ads' in request.url:
        route.abort()
    else:
        route.continue_()

page.route("**/*", handle_route)
```

## 🔍 DevTools Shortcuts

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Open DevTools | `F12` or `Ctrl+Shift+I` | `Cmd+Option+I` |
| Element Inspector | `Ctrl+Shift+C` | `Cmd+Shift+C` |
| Console | `Ctrl+Shift+J` | `Cmd+Option+J` |
| Network Tab | `Ctrl+Shift+E` | `Cmd+Option+E` |
| Refresh | `F5` or `Ctrl+R` | `Cmd+R` |
| Hard Refresh | `Ctrl+F5` | `Cmd+Shift+R` |

## 📱 Common Patterns

### Login Form Handling:
```python
# Get CSRF token
csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

# Login data
login_data = {
    'username': 'user',
    'password': 'pass',
    'csrf_token': csrf_token
}

# Post login
session.post(login_url, data=login_data)
```

### Pagination Handling:
```python
page = 1
while True:
    url = f"https://example.com/page/{page}"
    response = requests.get(url)
    
    if "No results" in response.text:
        break
    
    # Process page
    page += 1
    time.sleep(1)
```

### Infinite Scroll:
```python
# Playwright
previous_count = 0
while True:
    current_count = page.locator('.item').count()
    if current_count == previous_count:
        break
    
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(2000)
    previous_count = current_count
```

## 🚨 Common Errors & Solutions

| Error | Solution |
|-------|----------|
| `ConnectionError` | Check internet, add retry logic |
| `TimeoutError` | Increase timeout, check site speed |
| `403 Forbidden` | Change User-Agent, check robots.txt |
| `404 Not Found` | Verify URL, check if page exists |
| `Element not found` | Wait for element, check selector |
| `StaleElementReference` | Re-find element after page change |

## 📋 Project Structure Template

```
project/
├── src/
│   ├── scrapers/
│   ├── utils/
│   └── config/
├── data/
│   ├── raw/
│   └── processed/
├── tests/
├── logs/
├── requirements.txt
└── main.py
```

## ⚖️ Legal Checklist

- [ ] Check robots.txt
- [ ] Read Terms of Service
- [ ] Use reasonable delays
- [ ] Don't overload servers
- [ ] Respect copyright
- [ ] Don't scrape personal data
- [ ] Give attribution when needed

---

**এই রেফারেন্স সবসময় হাতের কাছে রাখুন! 📚**
