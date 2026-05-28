import requests
import sys
import json
import os

# GitHub Secretsから取得するように変更（推奨）
RAPIDAPI_KEY = os.environ.get('RAPIDAPI_KEY')
EURO_API_TOKEN = os.environ.get('FOOTBALL_DATA_TOKEN')

def fetch_api_data(url, headers, params=None):
    try:
        response = requests.get(url, headers=headers, params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Error at {url}: {e}")
        sys.exit(1)

def main():
    all_matches = []

    # 1. MLSの取得 (RapidAPI)
    print("Fetching MLS...")
    if RAPIDAPI_KEY:
        headers_mls = {
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": "api-football-v1.p.rapidapi.com"
        }
        # パラメータは実際のAPI仕様に合わせて調整してください
        mls_data = fetch_api_data("https://api-football-v1.p.rapidapi.com/v3/fixtures", headers_mls, params={"league": "253", "next": "10"})
        # 構造に応じて適宜調整してください
        all_matches.extend(mls_data.get('response', []))
    else:
        print("MLS API Key not found, skipping...")

    # 2. 欧州リーグの取得 (football-data.org)
    print("Fetching European leagues...")
    if EURO_API_TOKEN:
        headers_euro = {"X-Auth-Token": EURO_API_TOKEN}
        # ここでリーグごとにループして取得することも可能です
        leagues = ['PL', 'BL1', 'SA', 'PD', 'FL1'] # 必要に応じて追加
        for league in leagues:
            url = f"https://api.football-data.org/v4/competitions/{league}/matches"
            euro_data = fetch_api_data(url, headers_euro)
            all_matches.extend(euro_data.get('matches', []))
    else:
        print("Football-data Token not found, skipping...")

    # 3. JSON保存
    if not os.path.exists('data'):
        os.makedirs('data')
        
    with open('data/schedule.json', 'w', encoding='utf-8') as f:
        json.dump(all_matches, f, ensure_ascii=False, indent=2)
    print("Successfully updated schedule.json with combined data.")

if __name__ == "__main__":
    main()
