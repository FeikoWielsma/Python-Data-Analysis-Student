import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
print(df.dropna())
print(df.dropna(subset=["eggs", "spam"]).shape)
print(df.dropna(axis="columns").columns.tolist())
print(df.dropna(axis="columns", thresh=5).columns.tolist())
