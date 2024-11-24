from datetime import date
import pandas as pd

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
        for i in range(0, len(file), 4):
            filtered_date = file[i].replace('\n', '')
            day, month, year = filtered_date.split('/')
            game_date = date(2000 + int(year), int(month), int(day))
            teams = file[i + 1].replace('\n', '')
            map_name = file[i + 2].replace('\n', '')
            team_a, team_b= teams.split('\t')
            name_winner, score_winner = name_score_parser(team_a)
            name_loser, score_loser = name_score_parser(team_b)
            if score_loser > score_winner:
                name_winner, score_winner = name_score_parser(team_b)
                name_loser, score_loser = name_score_parser(team_a)
            dates.append(game_date)
            map_names.append(map_name)
            winner_names.append(name_winner)
            loser_names.append(name_loser)
            winner_scores.append(score_winner)
            loser_scores.append(score_loser)
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


def build_empty_elo_df():
    matches = pd.read_csv('config/match_data.csv')
    maps = set(matches['map_name'])
    teams = set(list(matches['win_team']) + list(matches['lose_team']))
    df_dict = {'team_name': list(teams)}
    for map_name in maps:
        df_dict[map_name] = [0]*len(teams)
    df = pd.DataFrame(df_dict)
    df.to_csv('config/elo.csv', index=False)


def populate_elo_database():
    matches = pd.read_csv('config/match_data.csv')
    for i, x in matches.iterrows():
        kwargs = x.to_dict()
        Match(**kwargs).modify_elo()
