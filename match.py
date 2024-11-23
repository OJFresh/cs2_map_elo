from team import Team


class Match:
    def __init__(self, date, map_name, team_a, team_b, score_a, score_b):
        self.date = date
        self.team_a = team_a
        self.team_b = team_b
        self.map_name = map_name
        self.score_a = score_a
        self.score_b = score_b


    def modify_elo(self):
        winner, loser = self.winner_loser
        print(f'old {winner} elo is now {winner.elo}')
        print(f'old {loser} elo is now {loser.elo}')
        diff = 16 - 32*(winner.elo - loser.elo)/800
        winner.elo += diff
        loser.elo -= diff
        print(f'New {winner} elo is now {winner.elo}')
        print(f'New {loser} elo is now {loser.elo}')

    @property
    def winner_loser(self):
        if self.score_a > self.score_b:
            return self.team_a, self.team_b
        else:
            return self.team_b, self.team_a

