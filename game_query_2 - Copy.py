import pymongo
from datetime import datetime

mongo_url = "mongodb://localhost:27017/"

client = pymongo.MongoClient(mongo_url)

db = client.premier_league_db

def find_matches_by_team(team_name):
    matches = db.league_data.find(
        {
            "$or": [
                {"homeTeam.name": team_name},
                {"awayTeam.name": team_name},
            ]
        }
    )
    return list(matches)

#Function to find player statistics for a specific player
def find_player_stats(player_name):
    stats = db.player_stats.find({"PLAYER": player_name})
    return list(stats)

#Function to find matches within a specific date range
def find_matches_by_date_range(start_date, end_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    matches = db.league_data.find(
        {
            "$and": [
                {"season.startDate": {"$lte": end_date}},
                {"season.endDate": {"$gte": start_date}},
            ]
        }
    )
    return list(matches)

def find_referee_and_venue(match_id):
    match = db.league_data.find_one({"_id": match_id})
    if match:
        referee_name = match.get("referee", "N/A")
        venue_name = match.get("venue", "N/A")
        return referee_name, venue_name
    else:
        return "Match not found", "N/A"

if __name__ == "__main__":
    # Find all matches played by a specific team
    team_name = "Manchester City FC"
    team_matches = find_matches_by_team(team_name)
    print("Matches played by Manchester City FC:")
    for match in team_matches:
        print(f"Match ID: {match['_id']}, Home Team: {match['homeTeam']['name']}, Away Team: {match['awayTeam']['name']}")

    # Find player statistics for a specific player
    player_name = "Harry Kane"
    player_stats = find_player_stats(player_name)
    if player_stats:
        print("Player statistics for Harry Kane:")
        for stat in player_stats:
            print(f"Rank: {stat['Rank']}, Team: {stat['TEAM']}, Goals: {stat['G']}, Assists: {stat['ASST']}")

    # Find matches within a date range
    start_date = "2022-08-05"
    end_date = "2023-05-28"
    date_range_matches = find_matches_by_date_range(start_date, end_date)
    print(f"Matches within date range ({start_date} - {end_date}):")
    for match in date_range_matches:
        print(f"Match ID: {match['_id']}, Home Team: {match['homeTeam']['name']}, Away Team: {match['awayTeam']['name']}")