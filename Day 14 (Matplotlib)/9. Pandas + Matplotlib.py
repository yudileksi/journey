import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")

type_count = df["Type1"].value_counts(ascending=True)   #ascending to ascend the most one

plt.barh(type_count.index, type_count.values, color="red",
                                            edgecolor="black")  # the edge color

plt.title("# Number of Pokemon Type")
plt.xlabel("Count")
plt.ylabel("Type")

plt.tight_layout()      # to make everything fit
plt.show()