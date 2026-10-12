import pandas as pd

prices = pd.Series([10.70, 10.86, 10.74], index=["Mon", "Tue", "Wed"])
print(prices.loc["Tue"], prices.iloc[1])
print(prices.loc["Mon":"Tue"].tolist())
print(prices.iloc[0:2].tolist())

numbered = pd.Series([10.70, 10.86, 10.74], index=[3, 2, 1])
print(numbered.loc[1], numbered.iloc[1])
