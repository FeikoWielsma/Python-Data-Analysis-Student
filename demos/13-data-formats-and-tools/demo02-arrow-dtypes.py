import pandas as pd

arrow = pd.read_csv("orders.csv", dtype={"order_id": "string[pyarrow]"}, dtype_backend="pyarrow")
print(arrow.dtypes)
print(arrow["units"].isna().sum())
