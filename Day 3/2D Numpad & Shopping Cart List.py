
print(">2D NUM PAD DESIGN<")
keypad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ["*", 0, "#"]]

for key in keypad:
    for element in key:
        print(element, end=" ")
    print()

print()

# Shopping Cart List

print(">Now is shopping cart list design<")
foods = []
prices = []
total = 0

while True:
    food = (input('Enter your food (q to quit): '))
    if food.lower() == 'q':
        break
    else:
        price = float(input(f'Enter the price of {food} : $'))
        foods.append(food)
        prices.append(price)


print("-----YOUR CART-----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f'Your Charge is : ${total}')
