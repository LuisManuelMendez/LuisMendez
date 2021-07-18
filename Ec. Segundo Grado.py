# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 08:46:57 2021

@author: Luis Manuel Méndez
"""
print("           ")
print("Autor: Luis Manuel Méndez")
print("           ")
print("           ")
print("    Ecuación de Segundo Grado o Resolvente:")
print("   ========================================")
a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))
print("           ")
print("RESULTADO:")
print("           ")
x1_arriba = (-b+pow(b**2-(4*a*c),0.5))
x1_abajo = (2*a)
print("Solución 1 = [(",x1_abajo,")X + (",-x1_arriba,")]")

x2_arriba = (-b-pow(b**2-(4*a*c),0.5))
x2_abajo = (2*a)
print("Solución 2 = [(",x2_abajo,")X + (",-x2_arriba,")]")
print("           ")

x1 = x1_arriba/x1_abajo
x2 = x2_arriba/x2_abajo

print("X1 =",round(x1,2))
print("X2 =",round(x2,2))
print("FIN")