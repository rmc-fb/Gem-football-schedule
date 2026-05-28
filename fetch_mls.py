import os
import requests
import json

API_KEY = os.environ.get("RAPIDAPI_KEY", "").strip()
API_HOST = "api-football186.p.rapidapi.com"
headers = {"x-rapidapi-host": API_HOST, "x-rapidapi-key": API_KEY}

TARGET_CID = "1855"
url = f"https://api-football186.p.rapidapi.com/competition/{TARGET_CID}/matches"

response = requests.get(url, headers=headers)
data = response.json()

# 構造を解析： response -> items の中に試合リストがある
items = data.get("response", {}).get("items", [])

final_dates = []
for match in items:
    # 試合データの中に日付情報が入っているはずや
    # ログを見ると 'result' などがあるので、もし日時キーがあれば抽出する
    # ※APIのレスポンスに 'datestart' があればそれを使う
    date = match.get("datestart")
    if date:
        final_dates.append(date)

# 保存
os.makedirs("data", exist_ok=True)
with open("data/schedule.json", "w", encoding="utf-8") as f:
    json.dump(final_dates, f, ensure_ascii=False, indent=2)

print(f"🎉 完了！ {len(final_dates)} 件の試合日時を保存しました。")
