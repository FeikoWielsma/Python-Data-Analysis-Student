import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
print(df["salt"]["Jan"])
print(df.eggs["Mar"])
print(df.loc["Jan", "salt"], df.loc["Mar", "eggs"])
