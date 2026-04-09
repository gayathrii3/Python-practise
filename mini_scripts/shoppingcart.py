items = []
prices = []
total = 0

while True:
    item = input("Enter your items(q to quit):")
    if item.lower() == "q":
        break
    else:
        price = float(input(f"Enter your price of {item}:$"))
        items.append(item)
        prices.append(price)
    
print("----------YOUR CART--------")
for item in items:
    print(f"{item} {price}")
for price in prices:
    total += price

print(f"your total is ${total:.2f}")
        
    