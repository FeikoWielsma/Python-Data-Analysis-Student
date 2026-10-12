import pandas as pd

stocks = pd.read_csv("stocks.csv").set_index(["Symbol", "Date"]).sort_index()
print(stocks.loc["AAPL"])
print(stocks.loc[("CSCO", "2026-10-06"), "Close"])
print(stocks.loc["CSCO":"MSFT", "Close"])
