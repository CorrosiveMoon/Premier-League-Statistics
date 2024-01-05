import requests
import json

url = "https://api.football-data.org/v4/competitions/PL/matches?season=2022"

headers = {'X-Auth-Token': "b7a758a85ac34145b191d10607fbca5a"}

response = requests.get(url, headers = headers)

if response.status_code == 200:
    premier_league_data = response.json()
    file_path = "premier_league_data.json"
    with open(file_path, "w") as f:
        json.dump(premier_league_data, f, indent = 4)


else:
    premier_league_data = None
    print("Error in retrieving data")
