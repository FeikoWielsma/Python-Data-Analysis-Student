import pandas as pd

shop = pd.read_csv("shop.csv")
print(shop["product"].str.startswith("C").tolist())
print(shop.loc[shop["product"].str.contains("a"), "product"].unique().tolist())
print(shop["order_id"].str.fullmatch(r"A\d{3}").all())
print(shop["order_id"].str[1:].str.isdigit().all())
print(shop["order_id"].str.lower().head(2).tolist())
