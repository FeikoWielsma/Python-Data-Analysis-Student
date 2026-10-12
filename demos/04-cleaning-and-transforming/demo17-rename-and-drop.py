import pandas as pd

shop = pd.read_csv("shop.csv")
orders = shop.rename(columns={"units": "quantity"}).drop(columns=["date"])
print(orders.columns.tolist())
print(shop.columns.tolist())
