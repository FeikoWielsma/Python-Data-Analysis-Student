import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
df2 = df.copy()
mask = df2["salt"] > 55
df2["eggs"][mask] += 5
print(df2["eggs"].tolist())
