# Exemple de création de classe
# Auteur : Neil Bel Hadj (tiré du support de cours CNED mais modifié)
# Date 28/10/2022

# D'abord définir la classe
class Point2D:
    """Un point dans l'espace 2D orthonormé"""
    # Constructeur de l'objet (x, y) et color optionnelle en 32bits RGBA
    def __init__(self, x, y, color = 0x0):
        self.x = x
        self.y = y
        self.color = color

    # Méthode pour déplacer le point
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
    
    # Méthode spéciale pour afficher l'objet dans la console python
    def __repr__(self):
        return f"({self.x}, {self.y}) with color {self.color}"

    # Méthode pour rotation de 180° par rapport au centre du repère
    def rotate180(self):
        self.x = -self.x
        self.y = -self.y
        
