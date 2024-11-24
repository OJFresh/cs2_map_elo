import pandas as pd
class Match:
    def __init__(self, date, map_name, win_team, lose_team, win_score, lose_score):
        self.date = date
        self.map_name = map_name
        self.win_team = win_team
        self.lose_team = lose_team
        self.win_score = win_score
        self.lose_score = lose_score

    @property
    def elo_dataframe(self):
        return pd.read_csv('config/team_elo.csv', index_col='Team Names')

    def modify_elo(self):
        winner_elo = self.elo_dataframe.loc[self.win_team, self.map_name]
        loser_elo = self.elo_dataframe.loc[self.lose_team, self.map_name]
        if not winner_elo:
            winner_elo = 100
        if not loser_elo:
            loser_elo = 100
        diff = 1 - 1*(winner_elo - loser_elo)/10
        self.elo_dataframe.loc[self.win_team, self.map_name] = winner_elo + diff
        self.elo_dataframe.loc[self.lose_team, self.map_name] = loser_elo - diff/2
        print(f'{self.win_team} beat {self.lose_team} on map {self.map_name}')
        print(f'Score:{self.win_score}:{self.lose_score}')
        print(f'Diff: {diff} on {self.date}')
        self.elo_dataframe.to_csv('team_elo.csv')
