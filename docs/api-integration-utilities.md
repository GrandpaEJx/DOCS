# 🔌 API Integration ও Utilities - Complete Guide

## 📚 সূচিপত্র
1. [REST API Integration](#rest-api)
2. [Webhook Handling](#webhooks)
3. [Notification Systems](#notifications)
4. [File Processing Utilities](#file-utilities)
5. [Scheduling & Automation](#scheduling)
6. [Error Handling & Logging](#error-handling)

---

## 🌐 REST API Integration {#rest-api}

### Advanced API Client:
```python
import requests
import json
import time
from datetime import datetime
import hashlib
import hmac
import base64
from urllib.parse import urlencode

class APIClient:
    def __init__(self, base_url, api_key=None, secret_key=None):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.secret_key = secret_key
        self.session = requests.Session()
        self.rate_limit_delay = 1  # seconds
        self.last_request_time = 0
        
        # Default headers
        self.session.headers.update({
            'User-Agent': 'Python-API-Client/1.0',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        
        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})
    
    def _rate_limit(self):
        """Rate limiting implementation"""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        if time_since_last < self.rate_limit_delay:
            sleep_time = self.rate_limit_delay - time_since_last
            time.sleep(sleep_time)
        
        self.last_request_time = time.time()
    
    def _generate_signature(self, method, endpoint, params=None, body=None):
        """Generate HMAC signature for authenticated requests"""
        
        if not self.secret_key:
            return None
        
        timestamp = str(int(time.time()))
        
        # Create string to sign
        string_to_sign = f"{method.upper()}\n{endpoint}\n{timestamp}"
        
        if params:
            query_string = urlencode(sorted(params.items()))
            string_to_sign += f"\n{query_string}"
        
        if body:
            if isinstance(body, dict):
                body = json.dumps(body, sort_keys=True)
            string_to_sign += f"\n{body}"
        
        # Generate signature
        signature = hmac.new(
            self.secret_key.encode(),
            string_to_sign.encode(),
            hashlib.sha256
        ).hexdigest()
        
        return {
            'timestamp': timestamp,
            'signature': signature
        }
    
    def request(self, method, endpoint, params=None, data=None, headers=None, auth_required=True):
        """Generic API request method"""
        
        self._rate_limit()
        
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        # Prepare headers
        request_headers = self.session.headers.copy()
        if headers:
            request_headers.update(headers)
        
        # Add authentication signature if required
        if auth_required and self.secret_key:
            auth_data = self._generate_signature(method, endpoint, params, data)
            if auth_data:
                request_headers.update({
                    'X-Timestamp': auth_data['timestamp'],
                    'X-Signature': auth_data['signature']
                })
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=data if isinstance(data, dict) else None,
                data=data if not isinstance(data, dict) else None,
                headers=request_headers,
                timeout=30
            )
            
            # Handle rate limiting
            if response.status_code == 429:
                retry_after = int(response.headers.get('Retry-After', 60))
                print(f"⚠️ Rate limited. Waiting {retry_after} seconds...")
                time.sleep(retry_after)
                return self.request(method, endpoint, params, data, headers, auth_required)
            
            response.raise_for_status()
            
            # Try to parse JSON response
            try:
                return response.json()
            except json.JSONDecodeError:
                return response.text
                
        except requests.exceptions.RequestException as e:
            print(f"❌ API request failed: {e}")
            return None
    
    def get(self, endpoint, params=None, **kwargs):
        """GET request"""
        return self.request('GET', endpoint, params=params, **kwargs)
    
    def post(self, endpoint, data=None, **kwargs):
        """POST request"""
        return self.request('POST', endpoint, data=data, **kwargs)
    
    def put(self, endpoint, data=None, **kwargs):
        """PUT request"""
        return self.request('PUT', endpoint, data=data, **kwargs)
    
    def delete(self, endpoint, **kwargs):
        """DELETE request"""
        return self.request('DELETE', endpoint, **kwargs)
    
    def paginated_get(self, endpoint, params=None, page_param='page', limit_param='limit', limit=100):
        """Paginated GET requests"""
        
        all_data = []
        page = 1
        
        while True:
            # Prepare pagination parameters
            page_params = params.copy() if params else {}
            page_params.update({
                page_param: page,
                limit_param: limit
            })
            
            print(f"📄 Fetching page {page}...")
            
            response = self.get(endpoint, params=page_params)
            
            if not response:
                break
            
            # Handle different response structures
            if isinstance(response, dict):
                if 'data' in response:
                    page_data = response['data']
                elif 'results' in response:
                    page_data = response['results']
                elif 'items' in response:
                    page_data = response['items']
                else:
                    page_data = response
            else:
                page_data = response
            
            if not page_data or len(page_data) == 0:
                break
            
            all_data.extend(page_data if isinstance(page_data, list) else [page_data])
            
            # Check if there are more pages
            if isinstance(response, dict):
                if 'has_more' in response and not response['has_more']:
                    break
                elif 'next_page' in response and not response['next_page']:
                    break
                elif len(page_data) < limit:
                    break
            
            page += 1
        
        print(f"✅ Fetched {len(all_data)} total items")
        return all_data

# Usage
def api_integration_example():
    """API integration example"""
    
    # Initialize API client
    client = APIClient(
        base_url="https://api.example.com/v1",
        api_key="your-api-key",
        secret_key="your-secret-key"
    )
    
    # Simple GET request
    users = client.get('/users')
    print(f"👥 Users: {len(users) if users else 0}")
    
    # POST request with data
    new_user = {
        "name": "John Doe",
        "email": "john@example.com",
        "role": "user"
    }
    
    created_user = client.post('/users', data=new_user)
    print(f"✅ Created user: {created_user}")
    
    # Paginated request
    all_posts = client.paginated_get('/posts', limit=50)
    print(f"📝 Total posts: {len(all_posts)}")

# api_integration_example()
```

### API Response Caching:
```python
import pickle
import os
from datetime import datetime, timedelta

class CachedAPIClient(APIClient):
    def __init__(self, *args, cache_dir="api_cache", cache_ttl=3600, **kwargs):
        super().__init__(*args, **kwargs)
        self.cache_dir = cache_dir
        self.cache_ttl = cache_ttl  # seconds
        
        # Create cache directory
        os.makedirs(cache_dir, exist_ok=True)
    
    def _get_cache_key(self, method, endpoint, params=None):
        """Generate cache key for request"""
        
        cache_data = f"{method}:{endpoint}"
        if params:
            cache_data += f":{json.dumps(params, sort_keys=True)}"
        
        return hashlib.md5(cache_data.encode()).hexdigest()
    
    def _get_cache_path(self, cache_key):
        """Get cache file path"""
        return os.path.join(self.cache_dir, f"{cache_key}.cache")
    
    def _is_cache_valid(self, cache_path):
        """Check if cache is still valid"""
        
        if not os.path.exists(cache_path):
            return False
        
        cache_time = datetime.fromtimestamp(os.path.getmtime(cache_path))
        expiry_time = cache_time + timedelta(seconds=self.cache_ttl)
        
        return datetime.now() < expiry_time
    
    def _save_to_cache(self, cache_path, data):
        """Save response to cache"""
        
        try:
            with open(cache_path, 'wb') as f:
                pickle.dump(data, f)
        except Exception as e:
            print(f"⚠️ Cache save failed: {e}")
    
    def _load_from_cache(self, cache_path):
        """Load response from cache"""
        
        try:
            with open(cache_path, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            print(f"⚠️ Cache load failed: {e}")
            return None
    
    def request(self, method, endpoint, params=None, data=None, use_cache=True, **kwargs):
        """Request with caching support"""
        
        # Only cache GET requests
        if method.upper() != 'GET' or not use_cache:
            return super().request(method, endpoint, params, data, **kwargs)
        
        # Check cache
        cache_key = self._get_cache_key(method, endpoint, params)
        cache_path = self._get_cache_path(cache_key)
        
        if self._is_cache_valid(cache_path):
            print(f"📦 Using cached response for {endpoint}")
            return self._load_from_cache(cache_path)
        
        # Make request
        response = super().request(method, endpoint, params, data, **kwargs)
        
        # Save to cache
        if response is not None:
            self._save_to_cache(cache_path, response)
            print(f"💾 Cached response for {endpoint}")
        
        return response
    
    def clear_cache(self, pattern=None):
        """Clear cache files"""
        
        cleared_count = 0
        
        for filename in os.listdir(self.cache_dir):
            if filename.endswith('.cache'):
                if pattern is None or pattern in filename:
                    file_path = os.path.join(self.cache_dir, filename)
                    os.remove(file_path)
                    cleared_count += 1
        
        print(f"🗑️ Cleared {cleared_count} cache files")

# Usage
def cached_api_example():
    """Cached API client example"""
    
    client = CachedAPIClient(
        base_url="https://jsonplaceholder.typicode.com",
        cache_ttl=1800  # 30 minutes
    )
    
    # First request - will be cached
    posts = client.get('/posts')
    print(f"📝 Posts: {len(posts) if posts else 0}")
    
    # Second request - will use cache
    posts_cached = client.get('/posts')
    print(f"📦 Cached posts: {len(posts_cached) if posts_cached else 0}")
    
    # Clear cache
    client.clear_cache()

# cached_api_example()
```

---

## 🔗 Webhook Handling {#webhooks}

### Webhook Server:
```python
from flask import Flask, request, jsonify
import threading
import json
from datetime import datetime

class WebhookServer:
    def __init__(self, host='localhost', port=5000):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.webhooks = {}
        self.webhook_logs = []
        
        self.setup_routes()
    
    def setup_routes(self):
        """Setup webhook routes"""
        
        @self.app.route('/webhook/<webhook_id>', methods=['POST'])
        def handle_webhook(webhook_id):
            try:
                # Get request data
                data = request.get_json() or {}
                headers = dict(request.headers)
                
                # Log webhook
                webhook_log = {
                    'webhook_id': webhook_id,
                    'timestamp': datetime.now().isoformat(),
                    'data': data,
                    'headers': headers,
                    'ip': request.remote_addr
                }
                
                self.webhook_logs.append(webhook_log)
                print(f"📨 Webhook received: {webhook_id}")
                
                # Process webhook if handler exists
                if webhook_id in self.webhooks:
                    handler = self.webhooks[webhook_id]
                    result = handler(data, headers)
                    
                    if result:
                        return jsonify(result)
                
                return jsonify({'status': 'received', 'webhook_id': webhook_id})
                
            except Exception as e:
                print(f"❌ Webhook error: {e}")
                return jsonify({'error': str(e)}), 500
        
        @self.app.route('/webhook-logs', methods=['GET'])
        def get_webhook_logs():
            return jsonify(self.webhook_logs)
        
        @self.app.route('/health', methods=['GET'])
        def health_check():
            return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})
    
    def register_webhook(self, webhook_id, handler_function):
        """Register webhook handler"""
        
        self.webhooks[webhook_id] = handler_function
        print(f"✅ Registered webhook handler: {webhook_id}")
    
    def start_server(self, debug=False):
        """Start webhook server"""
        
        def run_server():
            self.app.run(host=self.host, port=self.port, debug=debug)
        
        server_thread = threading.Thread(target=run_server)
        server_thread.daemon = True
        server_thread.start()
        
        print(f"🚀 Webhook server started at http://{self.host}:{self.port}")
        return server_thread

# Webhook handlers
def payment_webhook_handler(data, headers):
    """Handle payment webhooks"""
    
    print(f"💳 Payment webhook: {data.get('event_type')}")
    
    if data.get('event_type') == 'payment.completed':
        payment_id = data.get('payment_id')
        amount = data.get('amount')
        
        print(f"✅ Payment completed: {payment_id} - ${amount}")
        
        # Process payment completion
        # send_confirmation_email(data.get('customer_email'))
        # update_order_status(data.get('order_id'))
        
        return {'status': 'processed', 'payment_id': payment_id}
    
    return {'status': 'ignored'}

def user_webhook_handler(data, headers):
    """Handle user webhooks"""
    
    print(f"👤 User webhook: {data.get('action')}")
    
    if data.get('action') == 'user.created':
        user_id = data.get('user_id')
        email = data.get('email')
        
        print(f"🆕 New user created: {user_id} - {email}")
        
        # Process new user
        # send_welcome_email(email)
        # create_user_profile(user_id)
        
        return {'status': 'user_processed', 'user_id': user_id}
    
    return {'status': 'ignored'}

# Usage
def webhook_server_example():
    """Webhook server example"""
    
    # Create webhook server
    webhook_server = WebhookServer(host='0.0.0.0', port=8080)
    
    # Register webhook handlers
    webhook_server.register_webhook('payment', payment_webhook_handler)
    webhook_server.register_webhook('user', user_webhook_handler)
    
    # Start server
    server_thread = webhook_server.start_server()
    
    print("Webhook server is running...")
    print("Test webhooks:")
    print("  POST http://localhost:8080/webhook/payment")
    print("  POST http://localhost:8080/webhook/user")
    print("  GET  http://localhost:8080/webhook-logs")
    
    # Keep server running
    try:
        server_thread.join()
    except KeyboardInterrupt:
        print("\n👋 Webhook server stopped")

# webhook_server_example()
```

---

## 📢 Notification Systems {#notifications}

### Multi-Channel Notification System:
```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import json

class NotificationManager:
    def __init__(self):
        self.channels = {}
        self.templates = {}
        self.notification_log = []
    
    def add_email_channel(self, name, smtp_server, smtp_port, username, password):
        """Add email notification channel"""
        
        self.channels[name] = {
            'type': 'email',
            'config': {
                'smtp_server': smtp_server,
                'smtp_port': smtp_port,
                'username': username,
                'password': password
            }
        }
        
        print(f"📧 Email channel added: {name}")
    
    def add_slack_channel(self, name, webhook_url):
        """Add Slack notification channel"""
        
        self.channels[name] = {
            'type': 'slack',
            'config': {
                'webhook_url': webhook_url
            }
        }
        
        print(f"💬 Slack channel added: {name}")
    
    def add_discord_channel(self, name, webhook_url):
        """Add Discord notification channel"""
        
        self.channels[name] = {
            'type': 'discord',
            'config': {
                'webhook_url': webhook_url
            }
        }
        
        print(f"🎮 Discord channel added: {name}")
    
    def add_telegram_channel(self, name, bot_token, chat_id):
        """Add Telegram notification channel"""
        
        self.channels[name] = {
            'type': 'telegram',
            'config': {
                'bot_token': bot_token,
                'chat_id': chat_id
            }
        }
        
        print(f"📱 Telegram channel added: {name}")
    
    def add_template(self, name, subject_template, body_template):
        """Add notification template"""
        
        self.templates[name] = {
            'subject': subject_template,
            'body': body_template
        }
        
        print(f"📝 Template added: {name}")
    
    def send_email(self, config, to_email, subject, body):
        """Send email notification"""
        
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = config['username']
            msg['To'] = to_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email
            server = smtplib.SMTP(config['smtp_server'], config['smtp_port'])
            server.starttls()
            server.login(config['username'], config['password'])
            
            text = msg.as_string()
            server.sendmail(config['username'], to_email, text)
            server.quit()
            
            return True
            
        except Exception as e:
            print(f"❌ Email send failed: {e}")
            return False
    
    def send_slack(self, config, message):
        """Send Slack notification"""
        
        try:
            payload = {
                'text': message,
                'username': 'Notification Bot',
                'icon_emoji': ':robot_face:'
            }
            
            response = requests.post(
                config['webhook_url'],
                json=payload,
                timeout=10
            )
            
            return response.status_code == 200
            
        except Exception as e:
            print(f"❌ Slack send failed: {e}")
            return False
    
    def send_discord(self, config, message):
        """Send Discord notification"""
        
        try:
            payload = {
                'content': message,
                'username': 'Notification Bot'
            }
            
            response = requests.post(
                config['webhook_url'],
                json=payload,
                timeout=10
            )
            
            return response.status_code == 204
            
        except Exception as e:
            print(f"❌ Discord send failed: {e}")
            return False
    
    def send_telegram(self, config, message):
        """Send Telegram notification"""
        
        try:
            url = f"https://api.telegram.org/bot{config['bot_token']}/sendMessage"
            
            payload = {
                'chat_id': config['chat_id'],
                'text': message,
                'parse_mode': 'Markdown'
            }
            
            response = requests.post(url, json=payload, timeout=10)
            
            return response.status_code == 200
            
        except Exception as e:
            print(f"❌ Telegram send failed: {e}")
            return False
    
    def send_notification(self, channel_name, message, subject=None, recipient=None, template_name=None, template_data=None):
        """Send notification through specified channel"""
        
        if channel_name not in self.channels:
            print(f"❌ Channel not found: {channel_name}")
            return False
        
        channel = self.channels[channel_name]
        
        # Apply template if specified
        if template_name and template_name in self.templates:
            template = self.templates[template_name]
            
            if template_data:
                subject = template['subject'].format(**template_data)
                message = template['body'].format(**template_data)
            else:
                subject = template['subject']
                message = template['body']
        
        # Send notification based on channel type
        success = False
        
        if channel['type'] == 'email':
            if recipient and subject:
                success = self.send_email(channel['config'], recipient, subject, message)
        
        elif channel['type'] == 'slack':
            success = self.send_slack(channel['config'], message)
        
        elif channel['type'] == 'discord':
            success = self.send_discord(channel['config'], message)
        
        elif channel['type'] == 'telegram':
            success = self.send_telegram(channel['config'], message)
        
        # Log notification
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'channel': channel_name,
            'type': channel['type'],
            'success': success,
            'message': message[:100] + '...' if len(message) > 100 else message
        }
        
        self.notification_log.append(log_entry)
        
        if success:
            print(f"✅ Notification sent via {channel_name}")
        else:
            print(f"❌ Notification failed via {channel_name}")
        
        return success
    
    def broadcast_notification(self, message, channels=None, **kwargs):
        """Broadcast notification to multiple channels"""
        
        if channels is None:
            channels = list(self.channels.keys())
        
        results = {}
        
        for channel_name in channels:
            success = self.send_notification(channel_name, message, **kwargs)
            results[channel_name] = success
        
        successful_channels = sum(results.values())
        print(f"📡 Broadcast complete: {successful_channels}/{len(channels)} successful")
        
        return results

# Usage
def notification_system_example():
    """Notification system example"""
    
    notifier = NotificationManager()
    
    # Add channels
    notifier.add_email_channel(
        'gmail',
        'smtp.gmail.com',
        587,
        'your-email@gmail.com',
        'your-app-password'
    )
    
    notifier.add_slack_channel(
        'alerts',
        'https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK'
    )
    
    notifier.add_telegram_channel(
        'monitoring',
        'YOUR_BOT_TOKEN',
        'YOUR_CHAT_ID'
    )
    
    # Add templates
    notifier.add_template(
        'alert',
        'ALERT: {alert_type}',
        'Alert Details:\n\nType: {alert_type}\nMessage: {message}\nTime: {timestamp}\n\nPlease investigate immediately.'
    )
    
    notifier.add_template(
        'report',
        'Daily Report - {date}',
        'Daily Report Summary:\n\n- Total processed: {total_processed}\n- Errors: {error_count}\n- Success rate: {success_rate}%\n\nGenerated at: {timestamp}'
    )
    
    # Send individual notifications
    notifier.send_notification(
        'alerts',
        'System monitoring alert: High CPU usage detected!',
        template_name='alert',
        template_data={
            'alert_type': 'High CPU Usage',
            'message': 'CPU usage exceeded 90% for 5 minutes',
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    )
    
    # Broadcast notification
    notifier.broadcast_notification(
        'Scheduled maintenance will begin in 30 minutes.',
        channels=['alerts', 'monitoring']
    )
    
    print(f"📊 Notification log: {len(notifier.notification_log)} entries")

# notification_system_example()
```

---

## 📁 File Processing Utilities {#file-utilities}

### Advanced File Operations:
```python
import os
import shutil
import zipfile
import tarfile
import hashlib
from pathlib import Path
import mimetypes
from datetime import datetime

class FileProcessor:
    def __init__(self, base_dir="."):
        self.base_dir = Path(base_dir)
        self.processed_files = []
        self.file_stats = {}

    def scan_directory(self, directory, extensions=None, recursive=True):
        """Directory scan করে files list করা"""

        directory = Path(directory)
        files_found = []

        if recursive:
            pattern = "**/*"
        else:
            pattern = "*"

        for file_path in directory.glob(pattern):
            if file_path.is_file():
                if extensions is None or file_path.suffix.lower() in extensions:
                    file_info = {
                        'path': str(file_path),
                        'name': file_path.name,
                        'size': file_path.stat().st_size,
                        'modified': datetime.fromtimestamp(file_path.stat().st_mtime),
                        'extension': file_path.suffix.lower(),
                        'mime_type': mimetypes.guess_type(str(file_path))[0]
                    }
                    files_found.append(file_info)

        print(f"📁 Found {len(files_found)} files in {directory}")
        return files_found

    def calculate_file_hash(self, file_path, algorithm='md5'):
        """File hash calculate করা"""

        hash_algorithms = {
            'md5': hashlib.md5(),
            'sha1': hashlib.sha1(),
            'sha256': hashlib.sha256()
        }

        if algorithm not in hash_algorithms:
            print(f"❌ Unsupported hash algorithm: {algorithm}")
            return None

        hash_obj = hash_algorithms[algorithm]

        try:
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_obj.update(chunk)

            return hash_obj.hexdigest()

        except Exception as e:
            print(f"❌ Error calculating hash for {file_path}: {e}")
            return None

    def find_duplicate_files(self, directory):
        """Duplicate files খুঁজে বের করা"""

        files = self.scan_directory(directory)
        hash_map = {}
        duplicates = []

        print("🔍 Calculating file hashes...")

        for file_info in files:
            file_hash = self.calculate_file_hash(file_info['path'])

            if file_hash:
                if file_hash in hash_map:
                    # Duplicate found
                    duplicates.append({
                        'original': hash_map[file_hash],
                        'duplicate': file_info,
                        'hash': file_hash
                    })
                else:
                    hash_map[file_hash] = file_info

        print(f"🔄 Found {len(duplicates)} duplicate files")
        return duplicates

    def organize_files_by_type(self, source_dir, target_dir):
        """Files কে type অনুযায়ী organize করা"""

        file_type_mapping = {
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
            'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
            'spreadsheets': ['.xls', '.xlsx', '.csv', '.ods'],
            'presentations': ['.ppt', '.pptx', '.odp'],
            'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
            'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
            'archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c']
        }

        source_path = Path(source_dir)
        target_path = Path(target_dir)

        # Create target directories
        for category in file_type_mapping.keys():
            (target_path / category).mkdir(parents=True, exist_ok=True)

        # Create 'others' directory
        (target_path / 'others').mkdir(parents=True, exist_ok=True)

        files = self.scan_directory(source_dir, recursive=False)
        organized_count = 0

        for file_info in files:
            file_path = Path(file_info['path'])
            extension = file_info['extension']

            # Find appropriate category
            target_category = 'others'
            for category, extensions in file_type_mapping.items():
                if extension in extensions:
                    target_category = category
                    break

            # Move file
            target_file_path = target_path / target_category / file_path.name

            try:
                shutil.move(str(file_path), str(target_file_path))
                organized_count += 1
                print(f"📁 Moved {file_path.name} to {target_category}/")

            except Exception as e:
                print(f"❌ Error moving {file_path.name}: {e}")

        print(f"✅ Organized {organized_count} files")
        return organized_count

    def create_archive(self, source_paths, archive_path, archive_type='zip'):
        """Archive তৈরি করা"""

        try:
            if archive_type == 'zip':
                with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    for source_path in source_paths:
                        source = Path(source_path)

                        if source.is_file():
                            zipf.write(source, source.name)
                        elif source.is_dir():
                            for file_path in source.rglob('*'):
                                if file_path.is_file():
                                    arcname = file_path.relative_to(source.parent)
                                    zipf.write(file_path, arcname)

            elif archive_type == 'tar':
                with tarfile.open(archive_path, 'w:gz') as tarf:
                    for source_path in source_paths:
                        source = Path(source_path)
                        tarf.add(source, arcname=source.name)

            print(f"📦 Archive created: {archive_path}")
            return True

        except Exception as e:
            print(f"❌ Archive creation failed: {e}")
            return False

    def extract_archive(self, archive_path, extract_to):
        """Archive extract করা"""

        archive_path = Path(archive_path)
        extract_path = Path(extract_to)

        try:
            if archive_path.suffix == '.zip':
                with zipfile.ZipFile(archive_path, 'r') as zipf:
                    zipf.extractall(extract_path)

            elif archive_path.suffix in ['.tar', '.gz', '.tgz']:
                with tarfile.open(archive_path, 'r:*') as tarf:
                    tarf.extractall(extract_path)

            print(f"📂 Archive extracted to: {extract_path}")
            return True

        except Exception as e:
            print(f"❌ Archive extraction failed: {e}")
            return False

    def batch_rename_files(self, directory, pattern, replacement):
        """Batch file rename করা"""

        files = self.scan_directory(directory, recursive=False)
        renamed_count = 0

        for file_info in files:
            file_path = Path(file_info['path'])
            old_name = file_path.name

            if pattern in old_name:
                new_name = old_name.replace(pattern, replacement)
                new_path = file_path.parent / new_name

                try:
                    file_path.rename(new_path)
                    renamed_count += 1
                    print(f"📝 Renamed: {old_name} → {new_name}")

                except Exception as e:
                    print(f"❌ Error renaming {old_name}: {e}")

        print(f"✅ Renamed {renamed_count} files")
        return renamed_count

    def clean_empty_directories(self, directory):
        """Empty directories clean করা"""

        directory = Path(directory)
        removed_count = 0

        # Walk directory tree bottom-up
        for dir_path in sorted(directory.rglob('*'), key=lambda p: len(p.parts), reverse=True):
            if dir_path.is_dir():
                try:
                    # Try to remove if empty
                    dir_path.rmdir()
                    removed_count += 1
                    print(f"🗑️ Removed empty directory: {dir_path}")

                except OSError:
                    # Directory not empty, skip
                    pass

        print(f"✅ Removed {removed_count} empty directories")
        return removed_count

# Usage
def file_processing_example():
    """File processing utilities example"""

    processor = FileProcessor()

    # Scan directory
    files = processor.scan_directory("./test_files", extensions=['.txt', '.py', '.json'])

    # Find duplicates
    duplicates = processor.find_duplicate_files("./test_files")

    # Organize files
    processor.organize_files_by_type("./messy_folder", "./organized_folder")

    # Create archive
    processor.create_archive(
        ["./file1.txt", "./file2.py", "./folder1"],
        "./backup.zip",
        archive_type='zip'
    )

    # Extract archive
    processor.extract_archive("./backup.zip", "./extracted")

    # Batch rename
    processor.batch_rename_files("./test_files", "old_", "new_")

    # Clean empty directories
    processor.clean_empty_directories("./test_files")

# file_processing_example()
```

---

## ⏰ Scheduling & Automation {#scheduling}

### Advanced Task Scheduler:
```python
import schedule
import threading
import time
from datetime import datetime, timedelta
import json
import sqlite3

class TaskScheduler:
    def __init__(self, db_path="scheduler.db"):
        self.db_path = db_path
        self.running = False
        self.scheduler_thread = None
        self.tasks = {}

        self.init_database()

    def init_database(self):
        """Initialize scheduler database"""

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scheduled_tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_name TEXT UNIQUE,
                schedule_type TEXT,
                schedule_value TEXT,
                function_name TEXT,
                parameters TEXT,
                last_run DATETIME,
                next_run DATETIME,
                run_count INTEGER DEFAULT 0,
                is_active BOOLEAN DEFAULT 1,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS task_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_name TEXT,
                execution_time DATETIME,
                status TEXT,
                result TEXT,
                error_message TEXT,
                duration_seconds REAL
            )
        ''')

        conn.commit()
        conn.close()

    def add_task(self, task_name, schedule_type, schedule_value, function, parameters=None):
        """Add scheduled task"""

        if parameters is None:
            parameters = {}

        # Store task function
        self.tasks[task_name] = {
            'function': function,
            'parameters': parameters
        }

        # Save to database
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT OR REPLACE INTO scheduled_tasks
            (task_name, schedule_type, schedule_value, function_name, parameters)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            task_name,
            schedule_type,
            schedule_value,
            function.__name__,
            json.dumps(parameters)
        ))

        conn.commit()
        conn.close()

        # Schedule the task
        self._schedule_task(task_name, schedule_type, schedule_value, function, parameters)

        print(f"📅 Task scheduled: {task_name} ({schedule_type}: {schedule_value})")

    def _schedule_task(self, task_name, schedule_type, schedule_value, function, parameters):
        """Internal method to schedule task"""

        def wrapped_function():
            self._execute_task(task_name, function, parameters)

        if schedule_type == 'interval':
            # Every X seconds
            schedule.every(int(schedule_value)).seconds.do(wrapped_function)

        elif schedule_type == 'daily':
            # Daily at specific time
            schedule.every().day.at(schedule_value).do(wrapped_function)

        elif schedule_type == 'weekly':
            # Weekly on specific day and time
            day, time_str = schedule_value.split(' ')
            getattr(schedule.every(), day.lower()).at(time_str).do(wrapped_function)

        elif schedule_type == 'hourly':
            # Every hour at specific minute
            schedule.every().hour.at(f":{schedule_value:02d}").do(wrapped_function)

        elif schedule_type == 'cron':
            # Cron-like scheduling (simplified)
            # Format: "minute hour day month weekday"
            print(f"⚠️ Cron scheduling not fully implemented: {schedule_value}")

    def _execute_task(self, task_name, function, parameters):
        """Execute scheduled task"""

        start_time = time.time()
        execution_time = datetime.now()

        try:
            print(f"🚀 Executing task: {task_name}")

            # Execute function
            if parameters:
                result = function(**parameters)
            else:
                result = function()

            duration = time.time() - start_time

            # Log successful execution
            self._log_task_execution(
                task_name, execution_time, 'SUCCESS',
                str(result)[:500] if result else None, None, duration
            )

            # Update task statistics
            self._update_task_stats(task_name, execution_time)

            print(f"✅ Task completed: {task_name} ({duration:.2f}s)")

        except Exception as e:
            duration = time.time() - start_time

            # Log failed execution
            self._log_task_execution(
                task_name, execution_time, 'ERROR',
                None, str(e), duration
            )

            print(f"❌ Task failed: {task_name} - {e}")

    def _log_task_execution(self, task_name, execution_time, status, result, error, duration):
        """Log task execution"""

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO task_logs
            (task_name, execution_time, status, result, error_message, duration_seconds)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (task_name, execution_time, status, result, error, duration))

        conn.commit()
        conn.close()

    def _update_task_stats(self, task_name, execution_time):
        """Update task statistics"""

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE scheduled_tasks
            SET last_run = ?, run_count = run_count + 1
            WHERE task_name = ?
        ''', (execution_time, task_name))

        conn.commit()
        conn.close()

    def start_scheduler(self):
        """Start task scheduler"""

        if self.running:
            print("⚠️ Scheduler is already running")
            return

        self.running = True

        def run_scheduler():
            print("🚀 Task scheduler started")

            while self.running:
                schedule.run_pending()
                time.sleep(1)

            print("👋 Task scheduler stopped")

        self.scheduler_thread = threading.Thread(target=run_scheduler)
        self.scheduler_thread.daemon = True
        self.scheduler_thread.start()

    def stop_scheduler(self):
        """Stop task scheduler"""

        self.running = False

        if self.scheduler_thread:
            self.scheduler_thread.join(timeout=5)

        print("🛑 Scheduler stopped")

    def get_task_status(self):
        """Get status of all tasks"""

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT task_name, schedule_type, schedule_value, last_run,
                   run_count, is_active
            FROM scheduled_tasks
            ORDER BY task_name
        ''')

        tasks = cursor.fetchall()
        conn.close()

        print("📊 Task Status:")
        for task in tasks:
            print(f"  {task[0]}: {task[1]} {task[2]} | Runs: {task[4]} | Active: {task[5]}")

        return tasks

    def get_task_logs(self, task_name=None, limit=10):
        """Get task execution logs"""

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if task_name:
            cursor.execute('''
                SELECT task_name, execution_time, status, duration_seconds, error_message
                FROM task_logs
                WHERE task_name = ?
                ORDER BY execution_time DESC
                LIMIT ?
            ''', (task_name, limit))
        else:
            cursor.execute('''
                SELECT task_name, execution_time, status, duration_seconds, error_message
                FROM task_logs
                ORDER BY execution_time DESC
                LIMIT ?
            ''', (limit,))

        logs = cursor.fetchall()
        conn.close()

        return logs

# Example scheduled functions
def backup_database():
    """Example backup function"""
    print("💾 Performing database backup...")
    # Simulate backup process
    time.sleep(2)
    return "Database backup completed"

def send_daily_report():
    """Example report function"""
    print("📊 Generating daily report...")
    # Simulate report generation
    time.sleep(1)
    return "Daily report sent"

def cleanup_temp_files():
    """Example cleanup function"""
    print("🧹 Cleaning up temporary files...")
    # Simulate cleanup
    time.sleep(0.5)
    return "Temp files cleaned"

def monitor_system_health():
    """Example monitoring function"""
    print("🔍 Checking system health...")
    # Simulate health check
    import random
    if random.random() > 0.9:  # 10% chance of "failure"
        raise Exception("System health check failed")
    return "System is healthy"

# Usage
def scheduling_example():
    """Task scheduling example"""

    scheduler = TaskScheduler()

    # Add various scheduled tasks
    scheduler.add_task(
        'daily_backup',
        'daily',
        '02:00',  # 2 AM daily
        backup_database
    )

    scheduler.add_task(
        'hourly_health_check',
        'interval',
        '3600',  # Every hour
        monitor_system_health
    )

    scheduler.add_task(
        'daily_report',
        'daily',
        '09:00',  # 9 AM daily
        send_daily_report
    )

    scheduler.add_task(
        'weekly_cleanup',
        'weekly',
        'sunday 01:00',  # Sunday 1 AM
        cleanup_temp_files
    )

    # Start scheduler
    scheduler.start_scheduler()

    # Get task status
    scheduler.get_task_status()

    # Run for a while (in real usage, this would run indefinitely)
    print("Scheduler running... Press Ctrl+C to stop")

    try:
        time.sleep(60)  # Run for 1 minute for demo
    except KeyboardInterrupt:
        pass

    # Stop scheduler
    scheduler.stop_scheduler()

    # Show logs
    logs = scheduler.get_task_logs(limit=5)
    print(f"\n📋 Recent task logs: {len(logs)} entries")

# scheduling_example()
```

---

## 🚨 Error Handling & Logging {#error-handling}

### Advanced Error Handling System:
```python
import logging
import traceback
import functools
import sys
from datetime import datetime
import json
import smtplib
from email.mime.text import MIMEText

class ErrorHandler:
    def __init__(self, log_file="application.log", email_alerts=None):
        self.log_file = log_file
        self.email_alerts = email_alerts
        self.error_counts = {}

        self.setup_logging()

    def setup_logging(self):
        """Setup comprehensive logging"""

        # Create logger
        self.logger = logging.getLogger('ApplicationLogger')
        self.logger.setLevel(logging.DEBUG)

        # Clear existing handlers
        self.logger.handlers.clear()

        # File handler
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(logging.DEBUG)

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)8s | %(name)s | %(funcName)s:%(lineno)d | %(message)s'
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

        print(f"📝 Logging setup complete: {self.log_file}")

    def log_error(self, error, context=None, severity='ERROR'):
        """Log error with context"""

        error_info = {
            'timestamp': datetime.now().isoformat(),
            'error_type': type(error).__name__,
            'error_message': str(error),
            'traceback': traceback.format_exc(),
            'context': context or {},
            'severity': severity
        }

        # Log to file
        self.logger.error(f"Error occurred: {error_info}")

        # Track error counts
        error_key = f"{error_info['error_type']}:{error_info['error_message']}"
        self.error_counts[error_key] = self.error_counts.get(error_key, 0) + 1

        # Send email alert for critical errors
        if severity == 'CRITICAL' and self.email_alerts:
            self.send_error_alert(error_info)

        return error_info

    def send_error_alert(self, error_info):
        """Send email alert for critical errors"""

        try:
            subject = f"CRITICAL ERROR: {error_info['error_type']}"

            body = f"""
Critical Error Alert

Time: {error_info['timestamp']}
Error Type: {error_info['error_type']}
Message: {error_info['error_message']}

Context:
{json.dumps(error_info['context'], indent=2)}

Traceback:
{error_info['traceback']}

Please investigate immediately.
            """

            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = self.email_alerts['from']
            msg['To'] = ', '.join(self.email_alerts['to'])

            # Send email
            server = smtplib.SMTP(self.email_alerts['smtp_server'], self.email_alerts['smtp_port'])
            server.starttls()
            server.login(self.email_alerts['username'], self.email_alerts['password'])
            server.send_message(msg)
            server.quit()

            self.logger.info("📧 Critical error alert sent")

        except Exception as e:
            self.logger.error(f"Failed to send error alert: {e}")

    def retry_decorator(self, max_retries=3, delay=1, backoff=2, exceptions=(Exception,)):
        """Retry decorator with exponential backoff"""

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                retries = 0
                current_delay = delay

                while retries < max_retries:
                    try:
                        return func(*args, **kwargs)

                    except exceptions as e:
                        retries += 1

                        if retries >= max_retries:
                            self.log_error(
                                e,
                                context={
                                    'function': func.__name__,
                                    'args': str(args)[:200],
                                    'kwargs': str(kwargs)[:200],
                                    'retries': retries
                                },
                                severity='ERROR'
                            )
                            raise

                        self.logger.warning(
                            f"Retry {retries}/{max_retries} for {func.__name__}: {e}"
                        )

                        time.sleep(current_delay)
                        current_delay *= backoff

                return None

            return wrapper
        return decorator

    def exception_handler(self, func):
        """Exception handling decorator"""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)

            except Exception as e:
                error_info = self.log_error(
                    e,
                    context={
                        'function': func.__name__,
                        'args': str(args)[:200],
                        'kwargs': str(kwargs)[:200]
                    }
                )

                # Return None or raise based on configuration
                return None

        return wrapper

    def get_error_summary(self):
        """Get error summary statistics"""

        total_errors = sum(self.error_counts.values())

        summary = {
            'total_errors': total_errors,
            'unique_errors': len(self.error_counts),
            'top_errors': sorted(
                self.error_counts.items(),
                key=lambda x: x[1],
                reverse=True
            )[:10]
        }

        self.logger.info(f"Error Summary: {summary}")
        return summary

# Global error handler instance
error_handler = ErrorHandler(
    log_file="app_errors.log",
    email_alerts={
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587,
        'username': 'your-email@gmail.com',
        'password': 'your-app-password',
        'from': 'your-email@gmail.com',
        'to': ['admin@example.com']
    }
)

# Usage examples
@error_handler.exception_handler
def risky_function(data):
    """Function that might fail"""

    if not data:
        raise ValueError("Data cannot be empty")

    if len(data) < 5:
        raise ValueError("Data too short")

    # Simulate processing
    result = data.upper()
    return result

@error_handler.retry_decorator(max_retries=3, delay=1)
def unreliable_api_call():
    """Simulate unreliable API call"""

    import random

    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("API temporarily unavailable")

    return {"status": "success", "data": "API response"}

# Context manager for error handling
class ErrorContext:
    def __init__(self, operation_name, error_handler):
        self.operation_name = operation_name
        self.error_handler = error_handler
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        self.error_handler.logger.info(f"🚀 Starting operation: {self.operation_name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start_time

        if exc_type is None:
            self.error_handler.logger.info(
                f"✅ Operation completed: {self.operation_name} ({duration:.2f}s)"
            )
        else:
            self.error_handler.log_error(
                exc_val,
                context={
                    'operation': self.operation_name,
                    'duration': duration
                },
                severity='ERROR'
            )

        # Don't suppress exceptions
        return False

# Usage
def error_handling_example():
    """Error handling system example"""

    # Test exception handler
    print("Testing exception handler...")
    result1 = risky_function("hello world")
    result2 = risky_function("")  # Will cause error

    # Test retry decorator
    print("\nTesting retry decorator...")
    try:
        api_result = unreliable_api_call()
        print(f"API Result: {api_result}")
    except Exception as e:
        print(f"API call failed after retries: {e}")

    # Test context manager
    print("\nTesting context manager...")

    with ErrorContext("data_processing", error_handler):
        # Simulate some work
        time.sleep(1)
        print("Processing data...")

    with ErrorContext("failing_operation", error_handler):
        # Simulate failure
        raise RuntimeError("Something went wrong")

    # Get error summary
    summary = error_handler.get_error_summary()
    print(f"\n📊 Error Summary: {summary}")

# error_handling_example()
```

---

## 🎉 সমাপনী

এই API Integration ও Utilities গাইডে আপনি পেয়েছেন:

✅ **REST API Integration:** Advanced client with authentication ও caching
✅ **Webhook Handling:** Complete webhook server ও processing
✅ **Notification Systems:** Multi-channel notifications (Email, Slack, Discord, Telegram)
✅ **File Processing:** Advanced file operations, organization ও archiving
✅ **Task Scheduling:** Comprehensive scheduler with database logging
✅ **Error Handling:** Professional error management ও logging system

### 🚀 Key Features:

#### **API Integration:**
- Rate limiting ও retry mechanisms
- HMAC signature authentication
- Response caching system
- Paginated data fetching

#### **Webhook System:**
- Multi-endpoint webhook server
- Request logging ও processing
- Custom handler registration
- Health monitoring

#### **Notification System:**
- Multiple channels support
- Template-based messaging
- Broadcast capabilities
- Delivery tracking

#### **File Processing:**
- Duplicate detection
- Automatic organization
- Archive creation/extraction
- Batch operations

#### **Task Scheduling:**
- Database-backed scheduling
- Multiple schedule types
- Execution logging
- Error tracking

#### **Error Handling:**
- Comprehensive logging
- Retry mechanisms
- Email alerts
- Error statistics

### 📈 Integration Examples:

```python
# Complete automation workflow
def automated_workflow():
    """Example of integrated automation"""

    # 1. API data collection
    api_client = CachedAPIClient("https://api.example.com")
    data = api_client.paginated_get("/data")

    # 2. File processing
    processor = FileProcessor()
    processor.organize_files_by_type("./downloads", "./organized")

    # 3. Notification
    notifier = NotificationManager()
    notifier.broadcast_notification(f"Processed {len(data)} records")

    # 4. Scheduling next run
    scheduler = TaskScheduler()
    scheduler.add_task("daily_workflow", "daily", "02:00", automated_workflow)
```

### 🎯 Next Steps:
1. **Customize** করুন আপনার specific needs অনুযায়ী
2. **Integrate** করুন existing systems এর সাথে
3. **Monitor** করুন performance ও errors
4. **Scale** করুন production environments এর জন্য

**Happy Integrating! 🔌🚀**
```
```
