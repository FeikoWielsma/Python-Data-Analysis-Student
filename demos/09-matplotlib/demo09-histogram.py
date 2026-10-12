import matplotlib.pyplot as plt
import pandas as pd

auto = pd.read_csv("auto-mpg.csv")

fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(auto["mpg"], bins=20, edgecolor="white")
ax.axvline(auto["mpg"].median(), color="black", linestyle="--", label="median")
ax.set(title="Fuel economy of 392 cars", xlabel="Miles per gallon", ylabel="Number of cars")
ax.legend()
fig.tight_layout()
fig.savefig("histogram.png")
plt.show()
