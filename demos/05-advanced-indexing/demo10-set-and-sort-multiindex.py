import pandas as pd

stocks = pd.read_csv("stocks.csv")
print(stocks)
stocks = stocks.set_index(["Symbol", "Date"]).sort_index()
print(stocks)
