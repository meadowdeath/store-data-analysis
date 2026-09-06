import pandas as pd

from store_data_analysis.analysis.sales_analysis import (
    add_amount_column,
    get_average_sale_amount,
    get_highest_sale,
    get_least_sold_product_id,
    get_lowest_sale,
    get_most_sold_product_id,
    get_total_sales,
)


def create_sales_dataframe():
    return pd.DataFrame(
        [
            {
                "sale_id": 1,
                "client_id": 1,
                "product_id": 1,
                "quantity": 2,
                "unit_price": 100,
            },
            {
                "sale_id": 2,
                "client_id": 2,
                "product_id": 2,
                "quantity": 1,
                "unit_price": 500,
            },
            {
                "sale_id": 3,
                "client_id": 3,
                "product_id": 1,
                "quantity": 3,
                "unit_price": 100,
            },
        ]
    )


def test_add_amount_column():
    sales = create_sales_dataframe()

    result = add_amount_column(sales)

    assert result["amount"].tolist() == [
        200,
        500,
        300,
    ]


def test_get_total_sales():
    sales = add_amount_column(
        create_sales_dataframe()
    )

    result = get_total_sales(sales)

    assert result == 1000


def test_get_highest_sale():
    sales = add_amount_column(
        create_sales_dataframe()
    )

    result = get_highest_sale(sales)

    assert result["sale_id"] == 2
    assert result["amount"] == 500


def test_get_lowest_sale():
    sales = add_amount_column(
        create_sales_dataframe()
    )

    result = get_lowest_sale(sales)

    assert result["sale_id"] == 1
    assert result["amount"] == 200


def test_get_most_sold_product_id():
    sales = add_amount_column(
        create_sales_dataframe()
    )

    result = get_most_sold_product_id(sales)

    assert result == 1


def test_get_least_sold_product_id():
    sales = add_amount_column(
        create_sales_dataframe()
    )

    result = get_least_sold_product_id(sales)

    assert result == 2


def test_get_average_sale_amount():
    sales = add_amount_column(
        create_sales_dataframe()
    )

    result = get_average_sale_amount(sales)

    assert result == 1000 / 3