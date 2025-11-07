def determinant(ux, uy, vx, vy):
    return ux*vy-uy*vx

def systeme(a1, b1, c1, a2, b2, c2):
    D = determinant(a1,a2,b1,b2)
    if D==0:
        print("Le système n'admet pas un couple UNIQUE\
         de solutions")
    else:
        x= determinant(.................) / D
        y= ..................................
        print("Le système admet comme unique couple \
        de solutions,\n
        (x;y)=(", x, ";", y, ").")

#Exemple
systeme(2, -5, -41, -9, 4, 55)