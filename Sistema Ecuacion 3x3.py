# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 10:00:26 2021

@author: Luis Manuel Méndez
"""

print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("@author: Luis Méndez")
print("                        SISTEMA DE ECUACIONES:")
print("                          Tres (3) Variables")
print("                       -----------------------")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("                             a = bX + cY + dZ")
print("                             e = fX + gY + hZ")
print("                             i = jX + kY + lZ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("Coloca los valores de: a, b, c, d, e, f, g, h, i, j, k y l de tu Sistem de Ecuaciones")
"""
# ENTRADA DE VARIABLES
"""
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))
g = float(input("g: "))
h = float(input("h: "))
i = float(input("i: "))
j = float(input("j: "))
k = float(input("k: "))
l = float(input("l: "))
print("    ")
print("    ")

revisar = False
while revisar == False:
    print("¿Quieres COMPARAR tus Ecuaciones?")
    confirmacion = input("Sí(s) o No(n): ")
    if confirmacion =="n":
        revisar = True
    else: 
        print("REVISA CUIDADOSAMENTE TUS ECUACIONES:")
        print("                             (",a,") = (",b,")X + (",c,")Y + (",d,")Z")
        print("                             (",e,") = (",f,")X + (",g,")Y + (",h,")Z")
        print("                             (",i,") = (",j,")X + (",k,")Y + (",l,")Z")
print("        ")
print("ADELANTE")

"""
# Fórmula para hallar X:
"""
print("    ")
print("     Fórmula para hallar X:       Fórmula para hallar Y  ")
print("     -----------------------     ----------------------- ")
print("            a - cY - dZ           fa - be - (fd - bh)Z   ")   
print("     X =  _________________  Y =  ____________________   ")
print("                 b                      fc - bg          ")
print("    ")
print("                    Fórmula para hallar Z")
print("                 --------------------------")
print("              (jc - bk)(fa - be) - (fc - bg)(ja - bi)") 
print("       Z =  __________________________________________")
print("              (jc - bk)(fd - bh) - (fc - bg)(jd - bl)")
print()
print("                       RESULTADO:  ")
print("                      -----------")

# CÁLCULO DE X, Y y Z

z_arriba = (j*c-b*k)*(f*a-b*e)-(f*c-b*g)*(j*a-b*i)
z_abajo =  (j*c-b*k)*(f*d-b*h)-(f*c-b*g)*(j*d-b*l)
z = z_arriba/z_abajo
y_arriba = f*a-b*e-(f*d-b*h)*z
y_abajo =  f*c-b*g
y = y_arriba/y_abajo
x_arriba = a-c*y-d*z 
x_abajo = b
x = x_arriba/x_abajo

print("Z(fracción)= ",z_arriba,"/",z_abajo)
print("Z = ",round(z,3))
print()
print("Y(fracción)= ",y_arriba,"/",y_abajo)
print("Y = ",round(y,3))
print()
print("X(fracción)= ",x_arriba,"/",x_abajo)
print("X = ",round(x,3))
print()
print("FIN")