import pandas as pd

from match import Match


def execute():
    elo = pd.read_csv('config/elo.csv')
    for i, x in elo.iterrows():
        kwargs = x.to_dict()
        print(kwargs)


execute()
