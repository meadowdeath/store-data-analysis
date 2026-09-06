def print_sales_summary(
        total_sales,
        highest_sale,
        lowest_sale,
        most_sold_primate,
        least_sold_primate,
        average_sale_amount,
):
    print("\n=== SALES ANALYSIS ===")
    print(f"Total revenue: ${total_sales:,.2f}")
    print(f"Highest sale amount: ${highest_sale['amount']:,.2f}")
    print(f"Lowest sale amount: ${lowest_sale['amount']:,.2f}")
    print(f"Best-selling primate: {most_sold_primate}")
    print(f"Least-selling primate: {least_sold_primate}")
    print(f"Average sale amount: ${average_sale_amount:,.2f}")

def print_clients_summary(
    client_count,
    average_age,
    city_with_most_clients,
    oldest_client,
    youngest_client,
):
    print("\n=== CLIENTS ANALYSIS ===")
    print(f"Total clients: {client_count}")
    print(f"Average age: {average_age:.2f}")
    print(f"City with most clients: {city_with_most_clients}")
    print(
        f"Oldest client: "
        f"{oldest_client['name']} "
        f"({oldest_client['age']} years)"
    )
    print(
        f"Youngest client: "
        f"{youngest_client['name']} "
        f"({youngest_client['age']} years)"
    )


def print_products_summary(
    average_price,
    most_expensive_product,
    cheapest_product,
):
    print("\n=== PRIMATES ANALYSIS ===")
    print(f"Average price: ${average_price:,.2f}")
    print(
        f"Most expensive primate: "
        f"{most_expensive_product['name']} "
        f"(${most_expensive_product['price']:,.2f})"
    )
    print(
        f"Cheapest primate: "
        f"{cheapest_product['name']} "
        f"(${cheapest_product['price']:,.2f})"
    )


def print_comments_summary(
    counts,
    percentages,
    most_common_problem,
):
    print("\n=== COMMENTS ANALYSIS ===")
    print(f"Positive comments: {counts['positive']}")
    print(f"Negative comments: {counts['negative']}")
    print(f"Neutral comments: {counts['neutral']}")

    print(
        f"Positive percentage: "
        f"{percentages['positive']:.2f}%"
    )
    print(
        f"Negative percentage: "
        f"{percentages['negative']:.2f}%"
    )
    print(
        f"Neutral percentage: "
        f"{percentages['neutral']:.2f}%"
    )

    problem_labels = {
        "delivery_delay": "Delivery delays",
        "customer_service": "Customer service",
        "damaged_product": "Damaged primates",
    }
    print(f"Most common problem: {problem_labels[most_common_problem]}")


def print_integration_summary(
    product_with_highest_revenue,
    client_with_most_purchases,
    category_with_highest_revenue,
    total_store_revenue,
):
    print("\n=== INTEGRATED ANALYSIS ===")

    print(
        f"Primate with highest revenue: "
        f"{product_with_highest_revenue}"
    )

    print(
        f"Client with most purchases: "
        f"{client_with_most_purchases}"
    )

    print(
        f"Category with highest revenue: "
        f"{category_with_highest_revenue}"
    )

    print(
        f"Total store revenue: "
        f"${total_store_revenue:,.2f}"
    )


def print_primate_sales_performance(performance):
    print("\n=== PRIMATE SALES PERFORMANCE ===")
    print(performance.to_string(index=False))


def print_client_purchase_counts(purchases):
    print("\n=== CLIENT PURCHASE COUNTS ===")
    print(purchases.to_string(index=False))


def print_classified_comment_details(classified_comments):
    print("\n=== CLASSIFIED COMMENTS ===")

    for item in classified_comments:
        print(f"[{item['classification']}] {item['comment']}")


def print_integrated_sales_details(integrated):
    columns = [
        "sale_id",
        "client_name",
        "product_name",
        "category",
        "quantity",
        "amount",
    ]

    print("\n=== INTEGRATED SALES DETAILS ===")
    print(integrated[columns].to_string(index=False))
