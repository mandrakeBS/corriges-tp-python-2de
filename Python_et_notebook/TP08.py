# TP08

def f(x):
    # Définissez ici votre fonction.
    return x**2 - 2  # Par exemple, on cherche sqrt(2).

def trouve_bornes(n, x0, delta=0.1):
    precision = 10 ** (-n)
    a = x0  # Point de départ.
    b = x0 + delta  # Point suivant.
    fa = f(a)
    fb = f(b)
    # Cherche les bornes d'encadrement.
    while abs(b - a) > precision:
        if fa * fb > 0:  # Pas de changement de signe.
            a = b
            b += delta
            fa = fb
            fb = f(b)
        else:  # Changement de signe trouvé.
            return a, b
    return a, b

# Exécution du programme.
n = 3  # Par exemple, 10^{-3}.
x0 = 0  # Point de départ pour le balayage.
borne_inf, borne_sup = trouve_bornes(n, x0, 0.1)
print(f"Encadrement de la solution à 10^(-{n}):\t\
 {borne_inf:.{n}f} <= x <= {borne_sup:.{n}f}")
print(f"Amplitude : {borne_sup - borne_inf:.{n}f}")


