# 🌟 Playwright Real-World Examples - বাস্তব প্রজেক্ট

## 🛒 E-commerce Product Scraper

### Complete E-commerce Scraping System:
```python
from playwright.sync_api import sync_playwright
import json
import csv
import time
from datetime import datetime

class EcommerceScraper:
    def __init__(self, headless=True):
        self.headless = headless
        self.products = []
        
    def setup_browser(self):
        """Browser setup with optimization"""
        self.playwright = sync_playwright().start()
        
        self.browser = self.playwright.chromium.launch(
            headless=self.headless,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-blink-features=AutomationControlled"
            ]
        )
        
        # Context with mobile user agent (less detection)
        self.context = self.browser.new_context(
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15",
            viewport={'width': 375, 'height': 812}
        )
        
        self.page = self.context.new_page()
        
        # Block unnecessary resources
        self.page.route("**/*.{png,jpg,jpeg,gif,svg,css,woff,woff2}", lambda route: route.abort())
    
    def scrape_product_listing(self, url, max_pages=5):
        """Product listing page scrape করা"""
        
        self.page.goto(url)
        self.page.wait_for_load_state('networkidle')
        
        current_page = 1
        
        while current_page <= max_pages:
            print(f"🔍 Scraping page {current_page}...")
            
            # Wait for products to load
            self.page.wait_for_selector('.product-item, .product-card', timeout=10000)
            
            # Extract products from current page
            products = self.page.locator('.product-item, .product-card').all()
            
            for product in products:
                try:
                    product_data = self.extract_product_data(product)
                    if product_data:
                        self.products.append(product_data)
                except Exception as e:
                    print(f"❌ Error extracting product: {e}")
                    continue
            
            print(f"✅ Page {current_page}: {len(products)} products found")
            
            # Try to go to next page
            next_button = self.page.locator('.next-page, .pagination-next, [aria-label*="next"]')
            if next_button.is_visible() and next_button.is_enabled():
                next_button.click()
                self.page.wait_for_load_state('networkidle')
                current_page += 1
                time.sleep(2)  # Rate limiting
            else:
                print("📄 No more pages available")
                break
        
        return self.products
    
    def extract_product_data(self, product_element):
        """Single product থেকে data extract করা"""
        
        try:
            # Basic product info
            name = product_element.locator('.product-name, .title, h3, h4').first.text_content()
            price = product_element.locator('.price, .cost, .amount').first.text_content()
            
            # Optional fields
            rating = "N/A"
            rating_element = product_element.locator('.rating, .stars, .review-score')
            if rating_element.is_visible():
                rating = rating_element.text_content()
            
            # Product URL
            link_element = product_element.locator('a').first
            product_url = link_element.get_attribute('href') if link_element.is_visible() else ""
            
            # Image URL
            img_element = product_element.locator('img').first
            image_url = img_element.get_attribute('src') if img_element.is_visible() else ""
            
            # Availability
            availability = "In Stock"
            if product_element.locator('.out-of-stock, .unavailable').is_visible():
                availability = "Out of Stock"
            
            return {
                'name': name.strip() if name else "N/A",
                'price': price.strip() if price else "N/A",
                'rating': rating.strip() if rating else "N/A",
                'url': product_url,
                'image': image_url,
                'availability': availability,
                'scraped_at': datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"❌ Error in extract_product_data: {e}")
            return None
    
    def scrape_product_details(self, product_urls):
        """Individual product pages থেকে detailed info"""
        
        detailed_products = []
        
        for i, url in enumerate(product_urls[:10]):  # First 10 for demo
            print(f"🔍 Scraping product {i+1}/{len(product_urls[:10])}: {url}")
            
            try:
                self.page.goto(url)
                self.page.wait_for_load_state('networkidle')
                
                # Extract detailed info
                product_details = {
                    'url': url,
                    'title': self.safe_extract('.product-title, h1'),
                    'price': self.safe_extract('.price, .cost'),
                    'description': self.safe_extract('.description, .product-desc'),
                    'specifications': self.extract_specifications(),
                    'images': self.extract_images(),
                    'reviews_count': self.safe_extract('.review-count, .reviews-total'),
                    'rating': self.safe_extract('.rating, .stars'),
                    'availability': self.check_availability()
                }
                
                detailed_products.append(product_details)
                time.sleep(1)  # Rate limiting
                
            except Exception as e:
                print(f"❌ Error scraping {url}: {e}")
                continue
        
        return detailed_products
    
    def safe_extract(self, selector):
        """Safe text extraction with fallback"""
        try:
            element = self.page.locator(selector).first
            return element.text_content().strip() if element.is_visible() else "N/A"
        except:
            return "N/A"
    
    def extract_specifications(self):
        """Product specifications extract করা"""
        specs = {}
        
        try:
            spec_rows = self.page.locator('.spec-row, .specification-item, .feature-item').all()
            
            for row in spec_rows:
                key_element = row.locator('.spec-key, .feature-name, .label').first
                value_element = row.locator('.spec-value, .feature-value, .value').first
                
                if key_element.is_visible() and value_element.is_visible():
                    key = key_element.text_content().strip()
                    value = value_element.text_content().strip()
                    specs[key] = value
        except:
            pass
        
        return specs
    
    def extract_images(self):
        """Product images extract করা"""
        images = []
        
        try:
            img_elements = self.page.locator('.product-image img, .gallery img').all()
            
            for img in img_elements[:5]:  # First 5 images
                src = img.get_attribute('src')
                if src:
                    images.append(src)
        except:
            pass
        
        return images
    
    def check_availability(self):
        """Product availability check করা"""
        
        if self.page.locator('.out-of-stock, .unavailable, .sold-out').is_visible():
            return "Out of Stock"
        elif self.page.locator('.in-stock, .available').is_visible():
            return "In Stock"
        elif self.page.locator('.add-to-cart, .buy-now').is_enabled():
            return "In Stock"
        else:
            return "Unknown"
    
    def save_data(self, filename_prefix="products"):
        """Data save করা multiple formats এ"""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # JSON format
        json_file = f"{filename_prefix}_{timestamp}.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(self.products, f, ensure_ascii=False, indent=2)
        
        # CSV format
        csv_file = f"{filename_prefix}_{timestamp}.csv"
        if self.products:
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.products[0].keys())
                writer.writeheader()
                writer.writerows(self.products)
        
        print(f"💾 Data saved: {json_file}, {csv_file}")
        return json_file, csv_file
    
    def close(self):
        """Browser cleanup"""
        if hasattr(self, 'browser'):
            self.browser.close()
        if hasattr(self, 'playwright'):
            self.playwright.stop()

# Usage Example
def main():
    scraper = EcommerceScraper(headless=False)
    
    try:
        scraper.setup_browser()
        
        # Scrape product listing
        products = scraper.scrape_product_listing(
            "https://example-shop.com/products", 
            max_pages=3
        )
        
        print(f"✅ Total products scraped: {len(products)}")
        
        # Get detailed info for some products
        product_urls = [p['url'] for p in products if p['url']][:5]
        detailed_products = scraper.scrape_product_details(product_urls)
        
        # Save data
        scraper.save_data("ecommerce_products")
        
        # Print summary
        print("\n📊 Scraping Summary:")
        print(f"Total products: {len(products)}")
        print(f"Detailed products: {len(detailed_products)}")
        
        # Show sample data
        if products:
            print("\n🔍 Sample Product:")
            sample = products[0]
            for key, value in sample.items():
                print(f"  {key}: {value}")
    
    finally:
        scraper.close()

if __name__ == "__main__":
    main()
```

