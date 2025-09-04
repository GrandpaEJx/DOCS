# Learn Playwright Python 
🐍
## 1️⃣ Browser / Page Initialization

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--auto-open-devtools-for-tabs"])
    page = browser.new_page()
```

* `headless=False` → browser দেখা যাবে
* `args=["--auto-open-devtools-for-tabs"]` → DevTools auto open
* `page` হলো main tab

---

## 2️⃣ Navigate / Load URL

```python
page.goto("https://example.com")  # URL load
page.wait_for_load_state("networkidle")  # wait until network idle
print(page.title())  # print page title
```

* `networkidle` → সব requests finish হওয়ার পর execution চলবে
* `domcontentloaded` → HTML load হলে চলবে, network সব finish হবে না

---

## 3️⃣ Element Selectors / Scraping

```python
# Single element
text = page.locator("h1").text_content()
print(text)

# CSS selector
text = page.locator("div.classname > span").text_content()

# nth element
text = page.locator("div.item").nth(0).text_content()
```

* `locator()` → Modern Playwright way, old `page.query_selector()` deprecated

---

## 4️⃣ Click / Input Fill / Type

```python
page.click('button#login')           # click button
page.fill('input#username', 'myuser')  # fill input
page.fill('input#password', 'mypassword')
page.click('button[type="submit"]')
page.type('input#search', 'keyword')   # type like human (can simulate delay)
```

---

## 5️⃣ Wait / Timeout

```python
page.wait_for_timeout(5000)  # wait 5 seconds
page.wait_for_selector('div.loaded')  # wait until element appears
```

---

## 6️⃣ Route / Network Interception (AdBlock / Modify Requests)

```python
block_list = ["doubleclick.net", "googlesyndication.com"]

def handle_route(route, request):
    if any(domain in request.url for domain in block_list):
        route.abort()
    else:
        route.continue_()

page.route("**/*", handle_route)  # intercept all requests
```

* `request.resource_type` ব্যবহার করে শুধু `image`, `script`, `media` block করতে পারো

---

## 7️⃣ Screenshots / PDF

```python
page.screenshot(path="screenshot.png")         # screenshot png
page.pdf(path="page.pdf", format="A4")         # save pdf
```

---

## 8️⃣ Evaluate JavaScript

```python
# Run JS in page context
result = page.evaluate("() => document.title")
print(result)

# Example: return innerText of element
text = page.evaluate('() => document.querySelector("h1").innerText')
```

---

## 9️⃣ Cookies / LocalStorage / Storage

```python
cookies = page.context.cookies()
page.context.add_cookies([{"name":"token","value":"abc123","domain":"example.com"}])
local_storage = page.evaluate('() => localStorage.getItem("key")')
```

---

## 🔟 Frames / Iframes

```python
frame = page.frame(name="frame1")
frame.locator("button.submit").click()
```

---

## 1️⃣1️⃣ Multiple Pages / Tabs

```python
new_page = browser.new_page()
new_page.goto("https://another.com")
```

* `page.context.new_page()` → same browser context, share cookies

---

## 1️⃣2️⃣ Close / Cleanup

```python
browser.close()  # close browser
# with sync_playwright() auto stops Playwright, no need p.stop()
```

---

### 💡 Quick Tips / Templates:

| Task          | Command                                                                     |
| ------------- | --------------------------------------------------------------------------- |
| Open URL      | `page.goto("https://example.com")`                                          |
| Click         | `page.click('button#id')`                                                   |
| Fill Input    | `page.fill('input#id', 'text')`                                             |
| Scrape Text   | `page.locator("h1").text_content()`                                         |
| Screenshot    | `page.screenshot(path="file.png")`                                          |
| Wait          | `page.wait_for_load_state("networkidle")` / `page.wait_for_selector("div")` |
| Route Block   | `page.route("**/*", handle_route)`                                          |
| JS Eval       | `page.evaluate("() => document.title")`                                     |
| New Tab       | `browser.new_page()`                                                        |
| Close Browser | `browser.close()`                                                           |
