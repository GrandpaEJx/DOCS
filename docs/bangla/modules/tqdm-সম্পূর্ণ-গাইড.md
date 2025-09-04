# 📊 tqdm - সম্পূর্ণ বাংলা গাইড

## 🌟 tqdm কি?

tqdm (تقدّم, taqaddum, "progress" in Arabic) হলো Python এর একটি **fast, extensible progress bar library** যা দিয়ে আপনি loops, file operations ও long-running tasks এর progress track করতে পারেন।

### 🎯 **মূল বৈশিষ্ট্য:**
- ✅ **Fast ও lightweight** - Minimal overhead
- ✅ **Versatile** - Loops, iterables, manual updates
- ✅ **Customizable** - Colors, formats, descriptions
- ✅ **Nested progress bars** - Multiple levels
- ✅ **Jupyter support** - Notebook integration
- ✅ **Thread-safe** - Concurrent operations

---

## 🚀 Installation ও Setup

### 📦 **Installation:**
```bash
# tqdm install
pip install tqdm>=4.66.0

# With additional features
pip install tqdm[notebook]  # Jupyter notebook support

# Verify installation
python -c "from tqdm import tqdm; print('tqdm installed successfully!')"
```

### ✅ **Installation Verify:**
```python
# test_tqdm.py
from tqdm import tqdm
import time

def test_tqdm():
    print("🧪 tqdm installation test...")
    
    # Simple progress bar test
    for i in tqdm(range(10), desc="Testing"):
        time.sleep(0.1)
    
    print("✅ Basic progress bar works")
    
    # Manual progress bar
    with tqdm(total=100, desc="Manual test") as pbar:
        for i in range(10):
            time.sleep(0.05)
            pbar.update(10)
    
    print("🎉 tqdm working perfectly!")

test_tqdm()
```

---

## 📊 Basic Progress Bars

### 🔄 **Simple Loop Progress:**
```python
from tqdm import tqdm
import time
import random

def basic_progress_bars():
    """Basic progress bar examples"""
    
    print("📊 Basic Progress Bar Examples")
    
    # Simple loop with progress bar
    print("\n1. Simple loop progress:")
    for i in tqdm(range(20)):
        time.sleep(0.1)  # Simulate work
    
    # With description
    print("\n2. Progress with description:")
    for i in tqdm(range(15), desc="Processing"):
        time.sleep(0.1)
    
    # With custom format
    print("\n3. Custom format:")
    for i in tqdm(range(10), desc="Custom", unit="items"):
        time.sleep(0.2)
    
    # Processing a list
    print("\n4. Processing list:")
    items = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt']
    
    for item in tqdm(items, desc="Processing files"):
        # Simulate file processing
        time.sleep(0.3)
        print(f"  Processed: {item}")
    
    # Range with step
    print("\n5. Range with step:")
    for i in tqdm(range(0, 100, 5), desc="Step by 5"):
        time.sleep(0.05)
    
    # Variable processing time
    print("\n6. Variable processing time:")
    for i in tqdm(range(10), desc="Variable time"):
        # Random processing time
        time.sleep(random.uniform(0.1, 0.5))

basic_progress_bars()
```

### ⚙️ **Manual Progress Control:**
```python
def manual_progress_control():
    """Manual progress bar control"""
    
    print("⚙️ Manual Progress Control Examples")
    
    # Manual update
    print("\n1. Manual update:")
    with tqdm(total=100, desc="Manual") as pbar:
        for i in range(10):
            # Simulate work
            time.sleep(0.1)
            # Update progress by 10
            pbar.update(10)
    
    # Set progress directly
    print("\n2. Set progress directly:")
    with tqdm(total=100, desc="Direct set") as pbar:
        for progress in [0, 25, 50, 75, 100]:
            pbar.n = progress
            pbar.refresh()
            time.sleep(0.2)
    
    # Dynamic total
    print("\n3. Dynamic total:")
    pbar = tqdm(desc="Dynamic total")
    
    for i in range(20):
        # Simulate discovering more work
        if i == 10:
            pbar.total = 30
            pbar.refresh()
        
        pbar.update(1)
        time.sleep(0.05)
    
    pbar.close()
    
    # Indeterminate progress
    print("\n4. Indeterminate progress:")
    pbar = tqdm(desc="Unknown total", total=None)
    
    for i in range(15):
        pbar.update(1)
        time.sleep(0.1)
    
    pbar.close()
    
    # Progress with postfix
    print("\n5. Progress with postfix info:")
    with tqdm(total=20, desc="With info") as pbar:
        for i in range(20):
            # Update postfix with current info
            pbar.set_postfix({
                'loss': f'{random.uniform(0.1, 1.0):.3f}',
                'acc': f'{random.uniform(0.8, 1.0):.3f}'
            })
            pbar.update(1)
            time.sleep(0.1)

manual_progress_control()
```

