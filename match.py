from team import Team
elo_dict = {
    'Spirit': 100,
    'Vitality': 100,
    'MOUZ': 100,
    'G2': 100,
    'Natus Vincere': 100,
    'Eternal Fire': 100,
    'Astralis': 100,
    'Liquid': 100,
    'FaZe': 100,
    'HEROIC': 100,
    'FURIA': 100,
    'The MongolZ': 100,
}


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
        winner_elo, loser_elo = elo_dict[winner], elo_dict[loser]
        diff = 16 - 32*(winner_elo - loser_elo)/800
        elo_dict[winner] += diff
        elo_dict[loser] -= diff
        print(f'{winner} beat {loser}\nDiff: {diff} on {self.date}')

    @property
    def winner_loser(self):
        if self.score_a > self.score_b:
            return self.team_a, self.team_b
        else:
            return self.team_b, self.team_a

