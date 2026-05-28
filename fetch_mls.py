import os
import requests
import json

# APIキーを読み込み
API_KEY = os.environ.get("RAPIDAPI_KEY", "").strip()
API_HOST = "api-football186.p.rapidapi.com"
headers = {"X-RapidAPI-Key": API_KEY, "X-RapidAPI-Host": API_HOST}

# 今回見つけた2026年MLSのID
TARGET_CID = "1855"

print(f"🔍 cid={TARGET_CID} の生データを取得中...")

# 試合リストを取得するURL
url = "https://api-football186.p.rapidapi.com/competition/matches"
params = {"cid": TARGET_CID, "paged": "1"}

# リクエスト送信
response = requests.get(url, headers=headers, params=params)

# 【重要】APIが返してきた「生データ」を全部ログに出力する
print("--- 以下がAPIからの生データです ---")
print(json.dumps(response.json(), indent=2))
print("--- ここまで ---")
