import json

from store_data_analysis.config import CLIENTS_FILE


def generate_clients():
    clients = [
        {
            "client_id": 1,
            "name": "Ariana Garcia",
            "age": 23,
            "city": "Zapopan",
        },
        {
            "client_id": 2,
            "name": "Mike Gilpin",
            "age": 22,
            "city": "Tesistán",
        },
        {
            "client_id": 3,
            "name": "Alfredo Longoria",
            "age": 23,
            "city": "Guadalajara",
        },
        {
            "client_id": 4,
            "name": "Leonel Gonzalez",
            "age": 23,
            "city": "Tonalá",
        },
        {
            "client_id": 5,
            "name": "Uriel Arriaga",
            "age": 23,
            "city": "Guadalajara",
        },
        {
            "client_id": 6,
            "name": "Alexis de la Cruz",
            "age": 20,
            "city": "Zapopan",
        },
        {
            "client_id": 7,
            "name": "Santiago Ramírez",
            "age": 23,
            "city": "Zapopan",
        },
        {
            "client_id": 8,
            "name": "Yahir Hernández",
            "age": 23,
            "city": "Guadalajara",
        },
        {
            "client_id": 9,
            "name": "Ivan Amezcua",
            "age": 23,
            "city": "Zapopan",
        },
        {
            "client_id": 10,
            "name": "Victor Hugo Vazquez",
            "age": 23,
            "city": "Zapopan",
        },
    ]

    CLIENTS_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with CLIENTS_FILE.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            clients,
            file,
            ensure_ascii=False,
            indent=4,
        )
