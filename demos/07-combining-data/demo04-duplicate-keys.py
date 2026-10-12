from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "datasets"
frames = [
    pd.read_csv(DATA / f"orders-{month}.csv", dtype={"customer_id": str})
    for month in ["jan", "feb", "mar"]
]
orders = pd.concat(frames, ignore_index=True)
customers = pd.read_csv(DATA / "orders-customers.csv", dtype={"customer_id": str})

try:
    orders.merge(customers, on="customer_id", how="left", validate="many_to_one")
except pd.errors.MergeError:
    print("Rejected: customer lookup keys are not unique")
duplicates = customers.loc[customers.duplicated("customer_id", keep=False)]
print(duplicates.to_string(index=False))

bad = orders.merge(customers, on="customer_id", how="left")
print(bad[["order_id", "customer_id", "units"]].to_string(index=False))
print("Before:", len(orders), orders["units"].sum())
print("After:", len(bad), bad["units"].sum())

lookup = customers.drop_duplicates()  # documented exact repeated export
checked = orders.merge(lookup, on="customer_id", how="left", validate="many_to_one", indicator=True)
assert len(checked) == len(orders)
assert checked["units"].sum() == orders["units"].sum()
missing = checked.loc[checked["_merge"] == "left_only", "customer_id"]
print("Rows:", len(checked), "Units:", checked["units"].sum())
print("Missing lookup:", missing.tolist())
