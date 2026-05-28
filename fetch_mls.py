import os
import requests
import json

API_KEY = os.environ.get("RAPIDAPI_KEY", "").strip()
API_HOST = "api-football186.p.rapidapi.com"
headers = {"X-RapidAPI-Key": API_KEY, "X-RapidAPI-Host": API_HOST}

# 1. まず全大会リストから「MLS」かつ「2026年」のcidを探す
search_url = "https://api-football186.p.rapidapi.com/competitions"
response = requests.get(search_url, headers=headers, params={"search": "MLS"})
competitions = response.json().get("response", {}).get("items", [])

target_cid = None
for comp in competitions:
    # 2026年のMLSという名前の大会を探す
    if comp.get("cname") == "MLS" and comp.get("year") == "2026":
        target_cid = comp.get("cid")
        break

if not target_cid:
    print("❌ 2026年のMLSが見つかりませんでした。")
    # ここで一度、見つかった全大会のリストをログに出して確認する
    print(json.dumps(competitions, indent=2))
    exit(1)

print(f"✅ 2026年MLSのcidを発見: {target_cid}")

# 2. そのcidを使って試合リストを取得する
# 補足：このAPIの仕様に合わせて、エンドポイントとパラメータを調整する
matches_url = "https://api-football186.p.rapidapi.com/competition/matches"
# （ここに試合取得用のページ回し処理を記述）
