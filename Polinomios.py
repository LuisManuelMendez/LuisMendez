# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 09:30:18 2021

@author: Luis Manuel Méndez
"""
"""
Proyecto 1.
Escriba en Python la implementación del algoritmo para resolver el problema que
se le plantea y grabe un vídeo donde explique el funcionamiento del código.
Adjunte los archivos (código, vídeo) en un repositorio de su preferencia.
Envíeme el enlace de acceso a los archivos.
Solo se permite el uso de la biblioteca estándar math
(se valorará mucho si no recurre a bibliotecas),
sin usar los módulos de teoría de números de esta biblioteca.

Problema:
Dados dos polinomios con coeficientes reales, determinar:
i. Suma
ii. Resta
iii. Multiplicación
iv. Cociente y residuo al dividirlos
v. Grado de cada polinomio y de los polinomios hallados en los cuatro ítems anteriores
"""
# Polinomios con coeficientes reales.
# aX^5 + bX^4 + cX^3 + dX^2 + eX + f = 0
print("") 
print("")
print("Autor: Luis Manuel Méndez")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print(" ABRIR TODA LA CONSOLA A LA IZQUIERDA PARA OBSERVAR EL PROCESO MEJOR")
print("       -------------------------------------------------------") 
print("")
print("          INGRESA LAS VARIABLES DEL PRIMER (1) POLINOMIO")
print("") 
print("")
print("")
print("")
print("")
print("")
a1 = float(input("a1: "))
b1 = float(input("b1: "))
c1 = float(input("c1: "))
d1 = float(input("d1: "))
e1 = float(input("e1: "))
f1 = float(input("f1: "))
print("") 
print(" ",a1,"X^5 + ",b1,"X^4 + ",c1,"X^3 + ",d1,"X^2 + ",e1,"X + ",f1)
print("") 
print("         INGRESA LAS VARIABLES DEL SEGUNDO (2) POLINOMIO")
print("")
a2 = float(input("a2: "))
b2 = float(input("b2: "))
c2 = float(input("c2: "))
d2 = float(input("d2: "))
e2 = float(input("e2: "))
f2 = float(input("f2: "))
print("") 
print(" ",a1,"X^5 + ",b1,"X^4 + ",c1,"X^3 + ",d1,"X^2 + ",e1,"X + ",f1)
print("")
print(" ",a2,"X^5 + ",b2,"X^4 + ",c2,"X^3 + ",d2,"X^2 + ",e2,"X + ",f2)
print("")
revisar = False
while revisar == False:
    print("")
    confirmacion = input("Oprime 1, para sumarlos: ")
    if confirmacion =="1":
        revisar = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un 1, vuelve a intentarlo")
#CÁLCULO DE LA SUMA DE DOS PLINOMIOS:
s6 = f1 + f2
s5 = e1 + e2 
s4 = d1 + d2
s3 = c1 + c2
s2 = b1 + b2
s1 = a1 + a2
print("") 
print("         SUMA DE POLINOMIOS")
print("")
print("(",a1,")X^5 + (",b1,")X^4 + (",c1,")X^3 + (",d1,")X^2 + (",e1,")X + (",f1,")")
print("")
print("(",a2,")X^5 + (",b2,")X^4 + (",c2,")X^3 + (",d2,")X^2 + (",e2,")X + (",f2,")")
print(" ------------------------------------------------------------------")
print("(",s1,")X^5 + (",s2,")X^4 + (",s3,")X^3 + (",s4,")X^2 + (",s5,")X + (",s6,")")         
print("")
if a1 != 0:
    print("Polinomio 1 es de grado 5")
elif a1 == 0 and b1 != 0:
    print("Polinomio 1 es de grado 4")
elif a1 == 0 and b1 == 0 and c1 != 0:
    print("Polinomio 1 es de grado 3")
elif a1 == 0 and b1 == 0 and c1 == 0 and d1 != 0:
    print("Polinomio 1 es de grado 2")
elif a1 == 0 and b1 == 0 and c1 == 0 and d1 == 0 and e1 != 0:
    print("Polinomio 1 es de grado 1")    
elif a1 == 0 and b1 == 0 and c1 == 0 and d1 == 0 and e1 == 0 and f1 != 0:
    print("El polinomio 1 solo posee termino independiente")
else:
    print("El polinomio 1 NO EXISTE o es CERO")
print("")  
if a2 != 0:
    print("Polinomio 2 es de grado 5")
elif a2 == 0 and b2 != 0:
    print("Polinomio 2 es de grado 4")
elif a2 == 0 and b2 == 0 and c2 != 0:
    print("Polinomio 2 es de grado 3")
elif a2 == 0 and b2 == 0 and c2 == 0 and d2 != 0:
    print("Polinomio 2 es de grado 2")
elif a2 == 0 and b2 == 0 and c2 == 0 and d2 == 0 and e2 != 0:
    print("Polinomio 2 es de grado 1")    
elif a1 == 0 and b1 == 0 and c2 == 0 and d2 == 0 and e2 == 0 and f2 != 0:
    print("El polinomio 2 solo posee termino independiente")
else:
    print("El polinomio 2 NO EXISTE o es CERO")
print("") 
if s1 != 0:
    print("Polinomio resultado es de grado 5")
elif s1 == 0 and s2 != 0:
    print("Polinomio resultado es de grado 4")
elif s1 == 0 and s2 == 0 and s3 != 0:
    print("Polinomio resultado es de grado 3")
elif s1 == 0 and s2 == 0 and s3 == 0 and s4 != 0:
    print("Polinomio resultado es de grado 2")
elif s1 == 0 and s2 == 0 and s3 == 0 and s4 == 0 and s5 != 0:
    print("Polinomio resultado es de grado 1")    
elif s1 == 0 and s2 == 0 and s3 == 0 and s4 == 0 and s5 == 0 and s6 != 0:
    print("El polinomio resultado solo posee termino independiente")
else:
    print("El polinomio resultado NO EXISTE o es CERO")
    
revisar2 = False
while revisar2 == False:
    print("")
    confirmacion = input("Oprime 2, para restarlos: ")
    if confirmacion =="2":
        revisar2 = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un 2, vuelve a intentarlo")
#CÁLCULO DE LA RESTA DE DOS PLINOMIOS:
s6 = f1 - f2
s5 = e1 - e2 
s4 = d1 - d2
s3 = c1 - c2
s2 = b1 - b2
s1 = a1 - a2
print("") 
print("         RESTA DE POLINOMIOS")
print("")
print("(",a1,")X^5 + (",b1,")X^4 + (",c1,")X^3 + (",d1,")X^2 + (",e1,")X + (",f1,")")
print("")
print("(",a2,")X^5 + (",b2,")X^4 + (",c2,")X^3 + (",d2,")X^2 + (",e2,")X + (",f2,")")
print(" ------------------------------------------------------------------")
print("(",s1,")X^5 + (",s2,")X^4 + (",s3,")X^3 + (",s4,")X^2 + (",s5,")X + (",s6,")")         
print("")
if a1 != 0:
    print("Polinomio 1 es de grado 5")
elif a1 == 0 and b1 != 0:
    print("Polinomio 1 es de grado 4")
elif a1 == 0 and b1 == 0 and c1 != 0:
    print("Polinomio 1 es de grado 3")
elif a1 == 0 and b1 == 0 and c1 == 0 and d1 != 0:
    print("Polinomio 1 es de grado 2")
elif a1 == 0 and b1 == 0 and c1 == 0 and d1 == 0 and e1 != 0:
    print("Polinomio 1 es de grado 1")    
elif a1 == 0 and b1 == 0 and c1 == 0 and d1 == 0 and e1 == 0 and f1 != 0:
    print("El polinomio 1 solo posee termino independiente")
else:
    print("El polinomio 1 NO EXISTE o es CERO")
print("")  
if a2 != 0:
    print("Polinomio 2 es de grado 5")
elif a2 == 0 and b2 != 0:
    print("Polinomio 2 es de grado 4")
elif a2 == 0 and b2 == 0 and c2 != 0:
    print("Polinomio 2 es de grado 3")
elif a2 == 0 and b2 == 0 and c2 == 0 and d2 != 0:
    print("Polinomio 2 es de grado 2")
elif a2 == 0 and b2 == 0 and c2 == 0 and d2 == 0 and e2 != 0:
    print("Polinomio 2 es de grado 1")    
elif a1 == 0 and b1 == 0 and c2 == 0 and d2 == 0 and e2 == 0 and f2 != 0:
    print("El polinomio 2 solo posee termino independiente")
else:
    print("El polinomio 2 NO EXISTE o es CERO")
print("") 
if s1 != 0:
    print("Polinomio resultado es de grado 5")
elif s1 == 0 and s2 != 0:
    print("Polinomio resultado es de grado 4")
elif s1 == 0 and s2 == 0 and s3 != 0:
    print("Polinomio resultado es de grado 3")
elif s1 == 0 and s2 == 0 and s3 == 0 and s4 != 0:
    print("Polinomio resultado es de grado 2")
elif s1 == 0 and s2 == 0 and s3 == 0 and s4 == 0 and s5 != 0:
    print("Polinomio resultado es de grado 1")    
elif s1 == 0 and s2 == 0 and s3 == 0 and s4 == 0 and s5 == 0 and s6 != 0:
    print("El polinomio resultado solo posee termino independiente")
else:
    print("El polinomio resultado NO EXISTE o es CERO")
# MULTIPLICACIÓN DE POLINOMIOS
revisar3 = False
while revisar3 == False:
    print("")
    confirmacion = input("Oprime 3, para multiplicarlos: ")
    if confirmacion =="3":
        revisar3 = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un 3, vuelve a intentarlo")
print("")
print("")
print("         MULTIPLICACIÓN DE POLINOMIOS")
print("") 
print(" Polinomio 1: (",a1,")X^5 + (",b1,")X^4 + (",c1,")X^3 + (",d1,")X^2 + (",e1,")X + (",f1,")")
print("")
print(" Polinomio 2: (",a2,")X^5 + (",b2,")X^4 + (",c2,")X^3 + (",d2,")X^2 + (",e2,")X + (",f2,")")
print("")
# Mostrando la multiplicación:
print("")
print(" (",a1*a2,")X^10 + (",a1*b2,")X^9 + (",a1*c2,")X^8 + (",a1*d2,")X^7 + (",a1*e2,")X^6 + (",a1*f2,")X^5 +") 
print("")
print("               (",b1*a2,")X^9 + (",b1*b2,")X^8 + (",b1*c2,")X^7 + (",b1*d2,")X^6 + (",b1*e2,")X^5 + (",b1*f2,")X^4 +") 
print("")
print("                            (",c1*a2,")X^8 + (",c1*b2,")X^7 + (",c1*c2,")X^6 + (",c1*d2,")X^5 + (",c1*e2,")X^4 + (",c1*f2,")X^3 +") 
print("")
print("                                         (",d1*a2,")X^7 + (",d1*b2,")X^6 + (",d1*c2,")X^5 + (",d1*d2,")X^4 + (",d1*e2,")X^3 + (",d1*f2,")X^2 +") 
print("")
print("                                                      (",e1*a2,")X^6 + (",e1*b2,")X^5 + (",e1*c2,")X^4 + (",e1*d2,")X^3 + (",e1*e2,")X^2 + (",e1*f2,")X +") 
print("")
print("                                                                   (",f1*a2,")X^5 + (",f1*b2,")X^4 + (",f1*c2,")X^3 + (",f1*d2,")X^2 + (",f1*e2,")X + (",f1*f2,")") 
print("")
# Suma de los literales de cada grado:
x10 = a1*a2
x09 = a1*b2 + b1*a2
x08 = a1*c2 + b1*b2 + c1*a2
x07 = a1*d2 + b1*c2 + c1*b2 + d1*a2
x06 = a1*e2 + b1*d2 + c1*c2 + d1*b2 + e1*a2
x05 = a1*f2 + b1*e2 + c1*d2 + d1*c2 + e1*b2 + f1*a2
x04 =         b1*f2 + c1*e2 + d1*d2 + e1*c2 + f1*b2
x03 =                 c1*f2 + d1*e2 + e1*d2 + f1*c2
x02 =                         d1*f2 + e1*e2 + f1*d2
x01 =                                 e1*f2 + f1*e2
x00 =                                         f1*f2
print(" (",x10,")X^10 + (",x09,")X^9 + (",x08,")X^8 + (",x07,")X^7 + (",x06,")X^6 + (",x05,")X^5 +(",x04,")X^4 + (",x03,")X^3 + (",x02,")X^2 + (",x01,")X + (",x00,")") 
print("")
if a1 != 0:
    print("Polinomio 1 es de grado 5")
elif a1 == 0 and b1 != 0:
    print("Polinomio 1 es de grado 4")
elif a1 == 0 and b1 == 0 and c1 != 0:
    print("Polinomio 1 es de grado 3")
elif a1 == 0 and b1 == 0 and c1 == 0 and d1 != 0:
    print("Polinomio 1 es de grado 2")
elif a1 == 0 and b1 == 0 and c1 == 0 and d1 == 0 and e1 != 0:
    print("Polinomio 1 es de grado 1")    
elif a1 == 0 and b1 == 0 and c1 == 0 and d1 == 0 and e1 == 0 and f1 != 0:
    print("El polinomio 1 solo posee termino independiente")
else:
    print("El polinomio 1 NO EXISTE o es CERO")
print("")  
if a2 != 0:
    print("Polinomio 2 es de grado 5")
elif a2 == 0 and b2 != 0:
    print("Polinomio 2 es de grado 4")
elif a2 == 0 and b2 == 0 and c2 != 0:
    print("Polinomio 2 es de grado 3")
elif a2 == 0 and b2 == 0 and c2 == 0 and d2 != 0:
    print("Polinomio 2 es de grado 2")
elif a2 == 0 and b2 == 0 and c2 == 0 and d2 == 0 and e2 != 0:
    print("Polinomio 2 es de grado 1")    
elif a1 == 0 and b1 == 0 and c2 == 0 and d2 == 0 and e2 == 0 and f2 != 0:
    print("El polinomio 2 solo posee termino independiente")
else:
    print("El polinomio 2 NO EXISTE o es CERO")
print("")  
if x10 != 0:
    print("Polinomio resultado es de grado 10")
elif x10 == 0 and x09 != 0:
    print("Polinomio resultado es de grado 9")
elif x10 == 0 and x09 == 0 and x08 != 0:
    print("Polinomio resultado es de grado 8")
elif x10 == 0 and x09 == 0 and x08 == 0 and x07 != 0:
    print("Polinomio resultado es de grado 7")
elif x10 == 0 and x09 == 0 and x08 == 0 and x07 == 0 and x06 != 0:
    print("Polinomio resultado es de grado 6")    
elif x10 == 0 and x09 == 0 and x08 == 0 and x07 == 0 and x06 == 0 and x05 != 0:
    print("Polinomio resultado es de grado 5") 
elif x10 == 0 and x09 == 0 and x08 == 0 and x07 == 0 and x06 == 0 and x05 == 0 and x04 != 0:
    print("Polinomio resultado es de grado 4") 
elif x10 == 0 and x09 == 0 and x08 == 0 and x07 == 0 and x06 == 0 and x05 == 0 and x04 == 0 and x03 != 0:
    print("Polinomio resultado es de grado 3") 
elif x10 == 0 and x09 == 0 and x08 == 0 and x07 == 0 and x06 == 0 and x05 == 0 and x04 == 0 and x03 == 0 and x02 != 0:
    print("Polinomio resultado es de grado 2") 
elif x10 == 0 and x09 == 0 and x08 == 0 and x07 == 0 and x06 == 0 and x05 == 0 and x04 == 0 and x03 == 0 and x02 == 0 and x01 != 0:
    print("Polinomio resultado es de grado 1") 
elif x10 == 0 and x09 == 0 and x08 == 0 and x07 == 0 and x06 == 0 and x05 == 0 and x04 == 0 and x03 == 0 and x02 == 0 and x01 == 0 and x00 != 0:
    print("El polinomio resultado solo posee termino independiente")
else:
    print("El polinomio resultado NO EXISTE o es CERO")

# DIVISIÓN DE POLINOMIOS
revisar4 = False
while revisar4 == False:
    print("")
    confirmacion = input("Oprime 4, para hacer una división de polinomios: ")
    if confirmacion =="4":
        revisar4 = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un 4, vuelve a intentarlo")
print("") 
print("") 
print("") 
print("Autor: Luis Manuel Méndez")
print("")
print("")
print("") 
print("")
print("")
print("                      DIVISIÓN DE POLINOMIOS")
print("") 
print("") 
print("") 
print("") 
print("") 
print("                   PARA POLINOMIOS DE LA FORMA")
print("") 
print("    (a1)X^3 + (b1)X^2 + (c1)X + (d1)  /  (a2)X^2 + (b2)X + (c2)")
print("") 
print("INGRESA LAS VARIABLES DEL POLINOMIO 1:")
print("")
a1 = float(input("a1: "))
b1 = float(input("b1: "))
c1 = float(input("c1: "))
d1 = float(input("d1: "))
print("")
print("INGRESA LAS VARIABLES DEL POLINOMIO 2:")
print("")
a2 = float(input("a2: "))
b2 = float(input("b2: "))
c2 = float(input("c2: "))
print("")
if a2 != 0 and b1 == 0 or b2 != 0 and c1 == 0:
    print(" ERROR: Polinomio 2 es mayor que polinomio 1")
    print("")
elif a2 != 0:
    p1 = a1/a2
    p2 = (b1-(b2*p1))/a2
    p3 = c1-(c2*p1)
    print("")
    print(" (",a1,")X^3 + (",b1,")X^2 + (",c1,")X + (",d1,") ║ (",a2,")X^2 + (",b2,")X + (",c2,")")
    print("                                                   -------------------------------------")
    print("(",-a2*p1,")X^3 + (",-b2*p1,")X^2 + (",-c2*p1,")X                 (",p1,")X + (",p2,")")
    print("------------------------------------------")
    print("     0         (",b1-(b2*p1),")X^2 + (",c1-(c2*p1),")X + (",d1,")")
    print("")
    print("               (",-a2*p2,")X^2 + (",-b2*p2,")X + (",-c2*p2,")")
    print("              --------------------------------------")
    print("                     0        (",p3-(b2*p2),")X + (",d1-(c2*p2),")  RESIDUO") 
    print("") 
elif b2 != 0:
    p1 = a1/b2
    p2 = (b1-(c2*p1))/b2
    p3 = (c1-(c2*p2))/b2
    print("")
    print(" (",a1,")X^3 + (",b1,")X^2 + (",c1,")X + (",d1,") ║ (",b2,")X + (",c2,")")
    print("                                                   -------------------------------")
    print("(",-b2*p1,")X^3 + (",-c2*p1,")X^2                         (",p1,")X^2 + (",p2,")X + (",p3,")")
    print("------------------------------------------")
    print("     0         (",b1-(c2*p1),")X^2 + (",c1,")X + (",d1,")")
    print("")
    print("               (",-b2*p2,")X^2 + (",-c2*p2,")X + (",d1,")")
    print("              --------------------------------------")
    print("                   0          (",c1-(c2*p2),")X + (",d1,")") 
    print("")
    print("                              (",-b2*p3,")X + (",-c2*p3,")") 
    print("                          -------------------------------")
    print("                                   0       (",d1-(c2*p3),")  RESIDUO")
    print("") 
elif c2 != 0:
    p1 = a1/c2
    p2 = b1/c2
    p3 = c1/c2
    p4 = d1/c2
    print("")
    print(" (",a1,")X^3 + (",b1,")X^2 + (",c1,")X + (",d1,") ║ (",c2,")")
    print("                                                   --------------------------------------------------")
    print("(",-c2*p1,")X^3                                     (",p1,")X^3 + (",p2,")X^2 + (",p3,")X + (",p4,")")
    print("------------------------------------------")
    print("     0         (",b1,")X^2 + (",c1,")X + (",d1,")")
    print("               (",-c2*p2,")X^2")
    print("              --------------------------------------")
    print("                   0         (",c1,")X + (",d1,")") 
    print("                             (",-c2*p3,")X")
    print("                          ---------------------------")
    print("                                   0     (",d1,")") 
    print("                                         (",-c2*p4,")") 
    print("                                        ----------")
    print("                                         (",d1-c2*p4,")  RESIDUO") 
    print("") 
else:
    print("               NO PUEDES DIVIDIR POR CERO")    
    print("")     
    print("                    NO HAY RESULTADO")    
    print("")    
if a1 != 0:
    print("Polinomio 1 es de grado 3")
elif a1 == 0 and b1 != 0:
    print("Polinomio 1 es de grado 2")
elif a1 == 0 and b1 == 0 and c1 != 0:
    print("Polinomio 1 es de grado 1")
elif a1 == 0 and b1 == 0 and c1 == 0 and d1 != 0:
    print("El polinomio 1 solo posee termino independiente")
elif a1 == 0 and b1 == 0 and c1 == 0 and d1 == 0:
    print("El polinomio 1 NO EXISTE o es CERO")
print("")    
if a2 != 0:
    print("Polinomio 2 es de grado 2")
elif a2 == 0 and b2 != 0:
    print("Polinomio 2 es de grado 1")
elif a2 == 0 and b2 == 0 and c2 != 0:
    print("Polinomio 2 solo posee termino independiente")
elif a2 == 0 and b2 == 0 and c2 == 0:
    print("El polinomio 2 NO EXISTE o es CERO")
print("")
if a1 != 0 and a2 != 0:
    print("Polinomio resultado es de grado 1")
elif a1 != 0 and a2 == 0 and b2 != 0:
    print("Polinomio resultado es de grado 2")
elif a1 != 0 and a2 == 0 and b2 == 0 and c2 != 0:
    print("Polinomio resultado es de grado 3")
elif a2 != 0 and b1 == 0 or b2 != 0 and c1 == 0:
    print(" ERROR: No hay Resultado")
elif a1 == 0 and a2 != 0 and c2 != 0 or a1 == 0 and b1 == 0 and a2 == 0 and c2 != 0 or a1 == 0 and b1 == 0 and c1 == 0 and a2 == 0 and b2 == 0 and c2 != 0:
    print("Polinomio resultado solo posee termino independiente")
elif a1 == 0 and b1 == 0 and c1 == 0 and d1 == 0 and a2 == 0 and b2 == 0 and c2 == 0:
    print("            SOLO INGRESASTE CEROS EN TODO")