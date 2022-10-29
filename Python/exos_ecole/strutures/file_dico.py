# Auteur : Neil Bel Hadj
# Date 29/10/2022


LEN_FILE = 10

def creer_file():
    return {
        "tableau": ['_'] * LEN_FILE,
        "position_tete": 0,
        "nombre_elements": 0
    }

def est_vide_file(file):
    return file["nombre_elements"] == 0

def premier_file(file):
    assert( est_vide_file(file) == False )
    return file["tableau"][ file["position_tete"] ]
    
def ajouter_file(element, file):
    assert( file["nombre_elements"] < LEN_FILE )
    indice = (file["position_tete"] + file["nombre_elements"]) % LEN_FILE
    file["tableau"][indice] = element
    file["nombre_elements"] += 1
    return file

def retirer_file(file):
    assert( est_vide_file(file) == False )
    file["position_tete"] = (file["position_tete"] + 1) % LEN_FILE
    file["nombre_elements"] -= 1
    return file

A = creer_file()

ajouter_file("Neil", A)
ajouter_file("Naruto", A)
ajouter_file("Sangoku", A)
ajouter_file("Noa", A)

print(A)

while( est_vide_file(A) == False ):
    print("C'est le tour de : ", premier_file(A))
    retirer_file(A)


