from datetime import date
import pandas as pd
import re

from match import Match


def name_score_parser(team):
    name, score = team.split(' (')
    filtered_name = ''
    for num, char in enumerate(name[1:]):
        if char.isupper():
            filtered_name = name[num + 1:]
            break
    filtered_score = int(score[0:-1])
    return filtered_name, filtered_score


def create_matches_database():
    dates = []
    map_names = []
    winner_names = []
    loser_names = []
    winner_scores = []
    loser_scores = []
    with open('config/raw_match_data.txt', 'r') as f:
        file = f.readlines()
        matches = [file[n:n+4] for n in range(0, len(file), 4)]
        for match in matches:
            parsed_match_data = parse_match(match)
            dates.append(parsed_match_data[0])
            winner_names.append(parsed_match_data[1])
            winner_scores.append(parsed_match_data[2])
            loser_names.append(parsed_match_data[3])
            loser_scores.append(parsed_match_data[4])
            map_names.append(parsed_match_data[5])
    matches_dict = {
        'date': dates,
        'map_name': map_names,
        'win_team': winner_names,
        'lose_team': loser_names,
        'win_score': winner_scores,
        'lose_score': loser_scores,
    }
    df = pd.DataFrame(matches_dict)
    df.to_csv('config/match_data.csv', index=False)

def parse_match(match_lines):
    match_date, teams_scores, map_name, event_name = [line.replace('\n', '') for line in match_lines]
    day, month, year = match_date.split('/')
    game_date = date(2000 + int(year), int(month), int(day))
    filtered_team_scores = re.findall(r'\w+ *\.*\w*', teams_scores)
    if int(filtered_team_scores[1]) < int(filtered_team_scores[3]):
        filtered_team_scores = filtered_team_scores[2:4] + filtered_team_scores[:2]
    return [game_date] + filtered_team_scores + [map_name, event_name]

def build_empty_elo_df():
    matches = pd.read_csv('config/match_data.csv')
    maps = set(matches['map_name'])
    teams = set(list(matches['win_team']) + list(matches['lose_team']))
    df_dict = {'team_name': list(teams)}
    for map_name in maps:
        df_dict[map_name] = [0.0]*len(teams)
    df = pd.DataFrame(df_dict)
    df.to_csv('config/elo.csv', index=False)


def populate_elo_database():
    matches = pd.read_csv('config/match_data.csv')
    for i, x in matches.iterrows():
        kwargs = x.to_dict()
        Match(**kwargs).modify_elo()

create_matches_database()