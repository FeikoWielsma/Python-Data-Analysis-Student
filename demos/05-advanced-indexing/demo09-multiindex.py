import pandas as pd

rows = pd.DataFrame(
    {"state": ["CA", "CA", "NY"], "month": ["Jan", "Feb", "Jan"], "eggs": [47, 110, 221]}
)
by_state_month = rows.set_index(["state", "month"])
print(by_state_month)
print(by_state_month.index.is_unique, by_state_month.index.names)
print(by_state_month.loc[("CA", "Feb"), "eggs"])
