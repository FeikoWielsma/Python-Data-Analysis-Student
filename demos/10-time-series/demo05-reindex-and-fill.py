import pandas as pd

sales = pd.read_csv("sales-feb-2026.csv", parse_dates=["Date"], index_col="Date")
evening = pd.date_range("2026-02-11 20:00", periods=4, freq="h")
print(sales.reindex(evening))
print(sales.reindex(evening, method="ffill"))
print(sales.reindex(evening, method="bfill"))
