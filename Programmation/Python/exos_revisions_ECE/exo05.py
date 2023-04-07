def max_dico(dico):
    lemeilleur = (None, -1)
    for prenom, score in dico.items():
        if score > lemeilleur[1]:
            lemeilleur = (prenom, score)
    return lemeilleur

#print(max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}))
#print(max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}))


def lppvdll(l):
    lppv = l[0]
    for i in range(1, len(l)):
        if l[i] < lppv:
            lppv = l[i]
    return lppv

def lppvidll(l):
    lppv = l[0]
    ilppv = 0
    for i in range(1, len(l)):
        if l[i] < lppv:
            lppv = l[i]
            ilppv = i
    return (lppv, ilppv)

print(lppvidll([3, 5, 1, 2, 11, 7, 18, 0]))