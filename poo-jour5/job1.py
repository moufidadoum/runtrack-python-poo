def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)

n = int(input("Entrez un nombre entier : "))

resultat = factorielle(n)

print("La factorielle de", n, "est", resultat)
