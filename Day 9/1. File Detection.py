# Basic File Detection

# directory = just a folder
# /home/user/projects/   ← this is a directory

import os           # os = operation system

file_path = "test/text.txt"

if os.path.exists(file_path):
    print (f"The location of '{file_path}' exists")

    if os.path.isfile(file_path):
        print("This is a file")
    elif os.path.isdir(file_path):
        print("This is a directory")

else:
    print("The location doesn't exists")