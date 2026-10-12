import matplotlib.pyplot as plt
import pandas as pd

degrees = pd.read_csv("women-degrees.csv")

fields = ["physical_sciences", "computer_science", "health", "education"]
fig, axes = plt.subplots(2, 2, figsize=(7, 5), sharex=True, layout="constrained")
for ax, field in zip(axes.flat, fields):
    ax.plot(degrees["year"], degrees[field])
    ax.set_title(field.replace("_", " ").title())
axes[0, 0].set_ylabel("% women")
axes[1, 0].set_ylabel("% women")
fig.savefig("subplots.png")
plt.show()
