import pandas as pd
from pprint import pprint as pp

def execute():
    map_ranking('Mirage')


def map_ranking(map_name):
    print(f'{map_name} Ranking')
    elo = pd.read_csv('config/elo.csv', index_col='team_name')
    sorted_ranking = elo.sort_values(map_name, ascending=False)
    for i, (team, df_dict) in enumerate(sorted_ranking.iterrows()):
        print(f'{i+1}) {team} ({df_dict[map_name].round(2)})')


def compare_teams(team_a, team_b):
    elo = pd.read_csv('config/elo.csv', index_col='team_name')
    team_a_elos = dict(elo.loc[team_a])
    team_b_elos = dict(elo.loc[team_b])
    elo_diff = {map_name: (team_a_elos[map_name] - team_b_elos[map_name]) for map_name in elo.columns}
    sorted_elos = (sorted(elo_diff.items(), key=lambda item: item[1], reverse=True))
    pp(sorted_elos)

compare_teams('FaZe','G2')