---

## 🎨 Customization ও Styling

### 🌈 **Custom Formats ও Colors:**
```python
def custom_formats_colors():
    """Custom formatting and colors"""
    
    print("🎨 Custom Formats and Colors")
    
    # Custom bar format
    print("\n1. Custom bar format:")
    custom_format = "{l_bar}{bar:30}{r_bar}{bar:-30b}"
    
    for i in tqdm(range(20), desc="Custom format", bar_format=custom_format):
        time.sleep(0.05)
    
    # Different units
    print("\n2. Different units:")
    units = [
        ("bytes", "B"),
        ("items", "items"),
        ("files", "files"),
        ("records", "recs")
    ]
    
    for desc, unit in units:
        for i in tqdm(range(10), desc=f"Processing {desc}", unit=unit):
            time.sleep(0.05)
    
    # Custom colors (requires colorama)
    try:
        from colorama import Fore, Style, init
        init()
        
        print("\n3. Colored progress bars:")
        
        # Red progress bar
        for i in tqdm(range(10), desc=f"{Fore.RED}Red Progress{Style.RESET_ALL}"):
            time.sleep(0.05)
        
        # Green progress bar
        for i in tqdm(range(10), desc=f"{Fore.GREEN}Green Progress{Style.RESET_ALL}"):
            time.sleep(0.05)
        
        # Blue progress bar
        for i in tqdm(range(10), desc=f"{Fore.BLUE}Blue Progress{Style.RESET_ALL}"):
            time.sleep(0.05)
    
    except ImportError:
        print("   (Colorama not installed - skipping colored examples)")
    
    # ASCII vs Unicode bars
    print("\n4. Different bar styles:")
    
    # ASCII bar
    for i in tqdm(range(15), desc="ASCII bar", ascii=True):
        time.sleep(0.05)
    
    # Unicode bar (default)
    for i in tqdm(range(15), desc="Unicode bar", ascii=False):
        time.sleep(0.05)
    
    # Custom bar characters
    for i in tqdm(range(15), desc="Custom chars", ascii="▱▰"):
        time.sleep(0.05)

custom_formats_colors()
```

### 📏 **Size ও Position Control:**
```python
def size_position_control():
    """Control bar size and position"""
    
    print("📏 Size and Position Control")
    
    # Different bar widths
    print("\n1. Different bar widths:")
    
    for width in [10, 20, 50]:
        for i in tqdm(range(10), desc=f"Width {width}", ncols=width+30):
            time.sleep(0.05)
    
    # Disable progress bar (only show stats)
    print("\n2. Stats only (no bar):")
    for i in tqdm(range(15), desc="Stats only", disable=False, leave=False):
        time.sleep(0.05)
    
    # Leave progress bar after completion
    print("\n3. Leave vs don't leave:")
    
    # Don't leave
    for i in tqdm(range(10), desc="Don't leave", leave=False):
        time.sleep(0.05)
    
    # Leave (default)
    for i in tqdm(range(10), desc="Leave bar", leave=True):
        time.sleep(0.05)
    
    # Position control
    print("\n4. Position control:")
    
    # Multiple bars at different positions
    import threading
    
    def worker(position, desc):
        for i in tqdm(range(20), desc=desc, position=position, leave=False):
            time.sleep(0.02)
    
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(i, f"Worker {i+1}"))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print("   All workers completed")

size_position_control()
```

---

## 🔄 Advanced Features

### 📊 **Nested Progress Bars:**
```python
def nested_progress_bars():
    """Nested progress bars for hierarchical tasks"""
    
    print("📊 Nested Progress Bars")
    
    # Simple nested bars
    print("\n1. Simple nested bars:")
    
    outer_tasks = ['Task A', 'Task B', 'Task C']
    
    for task in tqdm(outer_tasks, desc="Main tasks", position=0):
        # Inner progress for subtasks
        for subtask in tqdm(range(5), desc=f"  {task} subtasks", 
                           position=1, leave=False):
            time.sleep(0.1)
    
    # Complex nested structure
    print("\n2. Complex nested structure:")
    
    projects = ['Project 1', 'Project 2']
    
    for project in tqdm(projects, desc="Projects", position=0):
        modules = ['Module A', 'Module B', 'Module C']
        
        for module in tqdm(modules, desc=f"  {project} modules", 
                          position=1, leave=False):
            # Files in each module
            for file_num in tqdm(range(3), desc=f"    {module} files", 
                               position=2, leave=False):
                time.sleep(0.05)
    
    # Parallel nested bars
    print("\n3. Parallel nested bars:")
    
    def process_batch(batch_id, position):
        """Process a batch with its own progress bar"""
        for i in tqdm(range(10), desc=f"Batch {batch_id}", 
                     position=position, leave=False):
            time.sleep(0.1)
    
    import threading
    
    threads = []
    for i in range(3):
        t = threading.Thread(target=process_batch, args=(i+1, i))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print("   All batches completed")

nested_progress_bars()
```

