import pandas as pd

raw = pd.DataFrame({"units": ["3", "1", "2"], "price": ["4.50", "3.20", "n/a"]})
print(raw.dtypes)
raw["units"] = raw["units"].astype("int64")
raw["price"] = pd.to_numeric(raw["price"], errors="coerce")
print(raw.dtypes)
print(raw)
