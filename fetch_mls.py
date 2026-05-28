import os
import requests
import json

# GitHubのSecretsからAPIキーを安全に読み込む
API_KEY = os.environ.get("RAPIDAPI_KEY")
API_HOST = "soccer-football-info.p.rapidapi.com"

if not API_KEY:
    print("❌ エラー: RAPIDAPI_KEY が設定されていません。")
    exit(1)

url = "https://soccer-football-info.p.rapidapi.com/competition/matches/list/"
headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": API_HOST
}

all_match_dates = []
page = 1

print("🚀 MLS全試合の「日時データ」取得を開始します...")

while True:
    print(f" ⏳ ページ {page} を取得中...")
    querystring = {"competitionid": "1855", "paged": str(page)}
    
    try:
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code != 200:
            print(f"❌ エラー status_code: {response.status_code}")
            break
            
        data = response.json()
        items = data.get("response", {}).get("items", [])
        
        if not items:
            print("✨ 全ページのデータを読み込み終えました。")
            break
            
        # 試合日時だけをシンプルに配列に追加
        for match in items:
            date_str = match.get("datestart")
            if date_str:
                all_match_dates.append(date_str)
            
        page += 1
        
    except Exception as e:
        print(f"❌ 通信エラーが発生しました: {e}")
        break

# 日付の古い順（開幕戦〜最終戦）に並び替える
all_match_dates.sort()

# dataフォルダの中に schedule.json として保存（上書き）
output_file = "data/schedule.json"
os.makedirs("data", exist_ok=True)

with open(output_file, "w", encoding="utf-8") as f:
    # 配列のままシンプルなJSONとして保存
    json.dump(all_match_dates, f, ensure_ascii=False, indent=2)

print(f"🎉 処理完了！合計 {len(all_match_dates)} 件の試合日時を {output_file} に保存しました。")
