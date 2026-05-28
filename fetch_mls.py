import os
import requests
import json

API_KEY = os.environ.get("RAPIDAPI_KEY", "").strip()
API_HOST = "api-football186.p.rapidapi.com"
headers = {"X-RapidAPI-Key": API_KEY, "X-RapidAPI-Host": API_HOST}
TARGET_CID = "1855" # 今回見つけたID

all_match_dates = []
page = 1

print(f"🚀 cid={TARGET_CID} の試合スケジュール取得を開始します...")

while True:
    print(f" ⏳ ページ {page} を取得中...")
    # API-Footballの試合リストエンドポイント
    url = "https://api-football186.p.rapidapi.com/competition/matches"
    params = {"cid": TARGET_CID, "paged": str(page)}
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    items = data.get("response", {}).get("items", [])
    
    if not items:
        print("✨ すべての取得が完了しました。")
        break
        
    for match in items:
        # ここでAPIレスポンスの日付キーを確認して抽出
        # ※API-Footballの仕様に合わせて取得キーを調整
        date_str = match.get("datestart")
        if date_str:
            all_match_dates.append(date_str)
    
    page += 1

# 重複削除＆並び替え
all_match_dates = sorted(list(set(all_match_dates)))

# 保存
output_file = "data/schedule.json"
os.makedirs("data", exist_ok=True)
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_match_dates, f, ensure_ascii=False, indent=2)

print(f"🎉 完了！合計 {len(all_match_dates)} 試合の日時を保存しました。")
