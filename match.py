f
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
    'Virtus.pro': 100,
    'StatesComplexity': 100,
    'SAW': 100,
}


class Match:
    def __init__(self, date, map_name, win_team, lose_team, win_score, lose_score):
        self.date = date
        self.map_name = map_name
        self.win_team = win_team
        self.lose_team = lose_team
        self.win_score = win_score
        self.lose_score = lose_score

    @property
    def round_diff(self):
        return self.win_score/(self.win_score+self.lose_score)

    def modify_elo(self):
        winner_elo, loser_elo = elo_dict[self.win_team], elo_dict[self.lose_team]
        if not winner_elo:
            winner_elo = 100
        if not loser_elo:
            loser_elo = 100
        diff = 1 - 1*(winner_elo - loser_elo)/10
        elo_dict[self.win_team] += diff
        elo_dict[self.lose_team] -= diff/2
        print(f'{self.win_team} beat {self.lose_team} on map {self.map_name}')
        print(f'Score:{self.win_score}:{self.lose_score}')
        print(f'Diff: {diff} on {self.date}')
