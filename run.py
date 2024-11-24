
from parse_match_data import create_matches_database, build_empty_elo_df, populate_elo_database


def execute():
    create_matches_database()
    build_empty_elo_df()
    populate_elo_database()


execute()
