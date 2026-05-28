import os
import requests
import json

# 設定
API_KEY = os.environ.get("RAPIDAPI_KEY", "").strip()
API_HOST = "api-football186.p.rapidapi.com"
headers = {"x-rapidapi-host": API_HOST, "x-rapidapi-key": API_KEY}

# 確認したいURL
TARGET_CID = "1855"
url = f"https://api-football186.p.rapidapi.com/competition/{TARGET_CID}/matches"

print(f"🚀 取得開始: {url}")

# リクエスト実行
response = requests.get(url, headers=headers)

# 結果を表示
print("--- ステータスコード ---")
print(response.status_code)
print("--- レスポンスの中身 (最初の500文字) ---")
print(response.text[:500])
