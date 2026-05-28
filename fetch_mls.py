import os
import requests
import json
from datetime import datetime

API_KEY = os.environ.get("RAPIDAPI_KEY", "").strip()
API_HOST = "api-football186.p.rapidapi.com"
headers = {"x-rapidapi-host": API_HOST, "x-rapidapi-key": API_KEY}

TARGET_CID = "1855"
url = f"https://api-football186.p.rapidapi.com/competition/{TARGET_CID}/matches"

# 今日の日付を取得 (比較用)
today = datetime.now()

response = requests.get(url, headers=headers)
data = response.json()

items = data.get("response", {}).get("items", [])

final_dates = []
for match in items:
    date_str = match.get("datestart")
    if date_str:
        # 日付文字列をdatetime型に変換
        match_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        
        # 今日以降の試合だけを追加
        if match_date >= today:
            final_dates.append(date_str)

# 保存
os.makedirs("data", exist_ok=True)
with open("data/schedule.json", "w", encoding="utf-8") as f:
    json.dump(final_dates, f, ensure_ascii=False, indent=2)

print(f"🎉 完了！今日(2026-05-28)以降の試合を {len(final_dates)} 件保存しました。")
