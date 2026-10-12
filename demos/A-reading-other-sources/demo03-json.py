import json

import pandas as pd

flat = pd.read_json("orders-flat.json")
print(flat)

with open("orders.json") as file:
    records = json.load(file)
orders = pd.json_normalize(records)
print(orders.columns.tolist())
print(orders[["order_id", "customer.city"]])
items = pd.json_normalize(records, record_path="items", meta=["order_id"])
print(items)
