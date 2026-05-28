import json
import time
import requests
import os
import sys

os.makedirs('data', exist_ok=True)

api_key = os.getenv('RAPIDAPI_KEY')
if not api_key:
    print("Error: RAPIDAPI_KEY is not set.")
    sys.exit(1)
api_key = api_key.strip() 

url = "https://sofascore.p.rapidapi.com/teams/get-next-matches"
headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': 'sofascore.p.rapidapi.com',
    'User-Agent': 'Mozilla/5.0'
}
params = {'teamId': '38', 'pageIndex': '0'}

try:
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    # --- ここで中身を確認するためのデバッグログを出力します ---
    print(f"DEBUG: APIから返ってきたキー一覧: {data.keys()}")
    # もし events 以外のキーにデータが入っている場合を見つけるため
    
    events = data.get('events', [])
    print(f"DEBUG: APIから取得したイベント総数: {len(events)}")
    
    if len(events) > 0:
        print(f"DEBUG: 最初のイベントの内容: {events[0]}")
    # ----------------------------------------------------

    now = time.time()
    future_events = [e for e in events if e.get('startTimestamp', 0) > now]

    with open('data/schedule.json', 'w', encoding='utf-8') as f:
        json.dump({'events': future_events}, f, indent=4, ensure_ascii=False)
    
    print(f"Successfully saved {len(future_events)} matches.")

except Exception as e:
    print(f"Error occurred: {e}")
    sys.exit(1)
