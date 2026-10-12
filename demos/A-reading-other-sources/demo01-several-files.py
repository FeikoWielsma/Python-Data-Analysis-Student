from glob import glob

import pandas as pd

filenames = sorted(glob("sales-*-2026.csv"))
print(filenames)
frames = [pd.read_csv(name, parse_dates=["Date"]).assign(source=name) for name in filenames]
sales = pd.concat(frames, ignore_index=True)
print(sales["source"].value_counts().sort_index())
print(len(sales), sales["Date"].min(), sales["Date"].max())
