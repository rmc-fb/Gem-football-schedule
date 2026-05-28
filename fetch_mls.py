import os
import requests
import json

API_KEY = os.environ.get("RAPIDAPI_KEY", "").strip()
API_HOST = "api-football186.p.rapidapi.com"
headers = {"X-RapidAPI-Key": API_KEY, "X-RapidAPI-Host": API_HOST}
params = {"competitionid": "1855", "paged": "1"}

# 試すパスの候補
urls = [
    "https://api-football186.p.rapidapi.com/competition/matches",
    "https://api-football186.p.rapidapi.com/competitions/matches",
    "https://api-football186.p.rapidapi.com/matches/list"
]

for url in urls:
    response = requests.get(url, headers=headers, params=params)
    print(f"URL: {url} -> ステータス: {response.status_code}")
    if response.status_code == 200:
        print("成功！データ:", response.json())
        break
