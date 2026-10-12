import matplotlib.pyplot as plt
import pandas as pd

degrees = pd.read_csv("women-degrees.csv")

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(degrees["year"], degrees["computer_science"])
ax.set(title="Computer Science degrees awarded to women", xlabel="Year", ylabel="% of degrees")
fig.tight_layout()
fig.savefig("line-plot.png")
plt.show()
