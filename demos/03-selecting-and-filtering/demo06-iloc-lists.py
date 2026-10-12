import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
print(df.iloc[[0, 4, 5], [0, 2]])
print(df.iloc[-2:, :])
