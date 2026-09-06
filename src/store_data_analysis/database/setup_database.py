from store_data_analysis.config import PRODUCTS_SQL_FILE
from store_data_analysis.database.connection import get_connection

def setup_database():
    sql = PRODUCTS_SQL_FILE.read_text(
        encoding="utf-8"
    )

    connection = get_connection()

    try:
        connection.executescript(sql)
        connection.commit()
    finally:
        connection.close()