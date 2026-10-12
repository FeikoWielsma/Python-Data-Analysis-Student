import pandas as pd

auto = pd.read_csv("auto-mpg.csv")
print(auto.head())


def zscore(series):
    return (series - series.mean()) / series.std()


print(zscore(auto["mpg"]).head())
