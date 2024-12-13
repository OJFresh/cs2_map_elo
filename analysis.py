import pandas as pd
from pprint import pprint as pp


class Analyser:
    @property
    def elo_df(self):
        return pd.read_csv('config/elo.csv', index_col='team_name')

    def map_rankings(self, map_name):
        print(f'{map_name} Ranking')
        sorted_ranking = self.elo_df.sort_values(map_name, ascending=False)
        for i, (team, df_dict) in enumerate(sorted_ranking.iterrows()):
            print(f'{i + 1}) {team} ({df_dict[map_name].round(2)})')

    # the more positive, more in favour of team_a
    def elo_diff(self, team_a, team_b):
        team_a_elos = dict(self.elo_df.loc[team_a])
        team_b_elos = dict(self.elo_df.loc[team_b])
        elo_diff = {map_name: float(team_a_elos[map_name]) - float(team_b_elos[map_name]) for map_name in self.elo_df.columns}
        return [[map_name, elo] for map_name, elo in sorted(elo_diff.items(), key=lambda item: item[1], reverse=True)]

    def veto_predictor(self, team_a, team_b):
        elo_diff = self.elo_diff(team_a, team_b)
        print(f'{team_a} bans {elo_diff[6][0]} (Diff: {elo_diff[6][1]})')
        print(f'{team_b} bans {elo_diff[0][0]} (Diff: {elo_diff[0][1]})')
        print(f'{team_a} picks {elo_diff[1][0]} (Diff: {elo_diff[1][1]})')
        print(f'{team_b} picks {elo_diff[5][0]} (Diff: {elo_diff[5][1]})')
        print(f'{team_a} bans {elo_diff[4][0]} (Diff: {elo_diff[4][1]})')
        print(f'{team_b} bans {elo_diff[2][0]} (Diff: {elo_diff[2][1]})')
        print(f'{elo_diff[3][0]} remaining (Diff: {elo_diff[3][1]})')

def execute():
    pp(Analyser().elo_diff('FaZe', 'G2'))

execute()