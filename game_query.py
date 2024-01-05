import pymongo
from datetime import datetime, timedelta


# Define the MongoDB connection URL (replace with your actual MongoDB URL)
mongo_url = "mongodb://localhost:27017/"

# Connect to the MongoDB server
client = pymongo.MongoClient(mongo_url)

# Access the premier_league_db database
db = client.premier_league_db_2

# Function to find all matches played by a specific team
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

# Function to find player statistics for a specific player
def find_player_stats(player_name):
    stats = db.player_stats.find({"PLAYER": player_name})
    return list(stats)

# Function to find matches within a specific date range
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

def find_matches_and_referee_by_team(team_name):
    matches = db.league_data.find(
        {
            "$or": [
                {"homeTeam.name": team_name},
                {"awayTeam.name": team_name},
            ]
        }
    )
    match_list = []
    for match in matches:
        match_info = {
            "Match ID": match["_id"],
            "Home Team": match["homeTeam"]["name"],
            "Away Team": match["awayTeam"]["name"],
            "Referee": match.get("referee", "N/A"),
        }
        match_list.append(match_info)
    return match_list

def find_matches_scores_and_referee_by_team(team_name):
    matches = db.league_data.find(
        {
            "$or": [
                {"homeTeam.name": team_name},
                {"awayTeam.name": team_name},
            ]
        }
    )
    match_list = []
    for match in matches:
        home_score = match["score"]["fullTime"]["home"]
        away_score = match["score"]["fullTime"]["away"]
        match_info = {
            "Match ID": match["_id"],
            "Home Team": match["homeTeam"]["name"],
            "Away Team": match["awayTeam"]["name"],
            "Referee": match.get("referee", "N/A"),
            "Score": f"{home_score} - {away_score}",
        }
        match_list.append(match_info)
    return match_list


def find_all_matches_by_team_with_dates(team_name):
    matches = db.league_data.find(
        {
            "$or": [
                {"homeTeam.name": team_name},
                {"awayTeam.name": team_name},
            ]
        }
    )
    match_list = []
    for match in matches:
        match_info = {
            "Match ID": match["_id"],
            "Home Team": match["homeTeam"]["name"],
            "Away Team": match["awayTeam"]["name"],
            "Match Date": match["utcDate"]
        }
        match_list.append(match_info)
    return match_list


def find_matches_by_referee(referee_name):
    matches = db.league_data.find({"referee": referee_name})
    match_list = []
    for match in matches:
        home_team = match["homeTeam"]["name"]
        away_team = match["awayTeam"]["name"]
        match_info = {
            "Match ID": match["_id"],
            "Home Team": home_team,
            "Away Team": away_team,
            "Referee": referee_name,
            "Match Date": match["utcDate"],
        }
        match_list.append(match_info)
    return match_list


def find_matches_by_score_range(min_score, max_score):
    matches = db.league_data.find({
        "score.fullTime.home": {"$gte": min_score},
        "score.fullTime.away": {"$gte": min_score},
        "score.fullTime.home": {"$lte": max_score},
        "score.fullTime.away": {"$lte": max_score},
    })
    match_list = []
    for match in matches:
        home_team = match["homeTeam"]["name"]
        away_team = match["awayTeam"]["name"]
        match_info = {
            "Match ID": match["_id"],
            "Home Team": home_team,
            "Away Team": away_team,
            "Home Score": match["score"]["fullTime"]["home"],
            "Away Score": match["score"]["fullTime"]["away"],
            "Match Date": match["utcDate"],
        }
        match_list.append(match_info)
    return match_list

# Function to find top goal scorers
def find_top_goal_scorers(num_players):
    top_scorers = db.player_stats.find().sort("G", pymongo.DESCENDING).limit(num_players)
    top_scorers_list = []
    for player in top_scorers:
        player_info = {
            "Player": player["PLAYER"],
            "Team": player["TEAM"],
            "Goals": player["G"],
        }
        top_scorers_list.append(player_info)
    return top_scorers_list


# Function to find top assist leaders
def find_top_assist_leaders(num_players):
    top_assist_leaders = db.player_stats.find().sort("ASST", pymongo.DESCENDING).limit(num_players)
    top_assist_leaders_list = []
    for player in top_assist_leaders:
        player_info = {
            "Player": player["PLAYER"],
            "Team": player["TEAM"],
            "Assists": player["ASST"],
        }
        top_assist_leaders_list.append(player_info)
    return top_assist_leaders_list

def find_player_with_most_minutes():
    player_most_minutes = db.player_stats.find().sort("MIN", pymongo.DESCENDING).limit(1)
    player_info = None
    for player in player_most_minutes:
        player_info = {
            "Player": player["PLAYER"],
            "Team": player["TEAM"],
            "Minutes Played": player["MIN"],
        }
    return player_info

# Function to calculate goal per game ratio
def calculate_goal_per_game_ratio(player_name):
    player_stats = db.player_stats.find_one({"PLAYER": player_name})
    if player_stats:
        goals = player_stats["G"]
        games_played = player_stats["GP"]
        if games_played > 0:
            goal_per_game_ratio = goals / games_played
            return goal_per_game_ratio
    return None

