import requests
import sys
import json
import os

# エラーハンドリング付きのフェッチ関数
def fetch_api_data(url, headers=None, params=None):
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        # 4xx や 5xx のエラーが発生した場合に例外を投げる
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        # ここで終了することで、GitHub Actionsは「失敗」として検知する
        sys.exit(1)

def main():
    all_matches = []

    # 1. MLSの取得 (RapidAPI)
    print("Fetching MLS...")
    mls_data = fetch_api_data("YOUR_MLS_API_URL", headers={"X-RapidAPI-Key": "YOUR_KEY"})
    # ここにデータを整形して all_matches に追加する処理
    # all_matches.extend(...)

    # 2. 欧州リーグの取得 (football-data.org)
    print("Fetching European leagues...")
    euro_data = fetch_api_data("https://api.football-data.org/v4/competitions/...", headers={"X-Auth-Token": "YOUR_TOKEN"})
    # ここにデータを整形して all_matches に追加する処理
    # all_matches.extend(...)

    # 3. JSON保存
    with open('data/schedule.json', 'w', encoding='utf-8') as f:
        json.dump(all_matches, f, ensure_ascii=False, indent=2)
    print("Successfully updated schedule.json")

if __name__ == "__main__":
    main()
