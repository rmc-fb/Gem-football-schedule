import os
import requests
import json

API_KEY = os.environ.get("RAPIDAPI_KEY", "").strip()
API_HOST = "api-football186.p.rapidapi.com"
headers = {"X-RapidAPI-Key": API_KEY, "X-RapidAPI-Host": API_HOST}

# Competition MatchesのエンドポイントURLはここや！
# 'competition' をパスに入れる必要があるんやね
url = "https://api-football186.p.rapidapi.com/competition/matches/list/"

# パラメータもさっきのIDを指定する
params = {"competitionid": "1855", "paged": "1"}

response = requests.get(url, headers=headers, params=params)
print("結果:", response.json())
