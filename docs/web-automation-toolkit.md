# 🤖 Web Automation Toolkit - Complete Guide

## 📚 সূচিপত্র
1. [Form Automation](#form-automation)
2. [File Upload/Download](#file-operations)
3. [Screenshot & PDF Generation](#screenshot-pdf)
4. [Email Automation](#email-automation)
5. [Social Media Automation](#social-media)
6. [Testing & Monitoring](#testing-monitoring)

---

## 📝 Form Automation {#form-automation}

### Advanced Form Filling:
```python
from playwright.sync_api import sync_playwright
import json
import time
import random

class FormAutomator:
    def __init__(self, headless=True):
        self.headless = headless
        self.form_data = {}
        
    def setup_browser(self):
        """Browser setup with human-like behavior"""
        self.playwright = sync_playwright().start()
        
        self.browser = self.playwright.chromium.launch(
            headless=self.headless,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-dev-shm-usage",
                "--no-sandbox"
            ]
        )
        
        # Human-like context
        self.context = self.browser.new_context(
            viewport={'width': 1366, 'height': 768},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            locale='en-US'
        )
        
        self.page = self.context.new_page()
        
        # Add human-like mouse movements
        self.page.evaluate("""
            // Override webdriver detection
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined,
            });
        """)
    
    def human_type(self, selector, text, delay_range=(50, 150)):
        """Human-like typing with random delays"""
        
        element = self.page.locator(selector)
        element.click()
        
        # Clear existing text
        element.fill("")
        
        # Type character by character
        for char in text:
            element.type(char)
            delay = random.randint(*delay_range)
            time.sleep(delay / 1000)  # Convert to seconds
    
    def human_click(self, selector, delay_range=(100, 300)):
        """Human-like clicking with delays"""
        
        element = self.page.locator(selector)
        
        # Scroll into view
        element.scroll_into_view_if_needed()
        
        # Random delay before click
        delay = random.randint(*delay_range)
        time.sleep(delay / 1000)
        
        # Click with slight offset for naturalness
        element.click(position={'x': random.randint(5, 15), 'y': random.randint(5, 15)})
    
    def fill_contact_form(self, form_data):
        """Contact form automatic fill করা"""
        
        try:
            # Name field
            if 'name' in form_data:
                name_selectors = ['input[name="name"]', '#name', '.name-input', 'input[placeholder*="name"]']
                for selector in name_selectors:
                    if self.page.locator(selector).is_visible():
                        self.human_type(selector, form_data['name'])
                        break
            
            # Email field
            if 'email' in form_data:
                email_selectors = ['input[type="email"]', 'input[name="email"]', '#email']
                for selector in email_selectors:
                    if self.page.locator(selector).is_visible():
                        self.human_type(selector, form_data['email'])
                        break
            
            # Phone field
            if 'phone' in form_data:
                phone_selectors = ['input[type="tel"]', 'input[name="phone"]', '#phone']
                for selector in phone_selectors:
                    if self.page.locator(selector).is_visible():
                        self.human_type(selector, form_data['phone'])
                        break
            
            # Message/Comment field
            if 'message' in form_data:
                message_selectors = ['textarea', 'input[name="message"]', '#message', '.message-input']
                for selector in message_selectors:
                    if self.page.locator(selector).is_visible():
                        self.human_type(selector, form_data['message'])
                        break
            
            # Subject field (if exists)
            if 'subject' in form_data:
                subject_selectors = ['input[name="subject"]', '#subject', '.subject-input']
                for selector in subject_selectors:
                    if self.page.locator(selector).is_visible():
                        self.human_type(selector, form_data['subject'])
                        break
            
            # Handle dropdowns
            if 'country' in form_data:
                country_select = self.page.locator('select[name="country"], #country')
                if country_select.is_visible():
                    country_select.select_option(form_data['country'])
            
            # Handle checkboxes
            if 'newsletter' in form_data and form_data['newsletter']:
                newsletter_checkbox = self.page.locator('input[type="checkbox"][name*="newsletter"]')
                if newsletter_checkbox.is_visible():
                    newsletter_checkbox.check()
            
            # Handle radio buttons
            if 'gender' in form_data:
                gender_radio = self.page.locator(f'input[type="radio"][value="{form_data["gender"]}"]')
                if gender_radio.is_visible():
                    gender_radio.check()
            
            print("✅ Form filled successfully")
            return True
            
        except Exception as e:
            print(f"❌ Error filling form: {e}")
            return False
    
    def submit_form(self, submit_selector=None):
        """Form submit করা"""
        
        if not submit_selector:
            # Common submit button selectors
            submit_selectors = [
                'button[type="submit"]',
                'input[type="submit"]',
                '.submit-btn',
                '#submit',
                'button:has-text("Submit")',
                'button:has-text("Send")'
            ]
        else:
            submit_selectors = [submit_selector]
        
        for selector in submit_selectors:
            submit_btn = self.page.locator(selector)
            if submit_btn.is_visible():
                self.human_click(selector)
                
                # Wait for submission result
                try:
                    # Wait for success message or redirect
                    self.page.wait_for_function(
                        "document.querySelector('.success, .thank-you, .confirmation') !== null || window.location.href !== arguments[0]",
                        self.page.url,
                        timeout=10000
                    )
                    print("✅ Form submitted successfully")
                    return True
                except:
                    print("⚠️ Form submitted but no confirmation detected")
                    return True
        
        print("❌ Submit button not found")
        return False
    
    def handle_captcha(self):
        """CAPTCHA detection ও handling"""
        
        # Check for common CAPTCHA types
        captcha_selectors = [
            '.g-recaptcha',  # Google reCAPTCHA
            '.h-captcha',    # hCaptcha
            '.captcha',      # Generic CAPTCHA
            '#captcha'
        ]
        
        for selector in captcha_selectors:
            if self.page.locator(selector).is_visible():
                print("🤖 CAPTCHA detected!")
                print("⚠️ Manual intervention required")
                
                # Wait for user to solve CAPTCHA
                input("Press Enter after solving CAPTCHA...")
                return True
        
        return False
    
    def close(self):
        """Cleanup"""
        if hasattr(self, 'browser'):
            self.browser.close()
        if hasattr(self, 'playwright'):
            self.playwright.stop()

# Usage
def automate_contact_form():
    """Contact form automation example"""
    
    automator = FormAutomator(headless=False)
    
    try:
        automator.setup_browser()
        
        # Navigate to form
        automator.page.goto("https://example.com/contact")
        
        # Form data
        form_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'phone': '+1234567890',
            'subject': 'Inquiry about services',
            'message': 'Hello, I would like to know more about your services.',
            'country': 'US',
            'newsletter': True,
            'gender': 'male'
        }
        
        # Fill and submit form
        if automator.fill_contact_form(form_data):
            # Check for CAPTCHA
            automator.handle_captcha()
            
            # Submit form
            automator.submit_form()
        
    finally:
        automator.close()

# automate_contact_form()
```

### Multi-Step Form Automation:
```python
class MultiStepFormAutomator:
    def __init__(self):
        self.current_step = 1
        self.form_data = {}
        self.step_selectors = {}
    
    def setup_step_navigation(self, step_config):
        """Multi-step form navigation setup"""
        self.step_selectors = step_config
    
    def fill_step(self, step_number, data):
        """Specific step fill করা"""
        
        print(f"📝 Filling step {step_number}...")
        
        # Wait for step to be visible
        step_container = f".step-{step_number}, #step{step_number}, .step[data-step='{step_number}']"
        self.page.wait_for_selector(step_container, timeout=10000)
        
        # Fill step-specific fields
        for field_name, field_value in data.items():
            try:
                # Dynamic selector based on step and field
                field_selector = f"{step_container} input[name='{field_name}'], {step_container} #{field_name}"
                
                if self.page.locator(field_selector).is_visible():
                    if isinstance(field_value, bool):
                        # Checkbox handling
                        if field_value:
                            self.page.locator(field_selector).check()
                    else:
                        # Text input
                        self.human_type(field_selector, str(field_value))
                
            except Exception as e:
                print(f"⚠️ Error filling {field_name}: {e}")
    
    def navigate_to_next_step(self):
        """Next step এ যাওয়া"""
        
        next_selectors = [
            '.next-step',
            '.btn-next',
            'button:has-text("Next")',
            'button:has-text("Continue")'
        ]
        
        for selector in next_selectors:
            if self.page.locator(selector).is_visible():
                self.human_click(selector)
                self.current_step += 1
                
                # Wait for next step to load
                time.sleep(2)
                return True
        
        return False
    
    def complete_multi_step_form(self, steps_data):
        """Complete multi-step form automation"""
        
        for step_num, step_data in steps_data.items():
            # Fill current step
            self.fill_step(step_num, step_data)
            
            # Navigate to next step (except for last step)
            if step_num < len(steps_data):
                if not self.navigate_to_next_step():
                    print(f"❌ Failed to navigate from step {step_num}")
                    return False
            else:
                # Last step - submit form
                self.submit_form()
        
        return True

# Usage
def multi_step_form_example():
    """Multi-step form automation"""
    
    automator = MultiStepFormAutomator()
    
    # Step data
    steps_data = {
        1: {  # Personal Information
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'phone': '1234567890'
        },
        2: {  # Address Information
            'street': '123 Main St',
            'city': 'New York',
            'state': 'NY',
            'zip_code': '10001'
        },
        3: {  # Preferences
            'newsletter': True,
            'notifications': False,
            'marketing_emails': True
        }
    }
    
    automator.complete_multi_step_form(steps_data)
```

---

## 📁 File Upload/Download {#file-operations}

### Advanced File Upload:
```python
def advanced_file_upload():
    """Advanced file upload with multiple files"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to upload page
        page.goto("https://example.com/upload")
        
        # Single file upload
        single_file_input = page.locator('input[type="file"]:not([multiple])')
        if single_file_input.is_visible():
            single_file_input.set_input_files("document.pdf")
            print("📄 Single file uploaded")
        
        # Multiple file upload
        multiple_file_input = page.locator('input[type="file"][multiple]')
        if multiple_file_input.is_visible():
            files_to_upload = [
                "image1.jpg",
                "image2.png",
                "document.pdf"
            ]
            multiple_file_input.set_input_files(files_to_upload)
            print(f"📁 {len(files_to_upload)} files uploaded")
        
        # Drag and drop upload
        drag_drop_area = page.locator('.dropzone, .drag-drop-area')
        if drag_drop_area.is_visible():
            # Create file input dynamically
            page.evaluate("""
                const input = document.createElement('input');
                input.type = 'file';
                input.multiple = true;
                input.style.display = 'none';
                document.body.appendChild(input);
                
                input.addEventListener('change', (e) => {
                    const files = e.target.files;
                    const dropzone = document.querySelector('.dropzone, .drag-drop-area');
                    
                    // Simulate drop event
                    const dropEvent = new DragEvent('drop', {
                        dataTransfer: new DataTransfer()
                    });
                    
                    for (let file of files) {
                        dropEvent.dataTransfer.items.add(file);
                    }
                    
                    dropzone.dispatchEvent(dropEvent);
                });
            """)
            
            # Set files to hidden input
            hidden_input = page.locator('input[type="file"]').last
            hidden_input.set_input_files(["upload_file.txt"])
            print("🎯 Drag-drop upload simulated")
        
        # Wait for upload completion
        upload_progress = page.locator('.upload-progress, .progress-bar')
        if upload_progress.is_visible():
            upload_progress.wait_for(state="hidden", timeout=30000)
            print("✅ Upload completed")
        
        browser.close()

# advanced_file_upload()
```

### Bulk File Download:
```python
import os
from pathlib import Path

def bulk_file_download():
    """Bulk file download with progress tracking"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Create download directory
        download_dir = Path("downloads")
        download_dir.mkdir(exist_ok=True)
        
        # Track downloads
        downloads = []
        
        def handle_download(download):
            """Download event handler"""
            filename = download.suggested_filename
            filepath = download_dir / filename
            
            print(f"📥 Downloading: {filename}")
            download.save_as(filepath)
            downloads.append(str(filepath))
            print(f"✅ Downloaded: {filename}")
        
        page.on("download", handle_download)
        
        # Navigate to download page
        page.goto("https://example.com/downloads")
        
        # Find all download links
        download_links = page.locator('a[href$=".pdf"], a[href$=".zip"], a[href$=".doc"], a[download]').all()
        
        print(f"🔍 Found {len(download_links)} download links")
        
        # Download all files
        for i, link in enumerate(download_links):
            try:
                print(f"🎯 Clicking download {i+1}/{len(download_links)}")
                
                # Click download link
                with page.expect_download() as download_info:
                    link.click()
                
                # Wait for download to complete
                download = download_info.value
                
                # Add delay between downloads
                time.sleep(2)
                
            except Exception as e:
                print(f"❌ Error downloading file {i+1}: {e}")
                continue
        
        print(f"🎉 Downloaded {len(downloads)} files:")
        for filepath in downloads:
            print(f"  📄 {filepath}")
        
        browser.close()
        return downloads

# files = bulk_file_download()
```

---

## 📸 Screenshot & PDF Generation {#screenshot-pdf}

### Advanced Screenshot Automation:
```python
def advanced_screenshot_automation():
    """Advanced screenshot automation with different modes"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # Different viewport sizes
        viewports = [
            {'name': 'desktop', 'width': 1920, 'height': 1080},
            {'name': 'tablet', 'width': 768, 'height': 1024},
            {'name': 'mobile', 'width': 375, 'height': 667}
        ]
        
        urls = [
            "https://example.com",
            "https://example.com/about",
            "https://example.com/contact"
        ]
        
        for viewport in viewports:
            context = browser.new_context(
                viewport={'width': viewport['width'], 'height': viewport['height']}
            )
            page = context.new_page()
            
            for url in urls:
                try:
                    print(f"📸 Screenshot: {viewport['name']} - {url}")
                    
                    page.goto(url)
                    page.wait_for_load_state('networkidle')
                    
                    # Page name from URL
                    page_name = url.split('/')[-1] or 'home'
                    
                    # Full page screenshot
                    screenshot_path = f"screenshots/{viewport['name']}_{page_name}_full.png"
                    page.screenshot(path=screenshot_path, full_page=True)
                    
                    # Viewport screenshot
                    viewport_path = f"screenshots/{viewport['name']}_{page_name}_viewport.png"
                    page.screenshot(path=viewport_path, full_page=False)
                    
                    # Element screenshot (if exists)
                    header = page.locator('header, .header, nav')
                    if header.is_visible():
                        header_path = f"screenshots/{viewport['name']}_{page_name}_header.png"
                        header.screenshot(path=header_path)
                    
                    print(f"✅ Screenshots saved for {viewport['name']} - {page_name}")
                    
                except Exception as e:
                    print(f"❌ Error taking screenshot: {e}")
                    continue
            
            context.close()
        
        browser.close()

# advanced_screenshot_automation()
```

### PDF Generation with Custom Options:
```python
def advanced_pdf_generation():
    """Advanced PDF generation with custom options"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        urls = [
            {"url": "https://example.com", "name": "homepage"},
            {"url": "https://example.com/about", "name": "about"},
            {"url": "https://example.com/services", "name": "services"}
        ]
        
        for url_info in urls:
            try:
                print(f"📄 Generating PDF: {url_info['name']}")
                
                page.goto(url_info['url'])
                page.wait_for_load_state('networkidle')
                
                # Remove unwanted elements
                page.evaluate("""
                    // Remove ads, popups, etc.
                    const unwanted = document.querySelectorAll('.ad, .popup, .modal, .cookie-banner');
                    unwanted.forEach(el => el.remove());
                    
                    // Hide navigation for cleaner PDF
                    const nav = document.querySelector('nav, .navigation');
                    if (nav) nav.style.display = 'none';
                """)
                
                # PDF options
                pdf_options = {
                    'path': f"pdfs/{url_info['name']}.pdf",
                    'format': 'A4',
                    'print_background': True,
                    'margin': {
                        'top': '1cm',
                        'right': '1cm',
                        'bottom': '1cm',
                        'left': '1cm'
                    },
                    'display_header_footer': True,
                    'header_template': f'<div style="font-size:10px; text-align:center; width:100%;">{url_info["url"]}</div>',
                    'footer_template': '<div style="font-size:10px; text-align:center; width:100%;">Page <span class="pageNumber"></span> of <span class="totalPages"></span></div>'
                }
                
                # Generate PDF
                page.pdf(**pdf_options)
                print(f"✅ PDF saved: {url_info['name']}.pdf")
                
            except Exception as e:
                print(f"❌ Error generating PDF for {url_info['name']}: {e}")
                continue
        
        browser.close()

# advanced_pdf_generation()
```

---

## 📧 Email Automation {#email-automation}

### Email Sending Automation:
```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

class EmailAutomator:
    def __init__(self, smtp_server, smtp_port, email, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password
        self.server = None

    def connect(self):
        """SMTP server এ connect করা"""
        try:
            self.server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            self.server.starttls()
            self.server.login(self.email, self.password)
            print("✅ Email server connected")
            return True
        except Exception as e:
            print(f"❌ Email connection failed: {e}")
            return False

    def send_email(self, to_email, subject, body, attachments=None, is_html=False):
        """Email send করা"""

        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = to_email
            msg['Subject'] = subject

            # Add body
            if is_html:
                msg.attach(MIMEText(body, 'html'))
            else:
                msg.attach(MIMEText(body, 'plain'))

            # Add attachments
            if attachments:
                for file_path in attachments:
                    if os.path.exists(file_path):
                        with open(file_path, "rb") as attachment:
                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload(attachment.read())

                        encoders.encode_base64(part)
                        part.add_header(
                            'Content-Disposition',
                            f'attachment; filename= {os.path.basename(file_path)}'
                        )
                        msg.attach(part)

            # Send email
            text = msg.as_string()
            self.server.sendmail(self.email, to_email, text)
            print(f"✅ Email sent to {to_email}")
            return True

        except Exception as e:
            print(f"❌ Error sending email: {e}")
            return False

    def send_bulk_emails(self, email_list, subject, body_template, is_html=False):
        """Bulk email sending"""

        sent_count = 0
        failed_count = 0

        for email_data in email_list:
            try:
                # Personalize email body
                personalized_body = body_template.format(**email_data)

                # Send email
                if self.send_email(
                    email_data['email'],
                    subject,
                    personalized_body,
                    is_html=is_html
                ):
                    sent_count += 1
                else:
                    failed_count += 1

                # Rate limiting
                time.sleep(1)

            except Exception as e:
                print(f"❌ Error sending to {email_data.get('email', 'unknown')}: {e}")
                failed_count += 1

        print(f"📊 Bulk email results: {sent_count} sent, {failed_count} failed")
        return sent_count, failed_count

    def close(self):
        """Connection close করা"""
        if self.server:
            self.server.quit()
            print("👋 Email server disconnected")

# Usage
def email_automation_example():
    """Email automation example"""

    # Email configuration (Gmail example)
    email_config = {
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587,
        'email': 'your-email@gmail.com',
        'password': 'your-app-password'  # Use app password for Gmail
    }

    automator = EmailAutomator(**email_config)

    if automator.connect():
        # Single email
        automator.send_email(
            to_email="recipient@example.com",
            subject="Test Email from Python",
            body="This is a test email sent using Python automation.",
            attachments=["report.pdf", "data.csv"]
        )

        # Bulk emails
        email_list = [
            {'email': 'user1@example.com', 'name': 'John', 'company': 'ABC Corp'},
            {'email': 'user2@example.com', 'name': 'Jane', 'company': 'XYZ Ltd'},
        ]

        body_template = """
        Dear {name},

        Thank you for your interest in our services at {company}.

        Best regards,
        Automation Team
        """

        automator.send_bulk_emails(
            email_list,
            "Welcome to Our Service",
            body_template
        )

        automator.close()

# email_automation_example()
```

### Email Reading & Processing:
```python
import imaplib
import email
from email.header import decode_header

class EmailReader:
    def __init__(self, imap_server, email_address, password):
        self.imap_server = imap_server
        self.email_address = email_address
        self.password = password
        self.mail = None

    def connect(self):
        """IMAP server এ connect করা"""
        try:
            self.mail = imaplib.IMAP4_SSL(self.imap_server)
            self.mail.login(self.email_address, self.password)
            print("✅ Email reader connected")
            return True
        except Exception as e:
            print(f"❌ Email reader connection failed: {e}")
            return False

    def get_unread_emails(self, folder="INBOX"):
        """Unread emails get করা"""

        try:
            self.mail.select(folder)

            # Search for unread emails
            status, messages = self.mail.search(None, 'UNSEEN')

            if status == "OK":
                email_ids = messages[0].split()
                print(f"📧 Found {len(email_ids)} unread emails")

                emails = []
                for email_id in email_ids:
                    email_data = self.get_email_content(email_id)
                    if email_data:
                        emails.append(email_data)

                return emails
            else:
                print("❌ Failed to search emails")
                return []

        except Exception as e:
            print(f"❌ Error getting unread emails: {e}")
            return []

    def get_email_content(self, email_id):
        """Email content extract করা"""

        try:
            status, msg_data = self.mail.fetch(email_id, '(RFC822)')

            if status == "OK":
                email_body = msg_data[0][1]
                email_message = email.message_from_bytes(email_body)

                # Extract email details
                subject = decode_header(email_message["Subject"])[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode()

                from_email = email_message.get("From")
                date = email_message.get("Date")

                # Extract body
                body = ""
                if email_message.is_multipart():
                    for part in email_message.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode()
                            break
                else:
                    body = email_message.get_payload(decode=True).decode()

                return {
                    'id': email_id.decode(),
                    'subject': subject,
                    'from': from_email,
                    'date': date,
                    'body': body[:500] + "..." if len(body) > 500 else body
                }

            return None

        except Exception as e:
            print(f"❌ Error extracting email content: {e}")
            return None

    def mark_as_read(self, email_id):
        """Email read হিসেবে mark করা"""
        try:
            self.mail.store(email_id, '+FLAGS', '\\Seen')
            return True
        except Exception as e:
            print(f"❌ Error marking email as read: {e}")
            return False

    def close(self):
        """Connection close করা"""
        if self.mail:
            self.mail.close()
            self.mail.logout()
            print("👋 Email reader disconnected")

# Usage
def email_reading_example():
    """Email reading automation"""

    reader = EmailReader(
        imap_server="imap.gmail.com",
        email_address="your-email@gmail.com",
        password="your-app-password"
    )

    if reader.connect():
        # Get unread emails
        unread_emails = reader.get_unread_emails()

        for email_data in unread_emails:
            print(f"\n📧 Email from: {email_data['from']}")
            print(f"📝 Subject: {email_data['subject']}")
            print(f"📅 Date: {email_data['date']}")
            print(f"💬 Body preview: {email_data['body'][:100]}...")

            # Mark as read
            reader.mark_as_read(email_data['id'])

        reader.close()

# email_reading_example()
```

---

## 📱 Social Media Automation {#social-media}

### Social Media Post Automation:
```python
class SocialMediaAutomator:
    def __init__(self, headless=True):
        self.headless = headless
        self.platforms = {}

    def setup_browser(self):
        """Browser setup for social media"""
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=self.headless,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-web-security",
                "--disable-features=VizDisplayCompositor"
            ]
        )

        # Use persistent context for login persistence
        self.context = self.browser.new_context(
            viewport={'width': 1366, 'height': 768},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )

        self.page = self.context.new_page()

    def login_facebook(self, email, password):
        """Facebook login automation"""

        try:
            print("🔐 Logging into Facebook...")

            self.page.goto("https://facebook.com/login")

            # Fill login form
            self.page.fill('#email', email)
            self.page.fill('#pass', password)

            # Submit login
            self.page.click('button[name="login"]')

            # Wait for login success
            self.page.wait_for_url('**/facebook.com/**', timeout=15000)

            # Check if login successful
            if self.page.locator('[data-testid="search"]').is_visible():
                print("✅ Facebook login successful")
                return True
            else:
                print("❌ Facebook login failed")
                return False

        except Exception as e:
            print(f"❌ Facebook login error: {e}")
            return False

    def post_to_facebook(self, text_content, image_path=None):
        """Facebook এ post করা"""

        try:
            print("📝 Posting to Facebook...")

            # Go to home page
            self.page.goto("https://facebook.com")

            # Click on "What's on your mind?" box
            post_box = self.page.locator('[data-testid="status-attachment-mentions-input"], [placeholder*="mind"]')
            post_box.click()

            # Wait for post composer
            self.page.wait_for_selector('[data-testid="tl_composer_editor"]', timeout=10000)

            # Type post content
            composer = self.page.locator('[data-testid="tl_composer_editor"]')
            composer.fill(text_content)

            # Add image if provided
            if image_path and os.path.exists(image_path):
                # Click photo/video button
                photo_button = self.page.locator('[data-testid="photo-video-button"]')
                photo_button.click()

                # Upload image
                file_input = self.page.locator('input[type="file"]')
                file_input.set_input_files(image_path)

                # Wait for image to upload
                self.page.wait_for_selector('[data-testid="media-manager-photo"]', timeout=15000)
                print("📸 Image uploaded")

            # Post the content
            post_button = self.page.locator('[data-testid="react-composer-post-button"]')
            post_button.click()

            # Wait for post to be published
            time.sleep(5)
            print("✅ Posted to Facebook successfully")
            return True

        except Exception as e:
            print(f"❌ Error posting to Facebook: {e}")
            return False

    def login_twitter(self, username, password):
        """Twitter/X login automation"""

        try:
            print("🔐 Logging into Twitter/X...")

            self.page.goto("https://twitter.com/login")

            # Enter username
            username_input = self.page.locator('input[name="text"]')
            username_input.fill(username)

            # Click Next
            self.page.click('div[role="button"]:has-text("Next")')

            # Enter password
            password_input = self.page.locator('input[name="password"]')
            password_input.fill(password)

            # Click Log in
            self.page.click('div[role="button"]:has-text("Log in")')

            # Wait for login success
            self.page.wait_for_url('**/home', timeout=15000)

            print("✅ Twitter login successful")
            return True

        except Exception as e:
            print(f"❌ Twitter login error: {e}")
            return False

    def post_to_twitter(self, text_content, image_path=None):
        """Twitter এ post করা"""

        try:
            print("📝 Posting to Twitter...")

            # Go to home page
            self.page.goto("https://twitter.com/home")

            # Click tweet compose box
            tweet_box = self.page.locator('[data-testid="tweetTextarea_0"]')
            tweet_box.click()
            tweet_box.fill(text_content)

            # Add image if provided
            if image_path and os.path.exists(image_path):
                # Click media button
                media_button = self.page.locator('[data-testid="fileInput"]')
                media_button.set_input_files(image_path)

                # Wait for image to upload
                self.page.wait_for_selector('[data-testid="removeMedia"]', timeout=15000)
                print("📸 Image uploaded to Twitter")

            # Tweet the content
            tweet_button = self.page.locator('[data-testid="tweetButtonInline"]')
            tweet_button.click()

            # Wait for tweet to be posted
            time.sleep(3)
            print("✅ Posted to Twitter successfully")
            return True

        except Exception as e:
            print(f"❌ Error posting to Twitter: {e}")
            return False

    def schedule_posts(self, posts_schedule):
        """Posts schedule করা"""

        import schedule

        for post_data in posts_schedule:
            schedule_time = post_data['time']  # Format: "10:30"
            platform = post_data['platform']
            content = post_data['content']
            image = post_data.get('image')

            if platform == 'facebook':
                schedule.every().day.at(schedule_time).do(
                    self.post_to_facebook, content, image
                )
            elif platform == 'twitter':
                schedule.every().day.at(schedule_time).do(
                    self.post_to_twitter, content, image
                )

        print(f"📅 Scheduled {len(posts_schedule)} posts")

        # Keep running to execute scheduled posts
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

    def close(self):
        """Cleanup"""
        if hasattr(self, 'browser'):
            self.browser.close()
        if hasattr(self, 'playwright'):
            self.playwright.stop()

# Usage
def social_media_automation_example():
    """Social media automation example"""

    automator = SocialMediaAutomator(headless=False)

    try:
        automator.setup_browser()

        # Login to platforms
        # automator.login_facebook("your-email@example.com", "your-password")
        # automator.login_twitter("your-username", "your-password")

        # Post content
        post_content = "Hello from Python automation! 🤖 #automation #python"

        # automator.post_to_facebook(post_content, "image.jpg")
        # automator.post_to_twitter(post_content, "image.jpg")

        # Schedule posts
        scheduled_posts = [
            {
                'time': '09:00',
                'platform': 'facebook',
                'content': 'Good morning! Starting the day with automation 🌅',
                'image': 'morning.jpg'
            },
            {
                'time': '18:00',
                'platform': 'twitter',
                'content': 'End of productive day! #productivity #automation',
                'image': None
            }
        ]

        # automator.schedule_posts(scheduled_posts)

    finally:
        automator.close()

# social_media_automation_example()
```

---

## 🧪 Testing & Monitoring {#testing-monitoring}

### Website Health Monitoring:
```python
import requests
import time
from datetime import datetime
import json

class WebsiteMonitor:
    def __init__(self):
        self.monitoring_data = []
        self.alerts = []

    def check_website_health(self, url, expected_status=200, timeout=10):
        """Website health check করা"""

        start_time = time.time()

        try:
            response = requests.get(url, timeout=timeout)
            response_time = (time.time() - start_time) * 1000  # Convert to ms

            health_data = {
                'url': url,
                'status_code': response.status_code,
                'response_time': round(response_time, 2),
                'timestamp': datetime.now().isoformat(),
                'is_healthy': response.status_code == expected_status,
                'content_length': len(response.content),
                'headers': dict(response.headers)
            }

            # Check for specific content
            if 'error' in response.text.lower() or 'exception' in response.text.lower():
                health_data['has_errors'] = True
                health_data['is_healthy'] = False
            else:
                health_data['has_errors'] = False

            self.monitoring_data.append(health_data)

            # Generate alerts
            if not health_data['is_healthy']:
                alert = {
                    'type': 'health_check_failed',
                    'url': url,
                    'status_code': response.status_code,
                    'timestamp': datetime.now().isoformat()
                }
                self.alerts.append(alert)
                print(f"🚨 ALERT: {url} health check failed - Status: {response.status_code}")

            if response_time > 5000:  # 5 seconds
                alert = {
                    'type': 'slow_response',
                    'url': url,
                    'response_time': response_time,
                    'timestamp': datetime.now().isoformat()
                }
                self.alerts.append(alert)
                print(f"⚠️ ALERT: {url} slow response - {response_time}ms")

            return health_data

        except requests.exceptions.RequestException as e:
            error_data = {
                'url': url,
                'error': str(e),
                'timestamp': datetime.now().isoformat(),
                'is_healthy': False
            }

            self.monitoring_data.append(error_data)

            alert = {
                'type': 'connection_error',
                'url': url,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
            self.alerts.append(alert)
            print(f"🚨 ALERT: {url} connection error - {e}")

            return error_data

    def monitor_multiple_sites(self, urls, interval=300):  # 5 minutes
        """Multiple websites monitor করা"""

        print(f"🔍 Starting monitoring for {len(urls)} websites...")
        print(f"⏰ Check interval: {interval} seconds")

        while True:
            print(f"\n📊 Health check at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            for url in urls:
                health_data = self.check_website_health(url)

                if health_data['is_healthy']:
                    print(f"✅ {url} - OK ({health_data['response_time']}ms)")
                else:
                    print(f"❌ {url} - FAILED")

            # Save monitoring data
            self.save_monitoring_data()

            # Wait for next check
            time.sleep(interval)

    def save_monitoring_data(self):
        """Monitoring data save করা"""

        timestamp = datetime.now().strftime("%Y%m%d")

        # Save health data
        with open(f"monitoring_data_{timestamp}.json", 'w') as f:
            json.dump(self.monitoring_data, f, indent=2)

        # Save alerts
        if self.alerts:
            with open(f"alerts_{timestamp}.json", 'w') as f:
                json.dump(self.alerts, f, indent=2)

    def generate_report(self):
        """Monitoring report generate করা"""

        if not self.monitoring_data:
            print("📊 No monitoring data available")
            return

        total_checks = len(self.monitoring_data)
        healthy_checks = sum(1 for data in self.monitoring_data if data.get('is_healthy', False))

        avg_response_time = sum(
            data.get('response_time', 0)
            for data in self.monitoring_data
            if 'response_time' in data
        ) / max(1, len([d for d in self.monitoring_data if 'response_time' in d]))

        print(f"\n📈 Monitoring Report:")
        print(f"  Total checks: {total_checks}")
        print(f"  Healthy checks: {healthy_checks}")
        print(f"  Success rate: {(healthy_checks/total_checks)*100:.1f}%")
        print(f"  Average response time: {avg_response_time:.2f}ms")
        print(f"  Total alerts: {len(self.alerts)}")

# Usage
def website_monitoring_example():
    """Website monitoring example"""

    monitor = WebsiteMonitor()

    # Websites to monitor
    websites = [
        "https://google.com",
        "https://github.com",
        "https://stackoverflow.com",
        "https://example.com"
    ]

    # Single health check
    for url in websites:
        health_data = monitor.check_website_health(url)
        print(f"Health check for {url}: {health_data}")

    # Generate report
    monitor.generate_report()

    # Continuous monitoring (uncomment to run)
    # monitor.monitor_multiple_sites(websites, interval=60)  # Check every minute

# website_monitoring_example()
```

---

## 🎉 সমাপনী

এই Web Automation Toolkit এ আপনি পেয়েছেন:

✅ **Form Automation:** Human-like form filling ও multi-step forms
✅ **File Operations:** Advanced upload/download automation
✅ **Screenshot & PDF:** Responsive screenshots ও custom PDFs
✅ **Email Automation:** Sending, reading, ও bulk email processing
✅ **Social Media:** Facebook, Twitter automation ও scheduling
✅ **Monitoring:** Website health monitoring ও alerting

### 🚀 Next Steps:
1. **Customize** করুন আপনার প্রয়োজন অনুযায়ী
2. **Combine** করুন different automation techniques
3. **Scale** করুন production environments এর জন্য
4. **Monitor** করুন automation performance

**Happy Automating! 🤖✨**
```
