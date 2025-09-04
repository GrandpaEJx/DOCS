# 🍲 BeautifulSoup - সম্পূর্ণ বাংলা গাইড

## 🌟 BeautifulSoup কি?

BeautifulSoup হলো Python এর একটি **HTML/XML parsing library** যা দিয়ে আপনি সহজেই web pages থেকে data extract করতে পারেন।

### 🎯 **মূল বৈশিষ্ট্য:**
- ✅ **HTML/XML parsing** - সব ধরনের markup handle
- ✅ **CSS selectors** - modern selector support
- ✅ **Tree navigation** - parent, child, sibling access
- ✅ **Search methods** - flexible element finding
- ✅ **Encoding detection** - automatic character encoding
- ✅ **Malformed HTML** - broken HTML handle করে

---

## 🚀 Installation ও Setup

### 📦 **Installation:**
```bash
# BeautifulSoup install
pip install beautifulsoup4>=4.12.0

# Parser dependencies
pip install lxml>=4.9.0        # Fast XML/HTML parser
pip install html5lib>=1.1      # Pure Python parser
```

### ✅ **Installation Verify:**
```python
# test_beautifulsoup.py
from bs4 import BeautifulSoup
import requests

def test_beautifulsoup():
    print("🧪 BeautifulSoup installation test...")
    
    # Simple HTML parsing
    html = "<html><body><h1>Hello World!</h1></body></html>"
    soup = BeautifulSoup(html, 'html.parser')
    
    title = soup.find('h1').text
    print(f"✅ Parsed title: {title}")
    
    # Web scraping test
    try:
        response = requests.get('https://quotes.toscrape.com')
        soup = BeautifulSoup(response.content, 'html.parser')
        
        quotes = soup.find_all('div', class_='quote')
        print(f"✅ Found {len(quotes)} quotes")
        print("🎉 BeautifulSoup working perfectly!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

test_beautifulsoup()
```

---

## 🏗️ Basic Parsing

### 📄 **HTML Parsing:**
```python
from bs4 import BeautifulSoup
import requests

def basic_parsing():
    """Basic HTML parsing examples"""
    
    # Simple HTML string
    html_content = """
    <html>
    <head>
        <title>Test Page</title>
    </head>
    <body>
        <h1 id="main-title">Welcome to BeautifulSoup</h1>
        <div class="content">
            <p class="intro">This is an introduction paragraph.</p>
            <p class="description">This is a description paragraph.</p>
            <ul class="list">
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
        <a href="https://example.com" target="_blank">External Link</a>
    </body>
    </html>
    """
    
    # Create BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Basic information
    print(f"Title: {soup.title.text}")
    print(f"Title tag: {soup.title}")
    print(f"Title parent: {soup.title.parent.name}")
    
    # Find elements
    h1 = soup.find('h1')
    print(f"H1 text: {h1.text}")
    print(f"H1 id: {h1.get('id')}")
    
    # Find by class
    intro = soup.find('p', class_='intro')
    print(f"Intro: {intro.text}")
    
    # Find all elements
    paragraphs = soup.find_all('p')
    print(f"Total paragraphs: {len(paragraphs)}")
    
    for i, p in enumerate(paragraphs, 1):
        print(f"  Paragraph {i}: {p.text}")

basic_parsing()
```

### 🌐 **Web Page Parsing:**
```python
def web_parsing():
    """Real web page parsing"""
    
    # Get web page
    url = 'https://quotes.toscrape.com'
    response = requests.get(url)
    
    # Parse with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Page information
    print(f"Page title: {soup.title.text}")
    print(f"Page encoding: {response.encoding}")
    
    # Find quotes
    quotes = soup.find_all('div', class_='quote')
    print(f"Total quotes found: {len(quotes)}")
    
    # Extract quote information
    for i, quote in enumerate(quotes[:3], 1):  # First 3 quotes
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]
        
        print(f"\nQuote {i}:")
        print(f"  Text: {text}")
        print(f"  Author: {author}")
        print(f"  Tags: {', '.join(tags)}")

web_parsing()
```

