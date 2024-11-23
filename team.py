class Team:
    elo = 1000

    def __init__(self, team_name):
        self.team_name = team_name

    def __str__(self):
        return self.team_name

    def __repr__(self):
        return f'{self.__class__.__name__}(team_name={self.team_name})'
