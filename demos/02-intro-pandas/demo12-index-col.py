import pandas as pd

users = pd.read_csv("users.csv", index_col=0)
print(users)
