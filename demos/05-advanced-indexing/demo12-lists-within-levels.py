import pandas as pd

stocks = pd.read_csv("stocks.csv").set_index(["Symbol", "Date"]).sort_index()
print(stocks.loc[(["AAPL", "MSFT"], "2026-10-07"), :])
print(stocks.loc[("CSCO", ["2026-10-07", "2026-10-05"]), "Close"])
