def placer_reine(plateau, col, n):
    for ligne in range(n):
        if est_valide(plateau, ligne, col, n):
            plateau[ligne][col] = 'X'
            if col == n - 1:
                return True
            else:
                if placer_reine(plateau, col + 1, n):
                    return True
            plateau[ligne][col] = 'O'
    return False

def est_valide(plateau, ligne, col, n):
    for i in range(col):
        if plateau[ligne][i] == 'X':
            return False
    for i, j in zip(range(ligne, -1, -1), range(col, -1, -1)):
        if plateau[i][j] == 'X':
            return False
    for i, j in zip(range(ligne, n), range(col, -1, -1)):
        if plateau[i][j] == 'X':
            return False
    return True

def afficher_plateau(plateau):
    """Affiche le plateau."""
    for ligne in plateau:
        print(' '.join(ligne))

n = int(input("Entrez la taille du plateau : "))
plateau = [['O' for _ in range(n)] for _ in range(n)]
if placer_reine(plateau, 0, n):
    afficher_plateau(plateau)
else:
    print("Aucune solution n'a été trouvée.")
