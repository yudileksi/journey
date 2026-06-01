# Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Enter your unit (kg/lb): ")

if unit == "kg":
    weight = weight * 2.205
    unit = 'lbs'
    print(f"Your weight is {round(weight, 2)} {unit}")
elif unit == "lb":
    weight = weight / 2.205
    unit = 'kgs'
    print(f"Your weight is {round(weight, 2)} {unit}")
else:
    print(f'{unit} is NOT a valid unit')