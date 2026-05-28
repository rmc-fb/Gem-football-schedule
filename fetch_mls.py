import os
import requests
import json

API_KEY = os.environ.get("RAPIDAPI_KEY", "").strip()
API_HOST = "api-football186.p.rapidapi.com"
headers = {"x-rapidapi-host": API_HOST, "x-rapidapi-key": API_KEY}

# 2026シーズンの全試合を狙う
TARGET_CID = "1855"
url = f"https://api-football186.p.rapidapi.com/competition/{TARGET_CID}/matches"

response = requests.get(url, headers=headers)
data = response.json()

# 取得できた試合の日付を全部表示させて、何が入っているか確認する
items = data.get("response", {}).get("items", [])
all_dates = [match.get("datestart") for match in items]

print("--- 取得できた全試合の日付 ---")
print(all_dates)
