class Ville:
    def __init__(self, nom, nb_habitants):
        self.nom = nom
        self.nb_habitants = nb_habitants

    def ajouterPopulation(self, nb_personnes):
        self.nb_habitants += nb_personnes

class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville
        self.ville.ajouterPopulation(1)  # Ajouter cette personne à la population de la ville

# Créer un objet “Ville” avec comme arguments “Paris” et 1000000.
ville_paris = Ville("Paris", 1000000)

# Créer un autre objet “Ville” avec comme arguments “Marseille” et 861635.
ville_marseille = Ville("Marseille", 861635)

# Création des objets Personnes
John = Personne("John", 45, ville_paris)
Myrtille = Personne("Myrtille", 4, ville_paris)
Chloe = Personne("Chloé", 18, ville_marseille)
# Ajouter une nouvelle personne à Paris
Michael = Personne("Michael", 21, ville_paris)

# Afficher le nombre d’habitants de Paris et de Marseille après l’arrivée de ces nouvelles personnes.
print("Population de la ville de Paris :", ville_paris.nb_habitants, "habitants")
print("Population de la ville de Marseille :", ville_marseille.nb_habitants, "habitants")


# Afficher le nombre d’habitants de Paris et de Marseille après l’arrivée de nouvelles personnes.
print("Mise à jour de la population de la ville de Paris :", ville_paris.nb_habitants, "habitants")
print("Mise à jour de la population de la ville de Marseille :", ville_marseille.nb_habitants, "habitants")
