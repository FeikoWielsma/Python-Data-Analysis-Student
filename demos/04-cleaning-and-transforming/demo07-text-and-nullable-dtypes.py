import pandas as pd

text = pd.Series(["Paris", None])
names = pd.Series(["Paris", None], dtype="string")
counts = pd.Series([7, None], dtype="Int64")
flags = pd.Series([True, None], dtype="boolean")
print(text.dtype, names.dtype, counts.dtype, flags.dtype)
print(text.isna().tolist(), counts.isna().tolist())
print((counts > 5).tolist())
