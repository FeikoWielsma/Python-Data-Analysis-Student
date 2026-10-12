import pandas as pd

heights = [59.0, 65.2, 62.9, 65.4, 63.7, 65.7, 64.1]
results = pd.DataFrame({"height": heights, "sex": "M"})
results.columns = ["height (in)", "sex"]
results.index = list("ABCDEFG")
print(results.head(3))

results = results.rename(columns={"height (in)": "height_in"})
print(results.columns.tolist())
