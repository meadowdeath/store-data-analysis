def get_average_price(products):
    return products["price"].mean()


def get_most_expensive_product(products):
    index = products["price"].idxmax()

    return products.loc[index]


def get_cheapest_product(products):
    index = products["price"].idxmin()

    return products.loc[index]


def get_products_by_category(products):
    return (
        products.groupby("category")
        .size()
        .sort_values(ascending=False)
    )