def nbpair(liste):
    compteur = 0
    for value in liste:
        if value % 2 == 0:
            compteur +=1
    return compteur

print (nbpair([1,2,3,1,7,4,10]))

def lpair(liste):
    lp= []
    for value in liste:
        if value % 2 == 0:
            lp.append(value)
    return lp

print (lpair([1,2,3,1,7,4,10]))
#[2, 4, 10]
print (lpair([1,5,3,1,7,11,-0]))
#[]
