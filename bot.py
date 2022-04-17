import requests
import json
import time
import os

token = os.getenv('TELEGRAM_BOT_TOKEN')
if not token:
    print('Error: Environment variable TELEGRAM_BOT_TOKEN not found.')
    exit(1)

def send_notification(username):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    requests.post(url, json={
        'chat_id': '@ballometer',
        'parse_mode': 'HTML',
        'disable_web_page_preview': True,
        'text': f'<a href="https://ballometer.io/{username}">{username}</a> is recording'
    })

def get_max_flight_id(username):
    ids_strings = json.loads(requests.get(f'https://api.ballometer.io/read/flightIds?username={username}').text)
    ids = [int(i) for i in ids_strings]
    return max(ids)

usernames = json.loads(requests.get('https://api.ballometer.io/read/listUsernames').text)
last = {username: None for username in usernames}

while True:
    for username in last:
        max_flight_id = get_max_flight_id(username)
        if not last[username]:
            last[username] = max_flight_id
            continue
        if last[username] != max_flight_id:
            send_notification(username)
            last[username] = max_flight_id
    time.sleep(1)
