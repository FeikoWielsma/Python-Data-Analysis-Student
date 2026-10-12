import pandas as pd

shop = pd.read_csv("shop.csv")
print(shop["product"].value_counts())
print(shop["product"].value_counts(normalize=True).round(2))
print(shop["city"].value_counts())
