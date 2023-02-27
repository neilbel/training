"""
Neil Bel Hadj
exo pour inverser l'ordre des éléments dans un tableau
une version qui modifie le tableau lui-même
l'autre créé un nouveau (inversé) et le renvoie
"""

def reverse(t):
    i=0
    j=len(t)-1
    while (i<j):
        tmp=t[i]
        t[i]=t[j]
        t[j]=tmp
        i+=1
        j-=1
    return t

def reverse2(t):
    rt=[]
    for x in t:
        rt.insert(0,x)
    return rt
        
def test():
    tab=[1,9,14,6,48,-12]
    print ("          tab :", tab)
    print (" reverse(tab) :", reverse(tab))
    print ("          tab :", tab)
    print ("reverse2(tab) :", reverse2(tab))
    print ("          tab :", tab)
    print ("j'appelle tab.reverse()")
    tab.reverse()
    print ("          tab :", tab)
    print ("j'appelle tab.sort()")
    tab.sort()
    print ("          tab :", tab)
    
test()


