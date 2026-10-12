import pandas as pd

orders = pd.read_csv(
    "orders.csv",
    dtype={"order_id": str, "units": "Int64", "region": "category", "status": "category"},
    parse_dates=["ordered_at"],
    date_format="%Y-%m-%d",
)
june_shipped = (
    orders["ordered_at"].ge("2026-06-01")
    & orders["ordered_at"].lt("2026-07-01")
    & orders["status"].eq("shipped")
)
selected = orders.loc[june_shipped & orders["region"].notna() & orders["units"].notna()]
print(june_shipped.sum(), len(selected))

answer = (
    selected.groupby("region", observed=True)
    .agg(units=("units", "sum"), orders=("units", "size"))
    .reset_index()
)
print(answer)
