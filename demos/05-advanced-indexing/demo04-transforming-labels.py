import pandas as pd

sales = pd.read_csv("sales.csv", index_col="month")
print(sales.index)
sales.index = sales.index.str.upper()
print(sales.index)
sales.index = sales.index.map(lambda month: month[0])
print(sales.index.tolist())