### 📁 **File Operations Progress:**
```python
import os

def file_operations_progress():
    """Progress bars for file operations"""
    
    print("📁 File Operations Progress")
    
    # Create sample files
    print("\n1. Creating sample files:")
    
    sample_files = []
    for i in tqdm(range(5), desc="Creating files"):
        filename = f"sample_file_{i}.txt"
        with open(filename, 'w') as f:
            # Write some content
            for line in range(100):
                f.write(f"Line {line} in file {i}\n")
        sample_files.append(filename)
        time.sleep(0.1)
    
    # File processing with size info
    print("\n2. Processing files with size info:")
    
    total_size = sum(os.path.getsize(f) for f in sample_files)
    
    with tqdm(total=total_size, desc="Processing", unit="B", unit_scale=True) as pbar:
        for filename in sample_files:
            file_size = os.path.getsize(filename)
            
            # Simulate processing file
            with open(filename, 'r') as f:
                for line in f:
                    pass  # Process line
            
            pbar.update(file_size)
            time.sleep(0.1)
    
    # File copying simulation
    print("\n3. File copying simulation:")
    
    def copy_file_with_progress(src, dst):
        """Simulate file copying with progress"""
        file_size = os.path.getsize(src)
        
        with tqdm(total=file_size, desc=f"Copying {os.path.basename(src)}", 
                 unit="B", unit_scale=True) as pbar:
            
            with open(src, 'rb') as fsrc, open(dst, 'wb') as fdst:
                chunk_size = 1024
                while True:
                    chunk = fsrc.read(chunk_size)
                    if not chunk:
                        break
                    fdst.write(chunk)
                    pbar.update(len(chunk))
                    time.sleep(0.01)  # Simulate I/O delay
    
    # Copy files
    for i, src_file in enumerate(sample_files):
        dst_file = f"copy_{i}.txt"
        copy_file_with_progress(src_file, dst_file)
    
    # Cleanup
    print("\n4. Cleaning up files:")
    all_files = sample_files + [f"copy_{i}.txt" for i in range(len(sample_files))]
    
    for filename in tqdm(all_files, desc="Cleaning up"):
        if os.path.exists(filename):
            os.remove(filename)
        time.sleep(0.05)
    
    print("   Cleanup completed")

file_operations_progress()
```

---

## 🌐 Integration Examples

### 🕷️ **Web Scraping Progress:**
```python
import requests
from urllib.parse import urljoin

def web_scraping_progress():
    """Progress bars for web scraping"""
    
    print("🕷️ Web Scraping Progress")
    
    # URLs to scrape
    base_url = "https://quotes.toscrape.com"
    urls_to_scrape = [
        f"{base_url}/page/{i}/" for i in range(1, 6)
    ]
    
    print("\n1. Scraping multiple pages:")
    
    all_quotes = []
    
    for url in tqdm(urls_to_scrape, desc="Scraping pages"):
        try:
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                # Simulate parsing
                time.sleep(0.2)  # Simulate processing time
                
                # In real scenario, you'd parse HTML here
                quotes_count = 10  # Simulated quotes per page
                all_quotes.extend([f"Quote {i}" for i in range(quotes_count)])
                
                # Update description with current status
                tqdm.write(f"✅ Scraped {url}: {quotes_count} quotes")
            else:
                tqdm.write(f"❌ Failed to scrape {url}: HTTP {response.status_code}")
                
        except Exception as e:
            tqdm.write(f"❌ Error scraping {url}: {e}")
    
    print(f"\n   Total quotes collected: {len(all_quotes)}")
    
    # Download simulation
    print("\n2. Download simulation:")
    
    download_urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2", 
        "https://httpbin.org/json",
        "https://httpbin.org/uuid",
        "https://httpbin.org/ip"
    ]
    
    def download_with_progress(url):
        """Download with progress tracking"""
        try:
            response = requests.get(url, stream=True, timeout=10)
            
            if response.status_code == 200:
                total_size = int(response.headers.get('content-length', 0))
                
                if total_size == 0:
                    # If no content-length, use indeterminate progress
                    with tqdm(desc=f"Downloading {url.split('/')[-1]}", 
                             unit="B", unit_scale=True) as pbar:
                        content = response.content
                        pbar.update(len(content))
                        return content
                else:
                    # Use determinate progress
                    with tqdm(total=total_size, desc=f"Downloading {url.split('/')[-1]}", 
                             unit="B", unit_scale=True) as pbar:
                        content = b""
                        for chunk in response.iter_content(chunk_size=1024):
                            if chunk:
                                content += chunk
                                pbar.update(len(chunk))
                        return content
            else:
                tqdm.write(f"❌ Download failed: HTTP {response.status_code}")
                return None
                
        except Exception as e:
            tqdm.write(f"❌ Download error: {e}")
            return None
    
    # Download all URLs
    downloaded_content = []
    for url in download_urls:
        content = download_with_progress(url)
        if content:
            downloaded_content.append(content)
    
    print(f"   Successfully downloaded: {len(downloaded_content)} files")

web_scraping_progress()
```

