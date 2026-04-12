# Print prime numbers from 1 to N

n = int(input())

for i in range(1,n+1,1):
    if n % i != 0:
        print(i,end=" ")
