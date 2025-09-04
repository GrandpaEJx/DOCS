# ⏰ Schedule - সম্পূর্ণ বাংলা গাইড

## 🌟 Schedule কি?

Schedule হলো Python এর একটি **simple job scheduling library** যা দিয়ে আপনি সহজেই periodic tasks, automated jobs ও time-based operations করতে পারেন।

### 🎯 **মূল বৈশিষ্ট্য:**
- ✅ **Simple syntax** - Human-friendly scheduling
- ✅ **Flexible timing** - Seconds, minutes, hours, days, weeks
- ✅ **Job management** - Start, stop, cancel jobs
- ✅ **Decorator support** - Easy function scheduling
- ✅ **Thread-safe** - Concurrent job execution
- ✅ **Lightweight** - No external dependencies

---

## 🚀 Installation ও Setup

### 📦 **Installation:**
```bash
# Schedule install
pip install schedule>=1.2.0

# Verify installation
python -c "import schedule; print('Schedule installed successfully!')"
```

### ✅ **Installation Verify:**
```python
# test_schedule.py
import schedule
import time
from datetime import datetime

def test_job():
    print(f"✅ Test job executed at {datetime.now().strftime('%H:%M:%S')}")

def test_schedule():
    print("🧪 Schedule installation test...")
    
    # Schedule a test job
    schedule.every(2).seconds.do(test_job)
    
    print("⏰ Running scheduler for 10 seconds...")
    start_time = time.time()
    
    while time.time() - start_time < 10:
        schedule.run_pending()
        time.sleep(1)
    
    print("🎉 Schedule working perfectly!")

test_schedule()
```

---

## ⏰ Basic Scheduling

### 📅 **Time-based Scheduling:**
```python
import schedule
import time
from datetime import datetime

def basic_scheduling():
    """Basic scheduling examples"""
    
    # Define job functions
    def job_every_second():
        print(f"🔄 Every second: {datetime.now().strftime('%H:%M:%S')}")
    
    def job_every_minute():
        print(f"⏰ Every minute: {datetime.now().strftime('%H:%M:%S')}")
    
    def job_every_hour():
        print(f"🕐 Every hour: {datetime.now().strftime('%H:%M:%S')}")
    
    def job_daily():
        print(f"📅 Daily job: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    def job_weekly():
        print(f"📆 Weekly job: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Schedule jobs with different intervals
    print("⏰ Setting up basic schedules...")
    
    # Every N seconds/minutes/hours
    schedule.every(5).seconds.do(job_every_second)
    schedule.every(1).minutes.do(job_every_minute)
    schedule.every(1).hours.do(job_every_hour)
    
    # Daily and weekly
    schedule.every().day.do(job_daily)
    schedule.every().week.do(job_weekly)
    
    # Specific times
    schedule.every().day.at("09:00").do(job_daily)
    schedule.every().monday.at("10:30").do(job_weekly)
    
    # Run scheduler
    print("🚀 Scheduler started. Running for 30 seconds...")
    start_time = time.time()
    
    while time.time() - start_time < 30:
        schedule.run_pending()
        time.sleep(1)
    
    print("✅ Basic scheduling demo completed")

basic_scheduling()
```

### 🎯 **Advanced Scheduling Patterns:**
```python
def advanced_scheduling():
    """Advanced scheduling patterns"""
    
    # Job functions with parameters
    def parameterized_job(name, value):
        print(f"📊 Job '{name}' executed with value: {value}")
    
    def conditional_job():
        current_hour = datetime.now().hour
        if 9 <= current_hour <= 17:  # Business hours
            print(f"💼 Business hours job: {datetime.now().strftime('%H:%M:%S')}")
        else:
            print(f"🌙 After hours job: {datetime.now().strftime('%H:%M:%S')}")
    
    def data_backup_job():
        print(f"💾 Data backup started: {datetime.now().strftime('%H:%M:%S')}")
        # Simulate backup process
        time.sleep(2)
        print(f"✅ Data backup completed: {datetime.now().strftime('%H:%M:%S')}")
    
    def cleanup_job():
        print(f"🧹 Cleanup job: {datetime.now().strftime('%H:%M:%S')}")
    
    # Schedule with parameters using lambda
    schedule.every(10).seconds.do(lambda: parameterized_job("DataSync", 42))
    schedule.every(15).seconds.do(lambda: parameterized_job("HealthCheck", "OK"))
    
    # Conditional scheduling
    schedule.every(5).seconds.do(conditional_job)
    
    # Different days of week
    schedule.every().monday.at("09:00").do(data_backup_job)
    schedule.every().tuesday.at("09:00").do(data_backup_job)
    schedule.every().wednesday.at("09:00").do(data_backup_job)
    schedule.every().thursday.at("09:00").do(data_backup_job)
    schedule.every().friday.at("09:00").do(data_backup_job)
    
    # Weekend cleanup
    schedule.every().saturday.at("02:00").do(cleanup_job)
    schedule.every().sunday.at("02:00").do(cleanup_job)
    
    # Multiple times per day
    for hour in [6, 12, 18]:
        schedule.every().day.at(f"{hour:02d}:00").do(
            lambda h=hour: print(f"🔔 Reminder at {h}:00")
        )
    
    print("⚙️ Advanced schedules configured")
    
    # Show all scheduled jobs
    print("\n📋 Scheduled Jobs:")
    for job in schedule.jobs:
        print(f"  - {job}")
    
    # Run for demonstration
    print("\n🚀 Running advanced scheduler for 60 seconds...")
    start_time = time.time()
    
    while time.time() - start_time < 60:
        schedule.run_pending()
        time.sleep(1)
    
    print("✅ Advanced scheduling demo completed")

advanced_scheduling()
```

