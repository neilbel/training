"""
Neil Bel Hadj

Plusieurs façons de rechercher l'indice d'un élément e dans un tableau t
"""

def index_of(e,t):
    for i in range (len(t)):
        if t[i] == e:
            return i
    return -1

def index_of_2(e,t):
    index = -1
    for i in range (len(t)):
        if t[i] == e:
            index = i
            break
    return index

def index_of_3(e,t):
    i = 0
    for x in t:
        if x == e:
            return i
        i += 1
    return -1


def index_of_r(e, t, i):
    if i >= len(t):
        return -1
    if t[i] == e:
        return i
    return index_of_r(e, t, i + 1)

def index_of_4(e,t):
    return index_of_r(e, t, 0)

def test():
    tab = [ 5, 32, 21, 9, 42, 18, 13, 7, 2, 4 ]
    # 1ère version
    print(index_of(42, tab)) # doit afficher 4
    print(index_of(13, tab)) # doit afficher 6
    print(index_of( 5, tab)) # doit afficher 0
    print(index_of( 1, tab)) # doit afficher -1 car n'y est pas
    # 2ème version
    print(index_of_2(42, tab)) # doit afficher 4
    print(index_of_2(13, tab)) # doit afficher 6
    print(index_of_2( 5, tab)) # doit afficher 0
    print(index_of_2( 1, tab)) # doit afficher -1 car n'y est pas
    # 3ème version
    print(index_of_3(42, tab)) # doit afficher 4
    print(index_of_3(13, tab)) # doit afficher 6
    print(index_of_3( 5, tab)) # doit afficher 0
    print(index_of_3( 1, tab)) # doit afficher -1 car n'y est pas
    # 4ème version (récursive)
    print(index_of_4(42, tab)) # doit afficher 4
    print(index_of_4(13, tab)) # doit afficher 6
    print(index_of_4( 5, tab)) # doit afficher 0
    print(index_of_4( 1, tab)) # doit afficher -1 car n'y est pas

test()
