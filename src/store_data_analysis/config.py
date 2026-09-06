from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "datos"
ANALYSIS_DIR = PROJECT_ROOT / "analisis"
QUERIES_DIR = PROJECT_ROOT / "consultas"

SALES_FILE = DATA_DIR / "ventas.csv"
CLIENTS_FILE = DATA_DIR / "clientes.json"
PRODUCTS_SQL_FILE = DATA_DIR / "productos.sql"
COMMENTS_FILE = DATA_DIR / "comentarios.txt"

DATABASE_FILE = DATA_DIR / "tienda.db"

ANALYZED_SALES_FILE = ANALYSIS_DIR / "ventas_analizadas.csv"
RESULTS_FILE = ANALYSIS_DIR / "resultados.xlsx"

QUERIES_FILE = QUERIES_DIR / "consultas.sql"
