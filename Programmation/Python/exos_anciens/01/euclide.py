"""
Neil Bel Hadj

Algorithme du pgcd d'Euclide
Source : https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide
"""

# version itérative d'origine
def pgcdi(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# version récursive
def pgcdr (a,b):
    if b == 0:
        return a
    else:
        return pgcdr(b, a % b)
    
        

def test_pgcd():
    print(pgcdi(81,54)) # doit retourner 27
    print(pgcdi(1365,343)) # doit retourner 7
    print(pgcdr(81,54)) # doit retourner 27
    print(pgcdr(1365,343)) # doit retourner 7

test_pgcd()
