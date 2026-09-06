import pandas as pd

from store_data_analysis.analysis.clients_analysis import (
    get_average_age,
    get_city_with_most_clients,
    get_client_count,
    get_oldest_client,
    get_youngest_client,
)


def create_clients_dataframe():
    return pd.DataFrame(
        [
            {
                "client_id": 1,
                "name": "Client One",
                "age": 20,
                "city": "Guadalajara",
            },
            {
                "client_id": 2,
                "name": "Client Two",
                "age": 30,
                "city": "Zapopan",
            },
            {
                "client_id": 3,
                "name": "Client Three",
                "age": 40,
                "city": "Guadalajara",
            },
        ]
    )


def test_get_client_count():
    clients = create_clients_dataframe()

    assert get_client_count(clients) == 3


def test_get_average_age():
    clients = create_clients_dataframe()

    assert get_average_age(clients) == 30


def test_get_city_with_most_clients():
    clients = create_clients_dataframe()

    assert (
        get_city_with_most_clients(clients)
        == "Guadalajara"
    )


def test_get_oldest_client():
    clients = create_clients_dataframe()

    result = get_oldest_client(clients)

    assert result["name"] == "Client Three"
    assert result["age"] == 40


def test_get_youngest_client():
    clients = create_clients_dataframe()

    result = get_youngest_client(clients)

    assert result["name"] == "Client One"
    assert result["age"] == 20