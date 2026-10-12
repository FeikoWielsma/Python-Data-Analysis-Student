import duckdb
import pandas as pd

orders = pd.read_csv(
    "orders.csv",
    dtype={"order_id": str, "units": "Int64", "region": "category", "status": "category"},
    parse_dates=["ordered_at"],
    date_format="%Y-%m-%d",
)

orders.to_parquet("orders.parquet", index=False)
SQL = """
SELECT region, CAST(SUM(units) AS INTEGER) AS units, COUNT(*) AS orders
FROM {source}
WHERE ordered_at >= DATE '2026-06-01' AND ordered_at < DATE '2026-07-01'
  AND status = 'shipped' AND region IS NOT NULL AND units IS NOT NULL
GROUP BY region ORDER BY region
"""
con = duckdb.connect()
con.register("orders", orders)
print(con.execute(SQL.format(source="orders")).df())
print(con.execute(SQL.format(source="read_parquet('orders.parquet')")).df())

plan = con.execute("EXPLAIN " + SQL.format(source="read_parquet('orders.parquet')")).fetchone()[1]
print(plan)
con.close()
