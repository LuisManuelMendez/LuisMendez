# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 06:14:52 2021

@author: Luis Manuel Méndez
"""
"""
# RUFFINI de Grado 5, 4 ó 3.

# aX^5 + bX^4 + cX^3 + dX^2 + eX + f = 0
"""
print("") 
print("")
print("Autor: Luis Manuel Méndez") 
print("") 
print("            INGRESA LAS VARIABLES DE TU ECUACIÓN")
print("") 
print("Si es de Grado 5, ingresa todas tus variables en orden") 
print("") 
print("Si es de Grado 4, coloca un cero(0) en (f)") 
print("") 
print("Si es de Grado 3, coloca un cero(0) en (f) y en (e)")
print("") 
print("") 
print("") 
print("") 
print("")
print("") 
print("") 
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
e = int(input("e: "))
f = int(input("f: "))
h = int(input("Coloca el Factor Primo: "))
r01 = (h*a)
r02 = (b+h*a)
r03 = (h*(b+h*a))
r04 = (c+h*(b+h*a))
r05 = (h*(c+h*(b+h*a)))
r06 = (d+h*(c+h*(b+h*a)))
r07 = (h*(d+h*(c+h*(b+h*a))))
r08 = (e+h*(d+h*(c+h*(b+h*a))))
r09 = (h*(e+h*(d+h*(c+h*(b+h*a)))))
r10 = (f+h*(e+h*(d+h*(c+h*(b+h*a)))))
print(" ") 
print("        ",a,"X^5 + ",b,"X^4 + ",c,"X^3 + ",d,"X^2 + ",e,"X + ",f,"= 0")
print(" ") 
print("X =",h)       
print("    ║",a,"        ",b,"        ",c,"        ",d,"        ",e,"      ",f)
print("    ║")
print("    ║")
print("    ║")
print("    ║")
print("    ║         ",r01,"        ",r03,"       ",r05,"       ",r07,"      ",r09)
print("------------------------------------------------------------------") 
print("     ",a,"       ",r02,"      ",r04,"       ",r06,"      ",r08,"       ",r10)      
print(" ")       
print("RESULTADO: ") 
print(" ") 
if (r10 < 0 or r10 > 0) and (f < 0 or f > 0):
    print("No hay resultado satisfactorio para X^5, vuelve a intentarlo")
    print(" ")
elif r10 == 0 and (f < 0 or f > 0):
    print("Resultado para X^5: ")
    print(" ")
    print(" (X  + ",-h,")((",a,")X^4 +(",r02,")X^3 +(",r04,")X^2 +(",r06,")X +(",r08,"))") 
elif f == 0 and (r08 < 0 or r08 > 0) and (e < 0 or e > 0):
    print(" ")
    print("No hay resultado satisfactorio para X^4, vuelve a intentarlo")
elif r10 == 0 and f == 0 and (e < 0 or e > 0):
    print("Resultado para X^4: ")
    print(" ")
    print(" (X  + ",-h,")((",a,")X^3 +(",r02,")X^2 +(",r04,")X +(",r06,"))")
elif e == 0 and (r06 < 0 or r06 > 0):
    print(" ")
    print("No hay resultado satisfactorio para X^3, vuelve a intentarlo")
elif r06 == 0 and r08 == 0 and (d < 0 or d > 0):
    print(" ") 
    print("Resultado para X^3: ")
    print(" (X  + ",-h,")((",a,")X^2 +(",r02,")X +(",r04,"))")
print("FIN")