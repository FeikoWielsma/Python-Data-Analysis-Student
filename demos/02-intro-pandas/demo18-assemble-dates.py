import pandas as pd

filepath = "ISSN_D_tot.csv"
col_names = ["year", "month", "day", "dec_date", "sunspots", "definite"]
sunspots = pd.read_csv(filepath, header=None, names=col_names, na_values={"sunspots": [" -1"]})
sunspots["date"] = pd.to_datetime(sunspots[["year", "month", "day"]])
sunspots = sunspots.drop(columns=["year", "month", "day"])
print(sunspots.iloc[10:13])
print(sunspots.dtypes)
print(sunspots["date"].iloc[[0, -1]].tolist())
