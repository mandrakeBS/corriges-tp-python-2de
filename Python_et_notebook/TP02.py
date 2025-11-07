# TP02
# Détermine le plus grand multiple de a qui
# est inférieur ou égal à b.

def plus_grand_multiple(a, b):
    if a == 0:
        return 0  # Si a est 0, tous les multiples sont 0.
    return ............  # Calcule le plus grand multiple.

# Exécution du programme.
a = int(input("Entrez un entier naturel a: "))
b = int(input("Entrez un entier naturel b: "))

# Vérification des conditions.
if a <= 0 or b < 0:
    print("Erreur: a doit être un entier naturel positif et \
    b doit être un entier naturel.")
else:
    resultat = plus_grand_multiple(a, b)
    print("Le plus grand multiple de",a,"qui est inférieur ou \
    égal à",b,"est :", resultat, ".")
