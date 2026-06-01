# Temperature Converter

unit = input("Enter the temperature unit (C/F) : ")
temp = float(input("Enter the temperature : "))

if unit.lower() == "C":
    temp = round((temp * 9/5) + 32, 1)
    unit = 'F'
    print(f'The temperature is {temp} {unit}')
elif unit.lower() == "F":
    temp = round((temp - 32) * 5/9, 1)
    unit = "C"
    print(f'The temperature is {temp} {unit}')
else:
    print(f'{unit} is NOT a valid unit')