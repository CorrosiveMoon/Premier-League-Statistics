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
                st.write(f"Match ID: {match['_id']}, Home Team: {match['homeTeam']['name']}, Away Team: {match['awayTeam']['name']}")

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
    
    elif query_options == "Find Matches by Score Range":
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


    



main()