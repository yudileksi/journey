# Read File (.txt, .json, .csv)
#------------------------------------------------------------------------------------------------------#
#file_path = "C:\\Users\\ACER\\OneDrive\\Desktop\\test.txt"

#try:
#    with open(file_path, "r") as file:              # "r" = read        # file = the name of file
#        content = file.read()
#        print(content)

#except FileNotFoundError:
#    print("That file was not found")
#except PermissionError:
#    print("That file is locked")

#------------------------------------------------------------------------------------------------------#
#.json

#import json

#file_path = "C:\\Users\\ACER\\OneDrive\\Desktop\\test.json"

#try:
#    with open(file_path, "r") as file:
#        content = json.load(file)
#        print(content["Name"])

#except FileNotFoundError:
#    print("That file was not found")
#except PermissionError:
#    print("That file is locked")


#------------------------------------------------------------------------------------------------------#
#.csv

import csv

file_path = "C:\\Users\\ACER\\OneDrive\\Desktop\\test.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])                          # read the row #

except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("That file is locked")