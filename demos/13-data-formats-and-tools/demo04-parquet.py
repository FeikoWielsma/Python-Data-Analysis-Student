import pandas as pd
import pyarrow.parquet as pq

orders = pd.read_csv(
    "orders.csv",
    dtype={"order_id": str, "units": "Int64", "region": "category", "status": "category"},
    parse_dates=["ordered_at"],
    date_format="%Y-%m-%d",
)

orders.to_parquet("orders.parquet", index=False)
restored = pd.read_parquet("orders.parquet")
print(restored.dtypes)
print(restored["order_id"].head(3).tolist())

print(pq.read_schema("orders.parquet"))
subset = pd.read_parquet("orders.parquet", columns=["region", "units"])
print(subset.columns.tolist())
