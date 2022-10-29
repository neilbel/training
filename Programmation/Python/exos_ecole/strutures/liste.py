# Bibliothèque de gestion de listes abstraites (comme dans Lisp)
# Auteur : Neil Bel Hadj (à partir du support de cours CNED)
# Date 29/10/2022

def creer_liste():
    return None

def ajouter_en_tete(x, L):
    return (x, L)

def queue(L):
    return L[1]

def tete(L):
    return L[0]

def est_vide(L):
    return L == None

def nombre_elements(L):
    if(est_vide(L)):
        return 0
    return 1 + nombre_elements( queue(L) )

def val(i, L):
    assert( est_vide(L) == False )
    if(i == 0):
        return tete(L)
    return val(i - 1, queue(L))

def est_dans(x, L):
    if(est_vide(L)):
        return False
    else:
        if(x == tete(L)):
            return True
        else:
            return est_dans(x, queue(L))

maListe = creer_liste()

maListe = ajouter_en_tete(42, maListe)
print(maListe)

maListe = queue(maListe)
print(maListe)
print(est_vide(maListe))

maListe = ajouter_en_tete(42, maListe)
maListe = ajouter_en_tete(7, maListe)
maListe = ajouter_en_tete(6, maListe)
maListe = ajouter_en_tete(3, maListe)
maListe = ajouter_en_tete(2, maListe)
maListe = ajouter_en_tete(1, maListe)

print("Toute la liste :", maListe)
print("Nombre d'éléments", nombre_elements(maListe))

#print("Au 6ème rang, j'ai :", val(6, maListe)) # assert error
print("Au 5ème rang, j'ai :", val(5, maListe))
print("9 est dans la liste ?", est_dans(9, maListe))
print("7 est dans la liste ?", est_dans(7, maListe))
