from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "datasets"

months = ["jan", "feb", "mar"]
frames = [pd.read_csv(DATA / f"orders-{month}.csv", dtype={"customer_id": str}) for month in months]
orders = pd.concat(
    [frame.assign(source=month) for month, frame in zip(months, frames)], ignore_index=True
)
print(orders[["source", "order_id", "customer_id", "units"]].to_string(index=False))

indexed = pd.concat(frames, keys=months, names=["source", "row"])
print(indexed.index.tolist())
print("Rows:", len(orders), "Units:", orders["units"].sum())
