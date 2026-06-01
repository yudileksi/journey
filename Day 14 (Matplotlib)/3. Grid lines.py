import matplotlib.pyplot as plt
import numpy as np

# help plot easier to read by adding reference lines

x = np.array([1, 2, 3, 4, 5])
y = np.array([16, 36, 24, 29, 20])

plt.grid(axis="y", linewidth=2,
         color="lightgrey", linestyle="dashed")

plt.plot(x, y)
plt.show()