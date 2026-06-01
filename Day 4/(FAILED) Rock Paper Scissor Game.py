# Rock Paper Scissor Game

import random

options = ("rock", "paper", "scissor")
attempts = 0
is_running = True



print("Python Rock Paper Scissor Game")
print(f"FACE IT TILL U WIN")

while is_running:
    opponent = random.choice(options)
    attempt = input("Select your option (rock/paper/scissor): ").lower()
    if attempt.isalpha():
        if attempt == "rock":
            print(f"Your opponent has {opponent}")
            attempts += 1
            if opponent == opponent[0]:
                print("Try Again!")
            elif opponent == opponent[1]:
                print("You LOSE")
                is_running = False
            elif opponent == opponent[2]:
                print("You WIN!")
                is_running = False

        elif attempt == "paper":
            print(f"Your opponent has {opponent}")
            attempts += 1
            if opponent == opponent[0]:
                print("You WIN!")
                is_running = False
            elif opponent == opponent[1]:
                print("Try Again!")

            elif opponent == opponent[2]:
                print("You LOSE")
                is_running = False

        elif attempt == "scissor":
            print(f"Your opponent has {opponent}")
            attempts += 1
            if opponent == opponent[0]:
                print("You LOSE")
                is_running = False
            elif opponent == opponent[1]:
                print("You WIN!")
                is_running = False
            elif opponent == opponent[2]:
                print("Try Again!")
        else:
            print("Invalid option!")
            print(f"Please select between rock, paper, and scissor!")

    else:
        print("Invalid option!")
        print(f"Please select between rock, paper, and scissor!")


#WRONG METHOD! BUT NICE TRY THO