import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
print(df.loc["May", "spam"])
print(df.loc["Jan", "salt"])
