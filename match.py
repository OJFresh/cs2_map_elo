from team import Team


class Match:

    def __init__(self, date, map_name, team_a, team_b, rounds_a, rounds_b):
        self.date = date
        self.team_a = team_a
        self.team_b = team_b
        self.map_name = map_name
        self.rounds_a = rounds_a
        self.rounds_b = rounds_b

    def modify_elo(self):
        diff = 16 - (self.winner.elo - self.loser.elo)/800
        self.winner.elo += diff
        self.loser.elo -= diff
        print(f'{self.winner} elo is now {self.winner.elo}')
        print(f'{self.loser} elo is now {self.loser.elo}')


    @property
    def winner(self):
        return self.team_a if self.rounds_a > self.rounds_b else self.team_b

    @property
    def loser(self):
        return self.team_a if self.rounds_a < self.rounds_b else self.team_b

vitality = Team()
mouz = Team()
navi = Team()
spirit = Team()
g2 = Team()

print(vitality.elo)
print(g2.elo)

major_final = Match(date='1234', team_a=vitality, team_b=g2, rounds_a=11, rounds_b=13, map_name='mirage')
major_final.modify_elo()
major_final2 = Match(date='1234', team_a=vitality, team_b=g2, rounds_a=11, rounds_b=13, map_name='mirage')
major_final2.modify_elo()
