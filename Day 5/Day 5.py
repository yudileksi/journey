# FUNCTION
# def = to create a function
# return = statement to end a function and send it back to the caller
# import time


#def sentence(name, age):
#    print(f"Happy birthday {name}!")
#    print(f"You are {age} years old")

#sentence("Yudi", 21)
#sentence("Rifa", 22)

# def name (first, last):
#    first = first.capitalize()
#    last = last.upper()
#    return first + " " + last

#full_name = name ("yudi", "grg")

#print(full_name)

#------------------------------------------------------------------#
# DEFAULT ARGUMENT

#def net_price(price, discount, tax):
    #return price * (1 - discount) * (1 + tax)

#print (net_price(100, 0, 0.05))

#Stopwatch
#def count(end, start=0):
#    for x in range(start, end+1):
#        print(x)
#        time.sleep(1)
#    print("DONE!")
#count(5)


#------------------------------------------------------------------#
# KEYWORD ARGUMENT

#def get_phone(country, area, first, last):
#    return f"Your phone number : {country}-{area}-{first}-{last}"

#phone_num = get_phone(country=1, area=234, first=345, last=5465)

#print(phone_num)


#------------------------------------------------------------------#
# ARBITRARY ARGUMENTS => To allow pass multiple arguments
# *args        =   for non-key arguments
# **kwargs     =   for key-words arguments

#def list_name(*args):
#    for arg in args:
#        print (arg)

#list_name("yudi", "rifa", "leksi", "ling")

#def adress(**kwargs):
#    for key, value in kwargs.items():
#        print(f"{key:10} : {value}")
#
#adress(country="Indonesia", province="North Sumatra", city="Siantar", road="Kartini")

#adress = {"country" : "indonesia", "province" : "north sumatra", "city" : "siantar", "road" : "kartini"}

#for key, value in adress.items():
#    print(f"{key} : {value}")

#place = input("Enter your option: ").lower()

#if place in adress:
#    print(f"{place} is in {adress[place]}")
#else:
#    print(f"{place} not available")

# (expression for value in iteration if condition)


#------------------------------------------------------------------#
# LIST COMPREHENSION => one-line for, in, if functions

#result = [x for x in range(1, 11)]

#print(result)

#num = (1, -2, 3, -4, 5, -6)

#positive_num = [x for x in num if x >= 0]
#negative_num = [x for x in num if x >= 0]
#even_num = [x for x in num if x % 2 == 0]
#odd_num = [x for x in num if x % 2 == 1]

#print(even_num)

grades = [23, 64, 86, 43, 75, 99, 62, 65]

passing = [x for x in grades if x >= 65]

print(passing)
