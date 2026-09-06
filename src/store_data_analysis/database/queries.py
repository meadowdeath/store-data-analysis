from store_data_analysis.config import QUERIES_FILE


GET_ALL_PRODUCTS = """
SELECT *
FROM products;
"""

GET_PRODUCTS_BY_CATEGORY = """
SELECT *
FROM products
WHERE category = ?;
"""

GET_PRODUCTS_ABOVE_500 = """
SELECT *
FROM products
WHERE price > 500;
"""

GET_PRODUCTS_ORDERED_BY_PRICE = """
SELECT *
FROM products
ORDER BY price DESC;
"""

GET_AVERAGE_PRICE = """
SELECT AVG(price)
FROM products;
"""

GET_MAX_PRICE = """
SELECT MAX(price)
FROM products;
"""

GET_MIN_PRICE = """
SELECT MIN(price)
FROM products;
"""


QUERIES_EXPORT = """-- Show all primates
SELECT *
FROM products;

-- Show primates from a specific category
SELECT *
FROM products
WHERE category = 'Nuevo Mundo';

-- Show primates with price greater than 500
SELECT *
FROM products
WHERE price > 500;

-- Order primates by price
SELECT *
FROM products
ORDER BY price DESC;

-- Average price
SELECT AVG(price) AS average_price
FROM products;

-- Maximum price
SELECT MAX(price) AS maximum_price
FROM products;

-- Minimum price
SELECT MIN(price) AS minimum_price
FROM products;
"""


def generate_queries_file():
    QUERIES_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    QUERIES_FILE.write_text(
        QUERIES_EXPORT,
        encoding="utf-8",
    )
