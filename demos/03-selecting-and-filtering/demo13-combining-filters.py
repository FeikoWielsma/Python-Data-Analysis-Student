import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
print(df[(df["salt"] >= 50) & (df["eggs"] < 200)])
print(df[(df["salt"] >= 50) | (df["eggs"] < 200)])
print(df[~(df["salt"] >= 50)])