---

## 🔍 Element Finding Methods

### 🎯 **find() ও find_all():**
```python
def finding_methods():
    """Element finding methods"""
    
    # Get sample page
    response = requests.get('https://quotes.toscrape.com')
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # find() - returns first match
    first_quote = soup.find('div', class_='quote')
    print(f"First quote author: {first_quote.find('small').text}")
    
    # find_all() - returns all matches
    all_quotes = soup.find_all('div', class_='quote')
    print(f"Total quotes: {len(all_quotes)}")
    
    # Find by tag
    all_links = soup.find_all('a')
    print(f"Total links: {len(all_links)}")
    
    # Find by attributes
    login_link = soup.find('a', href='/login')
    if login_link:
        print(f"Login link: {login_link.text}")
    
    # Find by multiple attributes
    quote_text = soup.find('span', {'class': 'text', 'itemprop': 'text'})
    if quote_text:
        print(f"Quote with itemprop: {quote_text.text[:50]}...")
    
    # Find by text content
    about_link = soup.find('a', string='About')
    if about_link:
        print(f"About link href: {about_link.get('href')}")
    
    # Find with regex
    import re
    
    # Find links with 'author' in href
    author_links = soup.find_all('a', href=re.compile(r'/author/'))
    print(f"Author links: {len(author_links)}")
    
    # Find tags with specific text pattern
    tags_with_life = soup.find_all('a', string=re.compile(r'life', re.I))
    print(f"Tags containing 'life': {len(tags_with_life)}")

finding_methods()
```

### 🎨 **CSS Selectors:**
```python
def css_selectors():
    """CSS selector examples"""
    
    response = requests.get('https://quotes.toscrape.com')
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Basic CSS selectors
    quotes = soup.select('.quote')  # Class selector
    print(f"Quotes with class selector: {len(quotes)}")
    
    # ID selector
    main_content = soup.select('#main')
    print(f"Main content: {len(main_content)}")
    
    # Tag selector
    paragraphs = soup.select('p')
    print(f"Paragraphs: {len(paragraphs)}")
    
    # Attribute selector
    external_links = soup.select('a[href^="http"]')
    print(f"External links: {len(external_links)}")
    
    # Descendant selector
    quote_texts = soup.select('.quote .text')
    print(f"Quote texts: {len(quote_texts)}")
    
    # Child selector
    direct_children = soup.select('.quote > span')
    print(f"Direct children: {len(direct_children)}")
    
    # Pseudo selectors
    first_quote = soup.select('.quote:first-child')
    last_quote = soup.select('.quote:last-child')
    nth_quote = soup.select('.quote:nth-child(3)')
    
    print(f"First quote: {len(first_quote)}")
    print(f"Last quote: {len(last_quote)}")
    print(f"3rd quote: {len(nth_quote)}")
    
    # Complex selectors
    author_in_quotes = soup.select('.quote .author')
    tags_in_quotes = soup.select('.quote .tags .tag')
    
    print(f"Authors in quotes: {len(author_in_quotes)}")
    print(f"Tags in quotes: {len(tags_in_quotes)}")

css_selectors()
```

---

## 🌳 Tree Navigation

