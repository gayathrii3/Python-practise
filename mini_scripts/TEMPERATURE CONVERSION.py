unit = input("Enter unit(C or F) :")
temperature = float(input("Enter temperature :"))

if unit == 'C':
    temperature = (9 * temperature)/  5 + 32 #(CELSIUS TO FAHREN) 
    print(f"The temperature in Fahrenheit is {temperature}F")
    unit 
elif unit == 'F':
    temperature = (temperature - 32)*5/9
    print(f"The temperture in Celsius is {temperature}C")
else:
    print(f"{unit} is invalid")