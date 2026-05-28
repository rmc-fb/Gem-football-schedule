import os
import requests
import json

API_KEY = os.environ.get("RAPIDAPI_KEY", "").strip()
API_HOST = "api-football186.p.rapidapi.com"
headers = {"X-RapidAPI-Key": API_KEY, "X-RapidAPI-Host": API_HOST}

# エンドポイントのリストを確認するために、まずはベースURLを叩く
# （もし何も出なければ、APIのドキュメントページで「Endpoints」の一覧を教えてくれれば、パスを特定する！）
url = "https://api-football186.p.rapidapi.com/matches" # '/competition' を取ってみた
params = {"cid": "1855", "paged": "1"}

response = requests.get(url, headers=headers, params=params)
print("結果:", response.json())
