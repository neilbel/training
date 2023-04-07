def multiplication_old(n1, n2):
    res=0
    if n2 < 0:
        n = -n2
    else:
        n = n2
    for i in range (0,n):
        res += n1
    if n2 < 0:
        return -res
    return res

def multiplication(n1, n2):
    res = 0
    if n2 < 0:
        for i in range (0,-n2):
            res -= n1
    else:
        for i in range (0,n2):
            res += n1
    return res

print(multiplication(3,5))
print(multiplication(-4,-8))
print(multiplication(-2,6))
print(multiplication(-2,0))
print(multiplication(3,-5))

