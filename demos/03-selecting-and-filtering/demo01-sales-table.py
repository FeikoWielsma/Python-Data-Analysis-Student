import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
print(df)
print(df.shape)
