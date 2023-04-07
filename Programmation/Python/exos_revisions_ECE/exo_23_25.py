# Exercice 1

def enumere(liste):
    d = {}
    for i in range(len(liste)):
        if liste[i] in d:
            d[liste[i]].append (i)
        else:
            d[liste[i]]=[i]
            
    return d

print(enumere([1, 1, 2, 3, 2, 1]))

# Exercice 2

class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def parcours(arbre, liste):
    if arbre != None:
        parcours(arbre.fg, liste)
        liste.append(arbre.v)
        parcours(arbre.fd, liste)
    return liste

def insere(arbre, cle):
    """ arbre est une instance de la classe Arbre qui implémente
        un arbre binaire de recherche.
    """
    if cle < arbre.v:
        if arbre.fg != None:
            insere(arbre.fg, cle)
        else:
            arbre.fg = Arbre(cle)
    else:
        if arbre.fd != None:
            insere(arbre.fd, cle)
        else:
            arbre.fd = Arbre(cle)

def tester():
    A = Arbre(5)
    insere (A, 2)
    insere (A, 3)
    insere (A, 7)
    insere (A, 1)
    insere (A, 4)
    insere (A, 6)
    insere (A, 8)
    l = []
    return parcours (A,l)
