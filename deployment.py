from game_query import (
    find_matches_by_team,
    find_player_stats,
    find_matches_by_date_range,
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
        "Find all matches by team with dates",
        "Find all matches by date range",
        "Find all matches and referee by team",
        "Find all matches, scores, and referee by team",
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
        
        



main()