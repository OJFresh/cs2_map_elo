from datetime import date
from match import Match


def name_score_parser(team):
    name, score = team.split(' (')
    filtered_name = ''
    for num, char in enumerate(name[1:]):
        if char.isupper():
            filtered_name = name[num+1:]
            break
    filtered_score = int(score[0:-1])
    return filtered_name, filtered_score


def matches():
    with open('match_info.txt', 'r') as f:
        file = f.readlines()
        matches = []
        for i in range(0, len(file), 4):
            filtered_date = file[i].replace('\n', '')
            day, month, year = filtered_date.split('/')
            teams = file[i+1].replace('\n', '')
            team_a, team_b = teams.split('\t')
            name_a, score_a = name_score_parser(team_a)
            name_b, score_b = name_score_parser(team_b)
            match = Match(
                date=date(2000+int(year), int(month), int(day)),
                map_name=file[i+2].replace('\n', ''),
                team_a=name_a,
                team_b=name_b,
                score_a=score_a,
                score_b=score_b,
            )
            matches.append(match)
    return sorted(matches, key=lambda game: game.date)