### 🤖 **Machine Learning Progress:**
```python
import random

def machine_learning_progress():
    """Progress bars for ML training simulation"""
    
    print("🤖 Machine Learning Progress")
    
    # Training simulation
    print("\n1. Model training simulation:")
    
    epochs = 5
    batches_per_epoch = 20
    
    for epoch in range(epochs):
        # Epoch progress
        epoch_pbar = tqdm(total=batches_per_epoch, 
                         desc=f"Epoch {epoch+1}/{epochs}", 
                         position=0)
        
        epoch_loss = 0
        epoch_acc = 0
        
        for batch in range(batches_per_epoch):
            # Simulate training batch
            time.sleep(0.05)
            
            # Simulate metrics
            batch_loss = random.uniform(0.1, 1.0) * (1 - epoch * 0.1)
            batch_acc = random.uniform(0.7, 1.0) * (1 + epoch * 0.05)
            
            epoch_loss += batch_loss
            epoch_acc += batch_acc
            
            # Update progress with metrics
            epoch_pbar.set_postfix({
                'loss': f'{batch_loss:.3f}',
                'acc': f'{batch_acc:.3f}'
            })
            
            epoch_pbar.update(1)
        
        # Final epoch metrics
        avg_loss = epoch_loss / batches_per_epoch
        avg_acc = epoch_acc / batches_per_epoch
        
        epoch_pbar.set_postfix({
            'avg_loss': f'{avg_loss:.3f}',
            'avg_acc': f'{avg_acc:.3f}'
        })
        
        epoch_pbar.close()
        
        # Validation
        print(f"   Epoch {epoch+1} - Loss: {avg_loss:.3f}, Acc: {avg_acc:.3f}")
    
    # Hyperparameter tuning simulation
    print("\n2. Hyperparameter tuning:")
    
    param_combinations = [
        {'lr': 0.001, 'batch_size': 32},
        {'lr': 0.01, 'batch_size': 32},
        {'lr': 0.001, 'batch_size': 64},
        {'lr': 0.01, 'batch_size': 64},
    ]
    
    best_score = 0
    best_params = None
    
    for params in tqdm(param_combinations, desc="Hyperparameter search"):
        # Simulate training with these parameters
        score = random.uniform(0.7, 0.95)
        
        if score > best_score:
            best_score = score
            best_params = params
        
        tqdm.write(f"   Params {params}: Score = {score:.3f}")
        time.sleep(0.2)
    
    print(f"\n   Best parameters: {best_params}")
    print(f"   Best score: {best_score:.3f}")
    
    # Data preprocessing simulation
    print("\n3. Data preprocessing:")
    
    preprocessing_steps = [
        ("Loading data", 100),
        ("Cleaning data", 80),
        ("Feature engineering", 60),
        ("Scaling features", 40),
        ("Splitting dataset", 20)
    ]
    
    for step_name, step_size in preprocessing_steps:
        for i in tqdm(range(step_size), desc=step_name):
            time.sleep(0.01)

machine_learning_progress()
```

---

## 🎉 সমাপনী

### ✅ **tqdm এ আপনি শিখেছেন:**
- Basic ও advanced progress bars
- Manual progress control
- Custom formatting ও styling
- Nested progress bars
- File operations progress tracking
- Web scraping integration
- Machine learning progress monitoring
- Threading ও parallel progress

### 🚀 **Next Steps:**
- **Rich** library দিয়ে advanced terminal UI
- **Click** দিয়ে CLI applications
- **Jupyter widgets** দিয়ে notebook progress
- **Custom progress** implementations

**tqdm mastery সম্পন্ন! 📊🇧🇩**
