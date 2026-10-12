from datetime import date

import pandas as pd
import polars as pl

pd.read_csv(
    "orders.csv", dtype={"order_id": str, "units": "Int64"}, parse_dates=["ordered_at"]
).to_parquet("orders.parquet", index=False)

query = (
    pl.scan_parquet("orders.parquet")
    .filter(
        (pl.col("ordered_at") >= pl.lit(date(2026, 6, 1)))
        & (pl.col("ordered_at") < pl.lit(date(2026, 7, 1)))
        & (pl.col("status") == "shipped")
        & pl.col("region").is_not_null()
        & pl.col("units").is_not_null()
    )
    .group_by("region")
    .agg(pl.col("units").sum(), pl.len().alias("orders"))
    .sort("region")
)
print(query.explain())
print(query.collect())
