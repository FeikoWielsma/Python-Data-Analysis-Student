import matplotlib.pyplot as plt
import pandas as pd

auto = pd.read_csv("auto-mpg.csv")

fig, ax = plt.subplots(figsize=(6, 4))
points = ax.scatter(auto["weight"], auto["mpg"], c=auto["hp"], cmap="viridis", s=20, alpha=0.8)
fig.colorbar(points, ax=ax, label="Horsepower")
ax.set(title="Heavier cars use more fuel", xlabel="Weight (lb)", ylabel="Miles per gallon")
fig.tight_layout()
fig.savefig("scatter.png")
plt.show()
