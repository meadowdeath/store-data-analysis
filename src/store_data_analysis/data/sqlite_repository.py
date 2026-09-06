import pandas as pd

from store_data_analysis.database.connection import get_connection


def load_products():
    connection = get_connection()

    try:
        return pd.read_sql_query(
            "SELECT * FROM products",
            connection,
        )
    finally:
        connection.close()