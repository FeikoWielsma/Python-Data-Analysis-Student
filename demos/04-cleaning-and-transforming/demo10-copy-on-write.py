import pandas as pd

df = pd.DataFrame({"visitors": [139, 237]})
column = df["visitors"]
column.iloc[0] = 0
print(df["visitors"].tolist())
df.loc[0, "visitors"] = 0
print(df["visitors"].tolist())
