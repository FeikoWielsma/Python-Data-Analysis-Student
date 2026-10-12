import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
print(df.fillna(0).loc["May"])
print(df["salt"].fillna(df["salt"].median()).loc["May"])
