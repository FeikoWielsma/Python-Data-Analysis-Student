import matplotlib.pyplot as plt
import pandas as pd

degrees = pd.read_csv("women-degrees.csv")

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(degrees["year"], degrees["computer_science"], label="Computer Science")
ax.plot(degrees["year"], degrees["physical_sciences"], label="Physical Sciences", linestyle="--")
ax.set(xlabel="Year", ylabel="% of degrees awarded to women")
ax.legend(loc="lower right")
fig.tight_layout()
fig.savefig("legend.png")
plt.show()
