# Find Smallest Digit in a Number 1234

num = int(input())

if num == 0:
    print(0)

if num < 0:
    num = -num
else:
    smallest = num % 10
    num //= 10

    while num > 0:
        digit = num % 10

        if digit < smallest:
            smallest = digit

        num //= 10

    print(smallest)