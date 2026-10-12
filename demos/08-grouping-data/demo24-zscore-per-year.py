import pandas as pd

auto = pd.read_csv("auto-mpg.csv")
print(auto.head())


def zscore(series):
    return (series - series.mean()) / series.std()


# a = auto.groupby('yr')['yr'].unique()
# print(a.head())
print(auto.groupby("yr")["mpg"].transform(zscore).head())
