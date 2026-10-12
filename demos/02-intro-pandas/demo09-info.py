import pandas as pd

aapl = pd.read_csv("AAPL.csv").set_index("Date")
aapl.info()
print(aapl.isna().sum())
