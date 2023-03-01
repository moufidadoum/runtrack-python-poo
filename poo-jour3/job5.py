import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, ennemi):
        points_degats = random.randint(1, 10)
        ennemi.vie -= points_degats
        print(f"{self.nom} attaque {ennemi.nom} et lui inflige {points_degats} points de dégâts !")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez un niveau de difficulté entre 1 et 3 : "))

    def lancerJeu(self):
        self.choisirNiveau()
        joueur = Personnage("Joueur", self.niveau * 50)
        ennemi = Personnage("Ennemi", self.niveau * 50)

        while joueur.vie > 0 and ennemi.vie > 0:
            print(f"{'=' * 20} Combat ! {'=' * 20}")
            print(f"{joueur.nom} : {'#' * joueur.vie}{'-' * (20 - joueur.vie)} [{joueur.vie}]")
            print(f"{ennemi.nom} : {'#' * ennemi.vie}{'-' * (20 - ennemi.vie)} [{ennemi.vie}]")
            print("=" * 50)

            print("Que voulez-vous faire ?")
            print("1. Attaquer")
            print("2. Ne rien faire")
            choix = input("Votre choix : ")
            if choix == "1":
                joueur.attaquer(ennemi)
            else:
                print(f"{joueur.nom} décide de ne rien faire.")
            
            if ennemi.vie <= 0:
                print(f"{joueur.nom} a vaincu {ennemi.nom} !")
            else:
                ennemi.attaquer(joueur)
                if joueur.vie <= 0:
                    print(f"{ennemi.nom} a vaincu {joueur.nom} !")

        print("=" * 45)
        print(f"{joueur.nom} : {'#' * joueur.vie}{'-' * (20 - joueur.vie)} [{joueur.vie}]")
        print(f"{ennemi.nom} : {'#' * ennemi.vie}{'-' * (20 - ennemi.vie)} [{ennemi.vie}]")
        print("=" * 45)


jeu = Jeu()
jeu.lancerJeu()
