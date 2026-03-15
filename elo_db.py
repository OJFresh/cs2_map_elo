import pandas as pd

from match import Match

TEAM_RANKINGS = [
    'Vitality',
    'FURIA',
    'MOUZ',
    'Falcons',
    'PARIVISION',
    'Spirit',
    'The MongolZ',
    'Aurora',
    'Natus Vincere',
    'G2',
    'FaZe',
    'Astralis',
    'FUT',
    '3DMAX',
    'paiN',
    'Liquid',
    'GamerLegion',
    'HEROIC',
    'B8',
    'Gentle Mates',
]
def build_empty_elo_df():
    matches = pd.read_csv('config/match_data.csv')
    maps = set(matches['map_name'])
    teams = set(list(matches['win_team']) + list(matches['lose_team']))
    df_dict = {'team_name': list(teams)}
    for map_name in maps:
        df_dict[map_name] = [0.0]*len(teams)
    df = pd.DataFrame(df_dict)
    df.to_csv('config/elo.csv', index=False)

def build_alt_elo_df():
    matches = pd.read_csv('config/match_data.csv')
    maps = set(matches['map_name'])
    df_dict = {'team_name': TEAM_RANKINGS}
    for map_name in maps:
        df_dict[map_name] = [100 + float(x)/2 for x in range(len(TEAM_RANKINGS), 0, -1)]
    df = pd.DataFrame(df_dict)
    df.to_csv('config/elo.csv', index=False)

def populate_elo_database():
    matches = pd.read_csv('config/match_data.csv')
    for i, x in matches.iterrows():
        kwargs = x.to_dict()
        Match(**kwargs).modify_elo()