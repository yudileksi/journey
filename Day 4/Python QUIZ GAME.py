# Python QUIZ GAME

questions = (("1. When the hell is your birthday date??"),
             ("2. What is Miki name?"),
             ("3. How many is your eyes?"),
             ("4. Are you stuppid?"))

options = (("A. 7", "B. 14", "C. 21", "D. 28"),
           ("A. Miki", "B. Micky", "C. Mikcy", "D. Mikey"),
           ("A. 0", "B. 1", "C. 2", "D. 3"),
           ("A. Yes", "B. No", "C. Maybe", "D. Can't tell"))

answers = ("B", "A", "C", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter answer (A, B, C, D) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print()
print("FINAL SCORE")

print(f"Guesses : ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print(f"Answers : ", end="")
for answer in answers:
    print(answer, end=" ")
print()

score = int(score / len(questions) * 100)
print(f'Your score is : {score}')