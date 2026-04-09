# Sum of Digits

num = int(input())
sum = 0

while num > 0:
    last_digit = num % 10
    sum += last_digit
    num = num // 10
print(sum)

