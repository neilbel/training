# Bibliothèque de gestion de file
# Auteur : Neil Bel Hadj (depuis exos de support de cours CNED)
# Date 29/10/2022


LEN_FILE = 10

def creer_file():
    return {
        "tableau": ['_'] * LEN_FILE,
        "position_tete": 0,
        "nombre_elements": 0
    }

def est_vide_file(maFile):
    return maFile["nombre_elements"] == 0

def premier_file(maFile):
    assert( est_vide_file(maFile) == False )
    return maFile["tableau"][ maFile["position_tete"] ]
    
def ajouter_file(element, maFile):
    assert( maFile["nombre_elements"] < LEN_FILE )
    indice = (maFile["position_tete"] + maFile["nombre_elements"]) % LEN_FILE
    maFile["tableau"][indice] = element
    maFile["nombre_elements"] += 1
    return maFile

def retirer_file(maFile):
    assert( est_vide_file(maFile) == False )
    maFile["position_tete"] = (maFile["position_tete"] + 1) % LEN_FILE
    maFile["nombre_elements"] -= 1
    return maFile


# je créé ma file et j'y mets quelques éléments
A = creer_file()
ajouter_file("Neil", A)
ajouter_file("Naruto", A)
ajouter_file("Sangoku", A)
ajouter_file("Noa", A)

print(A)

# test de défilement de la file
while( est_vide_file(A) == False ):
    print("C'est le tour de : ", premier_file(A))
    retirer_file(A)