---

## 🔧 Job Management

### 📋 **Job Control:**
```python
def job_management():
    """Job management and control"""
    
    # Job functions
    def task_a():
        print(f"🅰️ Task A: {datetime.now().strftime('%H:%M:%S')}")
    
    def task_b():
        print(f"🅱️ Task B: {datetime.now().strftime('%H:%M:%S')}")
    
    def task_c():
        print(f"🅲 Task C: {datetime.now().strftime('%H:%M:%S')}")
    
    def one_time_task():
        print(f"🎯 One-time task executed: {datetime.now().strftime('%H:%M:%S')}")
        return schedule.CancelJob  # Cancel this job after execution
    
    # Schedule jobs and store references
    job_a = schedule.every(3).seconds.do(task_a)
    job_b = schedule.every(5).seconds.do(task_b)
    job_c = schedule.every(7).seconds.do(task_c)
    
    # One-time job that cancels itself
    one_time_job = schedule.every(10).seconds.do(one_time_task)
    
    print("📋 Job Management Demo")
    print(f"Total jobs scheduled: {len(schedule.jobs)}")
    
    # Run for 20 seconds
    print("🚀 Running all jobs for 20 seconds...")
    start_time = time.time()
    
    while time.time() - start_time < 20:
        schedule.run_pending()
        time.sleep(1)
        
        # Cancel job_b after 15 seconds
        if time.time() - start_time > 15 and job_b in schedule.jobs:
            schedule.cancel_job(job_b)
            print("❌ Job B cancelled")
    
    print(f"Jobs remaining: {len(schedule.jobs)}")
    
    # Clear all jobs
    schedule.clear()
    print("🧹 All jobs cleared")
    print(f"Jobs after clear: {len(schedule.jobs)}")

job_management()
```

### 🏷️ **Job Tags ও Filtering:**
```python
def job_tags_and_filtering():
    """Job tagging and filtering"""
    
    # Job functions
    def database_backup():
        print(f"💾 Database backup: {datetime.now().strftime('%H:%M:%S')}")
    
    def send_report():
        print(f"📊 Sending report: {datetime.now().strftime('%H:%M:%S')}")
    
    def cleanup_logs():
        print(f"🧹 Cleaning logs: {datetime.now().strftime('%H:%M:%S')}")
    
    def health_check():
        print(f"❤️ Health check: {datetime.now().strftime('%H:%M:%S')}")
    
    # Schedule jobs with tags
    schedule.every(10).seconds.do(database_backup).tag('backup', 'database')
    schedule.every(15).seconds.do(send_report).tag('reporting', 'daily')
    schedule.every(20).seconds.do(cleanup_logs).tag('maintenance', 'cleanup')
    schedule.every(5).seconds.do(health_check).tag('monitoring', 'health')
    
    print("🏷️ Jobs scheduled with tags")
    
    # Show jobs by tag
    print("\n📋 Jobs by category:")
    
    backup_jobs = schedule.get_jobs('backup')
    print(f"Backup jobs: {len(backup_jobs)}")
    
    maintenance_jobs = schedule.get_jobs('maintenance')
    print(f"Maintenance jobs: {len(maintenance_jobs)}")
    
    monitoring_jobs = schedule.get_jobs('monitoring')
    print(f"Monitoring jobs: {len(monitoring_jobs)}")
    
    # Run for 30 seconds
    print("\n🚀 Running tagged jobs for 30 seconds...")
    start_time = time.time()
    
    while time.time() - start_time < 30:
        schedule.run_pending()
        time.sleep(1)
        
        # Cancel maintenance jobs after 20 seconds
        if time.time() - start_time > 20:
            cancelled = schedule.clear('maintenance')
            if cancelled:
                print("❌ Maintenance jobs cancelled")
    
    print(f"Jobs remaining: {len(schedule.jobs)}")
    
    # Clear specific tags
    schedule.clear('backup')
    print("❌ Backup jobs cleared")
    
    print(f"Final job count: {len(schedule.jobs)}")

job_tags_and_filtering()
```

