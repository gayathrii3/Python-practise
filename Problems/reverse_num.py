# Reverse a Number

n = int(input())
rev_num = 0

while n > 0:
    last_digit = n % 10
    rev_num = rev_num * 10 + last_digit
    n = n // 10
print(rev_num)


# 1234---->  rev_num = 4
            #  0 * 10 + 4 = 4
            #  4 * 10 + 3 = 4 3
            #  43 * 10 + 2 = 4 3 2
            #  432 * 10 + 1 = 4 3 2 1