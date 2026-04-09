weight = int(input("Enter your weight:"))
unit = input("Kilograms or Pounds? (K or L):")

if unit == 'K':
    weight = weight / 2.205
    unit = 'Kgs'
elif unit == 'L':
    weight = weight * 2.205
    unit = 'Lbs'
else:
    print(f"{weight} is not valid")
    
print(f"Your weight is {round(weight,1)} {unit}")
