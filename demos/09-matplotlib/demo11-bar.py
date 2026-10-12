import matplotlib.pyplot as plt
import pandas as pd

auto = pd.read_csv("auto-mpg.csv")

mean_mpg = auto.groupby("origin")["mpg"].mean().sort_values()
counts = auto["cyl"].value_counts().sort_index()

fig, (left, right) = plt.subplots(1, 2, figsize=(8, 3.5), layout="constrained")
left.barh(mean_mpg.index, mean_mpg.to_numpy())
left.set(title="Mean mpg by origin", xlabel="Miles per gallon")
right.bar(counts.index.astype(str), counts.to_numpy())
right.set(title="Cars by cylinders", xlabel="Cylinders", ylabel="Cars")
fig.savefig("bar.png")
plt.show()
