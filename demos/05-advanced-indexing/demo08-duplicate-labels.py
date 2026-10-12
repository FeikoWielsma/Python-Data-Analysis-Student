import pandas as pd

sales = pd.DataFrame(
    {"state": ["CA", "NY", "NY"], "month": ["Jan", "Jan", "Feb"], "eggs": [47, 221, 77]}
).set_index("state")
print(sales.index.is_unique)
print(sales.loc["NY"])
print(sales.iloc[1])
try:
    sales.reindex(["CA", "NY"])
except ValueError as error:
    print("ValueError:", error)
