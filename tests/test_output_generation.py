import sqlite3
from pathlib import Path

import pandas as pd

from store_data_analysis.config import PROJECT_ROOT
import store_data_analysis.database.connection as connection_module
import store_data_analysis.database.queries as queries_module
import store_data_analysis.database.setup_database as setup_database_module
import store_data_analysis.generators.generate_clients as clients_generator
import store_data_analysis.generators.generate_comments as comments_generator
import store_data_analysis.generators.generate_products as products_generator
import store_data_analysis.generators.generate_sales as sales_generator
import store_data_analysis.reports.excel_report as excel_report
from store_data_analysis.analysis.sales_analysis import add_amount_column


def test_project_root_is_repository_root():
    assert PROJECT_ROOT == Path(__file__).resolve().parents[1]


def test_generators_create_source_files(tmp_path, monkeypatch):
    sales_file = tmp_path / "datos" / "ventas.csv"
    clients_file = tmp_path / "datos" / "clientes.json"
    products_file = tmp_path / "datos" / "productos.sql"
    comments_file = tmp_path / "datos" / "comentarios.txt"

    monkeypatch.setattr(sales_generator, "SALES_FILE", sales_file)
    monkeypatch.setattr(clients_generator, "CLIENTS_FILE", clients_file)
    monkeypatch.setattr(products_generator, "PRODUCTS_SQL_FILE", products_file)
    monkeypatch.setattr(comments_generator, "COMMENTS_FILE", comments_file)

    sales_generator.generate_sales()
    clients_generator.generate_clients()
    products_generator.generate_products()
    comments_generator.generate_comments()

    assert sales_file.is_file()
    assert clients_file.is_file()
    assert products_file.is_file()
    assert comments_file.is_file()


def test_setup_database_creates_database_file(tmp_path, monkeypatch):
    products_file = tmp_path / "datos" / "productos.sql"
    database_file = tmp_path / "datos" / "tienda.db"
    products_file.parent.mkdir(parents=True)
    products_file.write_text(
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT);",
        encoding="utf-8",
    )

    monkeypatch.setattr(setup_database_module, "PRODUCTS_SQL_FILE", products_file)
    monkeypatch.setattr(connection_module, "DATABASE_FILE", database_file)

    setup_database_module.setup_database()

    assert database_file.is_file()

    with sqlite3.connect(database_file) as connection:
        tables = connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table'"
        ).fetchall()

    assert ("products",) in tables


def test_generate_queries_file_creates_sql_export(tmp_path, monkeypatch):
    queries_file = tmp_path / "consultas" / "consultas.sql"
    monkeypatch.setattr(queries_module, "QUERIES_FILE", queries_file)

    queries_module.generate_queries_file()

    content = queries_file.read_text(encoding="utf-8")
    assert queries_file.is_file()
    assert "Show all primates" in content
    assert "WHERE category = 'Nuevo Mundo'" in content
    assert "AVG(price)" in content
    assert "MAX(price)" in content
    assert "MIN(price)" in content


def test_reports_create_analyzed_sales_csv_and_excel(tmp_path, monkeypatch):
    analyzed_sales_file = tmp_path / "analisis" / "ventas_analizadas.csv"
    results_file = tmp_path / "analisis" / "resultados.xlsx"
    monkeypatch.setattr(excel_report, "ANALYZED_SALES_FILE", analyzed_sales_file)
    monkeypatch.setattr(excel_report, "RESULTS_FILE", results_file)

    sales = add_amount_column(
        pd.DataFrame(
            [{"sale_id": 1, "client_id": 1, "product_id": 1, "quantity": 2, "unit_price": 100}]
        )
    )
    clients = pd.DataFrame([{"client_id": 1, "name": "Client One", "age": 20, "city": "Zapopan"}])
    products = pd.DataFrame([{"product_id": 1, "name": "Capuchino", "category": "Nuevo Mundo", "price": 100}])
    integrated = pd.DataFrame([{"sale_id": 1, "client_name": "Client One", "product_name": "Capuchino", "amount": 200}])

    excel_report.generate_analyzed_sales_csv(sales)
    excel_report.generate_excel_report(
        sales,
        clients,
        products,
        [{"comment": "Excellent", "classification": "Positive"}],
        integrated,
        {"most_common_problem": "delivery_delay"},
    )

    assert analyzed_sales_file.is_file()
    assert pd.read_csv(analyzed_sales_file)["amount"].tolist() == [200]
    assert results_file.is_file()
    assert {
        "Sales",
        "Clients",
        "Primates",
        "Comments",
        "Integrated",
        "Summary",
    }.issubset(pd.ExcelFile(results_file).sheet_names)
