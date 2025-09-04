# 🎬 Playwright দিয়ে Image ও Video Download - Very Fast Way

## 📚 সূচিপত্র
1. [Setup ও Requirements](#setup)
2. [Image Download Techniques](#image-download)
3. [Video Download Methods](#video-download)
4. [Bulk Download System](#bulk-download)
5. [Advanced Download Features](#advanced-features)
6. [Performance Optimization](#performance-optimization)

---

## 🛠️ Setup ও Requirements {#setup}

### প্রয়োজনীয় Libraries:
```bash
# Core requirements
pip install playwright aiohttp aiofiles

# Additional utilities
pip install requests tqdm pillow

# Video processing (optional)
pip install yt-dlp ffmpeg-python

# Install browsers
playwright install
```

### Basic Imports:
```python
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
import aiohttp
import aiofiles
import asyncio
import os
import time
from urllib.parse import urljoin, urlparse
from pathlib import Path
import json
import concurrent.futures
```

---

## 🖼️ Image Download Techniques {#image-download}

### Method 1: Direct URL Download (দ্রুততম)
```python
import requests
from urllib.parse import urlparse
import os

def download_image_direct(url, folder="downloads"):
    """Direct URL থেকে image download"""
    
    try:
        # Create folder
        os.makedirs(folder, exist_ok=True)
        
        # Get filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename or '.' not in filename:
            filename = f"image_{int(time.time())}.jpg"
        
        filepath = os.path.join(folder, filename)
        
        # Download
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"✅ Downloaded: {filename}")
        return filepath
        
    except Exception as e:
        print(f"❌ Error downloading {url}: {e}")
        return None

# Usage
download_image_direct("https://example.com/image.jpg")
```

### Method 2: Playwright দিয়ে Page থেকে Images Extract
```python
def extract_and_download_images(page_url, download_folder="images"):
    """Page থেকে সব images extract করে download"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            print(f"🔍 Loading page: {page_url}")
            page.goto(page_url)
            page.wait_for_load_state('networkidle')
            
            # Get all image URLs
            image_urls = page.evaluate("""
                () => {
                    const images = Array.from(document.querySelectorAll('img'));
                    return images.map(img => ({
                        src: img.src,
                        alt: img.alt || '',
                        width: img.naturalWidth,
                        height: img.naturalHeight
                    })).filter(img => img.src && img.width > 100 && img.height > 100);
                }
            """)
            
            print(f"📸 Found {len(image_urls)} images")
            
            # Create download folder
            os.makedirs(download_folder, exist_ok=True)
            
            # Download images
            downloaded = []
            for i, img_info in enumerate(image_urls):
                try:
                    url = img_info['src']
                    
                    # Generate filename
                    parsed = urlparse(url)
                    filename = os.path.basename(parsed.path)
                    
                    if not filename or '.' not in filename:
                        ext = '.jpg'
                        if 'png' in url.lower():
                            ext = '.png'
                        elif 'gif' in url.lower():
                            ext = '.gif'
                        filename = f"image_{i+1}{ext}"
                    
                    filepath = os.path.join(download_folder, filename)
                    
                    # Download
                    response = requests.get(url, timeout=10)
                    response.raise_for_status()
                    
                    with open(filepath, 'wb') as f:
                        f.write(response.content)
                    
                    downloaded.append({
                        'filename': filename,
                        'url': url,
                        'size': f"{img_info['width']}x{img_info['height']}"
                    })
                    
                    print(f"✅ {i+1}/{len(image_urls)}: {filename}")
                    
                except Exception as e:
                    print(f"❌ Error downloading image {i+1}: {e}")
                    continue
            
            print(f"🎉 Downloaded {len(downloaded)} images to {download_folder}")
            return downloaded
            
        finally:
            browser.close()

# Usage
images = extract_and_download_images("https://unsplash.com/s/photos/nature")
```

### Method 3: Async Bulk Image Download (সবচেয়ে দ্রুত)
```python
async def download_image_async(session, url, folder, semaphore):
    """Async image download with semaphore for rate limiting"""
    
    async with semaphore:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    # Get filename
                    filename = os.path.basename(urlparse(url).path)
                    if not filename or '.' not in filename:
                        filename = f"image_{hash(url) % 10000}.jpg"
                    
                    filepath = os.path.join(folder, filename)
                    
                    # Write file
                    async with aiofiles.open(filepath, 'wb') as f:
                        async for chunk in response.content.iter_chunked(8192):
                            await f.write(chunk)
                    
                    return {'success': True, 'filename': filename, 'url': url}
                else:
                    return {'success': False, 'url': url, 'error': f'HTTP {response.status}'}
                    
        except Exception as e:
            return {'success': False, 'url': url, 'error': str(e)}

async def bulk_download_images(urls, folder="bulk_images", max_concurrent=10):
    """Bulk async image download"""
    
    os.makedirs(folder, exist_ok=True)
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async with aiohttp.ClientSession() as session:
        tasks = [download_image_async(session, url, folder, semaphore) for url in urls]
        
        print(f"🚀 Starting download of {len(urls)} images...")
        start_time = time.time()
        
        results = await asyncio.gather(*tasks)
        
        end_time = time.time()
        
        # Count results
        successful = sum(1 for r in results if r['success'])
        failed = len(results) - successful
        
        print(f"✅ Downloaded: {successful}")
        print(f"❌ Failed: {failed}")
        print(f"⏱️ Time taken: {end_time - start_time:.2f} seconds")
        
        return results

# Usage
image_urls = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.png",
    # ... more URLs
]

# Run async download
# asyncio.run(bulk_download_images(image_urls))
```

---

## 🎥 Video Download Methods {#video-download}

### Method 1: Direct Video URL Download
```python
def download_video_direct(url, folder="videos", chunk_size=8192):
    """Direct video download with progress"""
    
    try:
        os.makedirs(folder, exist_ok=True)
        
        # Get video info
        response = requests.head(url)
        total_size = int(response.headers.get('content-length', 0))
        
        filename = os.path.basename(urlparse(url).path)
        if not filename or '.' not in filename:
            filename = f"video_{int(time.time())}.mp4"
        
        filepath = os.path.join(folder, filename)
        
        print(f"📥 Downloading: {filename} ({total_size / 1024 / 1024:.1f} MB)")
        
        # Download with progress
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        downloaded = 0
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    
                    if total_size > 0:
                        progress = (downloaded / total_size) * 100
                        print(f"\r📊 Progress: {progress:.1f}%", end='', flush=True)
        
        print(f"\n✅ Downloaded: {filename}")
        return filepath
        
    except Exception as e:
        print(f"❌ Error downloading video: {e}")
        return None

# Usage
download_video_direct("https://example.com/video.mp4")
```

### Method 2: Playwright দিয়ে Video URLs Extract
```python
def extract_video_urls(page_url):
    """Page থেকে video URLs extract করা"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Capture network requests
        video_urls = []
        
        def handle_response(response):
            content_type = response.headers.get('content-type', '')
            if 'video/' in content_type or response.url.endswith(('.mp4', '.webm', '.avi', '.mov')):
                video_urls.append({
                    'url': response.url,
                    'content_type': content_type,
                    'size': response.headers.get('content-length', 'Unknown')
                })
                print(f"🎬 Found video: {response.url}")
        
        page.on('response', handle_response)
        
        try:
            print(f"🔍 Loading page: {page_url}")
            page.goto(page_url)
            page.wait_for_load_state('networkidle')
            
            # Also check for video elements in DOM
            dom_videos = page.evaluate("""
                () => {
                    const videos = Array.from(document.querySelectorAll('video'));
                    return videos.map(video => ({
                        src: video.src || video.currentSrc,
                        poster: video.poster,
                        duration: video.duration,
                        width: video.videoWidth,
                        height: video.videoHeight
                    })).filter(v => v.src);
                }
            """)
            
            # Combine network and DOM videos
            all_videos = video_urls + [{'url': v['src'], 'type': 'dom'} for v in dom_videos]
            
            print(f"🎥 Total videos found: {len(all_videos)}")
            return all_videos
            
        finally:
            browser.close()

# Usage
videos = extract_video_urls("https://example.com/video-page")
```

### Method 3: Advanced Video Download with yt-dlp Integration
```python
import yt_dlp
import subprocess

def download_video_advanced(url, output_folder="videos", quality="best"):
    """Advanced video download using yt-dlp"""
    
    try:
        os.makedirs(output_folder, exist_ok=True)
        
        ydl_opts = {
            'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
            'format': quality,  # 'best', 'worst', 'bestvideo+bestaudio'
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Get video info first
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'Unknown')
            duration = info.get('duration', 0)
            
            print(f"🎬 Title: {title}")
            print(f"⏱️ Duration: {duration // 60}:{duration % 60:02d}")
            
            # Download
            ydl.download([url])
            print(f"✅ Downloaded: {title}")
            
            return True
            
    except Exception as e:
        print(f"❌ Error downloading video: {e}")
        return False

# Usage
download_video_advanced("https://youtube.com/watch?v=VIDEO_ID")
```

---

## 📦 Bulk Download System {#bulk-download}

### Complete Media Scraper Class:
```python
class MediaScraper:
    def __init__(self, download_folder="downloads", max_concurrent=5):
        self.download_folder = download_folder
        self.max_concurrent = max_concurrent
        self.downloaded_files = []
        
        # Create folders
        self.image_folder = os.path.join(download_folder, "images")
        self.video_folder = os.path.join(download_folder, "videos")
        os.makedirs(self.image_folder, exist_ok=True)
        os.makedirs(self.video_folder, exist_ok=True)
    
    def scrape_page_media(self, url):
        """Page থেকে সব media scrape করা"""
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # Track network requests
            media_urls = {'images': [], 'videos': []}
            
            def handle_response(response):
                content_type = response.headers.get('content-type', '')
                url = response.url
                
                if content_type.startswith('image/'):
                    media_urls['images'].append(url)
                elif content_type.startswith('video/'):
                    media_urls['videos'].append(url)
            
            page.on('response', handle_response)
            
            try:
                print(f"🔍 Scraping: {url}")
                page.goto(url)
                page.wait_for_load_state('networkidle')
                
                # Get DOM media
                dom_media = page.evaluate("""
                    () => {
                        const images = Array.from(document.querySelectorAll('img')).map(img => img.src).filter(src => src);
                        const videos = Array.from(document.querySelectorAll('video')).map(video => video.src || video.currentSrc).filter(src => src);
                        
                        return { images, videos };
                    }
                """)
                
                # Combine network and DOM media
                all_images = list(set(media_urls['images'] + dom_media['images']))
                all_videos = list(set(media_urls['videos'] + dom_media['videos']))
                
                print(f"📸 Images found: {len(all_images)}")
                print(f"🎥 Videos found: {len(all_videos)}")
                
                return {'images': all_images, 'videos': all_videos}
                
            finally:
                browser.close()
    
    async def download_all_media(self, media_dict):
        """সব media async download করা"""
        
        # Download images
        if media_dict['images']:
            print("📸 Downloading images...")
            image_results = await self.bulk_download_images(media_dict['images'])
            
        # Download videos
        if media_dict['videos']:
            print("🎥 Downloading videos...")
            video_results = await self.bulk_download_videos(media_dict['videos'])
        
        return {
            'images': len([r for r in image_results if r['success']]) if media_dict['images'] else 0,
            'videos': len([r for r in video_results if r['success']]) if media_dict['videos'] else 0
        }
    
    async def bulk_download_images(self, urls):
        """Bulk image download"""
        semaphore = asyncio.Semaphore(self.max_concurrent)
        
        async with aiohttp.ClientSession() as session:
            tasks = [self.download_single_image(session, url, semaphore) for url in urls]
            return await asyncio.gather(*tasks)
    
    async def bulk_download_videos(self, urls):
        """Bulk video download"""
        semaphore = asyncio.Semaphore(2)  # Lower concurrency for videos
        
        async with aiohttp.ClientSession() as session:
            tasks = [self.download_single_video(session, url, semaphore) for url in urls]
            return await asyncio.gather(*tasks)
    
    async def download_single_image(self, session, url, semaphore):
        """Single image download"""
        async with semaphore:
            try:
                async with session.get(url, timeout=30) as response:
                    if response.status == 200:
                        filename = f"img_{hash(url) % 10000}.jpg"
                        filepath = os.path.join(self.image_folder, filename)
                        
                        async with aiofiles.open(filepath, 'wb') as f:
                            async for chunk in response.content.iter_chunked(8192):
                                await f.write(chunk)
                        
                        return {'success': True, 'filename': filename}
                    else:
                        return {'success': False, 'error': f'HTTP {response.status}'}
            except Exception as e:
                return {'success': False, 'error': str(e)}
    
    async def download_single_video(self, session, url, semaphore):
        """Single video download"""
        async with semaphore:
            try:
                async with session.get(url, timeout=60) as response:
                    if response.status == 200:
                        filename = f"vid_{hash(url) % 10000}.mp4"
                        filepath = os.path.join(self.video_folder, filename)
                        
                        async with aiofiles.open(filepath, 'wb') as f:
                            async for chunk in response.content.iter_chunked(8192):
                                await f.write(chunk)
                        
                        return {'success': True, 'filename': filename}
                    else:
                        return {'success': False, 'error': f'HTTP {response.status}'}
            except Exception as e:
                return {'success': False, 'error': str(e)}

# Usage
async def main():
    scraper = MediaScraper("downloads", max_concurrent=10)
    
    # Scrape media from page
    media = scraper.scrape_page_media("https://example.com")
    
    # Download all media
    results = await scraper.download_all_media(media)
    
    print(f"🎉 Download complete!")
    print(f"📸 Images: {results['images']}")
    print(f"🎥 Videos: {results['videos']}")

# Run
# asyncio.run(main())
```