### 👨‍👩‍👧‍👦 **Parent, Child, Sibling:**
```python
def tree_navigation():
    """Tree navigation examples"""
    
    html = """
    <div class="container">
        <h1>Title</h1>
        <div class="content">
            <p class="first">First paragraph</p>
            <p class="second">Second paragraph</p>
            <p class="third">Third paragraph</p>
        </div>
        <footer>Footer content</footer>
    </div>
    """
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find starting element
    second_p = soup.find('p', class_='second')
    
    # Parent navigation
    print(f"Parent tag: {second_p.parent.name}")
    print(f"Parent class: {second_p.parent.get('class')}")
    
    # Sibling navigation
    previous_sibling = second_p.previous_sibling
    next_sibling = second_p.next_sibling
    
    # Skip whitespace siblings
    prev_element = second_p.find_previous_sibling()
    next_element = second_p.find_next_sibling()
    
    print(f"Previous element: {prev_element.get('class') if prev_element else None}")
    print(f"Next element: {next_element.get('class') if next_element else None}")
    
    # All siblings
    all_siblings = second_p.find_all_previous_siblings()
    print(f"Previous siblings: {len(all_siblings)}")
    
    all_next_siblings = second_p.find_all_next_siblings()
    print(f"Next siblings: {len(all_next_siblings)}")
    
    # Children navigation
    content_div = soup.find('div', class_='content')
    
    # All children (including text nodes)
    all_children = list(content_div.children)
    print(f"All children: {len(all_children)}")
    
    # Only tag children
    tag_children = list(content_div.find_all(recursive=False))
    print(f"Tag children: {len(tag_children)}")
    
    # Descendants (all nested elements)
    all_descendants = list(content_div.descendants)
    print(f"All descendants: {len(all_descendants)}")

tree_navigation()
```

---

## 📊 Data Extraction

### 📖 **Text Extraction:**
```python
def text_extraction():
    """Text content extraction"""
    
    response = requests.get('https://quotes.toscrape.com')
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Simple text extraction
    first_quote = soup.find('div', class_='quote')
    
    # Get text content
    quote_text = first_quote.find('span', class_='text').text
    author_text = first_quote.find('small', class_='author').text
    
    print(f"Quote: {quote_text}")
    print(f"Author: {author_text}")
    
    # Get text with formatting
    quote_html = first_quote.find('span', class_='text')
    print(f"HTML: {quote_html}")
    print(f"Text only: {quote_html.get_text()}")
    
    # Extract all text from element
    all_text = first_quote.get_text()
    print(f"All text: {all_text}")
    
    # Clean text extraction
    clean_text = first_quote.get_text(strip=True)
    print(f"Clean text: {clean_text}")
    
    # Text with custom separator
    separated_text = first_quote.get_text(separator=' | ')
    print(f"Separated: {separated_text}")
    
    # Extract multiple texts
    all_authors = [author.text for author in soup.find_all('small', class_='author')]
    print(f"All authors: {all_authors}")
    
    # Text processing
    import re
    
    def clean_quote_text(text):
        # Remove quotes and extra whitespace
        cleaned = re.sub(r'^["""]|["""]$', '', text.strip())
        return cleaned
    
    all_quote_texts = []
    for quote in soup.find_all('span', class_='text'):
        cleaned_text = clean_quote_text(quote.text)
        all_quote_texts.append(cleaned_text)
    
    print(f"Cleaned quotes: {len(all_quote_texts)}")

text_extraction()
```

### 🔗 **Attribute Extraction:**
```python
def attribute_extraction():
    """Attribute extraction examples"""
    
    response = requests.get('https://quotes.toscrape.com')
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Single attribute
    first_link = soup.find('a')
    href = first_link.get('href')
    print(f"First link href: {href}")
    
    # Multiple attributes
    login_link = soup.find('a', href='/login')
    if login_link:
        attributes = {
            'href': login_link.get('href'),
            'text': login_link.text,
            'class': login_link.get('class')
        }
        print(f"Login link: {attributes}")
    
    # All attributes
    first_quote = soup.find('div', class_='quote')
    all_attrs = first_quote.attrs
    print(f"Quote attributes: {all_attrs}")
    
    # Check attribute existence
    has_class = first_quote.has_attr('class')
    has_id = first_quote.has_attr('id')
    print(f"Has class: {has_class}, Has id: {has_id}")
    
    # Extract all links with attributes
    links_data = []
    for link in soup.find_all('a', href=True):
        link_info = {
            'text': link.text.strip(),
            'href': link.get('href'),
            'title': link.get('title'),
            'target': link.get('target')
        }
        if link_info['text']:  # Only links with text
            links_data.append(link_info)
    
    print(f"Extracted {len(links_data)} links")
    for link in links_data[:3]:  # First 3 links
        print(f"  {link['text']} -> {link['href']}")
    
    # Extract images (if any)
    images = soup.find_all('img')
    for img in images:
        img_data = {
            'src': img.get('src'),
            'alt': img.get('alt'),
            'title': img.get('title')
        }
        print(f"Image: {img_data}")

attribute_extraction()
```

