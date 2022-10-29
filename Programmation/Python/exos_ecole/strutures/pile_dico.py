# Bibliothèque de gestion de pile (dans un dictionnaire)
# Auteur : Neil Bel Hadj
# Date 29/10/2022

# nombre maximal d'éléments dans la pile
LEN_PILE = 10

def creer_pile():
    return {
        "tableau": ['_'] * LEN_PILE,
        "sommet": -1
    }

def est_vide_pile(pile):
    return pile["sommet"] == -1

def sommet_pile(pile):
    assert( est_vide_pile(pile) == False )
    return pile["tableau"][ pile["sommet"] ]

def empiler(element, pile):
    assert( pile["sommet"] < LEN_PILE - 1 )
    pile["sommet"] += 1
    pile["tableau"][ pile["sommet"] ] = element
    return pile

def depiler(pile):
    assert( est_vide_pile(pile) == False )
    pile["sommet"] -= 1
    return pile

assiettes = creer_pile()

empiler("assiette de Papa ours", assiettes)
empiler("assiette de Maman ours", assiettes)
empiler("assiette de Emmanuel Macron", assiettes)
empiler("assiette de Petit frère ours", assiettes)

print(assiettes)

while( est_vide_pile(assiettes) == False ):
    print("Je pose l'", sommet_pile(assiettes), sep="")
    depiler(assiettes)


