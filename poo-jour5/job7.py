chaine1 = input("Entrez la première chaîne de caractères : ")
chaine2 = input("Entrez la deuxième chaîne de caractères : ")

# On enlève tous les astérisques de la chaîne 2
chaine2 = chaine2.replace('*', '')

if chaine2 in chaine1:
    print(1)
else:
    print(0)
