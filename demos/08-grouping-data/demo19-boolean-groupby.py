import pandas as pd

auto = pd.read_csv("auto-mpg.csv")
chevy = auto["name"].str.contains("chevrolet")
print(auto.groupby(["yr", chevy])["mpg"].mean().loc[70:76])
