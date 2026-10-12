import pandas as pd

shop = pd.read_csv("shop.csv")
print(shop["city"].unique().tolist())
shop["city"] = shop["city"].str.strip().str.title()
print(shop["city"].value_counts())
