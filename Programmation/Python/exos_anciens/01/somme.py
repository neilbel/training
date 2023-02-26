"""                                                                                                                                                               
Neil Bel Hadj                                                                                                                                                     
plusieurs façons de calculer la somme des n premiers entiers positifs                                                                                             
"""

# récursive                                                                                                                                                       
def sr(n):
    if n <= 0:
        return 0
    else:
        return sr(n-1) + n

# itérative                                                                                                                                                       
def si(n):
    somme= 0
    for i in range (0, n+1):
        somme = somme + i
    return somme

# formule (Gauss)                                                                                                                                                 
def sg(n):
    return (n*(n+1))//2

# tester sg par rapport à la forme itérative                                                                                                                      
def test_sg(n):
    for i in range (0, n+1):
        if sg(i) != si(i):
            print ("le test unitaire de sg a échoué")
            return
    print ("test unitaire de sg a réussi")
