import pandas as pd

small_orders = pd.DataFrame({"customer_id": ["001", "002", "004"], "units": [10, 20, 30]})
small_customers = pd.DataFrame(
    {"customer_id": ["001", "002", "003"], "region": ["North", "South", "West"]}
)

for how in ["inner", "left", "outer"]:
    result = small_orders.merge(
        small_customers, on="customer_id", how=how, validate="one_to_one", indicator=True
    )
    print(how, "rows:", len(result), "units:", result["units"].sum())

audit = small_orders.merge(
    small_customers, on="customer_id", how="outer", validate="one_to_one", indicator=True
)
print(audit[["customer_id", "_merge"]].to_string(index=False))
unmatched = audit.loc[audit["_merge"] != "both"]
print("Unmatched keys:", unmatched["customer_id"].tolist())

left = small_orders.assign(status="ordered")
right = small_customers.rename(columns={"customer_id": "id"}).assign(status="active")
named = left.merge(
    right,
    left_on="customer_id",
    right_on="id",
    how="left",
    suffixes=("_order", "_customer"),
    validate="one_to_one",
)
print(named[["customer_id", "status_order", "status_customer"]].to_string(index=False))
