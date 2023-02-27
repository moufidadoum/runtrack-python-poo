class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def SePresenter(self):
        return f"Je m'suis {self.prenom} {self.nom}"

personne1 = Personne("John", "Doe")
personne2 = Personne("Jean", "Dupond")

print(personne1.SePresenter())
print(personne2.SePresenter())
