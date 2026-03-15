import math
from itertools import combinations
from pprint import pprint as pp

import pandas as pd


class MatchupAnalyser:

    def __init__(self, team_a, team_b):
        self.team_a = team_a
        self.team_b = team_b

    @property
    def elo_df(self):
        return pd.read_csv('config/elo.csv', index_col='team_name')

    def map_rankings(self, map_name):
        print(f'{map_name} Ranking')
        sorted_ranking = self.elo_df.sort_values(map_name, ascending=False)
        for i, (team, df_dict) in enumerate(sorted_ranking.iterrows()):
            print(f'{i + 1}) {team} ({df_dict[map_name].round(2)})')

    # the more positive, more in favour of team_a
    @property
    def map_win_odds(self):
        team_a_elos = dict(self.elo_df.loc[self.team_a])
        team_b_elos = dict(self.elo_df.loc[self.team_b])
        elo_difference = [[map_name, elo - team_b_elos[map_name]] for map_name, elo in team_a_elos.items()]
        sorted_elo_diff = sorted(elo_difference, key=lambda item: item[1], reverse=True)
        return {map_name: self.elo_to_map_win_odds(float(elo)) for map_name, elo in sorted_elo_diff}

    def map_win_percentages(self):
        for map_name, elo in self.map_win_odds.items():
            print(f'{self.team_a} has a {elo*100:.2f}% of winning {map_name}')

    def elo_to_map_win_odds(self, map_elo_diff):
        map_elo_diff = min(map_elo_diff, 5)
        map_elo_diff = max(map_elo_diff, -5)
        return (map_elo_diff + 5)/10

    def match_win_odds(self, map_names):
        restricted_odds_list = {map_name: odds for map_name, odds in self.map_win_odds.items() if map_name in map_names}
        required_wins = math.ceil(len(map_names)/2) if len(map_names)%2 != 0 else math.ceil(len(map_names)/2) + 1
        index_combinations = [combinations(map_names, games) for games in range(required_wins)]
        seperated_chance_combinations = [index for index_combination in index_combinations for index in index_combination]
        total_list = []
        for chance_combination in seperated_chance_combinations:
            odds_list = [ ]
            for map_name, odds in restricted_odds_list.items():
                new_odds = 1 - odds if map_name in chance_combination else odds
                odds_list.append(new_odds)
            total_list.append(odds_list)
        win_chance = sum([math.prod(combination) for combination in total_list])
        print(f"The chance of {self.team_a} winning the game is {win_chance*100:.2f}%")

def execute():
    analyser = MatchupAnalyser('Natus Vincere', 'Aurora')
    analyser.match_win_odds([
        'Mirage',
        'Dust2',
        'Nuke',
        'Inferno',
        'Anubis'
    ])
    analyser.map_win_percentages()

if __name__ == '__main__':
    execute()