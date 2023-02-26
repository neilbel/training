"""                                                                                                                                                               
Neil Bel Hadj                                                                                                                                                     
Suite de Fibonacci récursive et itérative                                                                                                                         
"""

# fibonacci récursive                                                                                                                                             
# bien (élégante) mais très gourmande                                                                                                                             
# def fibo(n):                                                                                                                                                    
#     if n < 2:                                                                                                                                                   
#         return 1                                                                                                                                                
#     else:                                                                                                                                                       
#         return fibo(n - 1) + fibo(n - 2)                                                                                                                        

# fibonacci itérative                                                                                                                                             
# utilise c : courant, p : précédent et pp : précédent de précédent                                                                                               
def fibo(n):
    if n < 2:
        return 1
    if n == 2:
        return 2
    p = 1
    c = 2
    for i in range(3, n + 1):
        pp = p
        p = c
        c = pp + p
    return c

print(fibo(10000))
