import pandas as pd

shop = pd.read_csv("shop.csv")
print(shop["product"].unique().tolist())
print(shop["product"].nunique())
print(shop["units"].median(), shop["units"].mean())
