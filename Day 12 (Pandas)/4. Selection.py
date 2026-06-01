import pandas as pd

df = pd.read_csv("data.csv", index_col="Name")
                                    # index_col+""     to set what column you'd like to become index (first column)
# SELECTION BY COLUMN
#print(df["Name"].to_string())       # " " => column name
#print(df["Height"].to_string())
#print(df["Weight"].to_string())
#print(df[["Name", "Height", "Weight"]].to_string()) # to print more than 1 column

# SELECTION BY ROW/S     (find it through index) (u can edit the index by index_col="" like above
#print(df.loc["Pikachu"])           # has label (start from 0 if no edit of index)
#print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])
#print(df.iloc[0:11:2, 0:4])                # find by integer

# USER INPUT
pokemon = input("Enter a pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")