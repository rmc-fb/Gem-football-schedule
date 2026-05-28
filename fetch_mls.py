import json
import time
import requests
import os
import sys

# 絶対パスで保存先を指定
base_dir = os.getcwd()
data_dir = os.path.join(base_dir, 'data')
os.makedirs(data_dir, exist_ok=True)
output_path = os.path.join(data_dir, 'schedule.json')

print(f"Saving to: {output_path}") # どこに保存しようとしているか表示

api_key = os.getenv('API_KEY')
if not api_key:
    print("Error: API_KEY is not set.")
    sys.exit(1)

url = "https://api.sofascore.com/api/v1/tournaments/get-next-matches"
params = {'tournamentId': '242', 'seasonId': '86668'}
headers = {'X-API-Key': api_key} 

try:
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status() 
    data = response.json()

    now = time.time()
    future_events = [e for e in data.get('events', []) if e.get('startTimestamp', 0) > now]

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({'events': future_events}, f, indent=4, ensure_ascii=False)
    
    print(f"Successfully saved {len(future_events)} events.")

except Exception as e:
    print(f"Error occurred: {e}")
    sys.exit(1)
