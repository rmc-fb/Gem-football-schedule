import requests
import json
import os

target_leagues = ['PL', 'BL1', 'SA', 'PD', 'FL1', 'CL', 'DED', 'PPL', 'ELC', 'BSA', 'MLS']
API_TOKEN = os.environ.get('FOOTBALL_DATA_TOKEN')

def fetch_all_matches():
    all_matches = []
    headers = {'X-Auth-Token': API_TOKEN}
    
    for league in target_leagues:
        url = f'https://api.football-data.org/v4/competitions/{league}/matches'
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            all_matches.extend(data.get('matches', []))
        else:
            print(f"Failed to fetch {league}: {response.status_code}")

    # dataフォルダがなければ作成する処理
    if not os.path.exists('data'):
        os.makedirs('data')

    with open('data/schedule.json', 'w', encoding='utf-8') as f:
        json.dump(all_matches, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    fetch_all_matches()
