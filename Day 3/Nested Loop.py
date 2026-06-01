

rows = int(input("Enter the amount of rows: "))
columns = int(input("Enter the amount of columns: "))
symbol = input("Enter the symbol: ")

for x in range(rows):
    for y in range(0, columns):
        print(symbol, end=" ")
    print()