---

## 🏗️ HTML Structure Analysis

### 📋 **Table Parsing:**
```python
def table_parsing():
    """HTML table parsing"""
    
    # Sample table HTML
    table_html = """
    <table class="data-table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Age</th>
                <th>City</th>
                <th>Occupation</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>John Doe</td>
                <td>25</td>
                <td>New York</td>
                <td>Developer</td>
            </tr>
            <tr>
                <td>Jane Smith</td>
                <td>30</td>
                <td>Los Angeles</td>
                <td>Designer</td>
            </tr>
            <tr>
                <td>Bob Johnson</td>
                <td>35</td>
                <td>Chicago</td>
                <td>Manager</td>
            </tr>
        </tbody>
    </table>
    """
    
    soup = BeautifulSoup(table_html, 'html.parser')
    
    # Find table
    table = soup.find('table', class_='data-table')
    
    # Extract headers
    headers = []
    header_row = table.find('thead').find('tr')
    for th in header_row.find_all('th'):
        headers.append(th.text.strip())
    
    print(f"Headers: {headers}")
    
    # Extract data rows
    data_rows = []
    tbody = table.find('tbody')
    
    for row in tbody.find_all('tr'):
        row_data = []
        for td in row.find_all('td'):
            row_data.append(td.text.strip())
        data_rows.append(row_data)
    
    print(f"Data rows: {len(data_rows)}")
    
    # Create structured data
    table_data = []
    for row in data_rows:
        row_dict = {}
        for i, header in enumerate(headers):
            row_dict[header] = row[i]
        table_data.append(row_dict)
    
    print("Structured table data:")
    for person in table_data:
        print(f"  {person}")

table_parsing()
```

### 📝 **Form Analysis:**
```python
def form_analysis():
    """HTML form analysis"""
    
    # Sample form HTML
    form_html = """
    <form action="/submit" method="post" class="contact-form">
        <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
        </div>
        
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        
        <div class="form-group">
            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="4"></textarea>
        </div>
        
        <div class="form-group">
            <label for="category">Category:</label>
            <select id="category" name="category">
                <option value="general">General</option>
                <option value="support">Support</option>
                <option value="sales">Sales</option>
            </select>
        </div>
        
        <div class="form-group">
            <input type="checkbox" id="newsletter" name="newsletter" value="yes">
            <label for="newsletter">Subscribe to newsletter</label>
        </div>
        
        <button type="submit">Submit</button>
    </form>
    """
    
    soup = BeautifulSoup(form_html, 'html.parser')
    
    # Find form
    form = soup.find('form')
    
    # Form attributes
    form_data = {
        'action': form.get('action'),
        'method': form.get('method'),
        'class': form.get('class')
    }
    
    print(f"Form info: {form_data}")
    
    # Find all form fields
    fields = []
    
    # Input fields
    for input_field in form.find_all('input'):
        field_info = {
            'type': input_field.get('type'),
            'name': input_field.get('name'),
            'id': input_field.get('id'),
            'required': input_field.has_attr('required'),
            'value': input_field.get('value')
        }
        fields.append(field_info)
    
    # Textarea fields
    for textarea in form.find_all('textarea'):
        field_info = {
            'type': 'textarea',
            'name': textarea.get('name'),
            'id': textarea.get('id'),
            'rows': textarea.get('rows')
        }
        fields.append(field_info)
    
    # Select fields
    for select in form.find_all('select'):
        options = [option.get('value') for option in select.find_all('option')]
        field_info = {
            'type': 'select',
            'name': select.get('name'),
            'id': select.get('id'),
            'options': options
        }
        fields.append(field_info)
    
    print(f"Form fields: {len(fields)}")
    for field in fields:
        print(f"  {field}")

form_analysis()
```

