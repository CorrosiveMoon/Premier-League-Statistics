from game_query import (
    find_matches_by_team,
    find_player_stats,
    # find_matches_by_date_range,
    find_matches_and_referee_by_team,
    find_matches_scores_and_referee_by_team,
    find_all_matches_by_team_with_dates,
    find_matches_by_referee,
    find_matches_by_score_range,
    find_top_goal_scorers,
    find_top_assist_leaders,
    find_player_with_most_minutes,
    calculate_goal_per_game_ratio,
    calculate_assist_per_game_ratio,
)

import streamlit as st

def main():
    st.title("Premier League Statistics")
    st.sidebar.title("Navigation")

    st.sidebar.image('premierleague.png')


    query_options = st.sidebar.selectbox("Select a query option", [
        "Find all matches by team",
        "Find Player Statistics",
        "Find all matches and referee by team",
        "Find all matches, scores, and referee by team",
        "Find all matches by team with dates",
        # "Find all matches by date range",
        "Find all matches by referee",
        "Find all matches by score range",
        "Find top goal scorers",
        "Find top assist leaders",
        "Find player with most minutes",
        "Calculate goal per game ratio",
        "Calculate assist per game ratio",
    ])

    if query_options == "Find all matches by team":
        team_name = st.sidebar.text_input("Enter team name")
        if st.sidebar.button("Find Matches"):
            matches = find_matches_by_team(team_name)
            st.subheader(f"Matches for {team_name}:")
            for match in matches:
                home_team = match['homeTeam']
                away_team = match['awayTeam']

                if 'crest' in home_team and 'crest' in away_team:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.image(home_team['crest'], caption=home_team['name'], width=100)
                        st.write(f"Home Team: {home_team['name']}")
                    with col2:
                        st.image(away_team['crest'], caption=away_team['name'], width=100)
                        st.write(f"Away Team: {away_team['name']}")
            
                st.write(f"Match ID: {match['_id']}, Home Team: {home_team['name']}, Away Team: {away_team['name']}")
    
    
    elif query_options == "Find Player Statistics":
        player_name = st.sidebar.text_input("Enter Player Name")
        if st.sidebar.button("Find Statistics"):
            player_stats = find_player_stats(player_name)
            st.subheader(f"Player statistics for {player_name}:")
            for stat in player_stats:
                st.write(f"Rank: {stat['Rank']}, Team: {stat['TEAM']}, Goals: {stat['G']}, Assists: {stat['ASST']}")
    
    elif query_options == "Find all matches and referee by team":
        team_name = st.sidebar.text_input("Enter team name")
        if st.sidebar.button("Find Matches and Referee"):
            matches = find_matches_and_referee_by_team(team_name)
            st.subheader(f"Matches for {team_name}:")
            for match in matches:
                st.write(f"Match ID: {match['Match ID']}, Home Team: {match['Home Team']}, Away Team: {match['Away Team']}, Referee: {match['Referee']}")

    elif query_options == "Find all matches, scores, and referee by team":
        team_name = st.sidebar.text_input("Enter team name")
        if st.sidebar.button("Find Matches, Scores, and Referee"):
            matches = find_matches_scores_and_referee_by_team(team_name)
            st.subheader(f"Matches for {team_name}:")
            for match in matches:
                st.write(f"Match ID: {match['Match ID']}, Home Team: {match['Home Team']}, Away Team: {match['Away Team']}, Score: {match['Score']}, Referee: {match['Referee']}")

    elif query_options == "Find all matches by team with dates":
        team_name = st.sidebar.text_input("Enter team name")
        if st.sidebar.button("Find Matches with Dates"):
            matches = find_all_matches_by_team_with_dates(team_name)
            st.subheader(f"Matches for {team_name}:")
            for match in matches:
                st.write(f"Match ID: {match['Match ID']}, Home Team: {match['Home Team']}, Away Team: {match['Away Team']}, Match Date: {match['Match Date']}")

    elif query_options == "Find all matches by referee":
        referee_name = st.sidebar.text_input("Enter referee name")
        if st.sidebar.button("Find Matches"):
            matches = find_matches_by_referee(referee_name)
            st.subheader(f"Matches for {referee_name}:")
            for match in matches:
                st.write(f"Match ID: {match['Match ID']}, Home Team: {match['Home Team']}, Away Team: {match['Away Team']}, Match Date: {match['Match Date']}")
    

    elif query_options == "Find all matches by score range":
        st.sidebar.header("Score Range")
        st.sidebar.write("Enter the score range (0 - 15)")
        min_score = st.sidebar.number_input("Minimum Score", min_value=0, max_value=15, value=0, step=1)
        max_score = st.sidebar.number_input("Maximum Score", min_value=0, max_value=15, value=15, step=1)
        st.sidebar.write("*Note: Maximum score value is 15")
    
        if st.sidebar.button("Find Matches by Score Range"):
            matches = find_matches_by_score_range(min_score, max_score)
            st.subheader(f"Matches with scores between {min_score} and {max_score} goals:")
            for match in matches:
                st.write(f"Match ID: {match['Match ID']}, Home Team: {match['Home Team']}, Away Team: {match['Away Team']}, "
                     f"Home Score: {match['Home Score']}, Away Score: {match['Away Score']}, "
                     f"Match Date: {match['Match Date']}")
                
    elif query_options == "Find top goal scorers":
        num_players = st.sidebar.number_input("Enter number of players", min_value=1, max_value=100, value=10, step=1)
        if st.sidebar.button("Find Top Goal Scorers"):
            players = find_top_goal_scorers(num_players)
            st.subheader(f"Top {num_players} goal scorers:")
            for player in players:
                st.write(f"Player: {player['Player']}, Goals: {player['Goals']}, Team: {player['Team']}")
    
    elif query_options == "Find top assist leaders":
        num_players = st.sidebar.number_input("Enter number of players", min_value=1, max_value=100, value=10, step=1)
        if st.sidebar.button("Find Top Assist Leaders"):
            players = find_top_assist_leaders(num_players)
            st.subheader(f"Top {num_players} assist leaders:")
            for player in players:
                st.write(f"Player: {player['Player']}, Assists: {player['Assists']}, Team: {player['Team']}")
    
    elif query_options == "Find player with most minutes":
        if st.sidebar.button("Find Player with Most Minutes"):
            player = find_player_with_most_minutes()
            st.subheader(f"Player with most minutes:")
            st.write(f"Player: {player['Player']}, Minutes: {player['Minutes Played']}, Team: {player['Team']}")
    
    elif query_options == "Calculate goal per game ratio":
        player_name = st.sidebar.text_input("Enter player name")
        if st.sidebar.button("Calculate Goal Per Game Ratio"):
            ratio = calculate_goal_per_game_ratio(player_name)
            st.subheader(f"Goal per game ratio for {player_name}:")
            st.write(f"Ratio: {ratio}")
    
    elif query_options == "Calculate assist per game ratio":
        player_name = st.sidebar.text_input("Enter player name")
        if st.sidebar.button("Calculate Assist Per Game Ratio"):
            ratio = calculate_assist_per_game_ratio(player_name)
            st.subheader(f"Assist per game ratio for {player_name}:")
            st.write(f"Ratio: {ratio}")
    



main()

