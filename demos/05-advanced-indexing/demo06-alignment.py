import pandas as pd

sales = pd.Series([47, 110], index=["Jan", "Feb"], name="eggs")
adjustment = pd.Series([2, 1], index=["Feb", "Jan"])
print(sales + adjustment)

partial = pd.Series([2], index=["Feb"])
print(sales + partial)
print(sales.add(partial, fill_value=0))
