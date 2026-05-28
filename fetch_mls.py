import os
import requests

# キーはデバッグ用にハードコードせず、Secretsから取得
API_KEY = os.environ.get("RAPIDAPI_KEY", "").strip()
API_HOST = "api-football186.p.rapidapi.com"

# 最も基本的な「競合リスト検索」を叩いてみる（もしこれすら403なら、キー自体が死んでる）
url = "https://api-football186.p.rapidapi.com/competitions"
querystring = {"search": "MLS"}
headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": API_HOST
}

response = requests.get(url, headers=headers, params=querystring)
print(f"DEBUG STATUS: {response.status_code}")
print(f"DEBUG RESPONSE: {response.text}")
