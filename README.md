# store-data-analysis

School data-analysis project that generates store source files, creates a local SQLite database, analyzes the data with pandas, and exports CSV and Excel reports.

## Requirements

- Python 3.10 or newer
- pandas
- openpyxl
- pytest for development tests

SQLite is used through Python's built-in `sqlite3` module. Docker is not required.

## Install

```bash
python -m pip install -e ".[dev]"
```

If editable installation is not needed, install the listed requirements instead:

```bash
python -m pip install -r requirements.txt
```

For development tests, install pytest too:

```bash
python -m pip install pytest
```

## Run

```bash
python -m store_data_analysis.main
```

The program generates:

- `datos/ventas.csv`
- `datos/clientes.json`
- `datos/productos.sql`
- `datos/comentarios.txt`
- `datos/tienda.db`
- `analisis/ventas_analizadas.csv`
- `analisis/resultados.xlsx`
- `consultas/consultas.sql`

## Test

```bash
pytest
```
