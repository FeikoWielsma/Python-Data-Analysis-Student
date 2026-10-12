import pandas as pd

filepath = "ISSN_D_tot.csv"
sunspots = pd.read_csv(filepath)
print(sunspots.iloc[10:13])
