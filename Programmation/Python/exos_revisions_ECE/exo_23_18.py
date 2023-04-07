"""exercice 1"""
def max_et_indice_fb(tab):
    """
    Cette fonction prend en paramètre une liste non vide tab de
    nombres entiers et qui renvoie la valeur du plus grand élément
    de cette liste ainsi que l’indice de sa première apparition dans
    cette liste.
    """
    assert len(tab) > 0
    pg = (tab[0], 0) #provisoirement la plus grande valeur et son indice
    for i in range (1, len(tab)):
        if tab[i] > pg[0]:
            pg = (tab[i], i)
    return pg

def max_et_indice(tab):
    """
    Cette fonction prend en paramètre une liste non vide tab de
    nombres entiers et qui renvoie la valeur du plus grand élément
    de cette liste ainsi que l’indice de sa première apparition dans
    cette liste.
    """
    assert len(tab) > 0
    lpgv = tab[0] #provisoirement la pluq grande valeur trouvée
    ilpgv = 0 #provisoirement l'indice de cette derniere
    for i in range (1, len(tab)):
        if tab[i] > lpgv:
            lpgv = tab[i]
            ilpgv = i
    return (lpgv,ilpgv)




""" exercice 2 """

def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les entiers
    de 1 à  n, False sinon
    '''
    for i in range(1, len(tab) + 1):
        if not (i in tab):
            return False
    return True


def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de points de rupture de ordre qui représente un ordre
    de gènes de chromosome
    '''
    assert est_un_ordre(ordre)# ordre n'est pas un ordre de gènes
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1
        nb = nb + 1
    i = 0
    while i < n-1:
        if ordre[i]- ordre[i+1] not in [-1, 1]: # l'ecart n'est pas 1
            nb = nb + 1
        i = i + 1
    if ordre[n-1] != n: # le dernier n'est pas n
        nb = nb + 1
    return nb
