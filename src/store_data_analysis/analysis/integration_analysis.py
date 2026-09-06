def integrate_data(
    sales,
    clients,
    products,
):
    clients = clients.rename(
        columns={
            "name": "client_name",
        }
    )

    products = products.rename(
        columns={
            "name": "product_name",
        }
    )

    integrated = sales.merge(
        clients,
        on="client_id",
        how="left",
    )

    integrated = integrated.merge(
        products,
        on="product_id",
        how="left",
    )

    return integrated


def get_product_with_highest_revenue(
    integrated,
):
    revenues = (
        integrated
        .groupby("product_name")["amount"]
        .sum()
    )

    return revenues.idxmax()


def get_client_with_most_purchases(
    integrated,
):
    purchases = (
        integrated
        .groupby("client_name")["sale_id"]
        .count()
    )

    return purchases.idxmax()


def get_category_with_highest_revenue(
    integrated,
):
    revenues = (
        integrated
        .groupby("category")["amount"]
        .sum()
    )

    return revenues.idxmax()


def get_total_store_revenue(
    integrated,
):
    return integrated["amount"].sum()


def get_primate_sales_performance(integrated):
    return (
        integrated.groupby(
            ["product_name", "category"],
            as_index=False,
        )
        .agg(
            total_quantity=("quantity", "sum"),
            total_revenue=("amount", "sum"),
        )
        .sort_values(
            ["total_quantity", "total_revenue"],
            ascending=False,
        )
    )


def get_client_purchase_counts(integrated):
    return (
        integrated.groupby(
            "client_name",
            as_index=False,
        )
        .agg(purchase_count=("sale_id", "count"))
        .sort_values(
            "purchase_count",
            ascending=False,
        )
    )