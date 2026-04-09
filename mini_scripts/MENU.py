

menu = {"chilli chicken":299,
        "paneer grill":199,
        "tandoori chicken":459,
        "chicken fry":249,
        "Butter naan":75,
        "Fried rice":99,
        "chicken Pasta":159,
        "Manchuria":120}

order = []
price = 0
total = 0

print("----------------------MENU----------------------------")
for key,value in menu.items():
    print(f"{key:18} = \u20B9{value}")
    
    
while True:
    food = input("Enter your food (q to quit):")
    if food.lower() == "q":
        break
    else:
        order.append(food)

print("--------------------YOUR ORDER------------------------")

for food in order:
    print(f"{food:18} = \u20B9{menu.get(food)}")
    total += menu.get(food)
    
print("------------------------BILL--------------------------")

print(f"Total = \u20B9{total}")
print("Thank you!! for visiting")

    
