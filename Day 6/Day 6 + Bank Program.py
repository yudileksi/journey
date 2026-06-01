# SCOPE RESOLUTION
# LEGB = Local -> Enclosed -> Global -> Built-in

#def func1():
#    x = 1
#    print(x)

#def func2():
#    x = 2
#    print(x)

#func1()
#func2()
# Those x are Local in scope resolution

#def func1():
#    x = 1
#    def func2():
#        print(x)
#    func2()

#func1()

# print → just shows output, the value DISAPPEARS after
#def func_print():
#    print(5)

#func_print()       # shows 5
#result = func_print()
#print(result)      # shows None ← nothing was returned!


#PYTHON BANKING PROGRAM

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("How many would you like to deposit? : $"))
    if amount < 0 :
        print("Deposit can't be negative!")
        return 0
    else:
        return amount

def withdraw(balance):
    amount =  float(input("How many would you like to withdraw? : $"))
    if amount > balance :
        print("Insufficient funds!")
        return 0
    elif amount < 0:
        print("Amount must be greater than zero!")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("------------")
        print("  Welcome!  ")
        print("------------")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("------------")

        choice = input(f"What would you like to access: ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Your choice is invalid!")

    print("Thank you for using our service!")

if __name__ == "__main__":
    main()