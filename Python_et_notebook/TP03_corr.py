# TP03
# Détermine si n est un nombre premier.
import time
def est_premier(n):
    if n <= 1:
        # un nombre inférieur ou égal à 1 n'est pas premier.
        return False
    for i in range(2, n):
        if n % i == 0:
            # n est divisible par i, donc n n'est pas premier.
            return False
    return True  # n est un nombre premier.

# Exécution du programme.
n = int(input("Entrez un entier naturel n : "))
print("Calculs en cours ...")
date_debut=time.perf_counter()
# Vérification des conditions.
if n < 0:
    print("Erreur : n doit être un entier naturel.")
else:
    if est_premier(n):
        print(f"{n} est un nombre premier.")
    else:
        print(f"{n} n'est pas un nombre premier.")
date_fin=time.perf_counter()
duree=date_fin-date_debut

#conversion duree en heures, minutes et secondes
heures, reste = divmod(duree, 3600)
minutes, secondes = divmod(reste, 60)

print(f"Le temps d'execution du programme a été de: {duree} seconde(s), soit ")


print(f"{heures}h {minutes}m {secondes}s")