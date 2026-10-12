import pandas as pd

sales = pd.read_csv("sales-feb-2026.csv", parse_dates=["Date"], index_col="Date")
print(sales.loc["2026-02-19 11:00:00", "Company"])
print(sales.loc["2026-02-05"])
print(sales.loc["February 5, 2026"].shape, sales.loc["2026-Feb-5"].shape)
print(sales.loc["2026-02"].shape, sales.loc["2026"].shape)
