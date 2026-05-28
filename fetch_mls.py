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

TARGET_CID = "1855"
url = f"https://api-football186.p.rapidapi.com/competition/{TARGET_CID}/matches"

print(f"🚀 取得開始: {url}")

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    items = data.get("response", [])
    
    # 【修正点】itemsの中身が文字列か辞書かを確認して処理する
    final_dates = []
    if isinstance(items, list):
        for item in items:
            if isinstance(item, dict):
                # 辞書ならdatestartを取り出す
                date = item.get("datestart")
                if date: final_dates.append(date)
            else:
                # 文字列ならそのまま追加
                final_dates.append(item)
    
    # 保存
    os.makedirs("data", exist_ok=True)
    with open("data/schedule.json", "w", encoding="utf-8") as f:
        json.dump(final_dates, f, ensure_ascii=False, indent=2)
        
    print(f"🎉 成功！ {len(final_dates)} 件のデータを保存しました。")
else:
    print(f"❌ エラー発生: {response.status_code}")
    print(response.text)
