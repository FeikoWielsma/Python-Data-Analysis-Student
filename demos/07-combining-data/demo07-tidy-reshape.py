from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "datasets"
wide = pd.read_csv(DATA / "orders-wide.csv", dtype={"customer_id": str})

long = wide.melt(
    id_vars="customer_id", value_vars=["Jan", "Feb"], var_name="month", value_name="units"
)
print(long.to_string(index=False))
print("Measurements:", len(long), "Units:", long["units"].sum())

restored = long.pivot(index="customer_id", columns="month", values="units")
print(restored)

repeated = pd.concat([long, long.iloc[[0]]], ignore_index=True)
try:
    repeated.pivot(index="customer_id", columns="month", values="units")
except ValueError:
    print("Pivot rejected duplicate customer/month pairs")
totals = repeated.pivot_table(index="customer_id", columns="month", values="units", aggfunc="sum")
print(totals)
