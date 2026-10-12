import pandas as pd

sales = pd.read_csv("sales-feb-2026.csv", parse_dates=["Date"], index_col="Date")
print(sales.index.is_monotonic_increasing, sales.index.has_duplicates)
utc = sales.index.tz_localize("America/Chicago").tz_convert("UTC")
print(utc[:3])
