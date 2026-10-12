import pandas as pd

shares = pd.Series([10.70, 10.86], index=["Mon", "Tue"])
try:
    shares.index[0] = "Monday"
except TypeError as error:
    print("TypeError:", error)

shares = shares.rename(index={"Mon": "Monday", "Tue": "Tuesday"})
print(shares)

shares.index = ["M", "T"]
print(shares.index.tolist())
