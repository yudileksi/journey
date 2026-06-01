# Python Writing Files (.txt, .json, .csv)
import json

#.txt   =>  write text (txt)

#txt_data = "I like food"
#employees = ["Crabs", "SpongeBob", "Squidward", "Patrick"]

#file_path = "C:\\Users\\ACER\\OneDrive\\Desktop\\test.txt"

#with open(file_path, "w") as file :                 # 'w' = write (will overwrite if already exist) ;
#    file.write(file_path)                           # 'x' = write if there is no file exist u want to create
#    for employee in employees:                      # 'a' = append (add the text u input) ;
#        file.write(employee + "\n")                 # "\n" will create data in new line
#    print(f"The file {file_path} been created")


#------------------------------------------------------------------------------------------------------------------#
#.json  =>  made of KEY VALUE pairs { ... : ... }

#import json                                         # Do we really need to import? Cause without it, we can still run it

#employee = {"Name" : "SpongeBob",
#            "Position" : "Cook",
#            "Age" : 20}

#file_path = "C:\\Users\\ACER\\OneDrive\\Desktop\\test.json"

#with open(file_path, "w") as file :                 # "open" has 2 arguments = file_path & mode "w/x/r/a"
#    json.dump(employee, file, indent=4)             # indent=# add # before the text
#    print(f"The file {file_path} been created")


#------------------------------------------------------------------------------------------------------------------#
#.csv   =>  comma separated values

import csv                                         # Do we really need to import? Cause without it, we can still run it

employees = [["Name", "Age", "Job"],
            ["SpongeBob", 20, "Cook"],
            ["Patrick", 23, "Unemployed"],
            ["Sandy", 19, "Scientist"]]

file_path = "C:\\Users\\ACER\\OneDrive\\Desktop\\test.csv"     # \ = escape sequences, so we have to change with \\ or /

try:
    with open(file_path, "w", newline="") as file :     # Whats that "with" function for? = it'll close the file if we open it, so we have to use "with"
        writer = csv.writer(file)                       # Is this the fixed formula/code?
        for row in employees:
            writer.writerow(row)
        print(f"The file {file_path} been created")
except FileExistsError:
    print("The file already exists")