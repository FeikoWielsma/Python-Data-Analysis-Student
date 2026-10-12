import pandas as pd

sales = pd.read_csv("sales-feb-2026.csv", parse_dates=["Date"], index_col="Date")
two_days = sales.loc["2026-02-04":"2026-02-05", "Units"]
print(two_days)
print(two_days.resample("4h").sum())
