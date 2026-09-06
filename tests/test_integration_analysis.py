import pandas as pd

from store_data_analysis.analysis.integration_analysis import (
    get_category_with_highest_revenue,
    get_client_with_most_purchases,
    get_product_with_highest_revenue,
    get_total_store_revenue,
    integrate_data,
)


def create_test_data():
    sales = pd.DataFrame(
        [
            {
                "sale_id": 1,
                "client_id": 1,
                "product_id": 1,
                "quantity": 2,
                "unit_price": 100,
                "amount": 200,
            },
            {
                "sale_id": 2,
                "client_id": 1,
                "product_id": 2,
                "quantity": 1,
                "unit_price": 500,
                "amount": 500,
            },
            {
                "sale_id": 3,
                "client_id": 2,
                "product_id": 1,
                "quantity": 1,
                "unit_price": 100,
                "amount": 100,
            },
        ]
    )

    clients = pd.DataFrame(
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
        ]
    )

    products = pd.DataFrame(
        [
            {
                "product_id": 1,
                "name": "Capuchino",
                "category": "Nuevo Mundo",
                "price": 100,
            },
            {
                "product_id": 2,
                "name": "Gibon",
                "category": "Hominoideos",
                "price": 500,
            },
        ]
    )

    return sales, clients, products


def test_integrate_data():
    sales, clients, products = create_test_data()

    result = integrate_data(
        sales,
        clients,
        products,
    )

    assert len(result) == 3

    assert "client_name" in result.columns
    assert "product_name" in result.columns

    assert (
        result.loc[0, "client_name"]
        == "Client One"
    )

    assert (
        result.loc[0, "product_name"]
        == "Capuchino"
    )


def test_get_product_with_highest_revenue():
    sales, clients, products = create_test_data()

    integrated = integrate_data(
        sales,
        clients,
        products,
    )

    result = get_product_with_highest_revenue(
        integrated
    )

    assert result == "Gibon"


def test_get_client_with_most_purchases():
    sales, clients, products = create_test_data()

    integrated = integrate_data(
        sales,
        clients,
        products,
    )

    result = get_client_with_most_purchases(
        integrated
    )

    assert result == "Client One"


def test_get_category_with_highest_revenue():
    sales, clients, products = create_test_data()

    integrated = integrate_data(
        sales,
        clients,
        products,
    )

    result = get_category_with_highest_revenue(
        integrated
    )

    assert result == "Hominoideos"


def test_get_total_store_revenue():
    sales, clients, products = create_test_data()

    integrated = integrate_data(
        sales,
        clients,
        products,
    )

    result = get_total_store_revenue(
        integrated
    )

    assert result == 800