class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"

    def __str__(self):
        return f"{self.titre} ({self.statut}): {self.description}"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, tache):
        self.taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.statut = "terminé"

    def afficherListe(self):
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]


#---------------CREATION DES TACHES----------------------------------------------------------------#
tache1 = Tache("Finir ses projets", "Faire du python avec la runtrack poo")
tache2 = Tache("Faire du sport", "aller à la salle de sport")
tache3 = Tache("Lecture", "Finir mon livre")
listeDeTaches = ListeDeTaches() # Création de la liste de tâches

listeDeTaches.ajouterTache(tache1) # Ajout des tâches à la liste
listeDeTaches.ajouterTache(tache2)
listeDeTaches.ajouterTache(tache3)
#--------------------------------------------------------------------------------------------------#



#---------------AFFICHER LA LISTE DES TACHES-------------------------------------------------------#
print("#####################################################################")
print("Liste de tâches:")
listeDeTaches.afficherListe()
print("#####################################################################")
print("                                                                  ")
print("                                                                  ")
#--------------------------------------------------------------------------------------------------#



#---------------FILTRER ET NE GARDER QUE LES TACHES A FAIRE----------------------------------------#
# Filtrage de la liste pour ne garder que les tâches à faire
print("#####################################################################")
tachesAFaire = listeDeTaches.filterListe("à faire")
print("Tâches à faire:")
for tache in tachesAFaire:
    print(tache)
print("#####################################################################")
print("                                                                  ")
print("                                                                  ")
#--------------------------------------------------------------------------------------------------#


#---------------MARQUER UNE TACHE COMME TERMINEE----------------------------------------------------#
print("#####################################################################")
# Marquage d'une tâche comme terminée
listeDeTaches.marquerCommeFinie(tache1)

print("Liste de tâches mise à jour:") # Affichage de la liste de tâches mise à jour
listeDeTaches.afficherListe()
print("#####################################################################")
print("                                                                  ")
print("                                                                  ")
#--------------------------------------------------------------------------------------------------#


#---------------SUPPRIMER UN ELEMENT DE LA LISTE----------------------------------------------------#
print("#####################################################################")
listeDeTaches.supprimerTache(tache3) # Suppression de la tache 3 (lire un livre) de la liste comme exemple

print("Liste de tâches mise à jour:")
listeDeTaches.afficherListe()
print("#####################################################################")
#--------------------------------------------------------------------------------------------------#