import random

#print(help(random))


lowest_num = 1
highest_num = 100
guesses = 0
is_running = True

answer = random.randint(lowest_num, highest_num)

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess : ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess > highest_num or guess < lowest_num :
            print("Invalid guess!")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("The answer is higher")
        elif guess > answer:
            print("The answer is lower")
        else:
             print("Your guess is is right!!")
             print(f"The answer is {answer}")
             print(f"Number of guesses: {answer}")
             is_running = False

    else:
        print("Invalid guess!")
        print(f"Please select a number between {lowest_num} and {highest_num}")

print("----------------")
print(guesses)