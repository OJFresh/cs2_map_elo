import pandas as pd


def build_empty_elo_df(maps, teams):
    df_dict = {'team_name': list(teams)}
    for map_name in maps:
        df_dict[map_name] = [0]*len(teams)
    df = pd.DataFrame(df_dict)
    df.to_csv('config/elo.csv', index=False)


def execute():
    matches = pd.read_csv('config/match_data.csv')
    maps = set(matches['Map Name'])
    teams = set(list(matches['Winning Team Name']) + list(matches['Losing Team Name']))
    build_empty_elo_df(maps, teams)


execute()
