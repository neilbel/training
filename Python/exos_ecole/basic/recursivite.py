def fact(n):
    if(n < 2):
        return 1
    return n * fact(n - 1)

#print(fact(5))

def fib(n):
    if(n < 2):
        return 1
    return fib(n - 1) + fib(n - 2)

for i in range(2, 101):
    print("fib(", i, ") = ", fib(i))

