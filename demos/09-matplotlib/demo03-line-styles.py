import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 20)
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, x, color="tab:blue", linestyle="-", label="linear")
ax.plot(x, x**2, color="tab:orange", linestyle="--", marker="o", label="quadratic")
ax.plot(x, x**3, color="tab:green", linestyle=":", linewidth=3, label="cubic")
ax.plot(x, 2 * x, "k^-", markersize=4, label="format string 'k^-'")
ax.legend()
fig.tight_layout()
fig.savefig("line-styles.png")
plt.show()
