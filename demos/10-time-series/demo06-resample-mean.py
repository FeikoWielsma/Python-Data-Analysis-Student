import pandas as pd

sales = pd.read_csv("sales-feb-2026.csv", parse_dates=["Date"], index_col="Date")
daily_mean = sales["Units"].resample("D").mean()
print(daily_mean.head(8))
