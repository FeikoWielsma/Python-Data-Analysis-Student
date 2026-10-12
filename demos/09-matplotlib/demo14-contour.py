import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 200)
y = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + Y**2) / 2) - 0.6 * np.exp(-((X - 1.5) ** 2 + (Y - 1) ** 2))

fig, ax = plt.subplots(figsize=(6, 4.5))
filled = ax.contourf(X, Y, Z, levels=15, cmap="viridis")
lines = ax.contour(X, Y, Z, levels=8, colors="black", linewidths=0.6)
ax.clabel(lines, fontsize=8)
fig.colorbar(filled, ax=ax, label="height")
ax.set(title="Contour plot", xlabel="x", ylabel="y")
fig.tight_layout()
fig.savefig("contour.png")
plt.show()
