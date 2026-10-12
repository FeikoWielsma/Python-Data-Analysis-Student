import pandas as pd

aapl = pd.read_csv("AAPL.csv")
print(aapl.shape)
print(aapl.columns.tolist())
aapl = aapl.set_index("Date")
print(aapl.shape)
