from parse_match_data import matches

for match in matches():
    match.modify_elo()

print()