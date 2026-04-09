# Count Even and Odd Digits

num = int(input())
even = 0
odd = 0

while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
    num //= 10                      #remember to remove the current digit (increases count)
print(f"even : {even},odd : {odd}")
