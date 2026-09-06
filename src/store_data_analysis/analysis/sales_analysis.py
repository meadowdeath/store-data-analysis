def add_amount_column(sales):
    sales = sales.copy()
    sales["amount"] = sales["quantity"] * sales["unit_price"]
    return sales


def get_total_sales(sales):
    if sales.empty:
        return 0
    return sales["amount"].sum()


def get_highest_sale(sales):
    if sales.empty:
        return None
    index = sales["amount"].idxmax()
    return sales.loc[index]


def get_lowest_sale(sales):
    if sales.empty:
        return None
    index = sales["amount"].idxmin()
    return sales.loc[index]


def get_most_sold_product_id(sales):
    if sales.empty:
        return None
    return (
        sales.groupby("product_id")["quantity"]
        .sum()
        .idxmax()
    )


def get_least_sold_product_id(sales):
    if sales.empty:
        return None
    return (
        sales.groupby("product_id")["quantity"]
        .sum()
        .idxmin()
    )


def get_average_sale_amount(sales):
    if sales.empty:
        return 0
    return sales["amount"].mean()
