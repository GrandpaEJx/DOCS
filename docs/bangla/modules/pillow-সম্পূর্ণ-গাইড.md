# 🖼️ Pillow - সম্পূর্ণ বাংলা গাইড

## 🌟 Pillow কি?

Pillow (PIL - Python Imaging Library) হলো Python এর সবচেয়ে জনপ্রিয় **image processing library** যা দিয়ে আপনি images নিয়ে সব ধরনের কাজ করতে পারেন।

### 🎯 **মূল বৈশিষ্ট্য:**
- ✅ **Multiple formats** - JPEG, PNG, GIF, BMP, TIFF support
- ✅ **Image manipulation** - Resize, crop, rotate, flip
- ✅ **Filters ও effects** - Blur, sharpen, enhance
- ✅ **Drawing capabilities** - Text, shapes, graphics
- ✅ **Color space conversion** - RGB, CMYK, HSV
- ✅ **Batch processing** - Multiple images at once

---

## 🚀 Installation ও Setup

### 📦 **Installation:**
```bash
# Pillow install
pip install Pillow>=10.0.0

# Verify installation
python -c "from PIL import Image; print('Pillow installed successfully!')"
```

### ✅ **Installation Verify:**
```python
# test_pillow.py
from PIL import Image, ImageDraw, ImageFont
import os

def test_pillow():
    print("🧪 Pillow installation test...")
    
    # Create a simple image
    img = Image.new('RGB', (200, 100), color='lightblue')
    
    # Add text
    draw = ImageDraw.Draw(img)
    draw.text((10, 40), "Hello Pillow!", fill='black')
    
    # Save image
    img.save('test_image.png')
    print("✅ Test image created: test_image.png")
    
    # Load and display info
    loaded_img = Image.open('test_image.png')
    print(f"✅ Image size: {loaded_img.size}")
    print(f"✅ Image mode: {loaded_img.mode}")
    print(f"✅ Image format: {loaded_img.format}")
    
    print("🎉 Pillow working perfectly!")

test_pillow()
```

---

## 📁 Image Loading ও Saving

### 📂 **Basic Image Operations:**
```python
from PIL import Image
import os

def basic_image_operations():
    """Basic image loading and saving"""
    
    # Create a sample image first
    sample_img = Image.new('RGB', (300, 200), color='skyblue')
    sample_img.save('sample.jpg', 'JPEG')
    
    # Load image
    img = Image.open('sample.jpg')
    
    print(f"📊 Image Information:")
    print(f"Size: {img.size}")  # (width, height)
    print(f"Mode: {img.mode}")  # RGB, RGBA, L, etc.
    print(f"Format: {img.format}")  # JPEG, PNG, etc.
    
    # Image properties
    width, height = img.size
    print(f"Width: {width}, Height: {height}")
    print(f"Has transparency: {img.mode in ('RGBA', 'LA')}")
    
    # Save in different formats
    formats = {
        'PNG': 'sample.png',
        'BMP': 'sample.bmp',
        'GIF': 'sample.gif'
    }
    
    for format_name, filename in formats.items():
        if format_name == 'GIF' and img.mode == 'RGB':
            # Convert to palette mode for GIF
            img_converted = img.convert('P')
            img_converted.save(filename, format_name)
        else:
            img.save(filename, format_name)
        
        print(f"✅ Saved as {filename}")
    
    # Save with quality settings (JPEG)
    img.save('sample_high_quality.jpg', 'JPEG', quality=95)
    img.save('sample_low_quality.jpg', 'JPEG', quality=30)
    
    print("✅ Quality variants saved")
    
    # Get file sizes
    for filename in ['sample_high_quality.jpg', 'sample_low_quality.jpg']:
        size = os.path.getsize(filename)
        print(f"{filename}: {size} bytes")

basic_image_operations()
```

