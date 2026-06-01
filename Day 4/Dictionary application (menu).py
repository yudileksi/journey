# Concession stand program

menu = {"pisang" : 4.5,
        "tahu" : 3.2,
        "kentang" : 4,
        "pizza" : 10.5,
        "ayam" : 6.2,
        "bengkoang" : 9.6}
cart = []
total = 0

print("--------MENU--------")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("--------------------")

while True:
    food = (input("Which food do you order (q to finish order) : ")).lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------YOUR CART------")
for food in cart:
    total += menu.get(food)
    print (food, end=" ")

print()
print(f'Your charge is : ${total:.2f}')