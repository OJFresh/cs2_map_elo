from elo_db import build_empty_elo_df, populate_elo_database, build_alt_elo_df


# from parse_match_data import create_matches_database


def execute():
    # create_matches_database()
    build_alt_elo_df()
    populate_elo_database()

if __name__ == '__main__':
    execute()