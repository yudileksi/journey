# DataFrame = data with rows AND columns (2D)
#            Similar to an excel spreadsheet

import pandas as pd

data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])         #DataFrame = constructions

### Add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]

### Add a new row
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"},
                        {"Name": "Eugene", "Age": 60, "Job": "Manager"}],
                       index=["Employee 4", "Employee 5"])
df = pd.concat([df, new_row])      #(concatenate)

print(df)
#print(df.loc["Employee 2"])   #iloc.  for finding with int number


