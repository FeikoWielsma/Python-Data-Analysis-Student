# Data Formats and Tools demos (optional module)

The demos use the invented 12-row ledger in `datasets/demos/13-data-formats-and-tools/orders.csv`
(see the README there). Run them from that folder, for example:

```sh
cd datasets/demos/13-data-formats-and-tools
uv run --project ../../.. --frozen python ../../../demos/13-data-formats-and-tools/demo05-duckdb.py
```

Demos 04, 05 and 07 write `orders.parquet` into the working folder. Demo 08 needs the optional
Numba package: `uv sync --frozen --all-groups`.

References: [pandas and PyArrow](https://pandas.pydata.org/docs/user_guide/pyarrow.html),
[Parquet in pandas](https://pandas.pydata.org/docs/reference/api/pandas.read_parquet.html),
[DuckDB Python API](https://duckdb.org/docs/api/python/overview),
[Polars lazy API](https://docs.pola.rs/user-guide/lazy/).
