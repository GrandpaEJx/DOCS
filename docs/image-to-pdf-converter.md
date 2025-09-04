# 🖼️ Image to PDF Converter - Python দিয়ে

## 📚 সূচিপত্র
1. [প্রয়োজনীয় লাইব্রেরি](#required-libraries)
2. [বেসিক Image to PDF](#basic-conversion)
3. [Multiple Images to PDF](#multiple-images)
4. [Advanced PDF Features](#advanced-features)
5. [Batch Processing](#batch-processing)
6. [GUI Application](#gui-application)

---

## 📦 প্রয়োজনীয় লাইব্রেরি {#required-libraries}

### ইনস্টলেশন:
```bash
# Core libraries
pip install Pillow reportlab

# Advanced features
pip install PyPDF2 img2pdf fpdf2

# GUI (optional)
pip install tkinter customtkinter

# Image processing
pip install opencv-python numpy
```

### Import statements:
```python
from PIL import Image, ImageEnhance, ImageFilter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.utils import ImageReader
import img2pdf
import os
import glob
from pathlib import Path
```

---

## 🎯 বেসিক Image to PDF {#basic-conversion}

### Method 1: PIL (Pillow) ব্যবহার করে
```python
from PIL import Image

def simple_img_to_pdf(image_path, output_path):
    """সবচেয়ে সহজ way - single image to PDF"""
    
    try:
        # Image open করুন
        image = Image.open(image_path)
        
        # RGB mode এ convert করুন (PDF এর জন্য প্রয়োজন)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # PDF হিসেবে save করুন
        image.save(output_path, "PDF")
        print(f"✅ PDF created: {output_path}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# Usage
simple_img_to_pdf("photo.jpg", "output.pdf")
```

### Method 2: img2pdf library (দ্রুততম)
```python
import img2pdf

def fast_img_to_pdf(image_path, output_path):
    """সবচেয়ে দ্রুত method"""
    
    try:
        with open(output_path, "wb") as f:
            f.write(img2pdf.convert(image_path))
        print(f"🚀 Fast PDF created: {output_path}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# Usage
fast_img_to_pdf("photo.jpg", "fast_output.pdf")
```

---

## 📚 Multiple Images to PDF {#multiple-images}

### একসাথে অনেক ছবি PDF করা:
```python
def multiple_images_to_pdf(image_folder, output_pdf):
    """Folder এর সব images একটি PDF এ"""
    
    # Supported formats
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')
    
    # Get all image files
    image_files = []
    for ext in supported_formats:
        image_files.extend(glob.glob(f"{image_folder}/*{ext}"))
        image_files.extend(glob.glob(f"{image_folder}/*{ext.upper()}"))
    
    if not image_files:
        print("❌ No images found!")
        return
    
    # Sort files (natural order)
    image_files.sort()
    
    print(f"📸 Found {len(image_files)} images")
    
    # Convert to PDF
    images = []
    for img_path in image_files:
        try:
            img = Image.open(img_path)
            
            # Convert to RGB if needed
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            images.append(img)
            print(f"✅ Processed: {os.path.basename(img_path)}")
            
        except Exception as e:
            print(f"❌ Error processing {img_path}: {e}")
            continue
    
    if images:
        # Save as PDF
        images[0].save(
            output_pdf, 
            "PDF", 
            resolution=100.0, 
            save_all=True, 
            append_images=images[1:]
        )
        print(f"🎉 PDF created with {len(images)} pages: {output_pdf}")
    
    # Close images to free memory
    for img in images:
        img.close()

# Usage
multiple_images_to_pdf("photos/", "album.pdf")
```

### Advanced Multiple Images with img2pdf:
```python
def advanced_multiple_to_pdf(image_folder, output_pdf, page_size="A4"):
    """Advanced multiple images to PDF with custom page size"""
    
    # Get image files
    image_files = []
    for ext in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']:
        pattern = f"{image_folder}/**/*{ext}"
        image_files.extend(glob.glob(pattern, recursive=True))
    
    image_files.sort()
    
    if not image_files:
        print("❌ No images found!")
        return
    
    print(f"📸 Processing {len(image_files)} images...")
    
    # Page size mapping
    page_sizes = {
        "A4": img2pdf.mm_to_pt(210, 297),
        "A3": img2pdf.mm_to_pt(297, 420),
        "Letter": img2pdf.inch_to_pt(8.5, 11)
    }
    
    layout_fun = img2pdf.get_layout_fun(page_sizes.get(page_size, page_sizes["A4"]))
    
    try:
        with open(output_pdf, "wb") as f:
            f.write(img2pdf.convert(image_files, layout_fun=layout_fun))
        
        print(f"🎉 Advanced PDF created: {output_pdf}")
        print(f"📄 Pages: {len(image_files)}")
        print(f"📏 Page size: {page_size}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# Usage
advanced_multiple_to_pdf("photos/", "advanced_album.pdf", "A4")
```

---

## 🎨 Advanced PDF Features {#advanced-features}

### Image Quality ও Compression:
```python
def create_compressed_pdf(image_paths, output_pdf, quality=85, max_width=1200):
    """Compressed PDF with quality control"""
    
    images = []
    
    for img_path in image_paths:
        try:
            img = Image.open(img_path)
            
            # Resize if too large
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            # Convert to RGB
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Enhance image (optional)
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(1.2)  # Slightly sharpen
            
            images.append(img)
            print(f"✅ Processed: {os.path.basename(img_path)} ({img.size})")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            continue
    
    if images:
        # Save with compression
        images[0].save(
            output_pdf,
            "PDF",
            resolution=100.0,
            save_all=True,
            append_images=images[1:],
            optimize=True,
            quality=quality
        )
        
        print(f"🗜️ Compressed PDF created: {output_pdf}")
        print(f"📊 Quality: {quality}%, Max width: {max_width}px")

# Usage
image_list = ["photo1.jpg", "photo2.png", "photo3.jpeg"]
create_compressed_pdf(image_list, "compressed.pdf", quality=75, max_width=1000)
```

### PDF with Metadata ও Watermark:
```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import Color

def create_pdf_with_metadata(image_paths, output_pdf, title="My Album", author="Python Script"):
    """PDF with custom metadata and watermark"""
    
    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4
    
    # Set metadata
    c.setTitle(title)
    c.setAuthor(author)
    c.setSubject("Images converted to PDF")
    c.setCreator("Python PIL + ReportLab")
    
    for i, img_path in enumerate(image_paths):
        try:
            img = Image.open(img_path)
            
            # Calculate image position (center on page)
            img_width, img_height = img.size
            aspect_ratio = img_height / img_width
            
            # Fit image to page with margin
            margin = 50
            max_width = width - 2 * margin
            max_height = height - 2 * margin
            
            if img_width > max_width:
                img_width = max_width
                img_height = img_width * aspect_ratio
            
            if img_height > max_height:
                img_height = max_height
                img_width = img_height / aspect_ratio
            
            # Center image
            x = (width - img_width) / 2
            y = (height - img_height) / 2
            
            # Draw image
            c.drawImage(img_path, x, y, width=img_width, height=img_height)
            
            # Add watermark
            c.setFillColor(Color(0, 0, 0, alpha=0.1))
            c.setFont("Helvetica", 20)
            c.drawCentredText(width/2, 30, f"Page {i+1} - {title}")
            
            # Add page number
            c.setFillColor(Color(0, 0, 0, alpha=0.5))
            c.setFont("Helvetica", 10)
            c.drawRightString(width-20, 20, f"{i+1}/{len(image_paths)}")
            
            c.showPage()  # New page
            print(f"✅ Added page {i+1}: {os.path.basename(img_path)}")
            
        except Exception as e:
            print(f"❌ Error processing {img_path}: {e}")
            continue
    
    c.save()
    print(f"📖 PDF with metadata created: {output_pdf}")

# Usage
images = ["photo1.jpg", "photo2.png", "photo3.jpeg"]
create_pdf_with_metadata(images, "album_with_metadata.pdf", "My Photo Album", "John Doe")
```

---

## ⚡ Batch Processing {#batch-processing}

### Folder Structure অনুযায়ী PDF তৈরি:
```python
def batch_folder_to_pdf(root_folder):
    """প্রতিটি subfolder এর জন্য আলাদা PDF"""
    
    root_path = Path(root_folder)
    
    for folder_path in root_path.iterdir():
        if folder_path.is_dir():
            print(f"📁 Processing folder: {folder_path.name}")
            
            # Get images in this folder
            image_files = []
            for ext in ['.jpg', '.jpeg', '.png', '.bmp']:
                image_files.extend(folder_path.glob(f"*{ext}"))
                image_files.extend(folder_path.glob(f"*{ext.upper()}"))
            
            if image_files:
                # Sort files
                image_files.sort()
                
                # Create PDF name
                pdf_name = f"{folder_path.name}.pdf"
                pdf_path = root_path / pdf_name
                
                # Convert to PDF
                try:
                    image_paths = [str(img) for img in image_files]
                    
                    with open(pdf_path, "wb") as f:
                        f.write(img2pdf.convert(image_paths))
                    
                    print(f"✅ Created: {pdf_name} ({len(image_files)} images)")
                    
                except Exception as e:
                    print(f"❌ Error creating {pdf_name}: {e}")
            else:
                print(f"⚠️ No images found in {folder_path.name}")

# Usage
batch_folder_to_pdf("photo_albums/")
```

### Multi-threading দিয়ে দ্রুত Processing:
```python
import concurrent.futures
import threading

def process_single_folder(folder_info):
    """Single folder process করার function"""
    folder_path, output_dir = folder_info
    
    try:
        # Get images
        image_files = []
        for ext in ['.jpg', '.jpeg', '.png', '.bmp']:
            image_files.extend(folder_path.glob(f"*{ext}"))
        
        if not image_files:
            return f"⚠️ No images in {folder_path.name}"
        
        image_files.sort()
        
        # Create PDF
        pdf_name = f"{folder_path.name}.pdf"
        pdf_path = output_dir / pdf_name
        
        image_paths = [str(img) for img in image_files]
        
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(image_paths))
        
        return f"✅ {pdf_name}: {len(image_files)} images"
        
    except Exception as e:
        return f"❌ Error in {folder_path.name}: {e}"

def fast_batch_processing(root_folder, max_workers=4):
    """Multi-threading দিয়ে দ্রুত batch processing"""
    
    root_path = Path(root_folder)
    output_dir = root_path / "generated_pdfs"
    output_dir.mkdir(exist_ok=True)
    
    # Get all folders
    folders = [folder for folder in root_path.iterdir() if folder.is_dir() and folder != output_dir]
    folder_info = [(folder, output_dir) for folder in folders]
    
    print(f"🚀 Processing {len(folders)} folders with {max_workers} threads...")
    
    # Process with threading
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(process_single_folder, folder_info))
    
    # Print results
    for result in results:
        print(result)
    
    print(f"🎉 Batch processing complete! Check: {output_dir}")

# Usage
fast_batch_processing("photo_albums/", max_workers=6)
```
