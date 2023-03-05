def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Entrez un entier positif : "))

for i in range(10):
    resultat = fibonacci(n+i)
    print(f"Le {n+i}-ème nombre de la suite de Fibonacci est {resultat}.")
