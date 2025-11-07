# TP05

def trouve_premiere_puissance_plus_grande(base, limite):
    exposant = 0
    while base ** exposant <= limite:
        exposant += 1
    return exposant

def trouve_premiere_puissance_plus_petite(base, limite):
    exposant = 10
    while base ** exposant >= limite:
        exposant -= 1
    return exposant

# Exécution du programme.
base = 3  # Exemple de base (nombre positif).
puissance_sup_limite = 50
puissance_inf_limite = 20

# Déterminer la première puissance supérieure.
exposant_max = trouve_premiere_puissance_plus_grande(base, \
puissance_sup_limite)
print(f"La première puissance de {base} supérieure à \
{puissance_sup_limite} est : \
{base}^{exposant_max} = {base ** exposant_max}")

# Déterminer la première puissance inférieure.
exposant_min = trouve_premiere_puissance_plus_petite(base, \
puissance_inf_limite)
print(f"La première puissance de {base} inférieure à \
{puissance_inf_limite} est : \
{base}^{exposant_min} = {base ** exposant_min}")

