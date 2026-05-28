import json
import time
import requests

# API設定
API_URL = "https://api.example.com/tournaments/get-next-matches" # 実際のAPIエンドポイント
PARAMS = {'tournamentId': '242', 'seasonId': '86668'}
HEADERS = {'X-API-Key': 'YOUR_API_KEY'}

# 1. データ取得
response = requests.get(API_URL, params=PARAMS, headers=HEADERS)
data = response.json()

# 2. フィルタリング（過去の試合を削除）
now = time.time()
future_events = [e for e in data['events'] if e['startTimestamp'] > now]

# 3. ファイルに保存
with open('data/schedule.json', 'w') as f:
    json.dump({'events': future_events}, f, indent=4)
