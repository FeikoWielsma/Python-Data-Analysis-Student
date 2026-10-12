import pandas as pd

sales = pd.read_csv("sales.csv", index_col="month")
sales.index.name = "MONTHS"
sales.columns.name = "PRODUCTS"
print(sales.head(3))
print(sales.reset_index().columns.tolist())
