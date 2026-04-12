# Find Whether a Number is Armstrong(sum of power(no.of digits) == number)

n = int(input())

if n < 0:
    print("Invalid input")

else:
    original = n
    sum_digit = 0
    
    if n == 0:
        print("Armstrong")

    else:
        digits = len(str(n))

    while n > 0:
        digit = n % 10
        sum_digit += digit ** digits
        n //= 10
    
    print("Armstrong" if sum_digit == original else "Not Armstrong")

    