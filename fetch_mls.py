import os
import requests
import json

API_KEY = os.environ.get("RAPIDAPI_KEY", "").strip()
API_HOST = "api-football186.p.rapidapi.com"
headers = {"X-RapidAPI-Key": API_KEY, "X-RapidAPI-Host": API_HOST}

all_competitions = []
page = 1

print("🚀 全ページを検索して2026年MLSを探します...")

while True:
    # 検索結果をページごとに取得
    search_url = "https://api-football186.p.rapidapi.com/competitions"
    params = {"search": "MLS", "paged": str(page)}
    response = requests.get(search_url, headers=headers, params=params)
    data = response.json()
    items = data.get("response", {}).get("items", [])
    
    if not items:
        break
        
    all_competitions.extend(items)
    page += 1

# 2026年のMLSを探す
target_cid = None
for comp in all_competitions:
    if comp.get("cname") == "MLS" and comp.get("year") == "2026":
        target_cid = comp.get("cid")
        print(f"✅ 見つかった！ 2026年MLSのcid: {target_cid}")
        break

if not target_cid:
    print("❌ どうしても見つかりません。取得できた大会リストの全件をログに出します:")
    # 何が取れているか確認するために全部出す
    print(json.dumps(all_competitions, indent=2))
    exit(1)
