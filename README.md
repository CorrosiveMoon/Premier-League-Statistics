# Premier League Statistics Dashboard

## Work Done

This project involves the creation of a Premier League statistics dashboard that allows users to query and explore Premier League data using various criteria. The work includes:

1. Retrieving Premier League data from the Football Data API and storing it in a MongoDB database.
2. Implementing a set of Python functions to query the database for various statistics and information, including match details, player statistics, referee information, and more.
3. Creating a Streamlit web app that provides a user-friendly interface for interacting with the data and running queries.
4. The Streamlit app allows users to select different query options, input criteria (such as team names, player names, date ranges, score ranges, etc.), and view the results in a visually appealing format.
5. The provided Python scripts demonstrate how to use the functions to query the database and display relevant information to the user.

## Dependencies

The following dependencies are required to run the provided Python scripts and Streamlit web app:

- Python 3.x
- MongoDB (running locally or on a remote server)
- pymongo library
- requests library
- json library
- datetime library
- Streamlit library

Make sure to install these dependencies using `pip` or another package manager before running the scripts.

## Functionality

The Premier League Statistics Dashboard provides the following functionality:

1. **Find all matches by team**: Allows users to search for all matches played by a specific Premier League team and view match details.

2. **Find Player Statistics**: Enables users to search for statistics of a specific player, including goals, assists, and team information.

3. **Find all matches and referee by team**: Retrieves all matches played by a team and displays the referee for each match.

4. **Find all matches, scores, and referee by team**: Retrieves matches played by a team, including scores and the referee for each match.

5. **Find all matches by team with dates**: Displays matches played by a team along with their respective dates.

6. **Find all matches by referee**: Retrieves all matches officiated by a specific referee and displays match details.

7. **Find all matches by score range**: Allows users to specify a score range (minimum and maximum goals) and retrieves matches within that range.

8. **Find top goal scorers**: Retrieves the top goal scorers in the Premier League, with the option to specify the number of players to display.

9. **Find top assist leaders**: Retrieves the top assist leaders in the Premier League, with the option to specify the number of players to display.

10. **Find player with most minutes**: Identifies the player with the most minutes played in the Premier League.

11. **Calculate goal per game ratio**: Calculates and displays the goal per game ratio for a specific player.

12. **Calculate assist per game ratio**: Calculates and displays the assist per game ratio for a specific player.

## Code

The project consists of several Python scripts:

- `premier_league_data.py`: Retrieves Premier League data from the Football Data API and stores it in a JSON file.

- `data_fixing.py`: Imports data from JSON files and stores it in a MongoDB database.

- `premier_league_data_filtered.py`: Filters Premier League data for a specific season and stores it in a JSON file.

- `game_query.py`: Contains functions for querying the MongoDB database with various criteria.

- `deployment.py`: Implements a Streamlit web app that allows users to interact with the data and run queries.

## How to Run

Follow these steps to run the Premier League Statistics Dashboard:

1. Ensure that you have Python 3.x and the required libraries (pymongo, requests, json, datetime, and Streamlit) installed.

2. Set up a MongoDB database either locally or on a remote server. Update the MongoDB connection URL in the `game_query.py` script if necessary.

3. Run the following scripts in the following order:

   - `premier_league_data.py` to fetch Premier League data and store it in a JSON file.
   - `data_fixing.py` to import data from JSON files into the MongoDB database.
   - `premier_league_data_filtered.py` to filter data for a specific season and store it in a JSON file.

4. Finally, run the Streamlit app using the following command:
    - `streamlit run deployment.py`
