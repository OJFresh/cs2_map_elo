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

# the more positive, more in favour of team_a
def compare_teams(team_a, team_b):
    elo = pd.read_csv('config/elo.csv', index_col='team_name')
    team_a_elos = dict(elo.loc[team_a])
    team_b_elos = dict(elo.loc[team_b])
    elo_diff = {map_name: (team_a_elos[map_name] - team_b_elos[map_name]) for map_name in elo.columns}
    sorted_elos = [[map_name, elo] for map_name, elo in sorted(elo_diff.items(), key=lambda item: item[1], reverse=True)]
    print(f'{team_a} bans {sorted_elos[6][0]} (Diff: {sorted_elos[6][1]})')
    print(f'{team_b} bans {sorted_elos[0][0]} (Diff: {sorted_elos[0][1]})')
    print(f'{team_a} picks {sorted_elos[1][0]} (Diff: {sorted_elos[1][1]})')
    print(f'{team_b} picks {sorted_elos[5][0]} (Diff: {sorted_elos[5][1]})')
    print(f'{team_a} bans {sorted_elos[4][0]} (Diff: {sorted_elos[4][1]})')
    print(f'{team_b} bans {sorted_elos[2][0]} (Diff: {sorted_elos[2][1]})')
    print(f'{sorted_elos[3][0]} remaining (Diff: {sorted_elos[3][1]})')


compare_teams('Vitality','FaZe')
