import pandas as pd

shop = pd.read_csv("shop.csv")
print(shop.sort_values("units", ascending=False).head(3))
print(shop.sort_values(["product", "units"]).head(4))
