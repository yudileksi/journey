# Rock Paper Scissor Game

import random

options = ("rock", "paper", "scissor")
running = True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter your choice (rock, paper, scissor): ").lower()

    print(f'Player : {player}')
    print(f'Computer : {computer}')

    if player == computer:
        print("It's a TIE!")
    elif player == "rock" and computer == "scissor":
        print("You WIN!")
    elif player == "paper" and computer == "rock":
        print("You WIN!")
    elif player == "scissor" and computer == "paper":
        print("You WIN!")
    else:
        print("You LOSE!")

    if not input("Play Again (y/n): ").lower() == "y":
        running = False


print("Thanks for playing!")

