import pandas as pd


def execute():
    map_ranking('Mirage')


def map_ranking(map_name):
    print(f'{map_name} Ranking')
    elo = pd.read_csv('config/elo.csv', index_col='team_name')
    sorted_ranking = elo.sort_values(map_name, ascending=False)
    for i, (team, df_dict) in enumerate(sorted_ranking.iterrows()):
        print(f'{i+1}) {team} ({df_dict[map_name].round(2)})')


execute()
