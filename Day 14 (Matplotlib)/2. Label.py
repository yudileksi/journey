# Customize label title

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

x = np.array([2020, 2021, 2022, 2023])
y1 = np.array([13, 36, 24, 29])
y2 = np.array([21, 24, 31, 27])
y3 = np.array([34, 30, 19, 17])

plt.title("Class Size", fontsize=20,
          family="Arial", fontweight="bold",
          color="darkblue")

plt.xlabel("Year 1", fontsize=20,
           family="Arial", fontweight="bold",
           color="blue")

plt.ylabel("Students", fontsize=20,
           family="Arial", fontweight="bold",
           color="blue")

plt.tick_params(axis="both",
                color="red")

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.xticks(x)

plt.show()