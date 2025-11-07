# TP09

def f(x):
    # Définissez ici votre fonction.
    return x**2 - 2  # Par exemple, on cherche sqrt(2).
def dichotomie(n, a, b):
    precision = 10 ** (-n)
    # Vérification que f(a) et f(b) ont des signes opposés.
    while abs(b - a) > precision:
        milieu = (a + b) / 2
        if f(milieu) == 0:  # Si on trouve une racine exacte.
            return milieu, milieu
        elif f(a) * \
        f(milieu) < 0: #Changement de signe entre a et milieu.
            b = milieu
        else:  # Changement de signe entre milieu et b.
            a = milieu

    return a, b

# Exécution du programme.
n = 3  # Par exemple, 10^{-3}.
a = 0  # Intervalle de départ.
b = 2  # Intervalle de départ.
borne_inf, borne_sup = dichotomie(n, a, b)
print(f"Encadrement de la solution à 10^(-{n}):\t\
 {borne_inf:.{n}f} <= x <= {borne_sup:.{n}f}")
print(f"Amplitude : {borne_sup - borne_inf:.{n}f}")