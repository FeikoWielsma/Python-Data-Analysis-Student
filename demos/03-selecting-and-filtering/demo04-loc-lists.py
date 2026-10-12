import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
print(df.loc[["Jan", "Jun"], ["eggs", "spam"]])
print(df.loc["Feb":"Apr", ["spam", "eggs"]])