### 🎨 **Creating Images:**
```python
from PIL import Image, ImageDraw, ImageFont

def create_images():
    """Creating images from scratch"""
    
    # Create solid color image
    solid_img = Image.new('RGB', (400, 300), color='red')
    solid_img.save('solid_red.png')
    
    # Create gradient image
    gradient_img = Image.new('RGB', (400, 300))
    pixels = []
    
    for y in range(300):
        for x in range(400):
            # Create horizontal gradient
            red = int(255 * x / 400)
            green = int(255 * y / 300)
            blue = 128
            pixels.append((red, green, blue))
    
    gradient_img.putdata(pixels)
    gradient_img.save('gradient.png')
    
    # Create image with drawing
    canvas = Image.new('RGB', (500, 400), color='white')
    draw = ImageDraw.Draw(canvas)
    
    # Draw shapes
    draw.rectangle([50, 50, 150, 100], fill='blue', outline='black', width=2)
    draw.ellipse([200, 50, 300, 150], fill='green', outline='red', width=3)
    draw.polygon([(350, 50), (450, 100), (400, 150), (350, 100)], 
                fill='yellow', outline='purple', width=2)
    
    # Draw lines
    draw.line([(50, 200), (450, 200)], fill='black', width=5)
    draw.line([(50, 220), (450, 280)], fill='red', width=3)
    
    # Add text
    try:
        # Try to use a system font
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    draw.text((50, 320), "Created with Pillow!", fill='black', font=font)
    
    canvas.save('drawing_example.png')
    print("✅ Created images: solid_red.png, gradient.png, drawing_example.png")

create_images()
```

---

## 🔧 Image Manipulation

### ✂️ **Resize, Crop, Rotate:**
```python
def image_manipulation():
    """Image manipulation operations"""
    
    # Create or load a sample image
    original = Image.new('RGB', (400, 300))
    # Add some pattern
    pixels = []
    for y in range(300):
        for x in range(400):
            r = (x * 255) // 400
            g = (y * 255) // 300
            b = ((x + y) * 255) // 700
            pixels.append((r, g, b))
    original.putdata(pixels)
    original.save('original.png')
    
    print(f"📊 Original image size: {original.size}")
    
    # Resize operations
    # Resize to specific size
    resized = original.resize((200, 150))
    resized.save('resized.png')
    print(f"✅ Resized to: {resized.size}")
    
    # Resize with aspect ratio maintained
    original.thumbnail((300, 300))  # Modifies in-place
    original.save('thumbnail.png')
    print(f"✅ Thumbnail size: {original.size}")
    
    # Reload original for other operations
    original = Image.open('original.png')
    
    # Crop operations
    # Crop rectangle (left, top, right, bottom)
    cropped = original.crop((100, 75, 300, 225))
    cropped.save('cropped.png')
    print(f"✅ Cropped size: {cropped.size}")
    
    # Rotation
    rotated_90 = original.rotate(90, expand=True)
    rotated_45 = original.rotate(45, expand=True, fillcolor='white')
    
    rotated_90.save('rotated_90.png')
    rotated_45.save('rotated_45.png')
    print(f"✅ Rotated 90°: {rotated_90.size}")
    print(f"✅ Rotated 45°: {rotated_45.size}")
    
    # Flip operations
    flipped_horizontal = original.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_vertical = original.transpose(Image.FLIP_TOP_BOTTOM)
    
    flipped_horizontal.save('flipped_h.png')
    flipped_vertical.save('flipped_v.png')
    print("✅ Flipped images created")
    
    # Advanced transformations
    # Perspective transform (requires specific points)
    width, height = original.size
    
    # Define transformation matrix for slight perspective
    transform_matrix = [1, 0.1, 0, 0, 1, 0]  # Slight skew
    transformed = original.transform(
        (width, height), 
        Image.AFFINE, 
        transform_matrix,
        fillcolor='white'
    )
    transformed.save('transformed.png')
    print("✅ Transformed image created")

image_manipulation()
```

