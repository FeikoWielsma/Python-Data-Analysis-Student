import pandas as pd

march = pd.read_excel("shop.xlsx", sheet_name="March", skiprows=3)
print(march.head(3))

sheets = pd.read_excel("shop.xlsx", sheet_name=None)
print(list(sheets))
stores = pd.read_excel("shop.xlsx", sheet_name="Stores")
print(stores)
