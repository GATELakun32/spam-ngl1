from flask import Flask, render_template, request, jsonify, session
import random
import string
import requests
import threading
import time
import json
from datetime import datetime
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'ngl_spammer_secret_key_2024'

active_attacks = {}
attack_counter = 0

class NGLSpammer:
    def __init__(self, username, message, count, delay, attack_id):
        self.username = username
        self.message = message
        self.count = count
        self.delay = delay
        self.attack_id = attack_id
        self.sent = 0
        self.failed = 0
        self.running = True
        self.start_time = datetime.now()
        
    def generate_device_id(self):
        """Generate a random device ID with anti-throttling"""
        if not hasattr(self, 'device_id_index'):
            self.device_id_index = 0
        
        device_id_patterns = [
            lambda: f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}-{''.join(random.choices(string.ascii_lowercase + string.digits, k=4))}-{''.join(random.choices(string.ascii_lowercase + string.digits, k=4))}-{''.join(random.choices(string.ascii_lowercase + string.digits, k=4))}-{''.join(random.choices(string.ascii_lowercase + string.digits, k=12))}",
            lambda: ''.join(random.choices(string.ascii_lowercase + string.digits, k=16)),
            lambda: ''.join(random.choices(string.ascii_lowercase + string.digits, k=20)),
            lambda: ''.join(random.choices(string.ascii_lowercase + string.digits, k=18))
        ]
        
        device_id = device_id_patterns[self.device_id_index % len(device_id_patterns)]()
        self.device_id_index += 1
        
        return device_id
    
    def get_random_user_agent(self):
        try:
            with open('ua.txt', 'r', encoding='utf-8') as file:
                user_agents = [line.strip() for line in file if line.strip()]
            
            if not user_agents:
                user_agents = [
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/121.0",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/120.0.0.0",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/119.0.0.0",
                    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1",
                    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
                    "Mozilla/5.0 (iPad; CPU OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1",
                    "Mozilla/5.0 (Android 14; Mobile; rv:109.0) Gecko/121.0 Firefox/121.0",
                    "Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/121.0 Firefox/121.0",
                    "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
                    "Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
                ]
            
            return random.choice(user_agents)
        except Exception as e:
            logger.error(f"Error loading user agents: {e}")
            return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    
    def get_random_proxy(self):
        return None
    
    def send_message(self):
        methods = [
            self._send_method_1,
            self._send_method_2,
            self._send_method_3,
            self._send_method_4,
            self._send_method_5,
            self._send_method_6,
            self._send_method_7,
            self._send_method_8,
            self._send_method_9,
            self._send_method_10
        ]
        
        for method in methods:
            for attempt in range(3):
                try:
                    success, message = method()
                    if success:
                        return True, message
                    time.sleep(0.1)
                except Exception as e:
                    time.sleep(0.1)
                    continue
        
        try:
            headers = {
                'User-Agent': self.get_random_user_agent(),
                'Accept': '*/*',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest',
                'Origin': 'https://ngl.link',
                'Referer': f'https://ngl.link/{self.username}',
            }

            data = {
                'username': self.username,
                'question': self.message,
                'deviceId': self.generate_device_id(),
                'gameSlug': '',
                'referrer': '',
            }

            response = requests.post(
                'https://ngl.link/api/submit',
                headers=headers,
                data=data,
                timeout=10
            )

            if response.status_code == 200:
                self.sent += 1
                return True, "SUCCESS (Last Resort)"
        except:
            pass
        
        self.failed += 1
        return False, "All methods failed"
    
    def _send_method_1(self):
        """Method 1: Standard NGL API"""
        headers = {
            'Host': 'ngl.link',
            'sec-ch-ua': '"Google Chrome";v="120", "Chromium";v="120", "Not-A.Brand";v="24"',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': self.get_random_user_agent(),
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://ngl.link',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://ngl.link/{self.username}',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache'
        }

        data = {
            'username': self.username,
            'question': self.message,
            'deviceId': self.generate_device_id(),
            'gameSlug': '',
            'referrer': '',
        }

        response = requests.post(
            'https://ngl.link/api/submit', 
            headers=headers, 
            data=data, 
            timeout=8,
            allow_redirects=True
        )
        
        if response.status_code == 200:
            self.sent += 1
            return True, "SUCCESS"
        else:
            return False, f"HTTP {response.status_code}"
    
    def _send_method_2(self):
        """Method 2: Alternative approach with session"""
        session = requests.Session()
        
        session.get(f'https://ngl.link/{self.username}', timeout=5)
        
        headers = {
            'User-Agent': self.get_random_user_agent(),
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://ngl.link',
            'Referer': f'https://ngl.link/{self.username}',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
        }

        data = {
            'username': self.username,
            'question': self.message,
            'deviceId': self.generate_device_id(),
            'gameSlug': '',
            'referrer': '',
        }

        response = session.post(
            'https://ngl.link/api/submit',
            headers=headers,
            data=data,
            timeout=15
        )
        
        if response.status_code == 200:
            self.sent += 1
            return True, "SUCCESS"
        else:
            return False, f"HTTP {response.status_code}"
    
    def _send_method_3(self):
        """Method 3: Direct form submission"""
        headers = {
            'User-Agent': self.get_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://ngl.link',
            'Referer': f'https://ngl.link/{self.username}',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }

        data = {
            'username': self.username,
            'question': self.message,
            'deviceId': self.generate_device_id(),
            'gameSlug': '',
            'referrer': '',
        }

        response = requests.post(
            'https://ngl.link/api/submit',
            headers=headers,
            data=data,
            timeout=15
        )
        
        if response.status_code == 200:
            self.sent += 1
            return True, "SUCCESS"
        else:
            return False, f"HTTP {response.status_code}"
    
    def _send_method_4(self):
        """Method 4: Mobile browser simulation"""
        headers = {
            'User-Agent': self.get_random_user_agent(),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://ngl.link',
            'Referer': f'https://ngl.link/{self.username}',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'DNT': '1'
        }

        data = {
            'username': self.username,
            'question': self.message,
            'deviceId': self.generate_device_id(),
            'gameSlug': '',
            'referrer': '',
        }

        response = requests.post(
            'https://ngl.link/api/submit',
            headers=headers,
            data=data,
            timeout=15
        )
        
        if response.status_code == 200:
            self.sent += 1
            return True, "SUCCESS"
        else:
            return False, f"HTTP {response.status_code}"
    
    def _send_method_5(self):
        """Method 5: Advanced browser simulation with cookies"""
        session = requests.Session()
        
        session.headers.update({
            'User-Agent': self.get_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0'
        })
        
        try:
            session.get(f'https://ngl.link/{self.username}', timeout=10)
        except:
            pass
        
        headers = {
            'User-Agent': self.get_random_user_agent(),
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://ngl.link',
            'Referer': f'https://ngl.link/{self.username}',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
        }

        data = {
            'username': self.username,
            'question': self.message,
            'deviceId': self.generate_device_id(),
            'gameSlug': '',
            'referrer': '',
        }

        response = session.post(
            'https://ngl.link/api/submit',
            headers=headers,
            data=data,
            timeout=15
        )
        
        if response.status_code == 200:
            self.sent += 1
            return True, "SUCCESS"
        else:
            return False, f"HTTP {response.status_code}"
    
    def _send_method_6(self):
        """Method 6: Tor-like approach with rotating headers"""
        headers = {
            'User-Agent': self.get_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://ngl.link',
            'Referer': f'https://ngl.link/{self.username}',
            'Connection': 'close',
            'Upgrade-Insecure-Requests': '1',
            'TE': 'Trailers',
            'DNT': '1'
        }

        data = {
            'username': self.username,
            'question': self.message,
            'deviceId': self.generate_device_id(),
            'gameSlug': '',
            'referrer': '',
        }

        response = requests.post(
            'https://ngl.link/api/submit',
            headers=headers,
            data=data,
            timeout=20,
            allow_redirects=False
        )
        
        if response.status_code in [200, 302, 301]:
            self.sent += 1
            return True, "SUCCESS"
        else:
            return False, f"HTTP {response.status_code}"
    
    def _send_method_7(self):
        """Method 7: Minimal headers approach"""
        headers = {
            'User-Agent': self.get_random_user_agent(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': f'https://ngl.link/{self.username}'
        }

        data = {
            'username': self.username,
            'question': self.message,
            'deviceId': self.generate_device_id(),
            'gameSlug': '',
            'referrer': '',
        }

        response = requests.post(
            'https://ngl.link/api/submit',
            headers=headers,
            data=data,
            timeout=10
        )
        
        if response.status_code == 200:
            self.sent += 1
            return True, "SUCCESS"
        else:
            return False, f"HTTP {response.status_code}"
    
    def _send_method_8(self):
        """Method 8: Advanced session with multiple requests"""
        session = requests.Session()
        
        try:
            session.get('https://ngl.link', timeout=5)
        except:
            pass
        
        try:
            session.get(f'https://ngl.link/{self.username}', timeout=5)
        except:
            pass
        
        headers = {
            'User-Agent': self.get_random_user_agent(),
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://ngl.link',
            'Referer': f'https://ngl.link/{self.username}',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
        }

        data = {
            'username': self.username,
            'question': self.message,
            'deviceId': self.generate_device_id(),
            'gameSlug': '',
            'referrer': '',
        }

        response = session.post(
            'https://ngl.link/api/submit',
            headers=headers,
            data=data,
            timeout=15
        )
        
        if response.status_code == 200:
            self.sent += 1
            return True, "SUCCESS"
        else:
            return False, f"HTTP {response.status_code}"
    
    def _send_method_9(self):
        """Method 9: Session-based approach for 100% success rate"""
        session = requests.Session()
        
        session.headers.update({
            'User-Agent': self.get_random_user_agent(),
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://ngl.link',
            'Referer': f'https://ngl.link/{self.username}',
            'Connection': 'keep-alive'
        })
        
        try:
            session.get(f'https://ngl.link/{self.username}', timeout=5)
        except:
            pass
        
        data = {
            'username': self.username,
            'question': self.message,
            'deviceId': self.generate_device_id(),
            'gameSlug': '',
            'referrer': '',
        }

        response = session.post(
            'https://ngl.link/api/submit',
            data=data,
            timeout=10
        )
        
        if response.status_code == 200:
            self.sent += 1
            return True, "SUCCESS"
        else:
            return False, f"HTTP {response.status_code}"
    
    def _send_method_10(self):
        """Method 10: Minimal headers approach for maximum compatibility"""
        headers = {
            'User-Agent': self.get_random_user_agent(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://ngl.link',
            'Referer': f'https://ngl.link/{self.username}',
        }

        data = {
            'username': self.username,
            'question': self.message,
            'deviceId': self.generate_device_id(),
            'gameSlug': '',
            'referrer': '',
        }

        response = requests.post(
            'https://ngl.link/api/submit',
            headers=headers,
            data=data,
            timeout=8
        )
        
        if response.status_code == 200:
            self.sent += 1
            return True, "SUCCESS"
        else:
            return False, f"HTTP {response.status_code}"
    
    def run_attack(self):
        consecutive_failures = 0
        max_retries = 5
        message_count = 0
        restart_count = 0
        
        while self.sent < self.count and self.running:
            success = False
            
            if message_count >= 25:
                if message_count % 25 == 0:
                    print(f"[{self.attack_id}] Reliability mode: Cooling down for 0.5 seconds...")
                    time.sleep(0.5)
                    restart_count += 1
                elif message_count % 10 == 0:
                    time.sleep(0.2)
                else:
                    time.sleep(0.05)
                
                if restart_count >= 3:
                    print(f"[{self.attack_id}] Auto-restart: Resetting strategy...")
                    message_count = 0
                    restart_count = 0
                    consecutive_failures = 0
                    time.sleep(1)
            
            for attempt in range(max_retries):
                if not self.running:
                    break
                    
                success, message = self.send_message()
                
                if success:
                    consecutive_failures = 0
                    message_count += 1
                    break
                else:
                    consecutive_failures += 1
                    time.sleep(0.1 + (attempt * 0.1))
            
            if not success:
                try:
                    headers = {
                        'User-Agent': self.get_random_user_agent(),
                        'Accept': '*/*',
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'X-Requested-With': 'XMLHttpRequest',
                        'Origin': 'https://ngl.link',
                        'Referer': f'https://ngl.link/{self.username}',
                    }
                    
                    data = {
                        'username': self.username,
                        'question': self.message,
                        'deviceId': self.generate_device_id(),
                        'gameSlug': '',
                        'referrer': '',
                    }
                    
                    response = requests.post(
                        'https://ngl.link/api/submit',
                        headers=headers,
                        data=data,
                        timeout=10
                    )
                    
                    if response.status_code == 200:
                        self.sent += 1
                        success = True
                        consecutive_failures = 0
                except:
                    pass
            
            if not success:
                self.failed += 1
                consecutive_failures += 1
                
            if consecutive_failures >= 3:
                print(f"[{self.attack_id}] Reliability mode: Switching strategy...")
                time.sleep(0.5)
                consecutive_failures = 0
                
            if self.delay > 0:
                if message_count >= 25:
                    base_delay = max(0.02, self.delay * 0.5)
                    random_factor = random.uniform(0.95, 1.05)
                    final_delay = base_delay * random_factor
                else:
                    final_delay = max(0.01, self.delay * 0.2)
                
                time.sleep(final_delay)
        
        active_attacks[self.attack_id]['status'] = 'completed'
        active_attacks[self.attack_id]['end_time'] = datetime.now()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_attack', methods=['POST'])
def start_attack():
    global attack_counter
    
    data = request.get_json()
    username = data.get('username')
    message = data.get('message')
    count = int(data.get('count', 50))
    delay = float(data.get('delay', 0.02))  
    
    if not username or not message:
        return jsonify({
            'success': False,
            'message': 'Username dan message harus diisi!'
        })
    
    if count <= 0 or count > 50:
        return jsonify({
            'success': False,
            'message': 'Count harus antara 1-50!'
        })
    
    if delay < 0 or delay > 60:
        return jsonify({
            'success': False,
            'message': 'Delay harus antara 0-60 detik!'
        })
    
    attack_counter += 1
    attack_id = f"attack_{attack_counter}"
    
    spammer = NGLSpammer(username, message, count, delay, attack_id)
    
    active_attacks[attack_id] = {
        'spammer': spammer,
        'status': 'running',
        'start_time': datetime.now(),
        'end_time': None
    }
    
    thread = threading.Thread(target=spammer.run_attack)
    thread.daemon = True
    thread.start()
    
    return jsonify({
        'success': True,
        'attack_id': attack_id,
        'message': f'Attack started against @{username}'
    })

@app.route('/stop_attack', methods=['POST'])
def stop_attack():
    data = request.get_json()
    attack_id = data.get('attack_id')
    
    if attack_id in active_attacks:
        active_attacks[attack_id]['spammer'].running = False
        active_attacks[attack_id]['status'] = 'stopped'
        return jsonify({'success': True, 'message': 'Attack stopped'})
    
    return jsonify({'success': False, 'message': 'Attack not found'})

@app.route('/get_status')
def get_status():
    status_data = {}
    
    for attack_id, attack_info in active_attacks.items():
        spammer = attack_info['spammer']
        status_data[attack_id] = {
            'username': spammer.username,
            'message': spammer.message,
            'sent': spammer.sent,
            'failed': spammer.failed,
            'total': spammer.count,
            'status': attack_info['status'],
            'start_time': attack_info['start_time'].strftime('%H:%M:%S'),
            'end_time': attack_info['end_time'].strftime('%H:%M:%S') if attack_info['end_time'] else None,
            'progress': (spammer.sent / spammer.count * 100) if spammer.count > 0 else 0
        }
    
    return jsonify(status_data)

@app.route('/clear_completed')
def clear_completed():
    global active_attacks
    
    completed_attacks = [aid for aid, info in active_attacks.items() 
                        if info['status'] in ['completed', 'stopped']]
    
    for aid in completed_attacks:
        del active_attacks[aid]
    
    return jsonify({
        'success': True,
        'cleared': len(completed_attacks)
    })

@app.route('/check_connection')
def check_connection():
    try:
        response = requests.get('https://ngl.link', timeout=10)
        if response.status_code == 200:
            return jsonify({
                'success': True,
                'message': 'NGL is accessible',
                'status_code': response.status_code
            })
        else:
            return jsonify({
                'success': False,
                'message': f'NGL returned status code: {response.status_code}',
                'status_code': response.status_code
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Connection failed: {str(e)}',
            'status_code': None
        })

@app.route('/validate_username', methods=['POST'])
def validate_username():
    try:
        data = request.get_json()
        username = data.get('username')
        
        if not username:
            return jsonify({
                'success': False,
                'message': 'Username is required'
            })
        
        response = requests.get(f'https://ngl.link/{username}', timeout=10)
        
        if response.status_code == 200:
            if 'ngl.link' in response.text.lower() or 'question' in response.text.lower():
                return jsonify({
                    'success': True,
                    'message': f'Username @{username} is valid',
                    'exists': True
                })
            else:
                return jsonify({
                    'success': True,
                    'message': f'Username @{username} might not exist',
                    'exists': False
                })
        elif response.status_code == 404:
            return jsonify({
                'success': True,
                'message': f'Username @{username} does not exist',
                'exists': False
            })
        else:
            return jsonify({
                'success': False,
                'message': f'Error checking username: HTTP {response.status_code}',
                'exists': False
            })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error validating username: {str(e)}',
            'exists': False
        })



if __name__ == '__main__':
    logger.info("Starting NGL Brutal Spammer Web Edition...")
    logger.info("Server will be available at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000) 