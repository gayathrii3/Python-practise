# Print prime numbers from 1 to N (has only 2 factors)

n = int(input())

for i in range(1,n+1):
    if i > 1:
        count = 0

        for p in range(1,i+1):
            if i % p == 0:
                count+=1
        if count == 2:
            print(p,end=" ")
