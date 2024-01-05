import requests
import json

url = "https://api.football-data.org/v4/competitions/PL/matches?season=2022"

headers = {'X-Auth-Token': "b7a758a85ac34145b191d10607fbca5a"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    premier_league_data = response.json()
    winner_info = None

    for match in premier_league_data['matches']:
        if match['status'] == 'FINISHED' and match['season']['endDate'] == '2023-05-28':
            winner_info = {
                'name': match['season']['winner']['name'],
                'crest': match['season']['winner']['crest'],
                'tla': match['season']['winner']['tla'],
            }
            break

    filtered_data = []

    for match in premier_league_data['matches']:
        referee_name = match['referees'][0]['name'] if len(match['referees']) > 0 else "N/A"
        match_info = {
            'winner': match['score']['winner'],
            'start_date': match['season']['startDate'],
            'end_date': match['season']['endDate'],
            'matchday': match['matchday'],
            'utcDate': match['utcDate'],
            'homeTeam': match['homeTeam'],
            'awayTeam': match['awayTeam'],
            'score': match['score'],
            'referee': referee_name, 
        }
        filtered_data.append(match_info)

    if winner_info:
        print("Winner of the Premier League (2022-2023):")
        print(f"Name: {winner_info['name']}")
        print(f"Crest: {winner_info['crest']}")
        print(f"TLA (Short Name): {winner_info['tla']}")
    else:
        print("Premier League winner information not found for the specified season.")

    file_path = "premier_league_filtered_data.json"
    with open(file_path, "w") as f:
        json.dump(filtered_data, f, indent=4)
        print(f"Filtered data saved to {file_path}")

else:
    premier_league_data = None
    print("Error in retrieving data")
