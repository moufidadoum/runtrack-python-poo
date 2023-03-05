def plus_grand_chiffre(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        max_chiffre = plus_grand_chiffre(liste[1:])
        return liste[0] if liste[0] > max_chiffre else max_chiffre

liste = [12, 8, 8, 21, 5, 9, 36, 47, 16]

resultat = plus_grand_chiffre(liste)

print(f"Le plus grand chiffre de la liste {liste} est {resultat}.")
