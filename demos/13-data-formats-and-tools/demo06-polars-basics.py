import polars as pl

orders = pl.read_csv("orders.csv", schema_overrides={"order_id": pl.String}, try_parse_dates=True)
print(orders.head(3))
result = (
    orders.filter(pl.col("status") == "shipped")
    .filter(pl.col("region").is_in(["North", "South"]))
    .with_columns(pl.col("units").cast(pl.Float64).alias("units_f"))
    .select("order_id", "region", "units_f")
)
print(result.head(4))
