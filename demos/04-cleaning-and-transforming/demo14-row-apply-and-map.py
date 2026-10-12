import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
print(df.apply(lambda row: row.max() - row.min(), axis=1))
print(df.map(lambda value: f"{value:.0f}").loc["Jan"])
