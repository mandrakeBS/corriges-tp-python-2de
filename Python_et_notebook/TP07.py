# TP07

def f(x):
    # On définit la fonction dont on veut trouver l'extremum.
    return -1 * (x ** 2) + 4 * x  # Exemple : f(x)=-x^2+4x.

def trouve_maximum(a, b, epsilon):
    while (b - a) > epsilon:
        milieu = (a + b) / 2
        f_a = f(a)
        f_milieu = f(milieu)
        f_b = f(b)
        # Comparer les valeurs pour réduire l'intervalle.
        if f_milieu > f_a and f_milieu > f_b:
            # Si milieu max, nous réduisons
            #l'intervalle à [a; b].
            a = milieu
            # Ajustement pour garder b à une distance de epsilon.
            b = (a + b) / 2
        elif f_a > f_milieu and f_a > f_b:
            # Si a max, nous réduisons
            #l'intervalle à [a, milieu].
            b = milieu;
        else:
            # Si b maxi, nous réduisons
            #l'intervalle à [milieu; b].
            a = milieu
    # Calculer le point milieu final pour l'extremum.
    x_maximum = (a + b) / 2
    valeur_maximum = f(x_maximum)
    # Afficher le résultat.
    print(f"Maximum : f({x_maximum}) = {valeur_maximum}")

# Exécution du programme.
a = 0  # Borne inférieure.
b = 5  # Borne supérieure.
epsilon = 0.01  # Précision souhaitée.
trouve_maximum(a, b, epsilon)

