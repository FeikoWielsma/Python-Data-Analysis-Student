import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
print(df.iloc[4, 2])
print(df.iloc[2:5, 1:])
print(df.loc["Mar":"May", "salt":"spam"])
