class Personnage:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def bouger_haut(self):
        self.y -= 1
    
    def bouger_bas(self):
        self.y += 1
    
    def bouger_gauche(self):
        self.x -= 1
    
    def bouger_droite(self):
        self.x += 1

class Plateau:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.personnage = Personnage()
    
    def afficher(self):
        for y in range(self.hauteur):
            for x in range(self.largeur):
                if x == self.personnage.x and y == self.personnage.y:
                    print("P", end="")
                else:
                    print(".", end="")
            print()
    
    def jouer(self):
        while True:
            self.afficher()
            commande = input("Entrez une commande (haut, bas, gauche, droite) : ")
            if commande == "haut":
                self.personnage.bouger_haut()
            elif commande == "bas":
                self.personnage.bouger_bas()
            elif commande == "gauche":
                self.personnage.bouger_gauche()
            elif commande == "droite":
                self.personnage.bouger_droite()
            else:
                print("Commande invalide.")

plateau = Plateau(10, 5)
plateau.jouer()
