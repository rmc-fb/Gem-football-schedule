import os
import requests
import json

API_KEY = os.environ.get("RAPIDAPI_KEY", "").strip()
API_HOST = "api-football186.p.rapidapi.com"
headers = {
    "x-rapidapi-host": API_HOST,
    "x-rapidapi-key": API_KEY,
    "Content-Type": "application/json"
}

# さっき見つけたcid(1855)を埋め込む
TARGET_CID = "1855"
url = f"https://api-football186.p.rapidapi.com/competition/{TARGET_CID}/matches"

print(f"🚀 正しいURLで取得開始: {url}")

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # 試合データが入っていそうな場所を抽出
    items = data.get("response", [])
    
    # 日時を抽出
    all_match_dates = [match.get("datestart") for match in items if match.get("datestart")]
    
    # 保存
    os.makedirs("data", exist_ok=True)
    with open("data/schedule.json", "w", encoding="utf-8") as f:
        json.dump(all_match_dates, f, ensure_ascii=False, indent=2)
        
    print(f"🎉 成功！ {len(all_match_dates)} 件の試合を保存しました。")
else:
    print(f"❌ エラー発生: {response.status_code}")
    print(response.text)
