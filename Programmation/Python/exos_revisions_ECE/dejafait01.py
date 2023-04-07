def recherche(tab,n):
    res = len(tab)
    for i in range (0, len(tab)):
        if tab[i] ==n:
            res = i 
    return res


#print (recherche([5,3],1))
#print (recherche([2,4],2))
#print (recherche([2,3,5,2,4],2))




t=[4, 2, 1, 7, 9, 3]

i=1
longueur=len(t)
while(i < longueur):
    print("t[", i, "] =", t[i])
    i += 2


