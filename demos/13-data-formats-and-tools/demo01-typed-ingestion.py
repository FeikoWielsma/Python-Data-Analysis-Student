import pandas as pd

orders = pd.read_csv(
    "orders.csv",
    dtype={"order_id": str, "units": "Int64", "region": "category", "status": "category"},
    parse_dates=["ordered_at"],
    date_format="%Y-%m-%d",
)
print(orders.dtypes)
print(orders.head(4))

inferred = pd.read_csv("orders.csv")
print(inferred["order_id"].head(3).tolist(), inferred["units"].dtype)
