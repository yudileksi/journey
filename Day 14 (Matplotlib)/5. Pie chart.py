# Bar chart = Circular chart divided into slices to show percentages of the total
#             Good for visualizing distribution among categories

import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Freshmen", "Sophomores", "Juniors", "Seniors"])
values = np.array([34, 26, 16, 24])
colors = ["red", "blue", "yellow", "green"]

plt.pie(values, labels=categories,
                autopct="%1.1f%%",
                colors=colors,
                explode=[0, 0, 0, 0.1],
                shadow=True, startangle=90)

plt.show()