from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

degrees = pd.read_csv("women-degrees.csv")


fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(degrees["year"], degrees["computer_science"])
ax.set(title="Computer Science", ylabel="% women")

fig.savefig("degrees.png", dpi=200, bbox_inches="tight")
fig.savefig("degrees.svg")
fig.savefig("degrees.pdf")
for name in ["degrees.png", "degrees.svg", "degrees.pdf"]:
    print(name, Path(name).stat().st_size, "bytes")
plt.show()
plt.close(fig)
