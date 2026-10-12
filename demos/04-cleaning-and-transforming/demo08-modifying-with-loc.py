import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
df2 = df.copy()
mask = df2["salt"] > 55
print(df2.loc[mask, "eggs"])
df2.loc[mask, "eggs"] += 5
print(df2)
