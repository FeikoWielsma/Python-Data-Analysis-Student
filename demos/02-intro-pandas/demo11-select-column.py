import pandas as pd

aapl = pd.read_csv("AAPL.csv").set_index("Date")
close = aapl["Close"]
print(type(close).__name__)
print(close.head(3))

prices = close.to_numpy()
print(type(prices).__name__, prices[:3])