---

## 🎯 Advanced Techniques

### 🔍 **Custom Search Functions:**
```python
def custom_search():
    """Custom search functions"""
    
    response = requests.get('https://quotes.toscrape.com')
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Custom function to find elements
    def find_quotes_by_author(soup, author_name):
        """Find quotes by specific author"""
        quotes = []
        for quote in soup.find_all('div', class_='quote'):
            author = quote.find('small', class_='author').text
            if author.lower() == author_name.lower():
                quotes.append(quote)
        return quotes
    
    # Usage
    einstein_quotes = find_quotes_by_author(soup, 'Albert Einstein')
    print(f"Einstein quotes: {len(einstein_quotes)}")
    
    # Custom function with lambda
    def find_elements_by_condition(soup, tag, condition):
        """Find elements by custom condition"""
        return soup.find_all(tag, condition)
    
    # Find quotes with specific tag
    love_quotes = find_elements_by_condition(
        soup, 
        'div', 
        lambda tag: tag.get('class') == ['quote'] and 
                   any('love' in a.text.lower() for a in tag.find_all('a', class_='tag'))
    )
    
    print(f"Love quotes: {len(love_quotes)}")
    
    # Find long quotes (more than 100 characters)
    long_quotes = []
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').text
        if len(text) > 100:
            long_quotes.append(quote)
    
    print(f"Long quotes: {len(long_quotes)}")

custom_search()
```

### 🧹 **Data Cleaning:**
```python
import re

def data_cleaning():
    """Data cleaning techniques"""
    
    response = requests.get('https://quotes.toscrape.com')
    soup = BeautifulSoup(response.content, 'html.parser')
    
    def clean_text(text):
        """Clean extracted text"""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove quotes
        text = re.sub(r'^["""]|["""]$', '', text)
        
        # Strip whitespace
        text = text.strip()
        
        return text
    
    def extract_clean_quotes(soup):
        """Extract and clean all quotes"""
        quotes_data = []
        
        for quote in soup.find_all('div', class_='quote'):
            # Extract raw data
            raw_text = quote.find('span', class_='text').text
            raw_author = quote.find('small', class_='author').text
            raw_tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            
            # Clean data
            clean_quote = {
                'text': clean_text(raw_text),
                'author': clean_text(raw_author),
                'tags': [clean_text(tag) for tag in raw_tags],
                'word_count': len(clean_text(raw_text).split()),
                'char_count': len(clean_text(raw_text))
            }
            
            quotes_data.append(clean_quote)
        
        return quotes_data
    
    # Extract clean data
    clean_quotes = extract_clean_quotes(soup)
    
    print(f"Extracted {len(clean_quotes)} clean quotes")
    
    # Display first quote
    if clean_quotes:
        first = clean_quotes[0]
        print(f"\nFirst clean quote:")
        print(f"  Text: {first['text']}")
        print(f"  Author: {first['author']}")
        print(f"  Tags: {', '.join(first['tags'])}")
        print(f"  Words: {first['word_count']}, Characters: {first['char_count']}")

data_cleaning()
```

---

## 🎉 সমাপনী

### ✅ **BeautifulSoup এ আপনি শিখেছেন:**
- HTML/XML parsing techniques
- Element finding methods (find, find_all, CSS selectors)
- Tree navigation (parent, child, sibling)
- Text ও attribute extraction
- Table ও form parsing
- Advanced search ও data cleaning

### 🚀 **Next Steps:**
- **Requests** এর সাথে combine করে complete scraper
- **Pandas** দিয়ে data processing
- **Async scraping** with aiohttp
- **Advanced parsing** with lxml

**BeautifulSoup mastery সম্পন্ন! 🍲🇧🇩**