### 🎨 **Filters ও Effects:**
```python
from PIL import ImageFilter, ImageEnhance

def filters_and_effects():
    """Apply filters and effects"""
    
    # Create a sample image with some detail
    original = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(original)
    
    # Add some shapes for filter demonstration
    for i in range(0, 300, 30):
        draw.rectangle([i, i, i+20, i+20], fill=(i, 255-i, 128))
        draw.ellipse([i+150, i, i+170, i+20], fill=(255-i, i, 200))
    
    original.save('filter_test_original.png')
    
    # Basic filters
    filters = {
        'blur': ImageFilter.BLUR,
        'detail': ImageFilter.DETAIL,
        'edge_enhance': ImageFilter.EDGE_ENHANCE,
        'emboss': ImageFilter.EMBOSS,
        'find_edges': ImageFilter.FIND_EDGES,
        'sharpen': ImageFilter.SHARPEN,
        'smooth': ImageFilter.SMOOTH
    }
    
    print("🎨 Applying filters:")
    for name, filter_type in filters.items():
        filtered = original.filter(filter_type)
        filtered.save(f'filter_{name}.png')
        print(f"✅ Applied {name} filter")
    
    # Gaussian blur with radius
    gaussian_blur = original.filter(ImageFilter.GaussianBlur(radius=3))
    gaussian_blur.save('filter_gaussian_blur.png')
    
    # Unsharp mask
    unsharp = original.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    unsharp.save('filter_unsharp.png')
    
    # Enhancement operations
    print("\n✨ Applying enhancements:")
    
    # Brightness
    brightness_enhancer = ImageEnhance.Brightness(original)
    bright = brightness_enhancer.enhance(1.5)  # 1.5x brighter
    dark = brightness_enhancer.enhance(0.5)    # 0.5x darker
    
    bright.save('enhanced_bright.png')
    dark.save('enhanced_dark.png')
    
    # Contrast
    contrast_enhancer = ImageEnhance.Contrast(original)
    high_contrast = contrast_enhancer.enhance(2.0)
    low_contrast = contrast_enhancer.enhance(0.5)
    
    high_contrast.save('enhanced_high_contrast.png')
    low_contrast.save('enhanced_low_contrast.png')
    
    # Color saturation
    color_enhancer = ImageEnhance.Color(original)
    saturated = color_enhancer.enhance(2.0)
    desaturated = color_enhancer.enhance(0.2)
    
    saturated.save('enhanced_saturated.png')
    desaturated.save('enhanced_desaturated.png')
    
    # Sharpness
    sharpness_enhancer = ImageEnhance.Sharpness(original)
    sharp = sharpness_enhancer.enhance(2.0)
    soft = sharpness_enhancer.enhance(0.5)
    
    sharp.save('enhanced_sharp.png')
    soft.save('enhanced_soft.png')
    
    print("✅ All enhancements applied")

filters_and_effects()
```

---

## 🎨 Drawing ও Text

### ✏️ **Advanced Drawing:**
```python
def advanced_drawing():
    """Advanced drawing operations"""
    
    # Create canvas
    canvas = Image.new('RGB', (600, 400), 'white')
    draw = ImageDraw.Draw(canvas)
    
    # Draw various shapes with different styles
    print("🎨 Drawing shapes and text...")
    
    # Rectangles with different fills
    draw.rectangle([50, 50, 150, 100], fill='red', outline='black', width=2)
    draw.rectangle([170, 50, 270, 100], fill=None, outline='blue', width=3)
    
    # Circles and ellipses
    draw.ellipse([50, 120, 150, 170], fill='green', outline='darkgreen', width=2)
    draw.ellipse([170, 120, 270, 220], fill='yellow', outline='orange', width=4)
    
    # Polygons
    triangle = [(320, 50), (370, 100), (270, 100)]
    draw.polygon(triangle, fill='purple', outline='black', width=2)
    
    pentagon = [(400, 50), (450, 70), (440, 120), (360, 120), (350, 70)]
    draw.polygon(pentagon, fill='cyan', outline='navy', width=2)
    
    # Lines and curves
    draw.line([(50, 200), (550, 200)], fill='black', width=3)
    draw.line([(50, 220), (150, 180), (250, 220), (350, 180), (450, 220)], 
              fill='red', width=2)
    
    # Arc
    draw.arc([480, 120, 580, 220], start=0, end=180, fill='magenta', width=3)
    
    # Text with different fonts and sizes
    try:
        # Try different font sizes
        small_font = ImageFont.truetype("arial.ttf", 16)
        medium_font = ImageFont.truetype("arial.ttf", 24)
        large_font = ImageFont.truetype("arial.ttf", 32)
    except:
        # Fallback to default
        small_font = medium_font = large_font = ImageFont.load_default()
    
    # Text with different alignments
    draw.text((50, 250), "Small Text", fill='black', font=small_font)
    draw.text((50, 280), "Medium Text", fill='blue', font=medium_font)
    draw.text((50, 320), "Large Text", fill='red', font=large_font)
    
    # Multiline text
    multiline_text = "This is a\nmultiline text\nexample"
    draw.multiline_text((300, 250), multiline_text, fill='green', 
                       font=medium_font, align='center')
    
    # Text with background
    text = "Text with BG"
    bbox = draw.textbbox((400, 320), text, font=medium_font)
    draw.rectangle(bbox, fill='yellow', outline='black')
    draw.text((400, 320), text, fill='black', font=medium_font)
    
    canvas.save('advanced_drawing.png')
    print("✅ Advanced drawing saved as advanced_drawing.png")

advanced_drawing()
```

