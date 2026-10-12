import pandas as pd

sales = pd.read_csv("sales.csv", index_col="month")
print(sales.reindex(["Jun", "Jan", "Jul"]))
print(sales["eggs"].reindex(["Jan", "Jul"], fill_value=0))
