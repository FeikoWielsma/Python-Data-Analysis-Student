import numpy as np
import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")

print(np.sqrt(df["eggs"]).round(2))
print(np.log10(df).round(2))
