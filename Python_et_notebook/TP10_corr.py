# TP10

def points_alignes(point1, point2, point3):
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3

    # Calcul de l'aire du triangle.
    aire = 0.5 * \
    abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

    return aire == 0

# Exécution du programme.
point1 = (1, 2)  # Exemple de point A.
point2 = (2, 3)  # Exemple de point B.
point3 = (3, 4)  # Exemple de point C.

if points_alignes(point1, point2, point3):
    print("Les points sont alignés.")
else:
    print("Les points ne sont pas alignés.")

