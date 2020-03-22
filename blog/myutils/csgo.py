import requests
import json
import datetime
import os


def get_match_stats(link):
    # Get match_id from link and form request URL
    match_id = link[36:74]
    match_request_url = 'https://open.faceit.com/data/v4/matches/' + str(match_id)

    # Authorization and request
    faceit_app_id = os.environ['FACEIT_APP_ID']
    bearer = 'Bearer ' + os.environ['FACEIT_SERVER_API_KEY']
    headers = {
        'Authorization': bearer
    }
    response = requests.get(match_request_url, headers=headers)

    # Lets see if the response is ok
    if response.status_code != 200:
        comeback = 'Oops, error: ' + str(response.status_code) + ' all up in this bitch.'
        return comeback

    # and parse it
    r_j = response.json()
    """
    if r_j['game'] != 'csgo':
        return 'This is not a csgolink'
    game_type = r_j['competition_name']
    demo_link = r_j['demo_url'][0]
    region = r_j['region']
    started_at = (r_j['started_at'])
    game_status = r_j['status'].lower().capitalize()
    team_one = r_j['teams']['faction1']
    team_two = r_j['teams']['faction2']
    team_one_name = team_one['name']
    team_two_name = team_two['name']
    team_one_roster = team_one['roster']
    team_two_roster = team_two['roster']
    team_one_player_names = []
    team_one_player_steam_names = []
    for player in team_one_roster:
        team_one_player_names.append(player['nickname'])
        team_one_player_steam_names.append(player['game_player_name'])
    test_guy = team_one_roster[1]
    """
    return r_j


def epoch_to_string(epoch_time):
    ts = datetime.datetime.fromtimestamp(int(epoch_time)).strftime('%d.%m.%Y %H:%M')
    ts = str(ts)
    return ts
