class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print("J'ai", self.age, "ans")
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, age):
        self.age = age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def affichageAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        super().__init__()
        self.__matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("Le cours va commencer")

# Instanciation de Personne, Eleve et Professeur
p1 = Personne()
e1 = Eleve()
prof1 = Professeur("Maths")

# Affichage de l'age par défaut de l'élève
e1.affichageAge() # Output : "J'ai 14 ans"

# Appel de la méthode allerEnCours de l'élève
e1.allerEnCours() # Output : "Je vais en cours"

# Appel de la méthode enseigner du professeur
prof1.enseigner() # Output : "Le cours va commencer"
