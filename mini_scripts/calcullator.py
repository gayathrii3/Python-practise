operator = input("Enter an operator(+ - / * %) :")
num1 = float(input("Enter number :"))
num2 = float(input("Enter number :"))

if operator == '+':
    print("Answer =",num1 + num2)
elif operator == '-':
    print("Answer =",num1 - num2)
elif operator == '*':
    print("Answer =",num1 * num2)
elif operator == '/':
    print("Answer =",num1 / num2)
elif operator == '%':
    print("Answer =",num1 % num2)
else:
    print("syntax error")