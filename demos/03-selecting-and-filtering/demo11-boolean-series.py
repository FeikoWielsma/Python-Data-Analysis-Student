import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")
mask = df["salt"] > 60
print(mask)
