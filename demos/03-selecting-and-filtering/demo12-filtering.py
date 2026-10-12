import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
print(df[df["salt"] > 60])
enough_salt = df["salt"] > 60
print(df.loc[enough_salt, ["salt", "spam"]])
