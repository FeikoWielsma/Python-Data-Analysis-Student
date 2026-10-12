import pandas as pd

small_orders = pd.DataFrame({"customer_id": ["001", "002", "004"], "units": [10, 20, 30]})
small_customers = pd.DataFrame(
    {"customer_id": ["001", "002", "003"], "region": ["North", "South", "West"]}
)

indexed_orders = small_orders.set_index("customer_id")
indexed_customers = small_customers.set_index("customer_id")
joined = indexed_orders.join(indexed_customers, how="left", validate="one_to_one")
print(joined)
