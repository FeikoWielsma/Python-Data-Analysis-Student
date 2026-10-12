import pandas as pd

shop = pd.read_csv("shop.csv")
print(shop.nlargest(3, "units"))
print(shop["units"].idxmax(), shop["units"].max())
print(shop.loc[shop["units"].idxmax(), "order_id"])
