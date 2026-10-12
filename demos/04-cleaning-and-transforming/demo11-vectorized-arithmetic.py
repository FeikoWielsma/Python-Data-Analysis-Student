import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
print(df // 12)
print(df["eggs"] + df["spam"])
print(df["eggs"].add(df["salt"], fill_value=0))
