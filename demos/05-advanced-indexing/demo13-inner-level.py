import pandas as pd

stocks = pd.read_csv("stocks.csv").set_index(["Symbol", "Date"]).sort_index()
print(stocks.loc[(slice(None), "2026-10-06"), :])
print(stocks.xs("2026-10-06", level="Date"))
