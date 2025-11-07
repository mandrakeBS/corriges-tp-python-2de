# TP06

def f(x):
    # Définissez ici la fonction dont
    #vous voulez trouver l'extremum.
    return -1 * (x**2) + 4 * x  # f(x)=-x^2+4x.

def trouve_extremum(debut, fin, pas):
    x = debut
    valeur_max = float("-inf")
    valeur_min = float("inf")
    x_max = debut
    x_min = debut
    while x <= fin:
        valeur_courante = f(x)
        # Vérification du maximum.
        if valeur_courante > valeur_max:
            valeur_max = valeur_courante
            x_max = x
        # Vérification du minimum.
        if valeur_courante < valeur_min:
            valeur_min = valeur_courante
            x_min = x
        x += pas
    # Affichage des résultats.
    print(f"Maximum : f({x_max}) = {valeur_max}")
    print(f"Minimum : f({x_min}) = {valeur_min}")

# Exécution du programme.
debut = 0  # Borne inférieure.
fin = 5  # Borne supérieure.
pas = 0.1  # Pas de balayage.
trouve_extremum(debut, fin, pas)
