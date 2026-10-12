import pandas as pd

sales = pd.read_csv("sales-feb-2026.csv", parse_dates=["Date"], index_col="Date")
daily = sales["Units"].resample("D")
print(daily.agg(["count", "sum", "mean"]).loc["2026-02-05":"2026-02-08"])
print(sales["Units"].resample("D").sum(min_count=1).loc["2026-02-05":"2026-02-08"])
