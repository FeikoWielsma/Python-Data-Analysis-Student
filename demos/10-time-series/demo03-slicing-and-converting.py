import pandas as pd

sales = pd.read_csv("sales-feb-2026.csv", parse_dates=["Date"], index_col="Date")
print(sales.loc["2026-02-16":"2026-02-20"])
evening = pd.to_datetime(
    ["2026-02-11 20:00", "2026-02-11 21:00", "2026-02-11 22:00", "2026-02-11 23:00"]
)
print(evening)