# Function to calculate assist per game ratio
def calculate_assist_per_game_ratio(player_name):
    player_stats = db.player_stats.find_one({"PLAYER": player_name})
    if player_stats:
        assists = player_stats["ASST"]
        games_played = player_stats["GP"]
        if games_played > 0:
            assist_per_game_ratio = assists / games_played
            return assist_per_game_ratio
    return None


# Example usage
    # Find all matches played by a specific team
# team_name = "Manchester City FC"
# team_matches = find_matches_by_team(team_name)
# print("Matches played by Manchester City FC:")
# for match in team_matches:
#     print(f"Match ID: {match['_id']}, Home Team: {match['homeTeam']['name']}, Away Team: {match['awayTeam']['name']}")

#     # Find player statistics for a specific player
#     player_name = "Harry Kane"
#     player_stats = find_player_stats(player_name)
#     if player_stats:
#         print("Player statistics for Harry Kane:")
#         for stat in player_stats:
#             print(f"Rank: {stat['Rank']}, Team: {stat['TEAM']}, Goals: {stat['G']}, Assists: {stat['ASST']}")

#     # Find matches within a date range
#     start_date = "2022-08-05"
#     end_date = "2023-05-28"
#     date_range_matches = find_matches_by_date_range(start_date, end_date)
#     print(f"Matches within date range ({start_date} - {end_date}):")
#     for match in date_range_matches:
#         print(f"Match ID: {match['_id']}, Home Team: {match['homeTeam']['name']}, Away Team: {match['awayTeam']['name']}")

    # Example usage to get matches and referees for Manchester City FC
# team_matches_with_referee = find_matches_and_referee_by_team(team_name)
# print(f"Matches played by {team_name}:")
# for match_info in team_matches_with_referee:
#     print(f"Match ID: {match_info['Match ID']}, Home Team: {match_info['Home Team']}, Away Team: {match_info['Away Team']}, Referee: {match_info['Referee']}")

    
# team_matches_scores_and_referee = find_matches_scores_and_referee_by_team(team_name)
# print(f"Matches played by {team_name}:")
# for match_info in team_matches_scores_and_referee:
#     print(f"Match ID: {match_info['Match ID']}, Home Team: {match_info['Home Team']}, Away Team: {match_info['Away Team']}, Score: {match_info['Score']}, Referee: {match_info['Referee']}")


    # team_matches_with_dates = find_all_matches_by_team_with_dates(team_name)
    # print("\nAll Matches played by Manchester City FC with dates:")
    # for match_info in team_matches_with_dates:
    #     print(f"Match ID: {match_info['Match ID']}, Home Team: {match_info['Home Team']}, Away Team: {match_info['Away Team']}, Match Date: {match_info['Match Date']}")
        
    # referee_name = "Anthony Taylor"  # Replace with the desired referee's name
    # referee_matches = find_matches_by_referee(referee_name)
    # print(f"Matches officiated by {referee_name}:")
    # for match in referee_matches:
    #     print(f"Match ID: {match['Match ID']}, Home Team: {match['Home Team']}, Away Team: {match['Away Team']}, Match Date: {match['Match Date']}")
        
# min_score = 3
# max_score = 5
# score_range_matches = find_matches_by_score_range(min_score, max_score)
# print(f"Matches with scores between {min_score} and {max_score} goals:")
# for match in score_range_matches:
#     print(f"Match ID: {match['Match ID']}, Home Team: {match['Home Team']}, Away Team: {match['Away Team']}, "
#           f"Home Score: {match['Home Score']}, Away Score: {match['Away Score']}, "
#           f"Match Date: {match['Match Date']}")

num_top_scorers = 1
top_scorers = find_top_goal_scorers(num_top_scorers)
print(f"Top {num_top_scorers} Goal Scorers:")
for player_info in top_scorers:
    print(f"Player: {player_info['Player']}, Team: {player_info['Team']}, Goals: {player_info['Goals']}")

# Example usage to get top assist leaders
num_top_assist_leaders = 1
top_assist_leaders = find_top_assist_leaders(num_top_assist_leaders)
print(f"Top {num_top_assist_leaders} Assist Leaders:")
for player_info in top_assist_leaders:
    print(f"Player: {player_info['Player']}, Team: {player_info['Team']}, Assists: {player_info['Assists']}")

# Example usage to get player with most minutes played
most_minutes_player = find_player_with_most_minutes()
print("Player with Most Minutes Played:")
if most_minutes_player:
    print(f"Player: {most_minutes_player['Player']}, Team: {most_minutes_player['Team']}, Minutes Played: {most_minutes_player['Minutes Played']}")

# Example usage to calculate goal per game ratio for a specific player
player_name = "Harry Kane"
goal_per_game_ratio = calculate_goal_per_game_ratio(player_name)
if goal_per_game_ratio is not None:
    print(f"Goal Per Game Ratio for {player_name}: {goal_per_game_ratio:.2f}")

# Example usage to calculate assist per game ratio for a specific player
player_name = "Kevin De Bruyne"
assist_per_game_ratio = calculate_assist_per_game_ratio(player_name)
if assist_per_game_ratio is not None:
    print(f"Assist Per Game Ratio for {player_name}: {assist_per_game_ratio:.2f}")
        

# client.close()
