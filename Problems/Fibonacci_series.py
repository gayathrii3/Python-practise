# Fibonacci Series up to N Terms (Each next term is sum of previous two)

n = int(input())

a = 0
b = 1

for i in range(n):
    print(a,end=" ")         #a is always the number we want to print
    c = a + b
    a = b
    b = c



