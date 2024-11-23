from match import elo_dict
from parse_match_data import matches
from pprint import pprint as pp


for match in matches():
    match.modify_elo()

for team in sorted(elo_dict, key= lambda key: elo_dict[key]):
    print(f'{team}: {elo_dict[team]}')