import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
print(type(df["eggs"]).__name__, df["eggs"].shape)
print(type(df[["eggs"]]).__name__, df[["eggs"]].shape)
