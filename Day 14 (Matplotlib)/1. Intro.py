import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

x = np.array([2020, 2021, 2022, 2023])
y1 = np.array([13, 36, 24, 29])
y2 = np.array([21, 24, 31, 27])

line_style = dict(marker="o",
            ms=10, mfc= "red",
            markeredgecolor="red",
            linestyle="solid",
            linewidth=4, color="gray")              # this so it become default style

plt.plot(x,y1, **line_style)                 # you can customize other things by type it before **

plt.plot(x,y2, **line_style)

plt.show()