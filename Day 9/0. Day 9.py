# Decorator :   A function that extends the behavior of another functions without modifying the base function
#               Pass the base functions as an argument to the decorator

#def add_sprinkle(func):
#    def wrapper(*args, **kwargs):           # Why we must add *args, **kwargs so that base function can add the argument (flavor arg)?
#        print("*Add sprinkle*")
#        func(*args, **kwargs)
#    return wrapper

#def add_fudge(func):
#    def wrapper(*args, **kwargs):
#        print("*Add a fudge*")
#        func(*args, **kwargs)
#    return wrapper

#@add_sprinkle
#@add_fudge
#def get_ice_cream(flavor):
#    print(f"Here is your {flavor} ice cream 🍨")

#get_ice_cream("vanilla")


#---------------------------------------------------------------------------------#
# exception =   an event that interrupts the flow of program
#               (ZeroDivisionError, TypeError, ValueError)