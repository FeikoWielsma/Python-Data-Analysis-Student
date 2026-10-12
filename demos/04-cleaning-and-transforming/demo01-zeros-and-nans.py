import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
df2 = df.copy()
df2["bacon"] = [0, 0, 50, 60, 70, 80]
print(df2)
