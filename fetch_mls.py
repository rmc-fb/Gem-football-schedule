import os
import requests
import json
from datetime import datetime

API_KEY = os.environ.get("RAPIDAPI_KEY", "").strip()
API_HOST = "api-football186.p.rapidapi.com"
headers = {"x-rapidapi-host": API_HOST, "x-rapidapi-key": API_KEY}

today = datetime.now()
all_future_matches = []

# 全52ページをループ
for page in range(1, 53):
    print(f"🚀 ページ {page}/52 を取得中...")
    url = f"https://api-football186.p.rapidapi.com/competition/1855/matches"
    params = {"paged": page}
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    items = data.get("response", {}).get("items", [])
    
    for match in items:
        date_str = match.get("datestart")
        if date_str:
            match_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            # 今日以降の試合のみ保存
            if match_date >= today:
                home = match.get("teams", {}).get("home", {}).get("tname")
                away = match.get("teams", {}).get("away", {}).get("tname")
                all_future_matches.append({
                    "date": date_str,
                    "match": f"{home} vs {away}"
                })

# 結果を保存
os.makedirs("data", exist_ok=True)
with open("data/schedule.json", "w", encoding="utf-8") as f:
    json.dump(all_future_matches, f, ensure_ascii=False, indent=2)

print(f"🎉 完了！今日以降の試合を {len(all_future_matches)} 件保存しました。")
