import pandas as pd

from store_data_analysis.config import SALES_FILE


def generate_sales():
    sales = [
        {
            "sale_id": 1,
            "client_id": 1,
            "product_id": 1,
            "quantity": 2,
            "unit_price": 3500,
        },
        {
            "sale_id": 2,
            "client_id": 2,
            "product_id": 2,
            "quantity": 1,
            "unit_price": 4200,
        },
        {
            "sale_id": 3,
            "client_id": 3,
            "product_id": 3,
            "quantity": 2,
            "unit_price": 3900,
        },
        {
            "sale_id": 4,
            "client_id": 4,
            "product_id": 4,
            "quantity": 3,
            "unit_price": 2800,
        },
        {
            "sale_id": 5,
            "client_id": 5,
            "product_id": 5,
            "quantity": 1,
            "unit_price": 5100,
        },
        {
            "sale_id": 6,
            "client_id": 6,
            "product_id": 6,
            "quantity": 1,
            "unit_price": 4800,
        },
        {
            "sale_id": 7,
            "client_id": 7,
            "product_id": 7,
            "quantity": 2,
            "unit_price": 5600,
        },
        {
            "sale_id": 8,
            "client_id": 8,
            "product_id": 8,
            "quantity": 1,
            "unit_price": 6200,
        },
        {
            "sale_id": 9,
            "client_id": 9,
            "product_id": 9,
            "quantity": 1,
            "unit_price": 8500,
        },
        {
            "sale_id": 10,
            "client_id": 10,
            "product_id": 10,
            "quantity": 2,
            "unit_price": 3200,
        },
        {
            "sale_id": 11,
            "client_id": 1,
            "product_id": 4,
            "quantity": 2,
            "unit_price": 2800,
        },
        {
            "sale_id": 12,
            "client_id": 2,
            "product_id": 1,
            "quantity": 1,
            "unit_price": 3500,
        },
        {
            "sale_id": 13,
            "client_id": 3,
            "product_id": 2,
            "quantity": 2,
            "unit_price": 4200,
        },
        {
            "sale_id": 14,
            "client_id": 4,
            "product_id": 4,
            "quantity": 3,
            "unit_price": 2800,
        },
        {
            "sale_id": 15,
            "client_id": 5,
            "product_id": 8,
            "quantity": 1,
            "unit_price": 6200,
        },
        {
            "sale_id": 16,
            "client_id": 1,
            "product_id": 1,
            "quantity": 3,
            "unit_price": 3500,
        },
        {
            "sale_id": 17,
            "client_id": 7,
            "product_id": 3,
            "quantity": 1,
            "unit_price": 3900,
        },
        {
            "sale_id": 18,
            "client_id": 8,
            "product_id": 6,
            "quantity": 2,
            "unit_price": 4800,
        },
        {
            "sale_id": 19,
            "client_id": 9,
            "product_id": 4,
            "quantity": 2,
            "unit_price": 2800,
        },
        {
            "sale_id": 20,
            "client_id": 1,
            "product_id": 9,
            "quantity": 1,
            "unit_price": 8500,
        },
    ]

    SALES_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    dataframe = pd.DataFrame(sales)

    dataframe.to_csv(
        SALES_FILE,
        index=False,
    )
