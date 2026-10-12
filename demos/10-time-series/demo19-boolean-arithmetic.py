import pandas as pd

sales = pd.read_csv("sales-feb-2026.csv", parse_dates=["Date"])
is_ware = sales["Product"].str.contains("ware")
print(True + True, True + False)
print(is_ware.sum(), len(sales))
print(is_ware.mean().round(3))
