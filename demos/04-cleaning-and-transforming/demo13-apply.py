import pandas as pd

df = pd.read_csv("sales.csv", index_col="month")


def dozens(n):
    return n // 12


print(df.apply(dozens))
print(df.apply(lambda column: type(column).__name__))
