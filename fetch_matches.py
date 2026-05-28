import requests
import sys
import json
import os

# --- 設定部分 --- 
# GitHub Secretsから読み込むのが安全ですが、とりあえず直書きで動作確認してください
MLS_API_URL = "https://api-football-v1.p.rapidapi.com/v3/fixtures" # 例
RAPIDAPI_KEY = "あなたのAPIキー" 
EURO_API_URL = "https://api.football-data.org/v4/matches" # 例
EURO_API_TOKEN = "あなたのトークン"

def fetch_api_data(url, headers, params=None):
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Error at {url}: {e}")
        sys.exit(1) # これでActionが失敗して止まります

def main():
    all_matches = []

    # 1. MLSの取得 (RapidAPI)
    print("Fetching MLS...")
    headers_mls = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "api-football-v1.p.rapidapi.com" # 必要に応じて調整
    }
    # paramsは実際のクエリに合わせて設定してください
    # mls_data = fetch_api_data(MLS_API_URL, headers_mls, params={"league": "253", "next": "10"})
    # all_matches.extend(mls_data['response'])

    # 2. 欧州リーグの取得 (football-data.org)
    print("Fetching European leagues...")
    headers_euro = {"X-Auth-Token": EURO_API_TOKEN}
    # euro_data = fetch_api_data(EURO_API_URL, headers_euro)
    # all_matches.extend(euro_data['matches'])

    # 3. JSON保存
    with open('data/schedule.json', 'w', encoding='utf-8') as f:
        json.dump(all_matches, f, ensure_ascii=False, indent=2)
    print("Successfully updated schedule.json")

if __name__ == "__main__":
    main()
