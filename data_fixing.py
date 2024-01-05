import pymongo
import json

# Open the JSON file containing the filtered Premier League data
with open('premier_league_filtered_data.json', 'r') as league_data_file:
    league_data = json.load(league_data_file)

# Connect to the MongoDB instance (assuming it's running on localhost)
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['premier_league_db']

# Create a collection for the league data
league_data_collection = db['league_data']

# Insert each record from the filtered JSON data as an individual document
for record in league_data:
    league_data_collection.insert_one(record)

# Open the JSON file containing the player stats data
with open('Premier League Player Stats.json', 'r') as player_stats_file:
    player_stats_data = [json.loads(line) for line in player_stats_file]

# Create a collection for the player stats data and insert all records
player_stats_collection = db['player_stats']
player_stats_collection.insert_many(player_stats_data)

# Close the MongoDB connection
client.close()
