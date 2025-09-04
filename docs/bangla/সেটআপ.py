#!/usr/bin/env python3
"""
Playwright Web Scraping সেটআপ স্ক্রিপ্ট
=====================================

এই script automatically সব কিছু setup করে দেবে Playwright web scraping এর জন্য।

ব্যবহার:
    python সেটআপ.py

বৈশিষ্ট্য:
- Virtual environment তৈরি
- সব required packages install
- Playwright browsers install
- Installation test
- Usage examples প্রদান
"""

import subprocess
import sys
import os
import platform
from pathlib import Path

class PlaywrightSেটআপ:
    def __init__(self):
        self.system = platform.system().lower()
        self.python_cmd = self.get_python_command()
        self.venv_name = "playwright-scraping-env"
        self.venv_path = Path(self.venv_name)
        
    def get_python_command(self):
        """সঠিক Python command খুঁজে বের করা"""
        
        python_commands = ['python3', 'python', 'py']
        
        for cmd in python_commands:
            try:
                result = subprocess.run([cmd, '--version'], 
                                      capture_output=True, text=True)
                if result.returncode == 0 and 'Python 3' in result.stdout:
                    return cmd
            except FileNotFoundError:
                continue
        
        raise RuntimeError("Python 3 পাওয়া যায়নি। দয়া করে Python 3.7+ install করুন")
    
    def run_command(self, command, description=""):
        """Command চালানো এবং error handling"""
        
        print(f"🔄 {description}")
        print(f"   Command: {' '.join(command)}")
        
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            print(f"✅ {description} - সফল")
            return result
        except subprocess.CalledProcessError as e:
            print(f"❌ {description} - ব্যর্থ")
            print(f"   Error: {e.stderr}")
            return None
    
    def create_virtual_environment(self):
        """Python virtual environment তৈরি"""
        
        if self.venv_path.exists():
            print(f"⚠️  Virtual environment '{self.venv_name}' ইতিমধ্যে আছে")
            return True
        
        command = [self.python_cmd, '-m', 'venv', self.venv_name]
        result = self.run_command(command, f"Virtual environment '{self.venv_name}' তৈরি করা হচ্ছে")
        
        return result is not None
    
    def get_venv_python(self):
        """Virtual environment এর Python executable"""
        
        if self.system == 'windows':
            return str(self.venv_path / 'Scripts' / 'python.exe')
        else:
            return str(self.venv_path / 'bin' / 'python')
    
    def get_venv_pip(self):
        """Virtual environment এর pip executable"""
        
        if self.system == 'windows':
            return str(self.venv_path / 'Scripts' / 'pip.exe')
        else:
            return str(self.venv_path / 'bin' / 'pip')
    
    def upgrade_pip(self):
        """Virtual environment এ pip upgrade"""
        
        venv_python = self.get_venv_python()
        command = [venv_python, '-m', 'pip', 'install', '--upgrade', 'pip']
        result = self.run_command(command, "Pip upgrade করা হচ্ছে")
        
        return result is not None
    
    def install_requirements(self):
        """Required packages install"""
        
        venv_pip = self.get_venv_pip()
        
        # Core packages list
        packages = [
            'playwright>=1.40.0',
            'requests>=2.31.0',
            'beautifulsoup4>=4.12.0',
            'pandas>=2.1.0',
            'numpy>=1.24.0',
            'aiohttp>=3.9.0',
            'aiofiles>=23.2.0',
            'Pillow>=10.0.0',
            'matplotlib>=3.7.0',
            'tqdm>=4.66.0',
            'colorama>=0.4.6'
        ]
        
        for package in packages:
            command = [venv_pip, 'install', package]
            result = self.run_command(command, f"Installing {package.split('>=')[0]}")
            if not result:
                return False
        
        return True
    
    def install_playwright_browsers(self):
        """Playwright browsers install"""
        
        venv_python = self.get_venv_python()
        command = [venv_python, '-m', 'playwright', 'install']
        result = self.run_command(command, "Playwright browsers install করা হচ্ছে")
        
        return result is not None
    
    def test_installation(self):
        """Installation test"""
        
        venv_python = self.get_venv_python()
        
        test_script = '''
import sys
print("🧪 Module imports test করা হচ্ছে...")

modules_to_test = [
    ("playwright", "from playwright.sync_api import sync_playwright"),
    ("requests", "import requests"),
    ("beautifulsoup4", "from bs4 import BeautifulSoup"),
    ("pandas", "import pandas as pd"),
    ("numpy", "import numpy as np"),
    ("aiohttp", "import aiohttp"),
    ("aiofiles", "import aiofiles"),
    ("PIL", "from PIL import Image"),
    ("matplotlib", "import matplotlib.pyplot as plt"),
    ("tqdm", "from tqdm import tqdm"),
    ("colorama", "from colorama import Fore, init"),
]

success_count = 0
total_count = len(modules_to_test)

for module_name, import_statement in modules_to_test:
    try:
        exec(import_statement)
        print(f"✅ {module_name}: OK")
        success_count += 1
    except ImportError as e:
        print(f"❌ {module_name}: FAILED - {e}")

print(f"\\n📊 Test Results: {success_count}/{total_count} modules সফলভাবে import হয়েছে")

if success_count == total_count:
    print("🎉 সব modules সঠিকভাবে install হয়েছে!")
    sys.exit(0)
else:
    print("⚠️  কিছু modules import হতে পারেনি")
    sys.exit(1)
'''
        
        # Test script temporary file এ লেখা
        test_file = Path('test_installation_temp.py')
        test_file.write_text(test_script, encoding='utf-8')
        
        try:
            command = [venv_python, str(test_file)]
            result = self.run_command(command, "Installation test করা হচ্ছে")
            
            # Clean up
            test_file.unlink()
            
            return result is not None and result.returncode == 0
            
        except Exception as e:
            print(f"❌ Test ব্যর্থ: {e}")
            if test_file.exists():
                test_file.unlink()
            return False
    
    def create_activation_script(self):
        """Environment activation script তৈরি"""
        
        if self.system == 'windows':
            activate_script = f'''@echo off
echo 🚀 Playwright Scraping Environment activate করা হচ্ছে...
call {self.venv_name}\\Scripts\\activate.bat
echo ✅ Environment activate হয়েছে!
echo.
echo 📚 Available documentation:
echo    - docs/bangla/README.md - বাংলা documentation hub
echo    - docs/bangla/দ্রুত-শুরু.md - ৫ মিনিটে শুরু
echo    - docs/bangla/শেখার-গাইড.md - দ্রুত শেখার গাইড
echo.
echo 🎯 Quick start:
echo    python -c "from playwright.sync_api import sync_playwright; print('Playwright ready!')"
echo.
cmd /k
'''
            script_name = 'activate_env.bat'
        else:
            activate_script = f'''#!/bin/bash
echo "🚀 Playwright Scraping Environment activate করা হচ্ছে..."
source {self.venv_name}/bin/activate
echo "✅ Environment activate হয়েছে!"
echo ""
echo "📚 Available documentation:"
echo "   - docs/bangla/README.md - বাংলা documentation hub"
echo "   - docs/bangla/দ্রুত-শুরু.md - ৫ মিনিটে শুরু"
echo "   - docs/bangla/শেখার-গাইড.md - দ্রুত শেখার গাইড"
echo ""
echo "🎯 Quick start:"
echo "   python -c \\"from playwright.sync_api import sync_playwright; print('Playwright ready!')\\"
echo ""
exec bash
'''
            script_name = 'activate_env.sh'
        
        script_path = Path(script_name)
        script_path.write_text(activate_script, encoding='utf-8')
        
        if self.system != 'windows':
            # Unix systems এ script executable করা
            os.chmod(script_path, 0o755)
        
        print(f"📝 Activation script তৈরি: {script_name}")
        return script_path
    
    def create_sample_script(self):
        """Sample scraping script তৈরি"""
        
        sample_script = '''#!/usr/bin/env python3
"""
Sample Playwright Web Scraping Script
====================================

এটি একটি sample script যা দেখায় কিভাবে Playwright ব্যবহার করতে হয়।
"""

from playwright.sync_api import sync_playwright
import json
from datetime import datetime

def scrape_quotes():
    """Quotes website থেকে data scrape করা"""
    
    print("🚀 Quotes scraping শুরু করা হচ্ছে...")
    
    with sync_playwright() as p:
        # Browser launch
        browser = p.chromium.launch(headless=False)  # headless=True production এ
        page = browser.new_page()
        
        # Website এ যাওয়া
        print("🌐 Website এ যাওয়া হচ্ছে...")
        page.goto("https://quotes.toscrape.com")
        
        # Page load এর জন্য অপেক্ষা
        page.wait_for_load_state('networkidle')
        
        # Quotes extract করা
        print("📊 Quotes extract করা হচ্ছে...")
        quotes = page.locator(".quote").all()
        
        quotes_data = []
        
        for i, quote in enumerate(quotes, 1):
            # Data extract
            text = quote.locator(".text").text_content()
            author = quote.locator(".author").text_content()
            tags = quote.locator(".tags .tag").all_text_contents()
            
            # Structure data
            quote_info = {
                'id': i,
                'text': text.strip().strip('"').strip('"'),
                'author': author.strip(),
                'tags': [tag.strip() for tag in tags],
                'scraped_at': datetime.now().isoformat()
            }
            
            quotes_data.append(quote_info)
            print(f"  📝 Quote {i}: {author}")
        
        browser.close()
    
    # Data save করা
    print("💾 Data save করা হচ্ছে...")
    
    with open('quotes.json', 'w', encoding='utf-8') as f:
        json.dump(quotes_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ সফলভাবে {len(quotes_data)}টি quotes scrape করা হয়েছে!")
    print("📁 Data save হয়েছে: quotes.json")
    
    return quotes_data

if __name__ == "__main__":
    quotes = scrape_quotes()
    
    # First quote display
    if quotes:
        first_quote = quotes[0]
        print(f"\\n🌟 First Quote:")
        print(f"   Text: {first_quote['text']}")
        print(f"   Author: {first_quote['author']}")
        print(f"   Tags: {', '.join(first_quote['tags'])}")
'''
        
        script_path = Path('sample_scraper.py')
        script_path.write_text(sample_script, encoding='utf-8')
        
        print(f"📝 Sample script তৈরি: sample_scraper.py")
        return script_path
    
    def setup_complete(self):
        """Setup complete message"""
        
        print("🎉 Setup সফলভাবে সম্পন্ন হয়েছে!")
        print("")
        print("📋 যা install করা হয়েছে:")
        print("   ✅ Python virtual environment")
        print("   ✅ সব required Python packages")
        print("   ✅ Playwright browsers (Chromium, Firefox, WebKit)")
        print("   ✅ Development ও testing tools")
        print("")
        print("🚀 পরবর্তী steps:")
        
        if self.system == 'windows':
            print("   1. চালান: activate_env.bat")
        else:
            print("   1. চালান: ./activate_env.sh")
        
        print("   2. পড়ুন: docs/bangla/README.md")
        print("   3. শুরু করুন: docs/bangla/দ্রুত-শুরু.md")
        print("   4. Test করুন: python sample_scraper.py")
        print("")
        print("📚 বাংলা Documentation:")
        print("   - দ্রুত শুরু গাইড")
        print("   - সম্পূর্ণ Playwright টিউটোরিয়াল")
        print("   - Advanced techniques")
        print("   - Real-world examples")
        print("")
        print("শুভ স্ক্র্যাপিং! 🕷️🇧🇩")
    
    def run_setup(self):
        """Complete setup process চালানো"""
        
        print("🚀 Playwright Web Scraping সেটআপ")
        print("=" * 40)
        print(f"System: {platform.system()} {platform.release()}")
        print(f"Python: {self.python_cmd}")
        print("")
        
        steps = [
            ("Virtual environment তৈরি", self.create_virtual_environment),
            ("Pip upgrade", self.upgrade_pip),
            ("Python packages install", self.install_requirements),
            ("Playwright browsers install", self.install_playwright_browsers),
            ("Installation test", self.test_installation),
            ("Activation script তৈরি", self.create_activation_script),
            ("Sample script তৈরি", self.create_sample_script),
        ]
        
        for step_name, step_function in steps:
            print(f"📋 Step: {step_name}")
            
            if not step_function():
                print(f"❌ Setup ব্যর্থ হয়েছে: {step_name}")
                print("দয়া করে উপরের error messages দেখুন এবং আবার চেষ্টা করুন।")
                sys.exit(1)
            
            print("")
        
        self.setup_complete()

def main():
    """Main setup function"""
    
    try:
        setup = PlaywrightSেটআপ()
        setup.run_setup()
    except KeyboardInterrupt:
        print("\n⚠️  Setup user দ্বারা বন্ধ করা হয়েছে")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup error এর সাথে ব্যর্থ: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
