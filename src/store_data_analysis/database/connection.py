import sqlite3

from store_data_analysis.config import DATABASE_FILE


def get_connection():
    DATABASE_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    return sqlite3.connect(DATABASE_FILE)
