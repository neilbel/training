from random import *
def lancer (n):
    l= []
    for i in range(n):
        l.append (randint(1,6))
    return l


#print(lancer(5))



def paire_6(tab):
    compteur= 0
    for nombre in tab:
        if nombre==6:
            compteur +=1
            if compteur == 2:
                return True
    return False

#print(paire_6([2, 4, 6, 1, 6]))
#print(paire_6([2, 4, 6, 1, 5]))
#print(paire_6([6, 6, 6, 6, 6]))

for i in range(20):
    lst = lancer(20)
    print(lst)
    print(paire_6(lst))
