def determinant(ux, uy, vx, vy):
    return ux*vy-uy*vx

def systeme(a1, b1, c1, a2, b2, c2):
    D = determinant(a1,a2,b1,b2)
    if D==0:
        print("Le système n'admet pas un couple UNIQUE de solutions")
    else:
        x=determinant(c1, c2, b1, b2)/D
        y= determinant(a1, a2, c1, c2)/D
        print("Le système admet comme unique couple de solutions, (x;y)=(", x, ";", y, ").")