# coding: utf-8
# Tests de récursivité python3
# Neil Bel Hadj

# fonction fibonacci
def fib(n):
    """ fibonacci en double récursivité simple """
    if(n < 2):
        return 1
    return fib(n - 1) + fib(n - 2)

# ça rame très rapidement
for i in range(2, 43):
    print(f"fib({i}) =", fib(i))

# fonction factorielle
def fact(n):
    """ factorielle en récursivité simple """
    if(n < 2):
        return 1
    return n * fact(n - 1)

# la factorielle va vite
# la pile fait une erreur vers 998
for i in range(2, 2005):
    print("fact(", i, ") = ", fact(i))

