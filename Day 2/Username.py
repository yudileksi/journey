

name = input("Enter your username : ")

if len(name) > 12:
    print("The username must contain less than 12 characters")
elif not name.find(" ") == -1:
    print("The username must not contain spaces")
elif not name.isalpha():
    print("The username must not contain digits")
else:
    print(f'Hello {name}, Nice to meet you!')
