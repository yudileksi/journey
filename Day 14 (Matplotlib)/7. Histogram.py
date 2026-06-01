# Histogram = a visual representation of the distribution of quantitative data.
#             They group values into bins (intervals)
#             and counts how many fall in each range.

import matplotlib.pyplot as plt
import numpy as np

scores = np.random.normal(loc=80, scale=10, size=100)
scores = np.clip(scores, 0, 100)

plt.hist(scores, bins=10,
         color="lightblue", edgecolor="black")

plt.title("Exam scores")
plt.xlabel("Score")
plt.ylabel("# of Students")

plt.show()

