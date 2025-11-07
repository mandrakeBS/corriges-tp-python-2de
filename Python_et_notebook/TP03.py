# TP03
# Détermine si n est un nombre premier.

def est_premier(n):
    if n <= 1:
        # un nombre inférieur ou égal à 1 n'est pas premier.
        return False
    for i in range(... , ... ):
        if .......... :
            # n est divisible par i, donc n n'est pas premier.
            return False
    return True  # n est un nombre premier.

# Exécution du programme.
n = int(input("Entrez un entier naturel n : "))


# Vérification des conditions.
if n < 0:
    print("Erreur : n doit être un entier naturel.")
else:
    if est_premier(n):
        print(n,"est un nombre premier.")
    else:
        print(n,"n'est pas un nombre premier.")

