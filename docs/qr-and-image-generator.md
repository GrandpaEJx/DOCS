# 🎨 QR Code ও Image Generator - Python দিয়ে

## 📚 সূচিপত্র
1. [QR Code Generator](#qr-generator)
2. [Advanced QR Features](#advanced-qr)
3. [Image Generator](#image-generator)
4. [AI Image Generation](#ai-image-gen)
5. [Batch Processing](#batch-processing)
6. [GUI Applications](#gui-apps)

---

## 🔲 QR Code Generator {#qr-generator}

### প্রয়োজনীয় Libraries:
```bash
# QR Code generation
pip install qrcode[pil] pillow

# Advanced features
pip install segno colorama

# Image processing
pip install opencv-python numpy

# GUI (optional)
pip install tkinter customtkinter
```

### Basic QR Code Generation:
```python
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

def generate_basic_qr(data, filename="qr_code.png"):
    """সবচেয়ে সহজ QR code generation"""
    
    # QR code instance তৈরি
    qr = qrcode.QRCode(
        version=1,  # 1-40, controls size
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # L, M, Q, H
        box_size=10,  # pixels per box
        border=4,  # minimum border size
    )
    
    # Data add করুন
    qr.add_data(data)
    qr.make(fit=True)
    
    # Image তৈরি করুন
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save করুন
    img.save(filename)
    print(f"✅ QR Code saved: {filename}")
    
    return filename

# Usage
generate_basic_qr("https://github.com/your-repo", "github_qr.png")
generate_basic_qr("আমার নাম জন ডো", "bangla_text_qr.png")
```

### Advanced QR Code with Custom Design:
```python
def generate_custom_qr(data, filename="custom_qr.png", 
                      fill_color="black", back_color="white", 
                      logo_path=None, size_factor=10):
    """Custom design সহ QR code"""
    
    # QR code তৈরি
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for logo
        box_size=size_factor,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    # Image তৈরি
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    # Logo add করা (যদি থাকে)
    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path)
        
        # Logo size calculate করা (QR এর 10% এর বেশি না)
        qr_width, qr_height = img.size
        logo_size = min(qr_width, qr_height) // 5
        
        # Logo resize করা
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # Logo position (center)
        logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
        
        # Logo paste করা
        img.paste(logo, logo_pos)
    
    # Save করা
    img.save(filename)
    print(f"✅ Custom QR Code saved: {filename}")
    
    return filename

# Usage
generate_custom_qr(
    "https://example.com", 
    "custom_qr.png",
    fill_color="navy",
    back_color="lightblue",
    logo_path="logo.png"
)
```

### Batch QR Code Generation:
```python
def generate_batch_qr(data_list, output_folder="qr_codes"):
    """Multiple QR codes একসাথে তৈরি"""
    
    os.makedirs(output_folder, exist_ok=True)
    
    generated_files = []
    
    for i, data in enumerate(data_list):
        try:
            # Filename তৈরি
            if isinstance(data, dict):
                filename = f"{data.get('name', f'qr_{i+1}')}.png"
                qr_data = data.get('data', str(data))
            else:
                filename = f"qr_{i+1}.png"
                qr_data = str(data)
            
            filepath = os.path.join(output_folder, filename)
            
            # QR code তৈরি
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=8,
                border=4,
            )
            
            qr.add_data(qr_data)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(filepath)
            
            generated_files.append(filepath)
            print(f"✅ {i+1}/{len(data_list)}: {filename}")
            
        except Exception as e:
            print(f"❌ Error generating QR {i+1}: {e}")
            continue
    
    print(f"🎉 Generated {len(generated_files)} QR codes in {output_folder}")
    return generated_files

# Usage
qr_data = [
    {"name": "website", "data": "https://example.com"},
    {"name": "email", "data": "mailto:john@example.com"},
    {"name": "phone", "data": "tel:+8801712345678"},
    {"name": "wifi", "data": "WIFI:T:WPA;S:MyNetwork;P:password123;;"},
    "Just plain text QR code"
]

generate_batch_qr(qr_data)
```

---

## 🎨 Advanced QR Features {#advanced-qr}

### QR Code with Text Label:
```python
def generate_qr_with_label(data, label_text, filename="labeled_qr.png"):
    """QR code এর নিচে text label সহ"""
    
    # QR code তৈরি
    qr = qrcode.QRCode(version=1, box_size=8, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Font load করা (system font)
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    # Text size measure করা
    draw = ImageDraw.Draw(qr_img)
    text_bbox = draw.textbbox((0, 0), label_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    # New image তৈরি (QR + text space)
    qr_width, qr_height = qr_img.size
    total_height = qr_height + text_height + 20  # 20px padding
    
    final_img = Image.new('RGB', (qr_width, total_height), 'white')
    
    # QR code paste করা
    final_img.paste(qr_img, (0, 0))
    
    # Text draw করা
    draw = ImageDraw.Draw(final_img)
    text_x = (qr_width - text_width) // 2
    text_y = qr_height + 10
    
    draw.text((text_x, text_y), label_text, fill="black", font=font)
    
    # Save করা
    final_img.save(filename)
    print(f"✅ Labeled QR Code saved: {filename}")
    
    return filename

# Usage
generate_qr_with_label("https://github.com", "Visit My GitHub", "github_labeled.png")
```

### Colorful QR Codes:
```python
def generate_colorful_qr(data, filename="colorful_qr.png"):
    """রঙিন QR code তৈরি"""
    
    import random
    
    # Color combinations
    color_schemes = [
        {"fill": "#FF6B6B", "back": "#FFE5E5"},  # Red theme
        {"fill": "#4ECDC4", "back": "#E8F8F7"},  # Teal theme
        {"fill": "#45B7D1", "back": "#E3F2FD"},  # Blue theme
        {"fill": "#96CEB4", "back": "#F0F8F4"},  # Green theme
        {"fill": "#FFEAA7", "back": "#FFF9E6"},  # Yellow theme
        {"fill": "#DDA0DD", "back": "#F5F0F5"},  # Purple theme
    ]
    
    # Random color scheme select করা
    colors = random.choice(color_schemes)
    
    # QR code তৈরি
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    # Colorful image তৈরি
    img = qr.make_image(fill_color=colors["fill"], back_color=colors["back"])
    
    # Save করা
    img.save(filename)
    print(f"✅ Colorful QR Code saved: {filename} (Colors: {colors})")
    
    return filename

# Usage
generate_colorful_qr("https://example.com", "colorful_qr.png")
```

### QR Code Reader/Decoder:
```python
from pyzbar import pyzbar
import cv2

def read_qr_code(image_path):
    """QR code থেকে data read করা"""
    
    try:
        # Image load করা
        image = cv2.imread(image_path)
        
        # QR codes detect করা
        qr_codes = pyzbar.decode(image)
        
        if not qr_codes:
            print("❌ No QR code found in image")
            return None
        
        results = []
        for qr_code in qr_codes:
            # Data extract করা
            qr_data = qr_code.data.decode('utf-8')
            qr_type = qr_code.type
            
            # Bounding box
            (x, y, w, h) = qr_code.rect
            
            result = {
                'data': qr_data,
                'type': qr_type,
                'position': (x, y, w, h)
            }
            
            results.append(result)
            print(f"✅ QR Code found: {qr_data}")
        
        return results
        
    except Exception as e:
        print(f"❌ Error reading QR code: {e}")
        return None

# Usage (requires: pip install pyzbar opencv-python)
# qr_data = read_qr_code("qr_code.png")
```

---

## 🖼️ Image Generator {#image-generator}

### Text to Image Generator:
```python
from PIL import Image, ImageDraw, ImageFont
import textwrap

def generate_text_image(text, filename="text_image.png", 
                       width=800, height=600, 
                       bg_color="white", text_color="black",
                       font_size=24):
    """Text থেকে image তৈরি"""
    
    # Image তৈরি
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Font load করা
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # Text wrap করা (long text এর জন্য)
    max_chars_per_line = width // (font_size // 2)
    wrapped_text = textwrap.fill(text, width=max_chars_per_line)
    
    # Text position calculate করা
    text_bbox = draw.textbbox((0, 0), wrapped_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Text draw করা
    draw.text((x, y), wrapped_text, fill=text_color, font=font)
    
    # Save করা
    img.save(filename)
    print(f"✅ Text image saved: {filename}")
    
    return filename

# Usage
generate_text_image(
    "এটি একটি বাংলা টেক্সট ইমেজ। Python দিয়ে তৈরি করা হয়েছে।",
    "bangla_text.png",
    width=600,
    height=400,
    bg_color="lightblue",
    text_color="darkblue",
    font_size=20
)
```

### Gradient Background Generator:
```python
import numpy as np

def generate_gradient_image(width=800, height=600, 
                          color1=(255, 0, 0), color2=(0, 0, 255),
                          direction="horizontal", filename="gradient.png"):
    """Gradient background image তৈরি"""
    
    # Create arrays for RGB channels
    if direction == "horizontal":
        # Horizontal gradient
        r = np.linspace(color1[0], color2[0], width).astype(int)
        g = np.linspace(color1[1], color2[1], width).astype(int)
        b = np.linspace(color1[2], color2[2], width).astype(int)
        
        # Create image array
        img_array = np.zeros((height, width, 3), dtype=np.uint8)
        img_array[:, :, 0] = r  # Red channel
        img_array[:, :, 1] = g  # Green channel
        img_array[:, :, 2] = b  # Blue channel
        
    elif direction == "vertical":
        # Vertical gradient
        r = np.linspace(color1[0], color2[0], height).astype(int)
        g = np.linspace(color1[1], color2[1], height).astype(int)
        b = np.linspace(color1[2], color2[2], height).astype(int)
        
        # Create image array
        img_array = np.zeros((height, width, 3), dtype=np.uint8)
        img_array[:, :, 0] = r[:, np.newaxis]  # Red channel
        img_array[:, :, 1] = g[:, np.newaxis]  # Green channel
        img_array[:, :, 2] = b[:, np.newaxis]  # Blue channel
    
    elif direction == "diagonal":
        # Diagonal gradient
        img_array = np.zeros((height, width, 3), dtype=np.uint8)
        
        for y in range(height):
            for x in range(width):
                # Calculate position ratio (0 to 1)
                ratio = (x + y) / (width + height - 2)
                
                # Interpolate colors
                r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
                g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
                b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
                
                img_array[y, x] = [r, g, b]
    
    # Convert to PIL Image and save
    img = Image.fromarray(img_array)
    img.save(filename)
    print(f"✅ Gradient image saved: {filename}")
    
    return filename

# Usage
generate_gradient_image(
    width=1920, height=1080,
    color1=(255, 182, 193),  # Light pink
    color2=(135, 206, 235),  # Sky blue
    direction="diagonal",
    filename="gradient_bg.png"
)
```

### Pattern Generator:
```python
def generate_pattern_image(width=800, height=600, pattern="checkerboard", 
                          color1="black", color2="white", 
                          pattern_size=50, filename="pattern.png"):
    """Pattern image তৈরি"""
    
    img = Image.new('RGB', (width, height), color2)
    draw = ImageDraw.Draw(img)
    
    if pattern == "checkerboard":
        # Checkerboard pattern
        for y in range(0, height, pattern_size):
            for x in range(0, width, pattern_size):
                if (x // pattern_size + y // pattern_size) % 2 == 0:
                    draw.rectangle([x, y, x + pattern_size, y + pattern_size], fill=color1)
    
    elif pattern == "stripes_horizontal":
        # Horizontal stripes
        for y in range(0, height, pattern_size):
            if (y // pattern_size) % 2 == 0:
                draw.rectangle([0, y, width, y + pattern_size], fill=color1)
    
    elif pattern == "stripes_vertical":
        # Vertical stripes
        for x in range(0, width, pattern_size):
            if (x // pattern_size) % 2 == 0:
                draw.rectangle([x, 0, x + pattern_size, height], fill=color1)
    
    elif pattern == "dots":
        # Dot pattern
        dot_radius = pattern_size // 4
        for y in range(pattern_size // 2, height, pattern_size):
            for x in range(pattern_size // 2, width, pattern_size):
                draw.ellipse([x - dot_radius, y - dot_radius, 
                            x + dot_radius, y + dot_radius], fill=color1)
    
    # Save করা
    img.save(filename)
    print(f"✅ Pattern image saved: {filename}")
    
    return filename

# Usage
generate_pattern_image(
    width=600, height=400,
    pattern="checkerboard",
    color1="navy",
    color2="lightgray",
    pattern_size=30,
    filename="checkerboard.png"
)
```

### Placeholder Image Generator:
```python
def generate_placeholder(width=800, height=600, 
                        bg_color="lightgray", text_color="darkgray",
                        filename="placeholder.png"):
    """Placeholder image তৈরি (web development এর জন্য)"""
    
    # Image তৈরি
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Border draw করা
    border_width = 2
    draw.rectangle([0, 0, width-1, height-1], outline=text_color, width=border_width)
    
    # Center text
    text = f"{width} × {height}"
    
    # Font size calculate করা
    font_size = min(width, height) // 10
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # Text position
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Text draw করা
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Diagonal lines draw করা
    draw.line([0, 0, width, height], fill=text_color, width=1)
    draw.line([0, height, width, 0], fill=text_color, width=1)
    
    # Save করা
    img.save(filename)
    print(f"✅ Placeholder image saved: {filename}")
    
    return filename

# Usage
generate_placeholder(1920, 1080, filename="placeholder_1920x1080.png")
generate_placeholder(400, 300, filename="placeholder_400x300.png")
```

---

## 🤖 AI Image Generation {#ai-image-gen}

### Text-to-Image with Stable Diffusion (Local):
```python
# First install: pip install diffusers transformers accelerate torch torchvision
from diffusers import StableDiffusionPipeline
import torch

def generate_ai_image(prompt, filename="ai_generated.png",
                     width=512, height=512, steps=20):
    """AI দিয়ে image generate করা (requires GPU)"""

    try:
        # Load model (first time এ download হবে)
        pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        )

        # GPU use করা (যদি available থাকে)
        if torch.cuda.is_available():
            pipe = pipe.to("cuda")
            print("🚀 Using GPU for generation")
        else:
            print("💻 Using CPU for generation (slower)")

        # Image generate করা
        print(f"🎨 Generating image: '{prompt}'")
        image = pipe(
            prompt,
            width=width,
            height=height,
            num_inference_steps=steps
        ).images[0]

        # Save করা
        image.save(filename)
        print(f"✅ AI image saved: {filename}")

        return filename

    except Exception as e:
        print(f"❌ Error generating AI image: {e}")
        return None

# Usage (requires powerful GPU or patience for CPU)
# generate_ai_image("A beautiful sunset over mountains", "sunset.png")
```

### Online AI Image Generation (API):
```python
import requests
import base64

def generate_online_ai_image(prompt, api_key, filename="online_ai.png"):
    """Online AI service দিয়ে image generate (example with OpenAI DALL-E)"""

    try:
        # OpenAI DALL-E API call
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "prompt": prompt,
            "n": 1,
            "size": "512x512"
        }

        response = requests.post(
            "https://api.openai.com/v1/images/generations",
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            result = response.json()
            image_url = result['data'][0]['url']

            # Download image
            img_response = requests.get(image_url)
            with open(filename, 'wb') as f:
                f.write(img_response.content)

            print(f"✅ Online AI image saved: {filename}")
            return filename
        else:
            print(f"❌ API Error: {response.status_code}")
            return None

    except Exception as e:
        print(f"❌ Error: {e}")
        return None

# Usage (requires API key)
# generate_online_ai_image("A cat wearing sunglasses", "your-api-key", "cool_cat.png")
```

### Simple AI-like Pattern Generator:
```python
import random
import math

def generate_ai_like_pattern(width=800, height=600, filename="ai_pattern.png"):
    """AI-like abstract pattern তৈরি"""

    img = Image.new('RGB', (width, height), 'black')
    draw = ImageDraw.Draw(img)

    # Random colors
    colors = [
        (255, 100, 100), (100, 255, 100), (100, 100, 255),
        (255, 255, 100), (255, 100, 255), (100, 255, 255),
        (255, 200, 100), (200, 100, 255), (100, 255, 200)
    ]

    # Generate random shapes
    for _ in range(50):
        color = random.choice(colors)

        # Random shape type
        shape_type = random.choice(['circle', 'rectangle', 'line'])

        if shape_type == 'circle':
            x = random.randint(0, width)
            y = random.randint(0, height)
            radius = random.randint(10, 100)
            draw.ellipse([x-radius, y-radius, x+radius, y+radius],
                        fill=color, outline=None)

        elif shape_type == 'rectangle':
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            x2 = x1 + random.randint(20, 200)
            y2 = y1 + random.randint(20, 200)
            draw.rectangle([x1, y1, x2, y2], fill=color, outline=None)

        elif shape_type == 'line':
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            x2 = random.randint(0, width)
            y2 = random.randint(0, height)
            draw.line([x1, y1, x2, y2], fill=color, width=random.randint(2, 10))

    # Add some mathematical curves
    for _ in range(10):
        color = random.choice(colors)
        points = []

        for i in range(100):
            t = i / 100.0 * 4 * math.pi
            x = int(width/2 + 100 * math.sin(t + random.random()))
            y = int(height/2 + 100 * math.cos(t * 2 + random.random()))
            points.append((x, y))

        # Draw curve as connected lines
        for i in range(len(points)-1):
            draw.line([points[i], points[i+1]], fill=color, width=2)

    # Save করা
    img.save(filename)
    print(f"✅ AI-like pattern saved: {filename}")

    return filename

# Usage
generate_ai_like_pattern(1200, 800, "abstract_art.png")
```

---

## 📦 Batch Processing {#batch-processing}

### Batch QR + Image Generator:
```python
def batch_generate_qr_and_images(data_list, output_folder="batch_output"):
    """Batch QR codes এবং images তৈরি"""

    os.makedirs(output_folder, exist_ok=True)

    qr_folder = os.path.join(output_folder, "qr_codes")
    img_folder = os.path.join(output_folder, "images")
    os.makedirs(qr_folder, exist_ok=True)
    os.makedirs(img_folder, exist_ok=True)

    results = {"qr_codes": [], "images": []}

    for i, item in enumerate(data_list):
        try:
            name = item.get('name', f'item_{i+1}')

            # Generate QR Code
            if 'qr_data' in item:
                qr_file = os.path.join(qr_folder, f"{name}_qr.png")
                generate_custom_qr(
                    item['qr_data'],
                    qr_file,
                    fill_color=item.get('qr_color', 'black'),
                    back_color=item.get('qr_bg', 'white')
                )
                results["qr_codes"].append(qr_file)

            # Generate Text Image
            if 'text' in item:
                img_file = os.path.join(img_folder, f"{name}_text.png")
                generate_text_image(
                    item['text'],
                    img_file,
                    width=item.get('width', 800),
                    height=item.get('height', 600),
                    bg_color=item.get('bg_color', 'white'),
                    text_color=item.get('text_color', 'black'),
                    font_size=item.get('font_size', 24)
                )
                results["images"].append(img_file)

            # Generate Pattern
            if item.get('generate_pattern'):
                pattern_file = os.path.join(img_folder, f"{name}_pattern.png")
                generate_pattern_image(
                    width=item.get('width', 800),
                    height=item.get('height', 600),
                    pattern=item.get('pattern', 'checkerboard'),
                    color1=item.get('color1', 'black'),
                    color2=item.get('color2', 'white'),
                    pattern_size=item.get('pattern_size', 50),
                    filename=pattern_file
                )
                results["images"].append(pattern_file)

            print(f"✅ Processed item {i+1}: {name}")

        except Exception as e:
            print(f"❌ Error processing item {i+1}: {e}")
            continue

    print(f"🎉 Batch processing complete!")
    print(f"📱 QR Codes: {len(results['qr_codes'])}")
    print(f"🖼️ Images: {len(results['images'])}")

    return results

# Usage
batch_data = [
    {
        "name": "website",
        "qr_data": "https://example.com",
        "qr_color": "navy",
        "text": "Visit Our Website",
        "bg_color": "lightblue",
        "text_color": "darkblue"
    },
    {
        "name": "contact",
        "qr_data": "tel:+8801712345678",
        "text": "Call Us: +880 171 234 5678",
        "generate_pattern": True,
        "pattern": "stripes_horizontal"
    },
    {
        "name": "email",
        "qr_data": "mailto:info@example.com",
        "text": "Email: info@example.com",
        "font_size": 30
    }
]

batch_generate_qr_and_images(batch_data)
```

---

## 🖥️ GUI Applications {#gui-apps}

### Simple QR Generator GUI:
```python
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import ImageTk

class QRGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("600x500")

        self.setup_ui()

    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Input section
        ttk.Label(main_frame, text="QR Code Data:").grid(row=0, column=0, sticky=tk.W, pady=5)

        self.data_entry = tk.Text(main_frame, height=4, width=50)
        self.data_entry.grid(row=1, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        # Options
        options_frame = ttk.LabelFrame(main_frame, text="Options", padding="5")
        options_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

        ttk.Label(options_frame, text="Fill Color:").grid(row=0, column=0, sticky=tk.W)
        self.fill_color = ttk.Combobox(options_frame, values=["black", "navy", "red", "green", "purple"])
        self.fill_color.set("black")
        self.fill_color.grid(row=0, column=1, padx=5)

        ttk.Label(options_frame, text="Background:").grid(row=0, column=2, sticky=tk.W, padx=(20,0))
        self.bg_color = ttk.Combobox(options_frame, values=["white", "lightgray", "lightblue", "lightyellow"])
        self.bg_color.set("white")
        self.bg_color.grid(row=0, column=3, padx=5)

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Button(button_frame, text="Generate QR", command=self.generate_qr).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Save As...", command=self.save_qr).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_all).pack(side=tk.LEFT, padx=5)

        # Preview
        self.preview_label = ttk.Label(main_frame, text="QR Code Preview")
        self.preview_label.grid(row=4, column=0, columnspan=2, pady=10)

        self.current_qr = None

    def generate_qr(self):
        data = self.data_entry.get("1.0", tk.END).strip()

        if not data:
            messagebox.showwarning("Warning", "Please enter some data for QR code")
            return

        try:
            # Generate QR code
            qr = qrcode.QRCode(version=1, box_size=8, border=4)
            qr.add_data(data)
            qr.make(fit=True)

            # Create image
            qr_img = qr.make_image(
                fill_color=self.fill_color.get(),
                back_color=self.bg_color.get()
            )

            # Resize for preview
            qr_img = qr_img.resize((200, 200), Image.Resampling.LANCZOS)

            # Convert for tkinter
            self.current_qr = qr_img
            photo = ImageTk.PhotoImage(qr_img)

            # Update preview
            self.preview_label.configure(image=photo, text="")
            self.preview_label.image = photo  # Keep reference

            messagebox.showinfo("Success", "QR Code generated successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate QR code: {e}")

    def save_qr(self):
        if self.current_qr is None:
            messagebox.showwarning("Warning", "Please generate a QR code first")
            return

        filename = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )

        if filename:
            try:
                # Generate full-size QR for saving
                data = self.data_entry.get("1.0", tk.END).strip()
                qr = qrcode.QRCode(version=1, box_size=10, border=4)
                qr.add_data(data)
                qr.make(fit=True)

                qr_img = qr.make_image(
                    fill_color=self.fill_color.get(),
                    back_color=self.bg_color.get()
                )

                qr_img.save(filename)
                messagebox.showinfo("Success", f"QR Code saved as {filename}")

            except Exception as e:
                messagebox.showerror("Error", f"Failed to save QR code: {e}")

    def clear_all(self):
        self.data_entry.delete("1.0", tk.END)
        self.preview_label.configure(image="", text="QR Code Preview")
        self.current_qr = None

# Usage
def run_qr_gui():
    root = tk.Tk()
    app = QRGeneratorGUI(root)
    root.mainloop()

# Uncomment to run GUI
# run_qr_gui()
```

### Complete Media Generator GUI:
```python
class MediaGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("QR & Image Generator")
        self.root.geometry("800x600")

        # Create notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create tabs
        self.create_qr_tab()
        self.create_image_tab()
        self.create_batch_tab()

    def create_qr_tab(self):
        # QR Code tab
        qr_frame = ttk.Frame(self.notebook)
        self.notebook.add(qr_frame, text="QR Generator")

        # QR content here (similar to above)
        ttk.Label(qr_frame, text="QR Code Generator", font=("Arial", 16)).pack(pady=10)

    def create_image_tab(self):
        # Image Generator tab
        img_frame = ttk.Frame(self.notebook)
        self.notebook.add(img_frame, text="Image Generator")

        ttk.Label(img_frame, text="Image Generator", font=("Arial", 16)).pack(pady=10)

        # Image type selection
        type_frame = ttk.LabelFrame(img_frame, text="Image Type", padding="10")
        type_frame.pack(fill=tk.X, padx=10, pady=5)

        self.img_type = tk.StringVar(value="text")
        ttk.Radiobutton(type_frame, text="Text Image", variable=self.img_type, value="text").pack(side=tk.LEFT)
        ttk.Radiobutton(type_frame, text="Gradient", variable=self.img_type, value="gradient").pack(side=tk.LEFT)
        ttk.Radiobutton(type_frame, text="Pattern", variable=self.img_type, value="pattern").pack(side=tk.LEFT)
        ttk.Radiobutton(type_frame, text="Placeholder", variable=self.img_type, value="placeholder").pack(side=tk.LEFT)

    def create_batch_tab(self):
        # Batch Processing tab
        batch_frame = ttk.Frame(self.notebook)
        self.notebook.add(batch_frame, text="Batch Processing")

        ttk.Label(batch_frame, text="Batch Processing", font=("Arial", 16)).pack(pady=10)

        # Batch options here
        ttk.Button(batch_frame, text="Load CSV", command=self.load_csv).pack(pady=5)
        ttk.Button(batch_frame, text="Process All", command=self.process_batch).pack(pady=5)

    def load_csv(self):
        # CSV loading logic
        pass

    def process_batch(self):
        # Batch processing logic
        pass

# Usage
def run_media_gui():
    root = tk.Tk()
    app = MediaGeneratorGUI(root)
    root.mainloop()

# Uncomment to run
# run_media_gui()
```

---

## 🎉 সমাপনী

এই গাইডে আপনি শিখেছেন:

✅ **QR Code Generation:** Basic থেকে advanced QR codes
✅ **Custom QR Design:** Logo, colors, labels সহ
✅ **Image Generation:** Text, gradients, patterns
✅ **AI Integration:** Modern AI image generation
✅ **Batch Processing:** Multiple files একসাথে
✅ **GUI Applications:** User-friendly interfaces

### 🚀 Next Steps:
1. **Practice করুন** - বিভিন্ন QR codes ও images তৈরি করুন
2. **Customize করুন** - নিজের মতো করে modify করুন
3. **Integrate করুন** - Web applications এ ব্যবহার করুন
4. **Share করুন** - অন্যদের সাথে share করুন

**Happy Generating! 🎨📱**
```
