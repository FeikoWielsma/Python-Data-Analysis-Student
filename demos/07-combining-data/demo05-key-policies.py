from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "datasets"

left = pd.DataFrame({"id": ["001", None], "units": [10, 20]})
right = pd.DataFrame({"id": ["001", None], "region": ["North", "Unknown"]})
matched = left.merge(right, on="id", validate="one_to_one", indicator=True)
print(matched.to_string(index=False))

inferred = pd.read_csv(DATA / "orders-jan.csv")
typed = pd.read_csv(DATA / "orders-jan.csv", dtype={"customer_id": str})
print("Inferred IDs:", inferred["customer_id"].tolist())
print("Text IDs:", typed["customer_id"].tolist())
try:
    inferred.merge(typed, on="customer_id")
except ValueError:
    print("Rejected: integer and string merge keys")
