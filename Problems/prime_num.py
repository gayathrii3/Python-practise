# Check Prime Number(divisible by one and itself, contains only 2 factors)

n = int(input())

for i in range(2,int(n ** 0.5)+1):
    if n % i == 0:
        print(f"{n} is not prime")
        break
else:
    print(f"{n} is prime")
