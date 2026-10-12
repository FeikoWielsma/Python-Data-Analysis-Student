import pandas as pd

sales = pd.read_csv("sales.csv")
print(sales.head(3))
sales = sales.set_index("month")
print(sales.index.is_unique)
print(sales.loc["Feb", "eggs"], sales.iloc[1, 0])
