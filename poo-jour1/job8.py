from math import *

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon
        
    def afficherInfos(self):
        print("Rayon :", self.rayon)
        print("Circonférence :", self.circonference())
        print("Diamètre :", self.diametre())
        print("Aire :", self.aire())
        
    def circonference(self):
        return 2 * self.rayon * 3.14159265359
    
    def diametre(self):
        return 2 * self.rayon
    
    def aire(self):
        return self.rayon * self.rayon * 3.14159265359

# création des cercles
cercle1 = Cercle(8)
cercle2 = Cercle(3)

# affichage des informations des cercles
cercle1.afficherInfos()
cercle2.afficherInfos()

# calcul de la circonférence, du diamètre et de l'aire des cercles
print("Circonférence cercle1 :", cercle1.circonference())
print("Diamètre cercle1 :", cercle1.diametre())
print("Aire cercle1 :", cercle1.aire())
print("Circonférence cercle2 :", cercle2.circonference())
print("Diamètre cercle2 :", cercle2.diametre())
print("Aire cercle2 :", cercle2.aire())
