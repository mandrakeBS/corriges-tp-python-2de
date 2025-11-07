# TP01:
# Détermine si a est un multiple de b.

def est_multiple(a, b):
    return a % b == 0

# Exécution du programme.
a = int(input("Entrez un entier naturel a : "))
b = int(input("Entrez un entier naturel b : "))

# Vérification des conditions.
if b == 0:
    print("Erreur : On ne peut pas diviser par zéro.")
else:
    if est_multiple(a, b):
        print(f"{a} est un multiple de {b}.")
    else:
        print(f"{a} n'est pas un multiple de {b}.")
