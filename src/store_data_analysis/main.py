from store_data_analysis.analysis.clients_analysis import (
    get_average_age,
    get_city_with_most_clients,
    get_client_count,
    get_oldest_client,
    get_youngest_client,
)
from store_data_analysis.analysis.comments_analysis import (
    classify_comments,
    get_comment_counts,
    get_comment_percentages,
    get_most_common_problem,
)
from store_data_analysis.analysis.integration_analysis import (
    get_client_purchase_counts,
    get_category_with_highest_revenue,
    get_client_with_most_purchases,
    get_primate_sales_performance,
    get_product_with_highest_revenue,
    get_total_store_revenue,
    integrate_data,
)
from store_data_analysis.analysis.products_analysis import (
    get_average_price,
    get_cheapest_product,
    get_most_expensive_product,
)
from store_data_analysis.analysis.sales_analysis import (
    add_amount_column,
    get_average_sale_amount,
    get_highest_sale,
    get_least_sold_product_id,
    get_lowest_sale,
    get_most_sold_product_id,
    get_total_sales,
)

from store_data_analysis.data.csv_repository import load_sales
from store_data_analysis.data.json_repository import load_clients
from store_data_analysis.data.sqlite_repository import load_products
from store_data_analysis.data.txt_repository import load_comments

from store_data_analysis.database.setup_database import setup_database
from store_data_analysis.database.queries import generate_queries_file

from store_data_analysis.generators.generate_clients import (
    generate_clients,
)
from store_data_analysis.generators.generate_comments import (
    generate_comments,
)
from store_data_analysis.generators.generate_products import (
    generate_products,
)
from store_data_analysis.generators.generate_sales import (
    generate_sales,
)

from store_data_analysis.reports.console_report import (
    print_clients_summary,
    print_classified_comment_details,
    print_client_purchase_counts,
    print_comments_summary,
    print_integrated_sales_details,
    print_integration_summary,
    print_primate_sales_performance,
    print_products_summary,
    print_sales_summary,
)
from store_data_analysis.reports.excel_report import (
    generate_analyzed_sales_csv,
    generate_excel_report,
)


def main():
    print("=== STORE DATA ANALYSIS ===")

    print("\nGenerating source data...")

    generate_clients()
    generate_products()
    generate_sales()
    generate_comments()

    print("Source data generated.")

    print("\nSetting up database...")

    setup_database()
    generate_queries_file()

    print("Database ready.")

    print("\nLoading data...")

    sales = load_sales()
    clients = load_clients()
    products = load_products()
    comments = load_comments()

    print("Data loaded.")

    print("\nProcessing sales...")

    sales = add_amount_column(sales)

    total_sales = get_total_sales(sales)
    highest_sale = get_highest_sale(sales)
    lowest_sale = get_lowest_sale(sales)
    most_sold_product_id = get_most_sold_product_id(sales)
    least_sold_product_id = get_least_sold_product_id(sales)
    average_sale_amount = get_average_sale_amount(sales)

    product_names = products.set_index("product_id")["name"]
    most_sold_primate = product_names.get(
        most_sold_product_id,
        "Unknown primate",
    )
    least_sold_primate = product_names.get(
        least_sold_product_id,
        "Unknown primate",
    )

    print("\nProcessing clients...")

    client_count = get_client_count(clients)
    average_age = get_average_age(clients)
    city_with_most_clients = get_city_with_most_clients(clients)
    oldest_client = get_oldest_client(clients)
    youngest_client = get_youngest_client(clients)

    print("\nProcessing products...")

    average_price = get_average_price(products)
    most_expensive_product = get_most_expensive_product(products)
    cheapest_product = get_cheapest_product(products)

    print("\nProcessing comments...")

    classified_comments = classify_comments(comments)

    comment_counts = get_comment_counts(
        classified_comments
    )

    comment_percentages = get_comment_percentages(
        classified_comments
    )

    most_common_problem = get_most_common_problem(
        comments
    )

    print("\nIntegrating data...")

    integrated = integrate_data(
        sales,
        clients,
        products,
    )

    product_with_highest_revenue = (
        get_product_with_highest_revenue(
            integrated
        )
    )

    client_with_most_purchases = (
        get_client_with_most_purchases(
            integrated
        )
    )

    category_with_highest_revenue = (
        get_category_with_highest_revenue(
            integrated
        )
    )

    total_store_revenue = get_total_store_revenue(
        integrated
    )

    primate_sales_performance = get_primate_sales_performance(
        integrated
    )

    client_purchase_counts = get_client_purchase_counts(
        integrated
    )

    print_sales_summary(
        total_sales,
        highest_sale,
        lowest_sale,
        most_sold_primate,
        least_sold_primate,
        average_sale_amount,
    )

    print_clients_summary(
        client_count,
        average_age,
        city_with_most_clients,
        oldest_client,
        youngest_client,
    )

    print_products_summary(
        average_price,
        most_expensive_product,
        cheapest_product,
    )

    print_comments_summary(
        comment_counts,
        comment_percentages,
        most_common_problem,
    )

    print_integration_summary(
        product_with_highest_revenue,
        client_with_most_purchases,
        category_with_highest_revenue,
        total_store_revenue,
    )

    print_primate_sales_performance(
        primate_sales_performance,
    )

    print_client_purchase_counts(
        client_purchase_counts,
    )

    print_classified_comment_details(
        classified_comments,
    )

    print_integrated_sales_details(integrated)

    summary = {
        "total_revenue": total_store_revenue,
        "average_sale_amount": average_sale_amount,
        "client_count": client_count,
        "average_client_age": average_age,
        "city_with_most_clients": city_with_most_clients,
        "product_with_highest_revenue": product_with_highest_revenue,
        "client_with_most_purchases": client_with_most_purchases,
        "category_with_highest_revenue": category_with_highest_revenue,
        "positive_comments": comment_counts["positive"],
        "negative_comments": comment_counts["negative"],
        "positive_comment_percentage": (
            comment_percentages["positive"]
        ),
        "negative_comment_percentage": (
            comment_percentages["negative"]
        ),
        "most_common_problem": most_common_problem,
    }

    print("\nGenerating output files...")

    generate_analyzed_sales_csv(sales)

    generate_excel_report(
        sales,
        clients,
        products,
        classified_comments,
        integrated,
        summary,
    )

    print("Output files generated.")

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
