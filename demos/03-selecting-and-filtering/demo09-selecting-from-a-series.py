import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
eggs = df["eggs"]
print(eggs.loc["Feb":"Apr"])
print(eggs.iloc[0], eggs.iloc[-1])
