import pandas as pd

from store_data_analysis.config import SALES_FILE


def load_sales():
    return pd.read_csv(
        SALES_FILE, 
        encoding="utf-8", 
    )