import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
print(df[df["eggs"].between(100, 210)])
first_quarter = df.index.isin(["Jan", "Feb", "Mar"])
print(df[first_quarter])
