# Count Digits in a Number

n = int(input())    #1234
count = 0

if n == 0:           #checks if the input is only 0
    print(1)
else:
    count = 0

    if n < 0:        #checks for negative integers
        n = -n
    else:
        while n > 0:
            count += 1
            n //= 10          #extracts the last digit
        print(count)


