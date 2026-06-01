#SERIES = a single column in spreadsheet

import pandas as pd
from pandas.core import series

##data = [100, 102, 104, 200, 202]

##series = pd.Series(data, index=["a", "b", "c", "d", "e"]) #Series = constructor, not function
                                        # index=[] to change the label, the default start form 0

#print(series)
#print(series.loc["b"])               #loc= location by label

### to print or access a value, you access the loc property

#series.loc["c"] = 500

#print(series)

### series.iloc[] for integer location (from 0), usually to find the first or the last (maybe)

### to filter value just by > <

#print(series[series >= 200])

###Dictionary (key value pair [...:...])

calories = {"Day 1" : 1750, "Day 2" : 2100, "Day 3" : 1700}

series = pd.Series(calories)

series.loc["Day 1"] += 200

#print(series)
#print(series.loc["Day 1"])      #to access the value of targetted key
print(series[series < 2000])