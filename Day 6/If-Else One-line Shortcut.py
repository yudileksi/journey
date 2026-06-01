# Conditional expression (ternary operator)
# one-line shortcut for if-else operator
# Formula   =   X if conditions else Y

num = 20
a = 42
b = 5
age = 21
temp = 25
user_role = 'boy'

#print("Positive" if num > 0 else "Negative")
#result = "EVEN" if num % 2 == 0 else "ODD"
#max_num = a if a > b else b
#min_num = a if a < b else b
#adult = "You are old enough" if age > 18 else "You are not old enough"
#weather = "Schedule still going" if 30 > temp > 20 else "Schedule cancelled"
access = "You have full access" if user_role == "admin" else "You have limited access"

print(access)