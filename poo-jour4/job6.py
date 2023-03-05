class Vehicule:
    def __init__(self, marque, modele,annee, prix, portes):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
        self.portes = portes
        
    
    def informationsVehicule(self):
        print("Marque =", self.marque)
        print("Modèle =", self.modele)
        print("Année =", self.annee)
        print("Prix =", self.prix)
    
    def demarrer(self):
        print("Attention, je roule.")


class Voiture(Vehicule):
    def __init__(self, marque, modele,annee, prix,portes):
        super().__init__(marque, modele, annee, prix,portes)
        self.modele = modele
        self.portes = 4
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes =", self.portes)
    
    def demarrer(self):
        print("Je démarre ma voiture.")

ma_voiture = Voiture("Mercedes", "Classe A", 2020, 18500, 4)
ma_voiture.informationsVehicule()
ma_voiture.demarrer()


print("                                             ")
print("                                             ")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue):
        super().__init__(marque, modele, annee, prix, roue)
        self.roue = 2
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues =", self.roue)

    def demarrer(self):
        print("Je démarre ma moto.")

ma_moto = Moto("Yamaha", "1200 Vmax", 1978, 4500, 2)
ma_moto.informationsVehicule()
ma_moto.demarrer()


