import pandas as pd

sales = pd.read_csv("sales-feb-2026.csv", parse_dates=["Date"], index_col="Date")
daily_mean = sales["Units"].resample("D").mean()
print(daily_mean.loc["2026-02-02"])
print(sales.loc["2026-02-02", "Units"])
print(sales.loc["2026-02-02", "Units"].mean())
