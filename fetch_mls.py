import json
import time
import requests
import os

# 1. 保存用ディレクトリを確実に作成
os.makedirs('data', exist_ok=True)

# 2. API設定
# GitHub SecretsのAPI_KEYを読み込み
api_key = os.getenv('API_KEY')

# URLとパラメータ
url = "https://api.sofascore.com/api/v1/tournaments/get-next-matches"
params = {'tournamentId': '242', 'seasonId': '86668'}
# 認証ヘッダー（APIの仕様に合わせて調整してください）
headers = {'X-API-Key': api_key} 

try:
    # データ取得
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status() # エラーがあればここで停止
    data = response.json()

    # 3. フィルタリング（未来の試合のみ抽出）
    now = time.time()
    # eventsキーが存在しない場合の安全策も追加
    future_events = [e for e in data.get('events', []) if e.get('startTimestamp', 0) > now]

    # 4. JSONとして保存
    with open('data/schedule.json', 'w', encoding='utf-8') as f:
        json.dump({'events': future_events}, f, indent=4, ensure_ascii=False)
    
    print(f"Successfully updated schedule.json with {len(future_events)} events.")

except Exception as e:
    print(f"Error occurred: {e}")