## 📰 News Aggregator System

### Multi-Source News Scraper:
```python
class NewsAggregator:
    def __init__(self):
        self.news_sources = {
            'prothom_alo': {
                'url': 'https://www.prothomalo.com',
                'selectors': {
                    'articles': '.story-card',
                    'title': '.story-card__title',
                    'summary': '.story-card__summary',
                    'link': '.story-card__title a',
                    'time': '.story-card__time'
                }
            },
            'daily_star': {
                'url': 'https://www.thedailystar.net',
                'selectors': {
                    'articles': '.article-item',
                    'title': '.article-title',
                    'summary': '.article-summary',
                    'link': '.article-title a',
                    'time': '.article-time'
                }
            }
        }
        
        self.all_news = []
    
    def scrape_news_source(self, source_name, source_config):
        """Single news source থেকে news scrape করা"""
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            try:
                print(f"📰 Scraping {source_name}...")
                
                page.goto(source_config['url'])
                page.wait_for_load_state('networkidle')
                
                # Extract articles
                articles = page.locator(source_config['selectors']['articles']).all()
                
                source_news = []
                for article in articles[:10]:  # Top 10 news
                    try:
                        news_item = {
                            'source': source_name,
                            'title': article.locator(source_config['selectors']['title']).text_content().strip(),
                            'summary': self.safe_extract_text(article, source_config['selectors'].get('summary', '')),
                            'link': self.safe_extract_link(article, source_config['selectors']['link']),
                            'time': self.safe_extract_text(article, source_config['selectors'].get('time', '')),
                            'scraped_at': datetime.now().isoformat()
                        }
                        
                        source_news.append(news_item)
                        
                    except Exception as e:
                        print(f"❌ Error extracting article: {e}")
                        continue
                
                print(f"✅ {source_name}: {len(source_news)} articles")
                return source_news
                
            except Exception as e:
                print(f"❌ Error scraping {source_name}: {e}")
                return []
            
            finally:
                browser.close()
    
    def safe_extract_text(self, element, selector):
        """Safe text extraction"""
        try:
            if selector:
                return element.locator(selector).text_content().strip()
            return ""
        except:
            return ""
    
    def safe_extract_link(self, element, selector):
        """Safe link extraction"""
        try:
            link_element = element.locator(selector)
            href = link_element.get_attribute('href')
            
            # Make absolute URL if relative
            if href and href.startswith('/'):
                base_url = element.page.url.split('/')[0:3]  # protocol + domain
                href = '/'.join(base_url) + href
            
            return href or ""
        except:
            return ""
    
    def aggregate_all_news(self):
        """সব news sources থেকে news collect করা"""
        
        for source_name, source_config in self.news_sources.items():
            source_news = self.scrape_news_source(source_name, source_config)
            self.all_news.extend(source_news)
            
            # Rate limiting between sources
            time.sleep(2)
        
        # Remove duplicates based on title similarity
        self.all_news = self.remove_duplicate_news()
        
        return self.all_news
    
    def remove_duplicate_news(self):
        """Duplicate news remove করা"""
        unique_news = []
        seen_titles = set()
        
        for news in self.all_news:
            # Simple duplicate detection by title
            title_words = set(news['title'].lower().split())
            
            is_duplicate = False
            for seen_title in seen_titles:
                seen_words = set(seen_title.split())
                
                # If 70% words match, consider duplicate
                if len(title_words & seen_words) / len(title_words | seen_words) > 0.7:
                    is_duplicate = True
                    break
            
            if not is_duplicate:
                unique_news.append(news)
                seen_titles.add(news['title'].lower())
        
        print(f"🔄 Removed {len(self.all_news) - len(unique_news)} duplicate news")
        return unique_news

# Usage
aggregator = NewsAggregator()
all_news = aggregator.aggregate_all_news()
print(f"📰 Total unique news: {len(all_news)}")
```
