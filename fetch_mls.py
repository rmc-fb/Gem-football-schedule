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
api_key = api_key.strip() 

# ★修正点：見つけた正しいURLに更新しました
url = "https://sofascore.p.rapidapi.com/teams/get-next-matches"

headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': 'sofascore.p.rapidapi.com',
    'User-Agent': 'Mozilla/5.0'
}

# ★修正点：URLに含まれていたパラメータをこちらに移動
params = {'teamId': '38', 'pageIndex': '0'}

try:
    response = requests.get(url, headers=headers, params=params)
    
    # エラー時は詳細を表示
    if response.status_code != 200:
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
    
    response.raise_for_status()
    data = response.json()

    # 未来の試合のみ抽出（eventsキーがあるか確認してフィルタリング）
    now = time.time()
    # 構造が変更されている可能性があるため、dataそのものを確認してください
    # もし data に直接イベントが入っていれば data.get('events', []) を data に変更します
    future_events = [e for e in data.get('events', []) if e.get('startTimestamp', 0) > now]

    # JSON保存
    with open('data/schedule.json', 'w', encoding='utf-8') as f:
        json.dump({'events': future_events}, f, indent=4, ensure_ascii=False)
    
    print(f"Successfully saved {len(future_events)} matches.")

except Exception as e:
    print(f"Error occurred: {e}")
    sys.exit(1)
