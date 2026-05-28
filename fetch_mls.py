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
# ★ここを一旦 pageIndex=0 だけにしてシンプルに確認します
params = {'teamId': '38', 'pageIndex': '0'}

try:
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    # ★ここが重要！何が返ってきているかログに出力します
    print("--- APIから返ってきたデータの構造 ---")
    print(json.dumps(data, indent=2, ensure_ascii=False)[:1000]) # 最初の1000文字だけ表示
    print("---------------------------------")

    # 構造の確認：eventsキーがあるかチェック
    events = data.get('events', [])
    
    # ★フィルタリングのロジックが厳しすぎる可能性があるので、
    # 一旦フィルタリングを外してデータをそのまま保存してみます（デバッグ用）
    future_events = events 

    with open('data/schedule.json', 'w', encoding='utf-8') as f:
        json.dump({'events': future_events}, f, indent=4, ensure_ascii=False)
    
    print(f"Successfully saved {len(future_events)} events.")

except Exception as e:
    print(f"Error occurred: {e}")
    sys.exit(1)
