import pandas as pd

sales = pd.read_csv("sales-feb-2026.csv", parse_dates=["Date"], index_col="Date")
daily_sum = sales["Units"].resample("D").sum()
print(daily_sum.head(8))
print(sales["Units"].resample("D").sum().max())
print(sales["Units"].resample("D").sum().idxmax())
