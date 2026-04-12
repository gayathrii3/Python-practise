# Check perfect number  (Sum of its proper factors = the number itself)

n = int(input())

if n <= 0:                             # zero is not a perfect number
    print("Invalid input")
else:
    original = n
    sum_digits = 0

    for i in range(1,n):
        if n % i == 0:
            sum_digits += i
        
    if sum_digits == original:
        print(f"{original} is a perfect number")
    else:
        print(f"{original} is not a perfect number")