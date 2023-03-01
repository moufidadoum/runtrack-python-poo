class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0
    
    def marquerUnBut(self):
        self.buts_marques += 1
    
    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
    
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
    
    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
    
    def afficherStatistiques(self):
        print("Statistiques de", self.nom)
        print("Numéro:", self.numero)
        print("Position:", self.position)
        print("Buts marqués:", self.buts_marques)
        print("Passes décisives:", self.passes_decisives)
        print("Cartons jaunes reçus:", self.cartons_jaunes)
        print("Cartons rouges reçus:", self.cartons_rouges)
        print()

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []
    
    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)
    
    def afficherStatistiquesJoueurs(self):
        print("Statistiques des joueurs de", self.nom)
        for joueur in self.joueurs:
            joueur.afficherStatistiques()
    
    def mettreAJourStatistiquesJoueur(self, nom, buts=0, passes=0, jaunes=0, rouges=0):
        for joueur in self.joueurs:
            if joueur.nom == nom:
                joueur.buts_marques += buts
                joueur.passes_decisives += passes
                joueur.cartons_jaunes += jaunes
                joueur.cartons_rouges += rouges
                break
    
    def afficherJoueurs(self):
        print("Joueurs de", self.nom)
        for joueur in self.joueurs:
            print(joueur.nom, "- Numéro", joueur.numero, "- Position", joueur.position)
        print()

# Création des joueurs
joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Neymar", 10, "Attaquant")
joueur4 = Joueur("Modric", 10, "Milieu")
joueur5 = Joueur("Pogba", 6, "Milieu")
joueur6 = Joueur("Varane", 4, "Défenseur")

# Création des équipes
equipe1 = Equipe("FC Barcelone")
equipe2 = Equipe("Real Madrid")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur3)
equipe1.ajouterJoueur(joueur6)

equipe2.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur4)
equipe2.ajouterJoueur(joueur5)

# Affichage des joueurs de chaque équipe
equipe1.afficherJoueurs()
equipe2.afficherJoueurs()

# Simulation d'un match
joueur1.marquerUnBut()
joueur1.effectuerUnePasseDecisive()
joueur2.recevoirUnCartonJaune()
joueur3.recevoirUnCartonJaune()
joueur5.recevoirUnCartonRouge()

# Mise à jour des statistiques des joueurs
equipe1.mettreAJourStatistiquesJoueur("Messi", buts=1, passes=1)
equipe2.mettreAJourStatistiquesJoueur("Ronaldo", jaunes=1)
equipe1.mettreAJourStatistiquesJoueur("Neymar", jaunes=1)
equipe2.mettreAJourStatistiquesJoueur("Pogba", rouges=1)

# Affichage des statistiques de tous les joueurs des deux équipes
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
