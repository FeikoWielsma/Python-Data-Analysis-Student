import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 80)
y = np.linspace(-3, 3, 80)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + Y**2) / 2) - 0.6 * np.exp(-((X - 1.5) ** 2 + (Y - 1) ** 2))

fig, ax = plt.subplots(figsize=(6, 4.5), subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="none")
ax.set(title="Surface plot", xlabel="x", ylabel="y", zlabel="height")
fig.tight_layout()
fig.savefig("surface-3d.png")
plt.show()