### 🖼️ **Image Composition:**
```python
def image_composition():
    """Compose multiple images together"""
    
    # Create base images
    bg = Image.new('RGB', (400, 300), 'lightblue')
    
    # Create foreground elements
    circle = Image.new('RGBA', (100, 100), (0, 0, 0, 0))  # Transparent
    draw = ImageDraw.Draw(circle)
    draw.ellipse([10, 10, 90, 90], fill='red')
    
    square = Image.new('RGBA', (80, 80), (0, 0, 0, 0))
    draw = ImageDraw.Draw(square)
    draw.rectangle([10, 10, 70, 70], fill='green')
    
    # Paste with transparency
    bg.paste(circle, (50, 50), circle)  # Third parameter is mask
    bg.paste(square, (200, 100), square)
    
    # Create a watermark
    watermark = Image.new('RGBA', (200, 50), (0, 0, 0, 0))
    draw = ImageDraw.Draw(watermark)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
    
    draw.text((10, 15), "WATERMARK", fill=(255, 255, 255, 128), font=font)
    
    # Paste watermark
    bg.paste(watermark, (100, 200), watermark)
    
    bg.save('composition.png')
    print("✅ Image composition saved")
    
    # Blend two images
    img1 = Image.new('RGB', (200, 200), 'red')
    img2 = Image.new('RGB', (200, 200), 'blue')
    
    # Add some patterns
    draw1 = ImageDraw.Draw(img1)
    draw2 = ImageDraw.Draw(img2)
    
    for i in range(0, 200, 20):
        draw1.line([(i, 0), (i, 200)], fill='darkred', width=2)
        draw2.ellipse([i, i, i+40, i+40], fill='lightblue')
    
    # Blend images
    blended = Image.blend(img1, img2, alpha=0.5)  # 50% blend
    blended.save('blended.png')
    
    # Composite with mask
    mask = Image.new('L', (200, 200), 0)  # Black mask
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse([50, 50, 150, 150], fill=255)  # White circle
    
    composite = Image.composite(img1, img2, mask)
    composite.save('composite.png')
    
    print("✅ Blended and composite images created")

image_composition()
```

---

## 🔄 Batch Processing

### 📁 **Process Multiple Images:**
```python
import os
import glob

def batch_processing():
    """Batch process multiple images"""
    
    # Create sample images for batch processing
    sample_images = []
    for i in range(5):
        img = Image.new('RGB', (200, 150))
        # Create different colored images
        color = (i * 50, (4-i) * 50, 100)
        pixels = [color] * (200 * 150)
        img.putdata(pixels)
        
        filename = f'batch_sample_{i}.png'
        img.save(filename)
        sample_images.append(filename)
    
    print(f"📁 Created {len(sample_images)} sample images")
    
    # Batch resize
    def batch_resize(input_pattern, output_dir, new_size):
        """Resize all images matching pattern"""
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        files = glob.glob(input_pattern)
        processed = 0
        
        for file_path in files:
            try:
                with Image.open(file_path) as img:
                    # Resize maintaining aspect ratio
                    img.thumbnail(new_size, Image.Resampling.LANCZOS)
                    
                    # Save to output directory
                    filename = os.path.basename(file_path)
                    output_path = os.path.join(output_dir, f'resized_{filename}')
                    img.save(output_path)
                    
                    processed += 1
                    print(f"✅ Resized: {filename}")
                    
            except Exception as e:
                print(f"❌ Error processing {file_path}: {e}")
        
        return processed
    
    # Batch convert format
    def batch_convert(input_pattern, output_format, quality=85):
        """Convert all images to specified format"""
        
        files = glob.glob(input_pattern)
        converted = 0
        
        for file_path in files:
            try:
                with Image.open(file_path) as img:
                    # Convert mode if necessary
                    if output_format.upper() == 'JPEG' and img.mode in ('RGBA', 'LA'):
                        # Convert to RGB for JPEG
                        rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                        rgb_img.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                        img = rgb_img
                    
                    # Generate output filename
                    base_name = os.path.splitext(os.path.basename(file_path))[0]
                    output_path = f'{base_name}_converted.{output_format.lower()}'
                    
                    # Save with quality setting for JPEG
                    if output_format.upper() == 'JPEG':
                        img.save(output_path, output_format, quality=quality)
                    else:
                        img.save(output_path, output_format)
                    
                    converted += 1
                    print(f"✅ Converted: {output_path}")
                    
            except Exception as e:
                print(f"❌ Error converting {file_path}: {e}")
        
        return converted
    
    # Batch apply filter
    def batch_filter(input_pattern, filter_type, output_suffix='_filtered'):
        """Apply filter to all images"""
        
        files = glob.glob(input_pattern)
        filtered = 0
        
        for file_path in files:
            try:
                with Image.open(file_path) as img:
                    # Apply filter
                    filtered_img = img.filter(filter_type)
                    
                    # Generate output filename
                    base_name = os.path.splitext(file_path)[0]
                    ext = os.path.splitext(file_path)[1]
                    output_path = f'{base_name}{output_suffix}{ext}'
                    
                    filtered_img.save(output_path)
                    filtered += 1
                    print(f"✅ Filtered: {os.path.basename(output_path)}")
                    
            except Exception as e:
                print(f"❌ Error filtering {file_path}: {e}")
        
        return filtered
    
    # Execute batch operations
    print("\n🔄 Batch Processing Operations:")
    
    # Resize all sample images
    resized_count = batch_resize('batch_sample_*.png', 'resized_images', (100, 100))
    print(f"📏 Resized {resized_count} images")
    
    # Convert to JPEG
    converted_count = batch_convert('batch_sample_*.png', 'JPEG', quality=90)
    print(f"🔄 Converted {converted_count} images to JPEG")
    
    # Apply blur filter
    filtered_count = batch_filter('batch_sample_*.png', ImageFilter.BLUR)
    print(f"🎨 Applied filter to {filtered_count} images")
    
    # Cleanup sample files
    for filename in sample_images:
        if os.path.exists(filename):
            os.remove(filename)
    
    print("✅ Batch processing completed")

batch_processing()
```

