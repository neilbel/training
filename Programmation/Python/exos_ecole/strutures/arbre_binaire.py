# structure pour un arbre binaire en python3
# Auteur : Neil Bel Hadj
# Date : 30/10/2022

class Noeud:
    def __init__(self, valeur, enfant_gauche = None, enfant_droite = None):
        self.enfant_gauche = enfant_gauche
        self.valeur = valeur
        self.enfant_droite = enfant_droite
    def hauteur(self):
        h_g = 0 if(self.enfant_gauche == None) else self.enfant_gauche.hauteur()
        h_d = 0 if(self.enfant_droite == None) else self.enfant_droite.hauteur()
        return 1 + max(h_g, h_d)
    def taille(self):
        t_g = 0 if(self.enfant_gauche == None) else self.enfant_gauche.taille()
        t_d = 0 if(self.enfant_droite == None) else self.enfant_droite.taille()
        return 1 + t_g + t_d
    def __repr__(self):
        return f"{self.valeur}({str(self.enfant_gauche)}, {str(self.enfant_droite)})"

G  = Noeud("G", Noeud("Gg"))
D  = Noeud("D", Noeud("Dg"), Noeud("Dd"))
A  = Noeud("A", G, D)
print("L'arbre :", A)
print("Sa hauteur :", A.hauteur())
print("Sa taille :", A.taille())

