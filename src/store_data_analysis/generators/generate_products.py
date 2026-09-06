from store_data_analysis.config import PRODUCTS_SQL_FILE


def generate_products():
    sql = """
DROP TABLE IF EXISTS products;

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
);

INSERT INTO products (
    product_id, 
    name, 
    category, 
    price
)
VALUES
    (1, 'Capuchino', 'Nuevo Mundo', 3500),
    (2, 'Mono arana', 'Nuevo Mundo', 4200),
    (3, 'Mono aullador', 'Nuevo Mundo', 3900),
    (4, 'Tití', 'Nuevo Mundo', 2800),
    (5, 'Macaco japonés', 'Viejo Mundo', 5100),
    (6, 'Babuino', 'Viejo Mundo', 4800),
    (7, 'Mandril', 'Viejo Mundo', 5600),
    (8, 'Gibón', 'Hominoideos', 6200),
    (9, 'Orangután', 'Hominoideos', 8500),
    (10, 'Lémur', 'Prosimios', 3200);
"""

    PRODUCTS_SQL_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    PRODUCTS_SQL_FILE.write_text(
        sql.strip() + "\n",
        encoding="utf-8",
    )