---

## 🎯 Real-World Applications

### 🕷️ **Web Scraping Scheduler:**
```python
import requests
from datetime import datetime
import json
import os

def web_scraping_scheduler():
    """Automated web scraping with scheduling"""
    
    def scrape_quotes():
        """Scrape quotes from website"""
        try:
            print(f"🕷️ Starting quote scraping: {datetime.now().strftime('%H:%M:%S')}")
            
            response = requests.get('https://quotes.toscrape.com/api/quotes?page=1')
            
            if response.status_code == 200:
                data = response.json()
                quotes = data.get('quotes', [])
                
                # Save to file with timestamp
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f'quotes_{timestamp}.json'
                
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(quotes, f, ensure_ascii=False, indent=2)
                
                print(f"✅ Scraped {len(quotes)} quotes, saved to {filename}")
                
            else:
                print(f"❌ Scraping failed: HTTP {response.status_code}")
                
        except Exception as e:
            print(f"❌ Scraping error: {e}")
    
    def cleanup_old_files():
        """Clean up old scraping files"""
        try:
            print(f"🧹 Cleaning old files: {datetime.now().strftime('%H:%M:%S')}")
            
            current_time = time.time()
            cleaned = 0
            
            for filename in os.listdir('.'):
                if filename.startswith('quotes_') and filename.endswith('.json'):
                    file_time = os.path.getmtime(filename)
                    
                    # Delete files older than 1 hour (3600 seconds)
                    if current_time - file_time > 3600:
                        os.remove(filename)
                        cleaned += 1
                        print(f"🗑️ Deleted old file: {filename}")
            
            print(f"✅ Cleaned {cleaned} old files")
            
        except Exception as e:
            print(f"❌ Cleanup error: {e}")
    
    def generate_report():
        """Generate scraping report"""
        try:
            print(f"📊 Generating report: {datetime.now().strftime('%H:%M:%S')}")
            
            quote_files = [f for f in os.listdir('.') if f.startswith('quotes_') and f.endswith('.json')]
            
            total_quotes = 0
            for filename in quote_files:
                try:
                    with open(filename, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        total_quotes += len(data)
                except:
                    continue
            
            report = {
                'timestamp': datetime.now().isoformat(),
                'total_files': len(quote_files),
                'total_quotes': total_quotes,
                'files': quote_files
            }
            
            with open('scraping_report.json', 'w', encoding='utf-8') as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
            
            print(f"📈 Report: {len(quote_files)} files, {total_quotes} quotes")
            
        except Exception as e:
            print(f"❌ Report error: {e}")
    
    # Schedule scraping jobs
    print("🕷️ Setting up web scraping scheduler...")
    
    # Scrape every 30 seconds (for demo - normally would be longer)
    schedule.every(30).seconds.do(scrape_quotes).tag('scraping')
    
    # Generate report every 2 minutes
    schedule.every(2).minutes.do(generate_report).tag('reporting')
    
    # Cleanup every 5 minutes
    schedule.every(5).minutes.do(cleanup_old_files).tag('maintenance')
    
    print("⏰ Scraping scheduler running for 3 minutes...")
    start_time = time.time()
    
    while time.time() - start_time < 180:  # 3 minutes
        schedule.run_pending()
        time.sleep(1)
    
    print("✅ Web scraping scheduler demo completed")

web_scraping_scheduler()
```

