import pandas as pd

aapl = pd.read_csv("AAPL.csv").set_index("Date")
print(aapl.head(3))
print(aapl.tail(3))
