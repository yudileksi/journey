#Bar charts = compare categories data by representing each categories with a bar

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2012, 2013, 2014, 2015, 2016])
y = np.array([16, 36, 24, 29, 20])

plt.bar(x, y, color="red")

plt.title("I don't know man")
plt.xlabel("Number")
plt.ylabel("Also Number")

plt.show()