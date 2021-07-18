# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 07:34:19 2021

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
print("                          Dos (2) Variables")
print("                       -----------------------")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("                             a = bX + cY")
print("                             d = eX + fY")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("Coloca los valores de: a, b, c, d, e, f de tu Sistem de Ecuaciones")
"""
# ENTRADA DE VARIABLES
"""
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))
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
        print("                             (",a,") = (",b,")X + (",c,")Y")
        print("                             (",d,") = (",e,")X + (",f,")Y")
print("        ")
print("ADELANTE")

"""
# Fórmula para hallar X:
"""
print("    ")
print("   Fórmula para hallar X:         Fórmula para hallar Y")
print("  -----------------------        -----------------------")
print("          a - c * Y                      b * d - e * a")
print(" X =  __________________          Y =   ________________")
print("               e                         b * f - e * c")
print("    ")
print("                      SUSTITUYENDO:")
print("                     -------------- ")
print("        (",a,")-(",c,") * Y                (",b,")*(",d,")-(",e,")*(",a,")")
print(" X =   __________________       Y =   ___________________________")
print("              (",e,")                    (",b,")*(",f,")-(",e,")*(",c,")")
print("    ")
print("                       RESULTADO:  ")
print("                      -----------")
"""
# CÁLCULO DE Y y X
"""
Y_arriba = b*d - e*a
Y_abajo = b*f - e*c
Y = Y_arriba/Y_abajo
X_arriba = a - c*((b*d - e*a)/(b*f - e*c))
X_abajo = b
X = X_arriba/X_abajo
print("X(fracción) =",X_arriba,"/",X_abajo)
print(" ")
print("X = ",round(X,3))
print("    ")
print("Y(fracción) =",Y_arriba,"/",Y_abajo)
print(" ")
print("Y = ",round(Y,3))
print()
print("FIN")