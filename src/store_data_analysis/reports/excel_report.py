import pandas as pd

from store_data_analysis.config import (
    ANALYZED_SALES_FILE,
    RESULTS_FILE,
)


SUMMARY_LABELS = {
    "total_revenue": "Total store revenue",
    "average_sale_amount": "Average sale amount",
    "client_count": "Client count",
    "average_client_age": "Average client age",
    "city_with_most_clients": "City with most clients",
    "product_with_highest_revenue": "Primate with highest revenue",
    "client_with_most_purchases": "Client with most purchases",
    "category_with_highest_revenue": "Category with highest revenue",
    "positive_comments": "Positive comments",
    "negative_comments": "Negative comments",
    "positive_comment_percentage": "Positive comment percentage",
    "negative_comment_percentage": "Negative comment percentage",
    "most_common_problem": "Most common problem",
}

PROBLEM_LABELS = {
    "delivery_delay": "Delivery delays",
    "customer_service": "Customer service",
    "damaged_product": "Damaged primates",
}


def generate_analyzed_sales_csv(sales):
    ANALYZED_SALES_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    sales.to_csv(
        ANALYZED_SALES_FILE,
        index=False,
        encoding="utf-8",
    )


def generate_excel_report(
    sales,
    clients,
    products,
    classified_comments,
    integrated,
    summary,
):
    comments_dataframe = pd.DataFrame(
        classified_comments
    )

    summary_dataframe = pd.DataFrame(
        [
            {
                "metric": SUMMARY_LABELS.get(key, key),
                "value": PROBLEM_LABELS.get(value, value),
            }
            for key, value in summary.items()
        ]
    )

    RESULTS_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with pd.ExcelWriter(
        RESULTS_FILE,
        engine="openpyxl",
    ) as writer:
        sales.to_excel(
            writer,
            sheet_name="Sales",
            index=False,
        )

        clients.to_excel(
            writer,
            sheet_name="Clients",
            index=False,
        )

        products.to_excel(
            writer,
            sheet_name="Primates",
            index=False,
        )

        comments_dataframe.to_excel(
            writer,
            sheet_name="Comments",
            index=False,
        )

        integrated.to_excel(
            writer,
            sheet_name="Integrated",
            index=False,
        )

        summary_dataframe.to_excel(
            writer,
            sheet_name="Summary",
            index=False,
        )