---

## 📊 Image Analysis

### 🔍 **Image Information ও Statistics:**
```python
def image_analysis():
    """Analyze image properties and statistics"""
    
    # Create a sample image with varied content
    img = Image.new('RGB', (300, 200))
    draw = ImageDraw.Draw(img)
    
    # Add varied content for analysis
    draw.rectangle([0, 0, 100, 200], fill='red')
    draw.rectangle([100, 0, 200, 200], fill='green')
    draw.rectangle([200, 0, 300, 200], fill='blue')
    
    # Add some noise/variation
    import random
    for _ in range(1000):
        x = random.randint(0, 299)
        y = random.randint(0, 199)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.point((x, y), fill=color)
    
    img.save('analysis_sample.png')
    
    print("📊 Image Analysis:")
    print(f"Size: {img.size}")
    print(f"Mode: {img.mode}")
    print(f"Bands: {img.getbands()}")
    
    # Get image statistics
    stat = img.histogram()
    print(f"Histogram length: {len(stat)}")  # 256 * number of bands
    
    # Analyze each color channel
    if img.mode == 'RGB':
        r, g, b = img.split()
        
        channels = {'Red': r, 'Green': g, 'Blue': b}
        
        for name, channel in channels.items():
            # Get extrema (min, max)
            extrema = channel.getextrema()
            print(f"{name} channel - Min: {extrema[0]}, Max: {extrema[1]}")
            
            # Get histogram for this channel
            hist = channel.histogram()
            
            # Calculate basic statistics
            total_pixels = sum(hist)
            weighted_sum = sum(i * count for i, count in enumerate(hist))
            mean = weighted_sum / total_pixels if total_pixels > 0 else 0
            
            print(f"{name} channel - Mean: {mean:.2f}")
    
    # Bounding box of non-zero pixels
    bbox = img.getbbox()
    if bbox:
        print(f"Bounding box: {bbox}")
    
    # Convert to different modes for analysis
    grayscale = img.convert('L')
    grayscale.save('analysis_grayscale.png')
    
    # Analyze grayscale
    gray_extrema = grayscale.getextrema()
    print(f"Grayscale - Min: {gray_extrema[0]}, Max: {gray_extrema[1]}")
    
    # Get pixel access for detailed analysis
    pixels = list(img.getdata())
    print(f"Total pixels: {len(pixels)}")
    print(f"First 5 pixels: {pixels[:5]}")
    
    # Color analysis
    unique_colors = set(pixels)
    print(f"Unique colors: {len(unique_colors)}")
    
    # Most common colors
    from collections import Counter
    color_counts = Counter(pixels)
    most_common = color_counts.most_common(5)
    
    print("Most common colors:")
    for color, count in most_common:
        print(f"  {color}: {count} pixels ({count/len(pixels)*100:.1f}%)")

image_analysis()
```

---

## 🎉 সমাপনী

### ✅ **Pillow এ আপনি শিখেছেন:**
- Image loading, saving ও format conversion
- Image manipulation (resize, crop, rotate, flip)
- Filters ও effects application
- Drawing shapes, text ও graphics
- Image composition ও blending
- Batch processing techniques
- Image analysis ও statistics

### 🚀 **Next Steps:**
- **OpenCV** দিয়ে advanced computer vision
- **NumPy** integration for numerical image processing
- **Matplotlib** দিয়ে image visualization
- **Web frameworks** integration for image APIs

**Pillow mastery সম্পন্ন! 🖼️🇧🇩**
