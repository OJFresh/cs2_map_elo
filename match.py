

class Match:

    def __init__(self, date, team_a, team_b, rounds_a, rounds_b):
        self.date = date
        self.team_a = team_a
        self.team_b = team_b
        self.rounds_a = rounds_a
        self.rounds_b = rounds_b

    @property
    def winner(self):
        return self.team_a if self.rounds_a > self.rounds_b else self.team_b
