import pandas as pd

from match import Match


def execute():
    matches = pd.read_csv('config/match_data.csv')
    for i, x in matches.iterrows():
        kwargs = x.to_dict()
        Match(**kwargs).modify_elo()


execute()
