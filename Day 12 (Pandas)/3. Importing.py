# IMPORTING (CSV & JSON)
# CSV = Comma-separated values  ;   JSON = JavaScript Object Notation

import pandas as pd

df = pd.read_csv("data.csv")    # pd.read_csv   to read csv data/ for json, just change the csv (pd.read_json)

print(df.to_string())       # to print all data use .to_string()
