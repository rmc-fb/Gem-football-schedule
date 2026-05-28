import json
import time
import requests
import os
import sys

# 保存ディレクトリ作成
os.makedirs('data', exist_ok=True)

# API設定
api_key = os.getenv('RAPIDAPI_KEY')
if not api_key:
    print("Error: RAPIDAPI_KEY is not set.")
    sys.exit(1)

# APIエンドポイント
url = "https://api.sofascore.com/api/v1/tournaments/get-next-matches"
# RapidAPIのヘッダー情報（必ずRapidAPIのサイトで確認してください）
headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': 'api.sofascore.com' # ここはAPIのホスト名に合わせてください
}
params = {'tournamentId': '242', 'seasonId': '86668'}

try:
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    # 未来の試合のみ抽出
    now = time.time()
    future_events = [e for e in data.get('events', []) if e.get('startTimestamp', 0) > now]

    # JSON保存
    with open('data/schedule.json', 'w', encoding='utf-8') as f:
        json.dump({'events': future_events}, f, indent=4, ensure_ascii=False)
    
    print(f"Successfully saved {len(future_events)} matches.")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
