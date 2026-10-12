import pandas as pd

aapl = pd.read_csv("AAPL.csv").set_index("Date")
print(aapl[["Close", "Volume"]].describe().round(2))
