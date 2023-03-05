def power(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return power(x * x, n // 2)
    else:
        return x * power(x * x, (n - 1) // 2)

x = int(input("Entrez un nombre entier x : "))
n = int(input("Entrez un nombre entier n : "))

resultat = power(x, n)

print(f"{x}^{n} = {resultat}")
