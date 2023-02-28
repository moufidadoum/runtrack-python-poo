class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur


r = Rectangle(10, 5)
print("Longueur du rectangle :", r.get_longueur()) 
print("Largeur du rectangle :", r.get_largeur()) 

r.set_longueur(7)
r.set_largeur(3)
print("Nouvelle longueur du rectangle :", r.get_longueur())
print("Nouvelle largeur du rectangle :", r.get_largeur())
