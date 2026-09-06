import pandas as pd

from store_data_analysis.config import CLIENTS_FILE


def load_clients():
    return pd.read_json(
        CLIENTS_FILE, 
        encoding="utf-8", 
        orient="records"
    )