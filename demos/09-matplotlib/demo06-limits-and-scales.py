import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

degrees = pd.read_csv("women-degrees.csv")


fig, (left, right) = plt.subplots(1, 2, figsize=(8, 3.5), layout="constrained")
left.plot(degrees["year"], degrees["computer_science"])
left.set_xlim(1990, 2010)
left.set_ylim(0, 50)
left.set_xticks([1990, 2000, 2010])
left.set_title("Limits and ticks")

x = np.arange(1, 9)
right.plot(x, 10.0**x, marker="o")
right.set_yscale("log")
right.set_title("Log scale")
fig.savefig("limits-and-scales.png")
plt.show()
