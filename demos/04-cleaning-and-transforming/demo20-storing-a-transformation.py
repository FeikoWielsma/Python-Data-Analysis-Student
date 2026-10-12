import pandas as pd

shop = pd.read_csv("shop.csv")
shop["city"] = shop["city"].str.strip().str.title()
shop["revenue"] = shop["units"] * shop["price"]
print(shop[["order_id", "city", "units", "price", "revenue"]].head(4))
print(shop["revenue"].sum().round(2))
