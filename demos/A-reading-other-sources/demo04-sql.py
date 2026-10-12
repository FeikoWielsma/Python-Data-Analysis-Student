import sqlite3

import pandas as pd

con = sqlite3.connect(":memory:")
sales = pd.read_csv("sales-feb-2026.csv")
sales.to_sql("sales", con, index=False)

query = """
SELECT Company, SUM(Units) AS units, COUNT(*) AS orders
FROM sales
GROUP BY Company
ORDER BY units DESC
"""
print(pd.read_sql(query, con))
print(pd.read_sql("SELECT * FROM sales WHERE Units > ?", con, params=(15,)))
con.close()