### 📊 **Data Processing Pipeline:**
```python
def data_processing_pipeline():
    """Automated data processing pipeline"""
    
    # Simulate data sources
    def collect_data():
        """Collect data from various sources"""
        print(f"📥 Collecting data: {datetime.now().strftime('%H:%M:%S')}")
        
        # Simulate data collection
        import random
        data = {
            'timestamp': datetime.now().isoformat(),
            'metrics': {
                'cpu_usage': random.uniform(10, 90),
                'memory_usage': random.uniform(20, 80),
                'disk_usage': random.uniform(30, 70),
                'network_io': random.randint(100, 1000)
            }
        }
        
        # Save raw data
        filename = f"raw_data_{datetime.now().strftime('%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"✅ Data collected: {filename}")
        return filename
    
    def process_data():
        """Process collected data"""
        print(f"⚙️ Processing data: {datetime.now().strftime('%H:%M:%S')}")
        
        # Find raw data files
        raw_files = [f for f in os.listdir('.') if f.startswith('raw_data_')]
        
        if not raw_files:
            print("⚠️ No raw data files found")
            return
        
        processed_data = []
        
        for filename in raw_files:
            try:
                with open(filename, 'r') as f:
                    data = json.load(f)
                    
                    # Process data (calculate averages, etc.)
                    metrics = data['metrics']
                    processed_metrics = {
                        'timestamp': data['timestamp'],
                        'avg_usage': (metrics['cpu_usage'] + metrics['memory_usage']) / 2,
                        'total_io': metrics['network_io'],
                        'status': 'healthy' if metrics['cpu_usage'] < 80 else 'warning'
                    }
                    
                    processed_data.append(processed_metrics)
                
                # Remove processed raw file
                os.remove(filename)
                
            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")
        
        if processed_data:
            # Save processed data
            output_file = f"processed_data_{datetime.now().strftime('%H%M%S')}.json"
            with open(output_file, 'w') as f:
                json.dump(processed_data, f, indent=2)
            
            print(f"✅ Processed {len(processed_data)} records: {output_file}")
    
    def generate_alerts():
        """Generate alerts based on processed data"""
        print(f"🚨 Checking for alerts: {datetime.now().strftime('%H:%M:%S')}")
        
        # Find processed data files
        processed_files = [f for f in os.listdir('.') if f.startswith('processed_data_')]
        
        alerts = []
        
        for filename in processed_files:
            try:
                with open(filename, 'r') as f:
                    data = json.load(f)
                    
                    for record in data:
                        if record['status'] == 'warning':
                            alerts.append({
                                'timestamp': record['timestamp'],
                                'message': f"High usage detected: {record['avg_usage']:.1f}%",
                                'severity': 'warning'
                            })
                        
                        if record['avg_usage'] > 90:
                            alerts.append({
                                'timestamp': record['timestamp'],
                                'message': f"Critical usage: {record['avg_usage']:.1f}%",
                                'severity': 'critical'
                            })
            
            except Exception as e:
                print(f"❌ Error checking {filename}: {e}")
        
        if alerts:
            alert_file = f"alerts_{datetime.now().strftime('%H%M%S')}.json"
            with open(alert_file, 'w') as f:
                json.dump(alerts, f, indent=2)
            
            print(f"🚨 Generated {len(alerts)} alerts: {alert_file}")
        else:
            print("✅ No alerts generated")
    
    # Set up data processing pipeline
    print("📊 Setting up data processing pipeline...")
    
    # Collect data every 20 seconds
    schedule.every(20).seconds.do(collect_data).tag('collection')
    
    # Process data every 45 seconds
    schedule.every(45).seconds.do(process_data).tag('processing')
    
    # Check for alerts every minute
    schedule.every(1).minutes.do(generate_alerts).tag('alerting')
    
    print("🚀 Data pipeline running for 2 minutes...")
    start_time = time.time()
    
    while time.time() - start_time < 120:  # 2 minutes
        schedule.run_pending()
        time.sleep(1)
    
    print("✅ Data processing pipeline demo completed")

data_processing_pipeline()
```

---

## 🔄 Threading ও Async

### 🧵 **Threaded Scheduler:**
```python
import threading

def threaded_scheduler():
    """Run scheduler in separate thread"""
    
    def background_task():
        print(f"🔄 Background task: {datetime.now().strftime('%H:%M:%S')}")
    
    def long_running_task():
        print(f"⏳ Long task started: {datetime.now().strftime('%H:%M:%S')}")
        time.sleep(3)  # Simulate long-running task
        print(f"✅ Long task completed: {datetime.now().strftime('%H:%M:%S')}")
    
    # Schedule jobs
    schedule.every(5).seconds.do(background_task).tag('background')
    schedule.every(15).seconds.do(long_running_task).tag('long_running')
    
    def run_scheduler():
        """Run scheduler in thread"""
        print("🧵 Scheduler thread started")
        
        while True:
            schedule.run_pending()
            time.sleep(1)
    
    # Start scheduler in background thread
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()
    
    print("🚀 Threaded scheduler started")
    print("💻 Main thread continues working...")
    
    # Main thread does other work
    for i in range(30):
        print(f"📋 Main thread work: {i+1}/30")
        time.sleep(2)
    
    print("✅ Threaded scheduler demo completed")

threaded_scheduler()
```

---

## 🎉 সমাপনী

### ✅ **Schedule এ আপনি শিখেছেন:**
- Basic ও advanced scheduling patterns
- Job management ও control
- Job tagging ও filtering
- Real-world applications (web scraping, data processing)
- Threading ও background execution
- Error handling ও monitoring

### 🚀 **Next Steps:**
- **APScheduler** দিয়ে advanced scheduling
- **Celery** দিয়ে distributed task queues
- **Cron jobs** integration
- **Database-backed** job persistence

**Schedule mastery সম্পন্ন! ⏰🇧🇩**
