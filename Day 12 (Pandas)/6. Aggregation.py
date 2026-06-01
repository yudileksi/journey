# aggregate functions = Reducing a set of values into a single summary value
#                       Used to summarize and analyze data
#                       Often used with the groupby() function

import pandas as pd

df = pd.read_csv("data.csv")

# WHOLE dataframe
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

# SINGLE COLUMN
# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())

group = df.groupby("Type1")
#print(group["Height"].mean())
# print(group["Height"].sum())
# print(group["Height"].min())    #/ max
print(group["Height"].count())