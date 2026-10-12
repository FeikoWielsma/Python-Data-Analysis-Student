import pandas as pd

shop = pd.read_csv("shop.csv")
kind = {"Coffee": "drink", "Tea": "drink"}
shop["kind"] = shop["product"].map(kind)
print(shop[["product", "kind"]].head(4))
