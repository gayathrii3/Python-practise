# Find largest digit in a number

num = int(input())

if num == 0:
    print(0)
if num < 0:
    num = -num
    print(f"{num} is negative")
else:
    largest = num % 10
    num //= 10

    while num > 0:
        digit = num % 10
        if digit > largest:
            largest = digit
        num //= 10
    
    print(largest)
