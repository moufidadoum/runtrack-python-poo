import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        
    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
        
    def aire(self):
        return math.pi * (self.radius ** 2)

mon_rectangle = Rectangle(5, 10)
print(mon_rectangle.aire())

mon_cercle = Cercle(4)
print(mon_cercle.aire())  
