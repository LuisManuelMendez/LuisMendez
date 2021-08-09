# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 12:38:12 2021

@author: Luis Manuel Méndez


Escriba en Python la implementación del algoritmo para resolver
el problema que se le plantea:
Dados dos polinomios con coeficientes reales, determinar:
1. Suma
2. Resta
3. Multiplicación
4. Cociente y residuo al dividirlos
5. Las raíces de cada polinomio y de los polinomios hallados.
6. Asociar cada polinomio y polinomios hallados a funciones,
para hallar los PUNTOS CRÍTICOS
7. Las gráficas de cada función indicando los puntos hallados.
8. Las gráficas de cada función con su respectiva función primitiva
y función derivada.

Polinomio 1 RECOMENDADO: 7.0 + 0.0 x**1 - 12.0 x**2 + 4.0 x**3 + 3.0 x**4
    
Polinomio 2 RECOMENDADO: 9.0 + 5.0 x**1 - 2.0 x**2 - 4.0 x**3 + 1.0 x**4

Estos Polinomios se usaron en el vídeo.

"""
# Polinomios
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
print()
print()
print()
print()
print()
print()
print()
print("Autor: Luis Manuel Méndez")
print()
print()
print()
print()
print()
print()
print()
print()
print(" INGRESA LOS DATOS DEL PRIMER POLINOMIO EN ORDEN ASCENDENTE:")
print("-------------------------------------------------------------")
print()
print()
print()
print()
print()
print()
print()
print()
print()
pol1 = []
pol1.append(float(input("TI: ")))
pol1.append(float(input("X1: ")))
pol1.append(float(input("X2: ")))
pol1.append(float(input("X3: ")))
pol1.append(float(input("X4: ")))
pol1.append(float(input("X5: ")))
pol1.append(float(input("X6: ")))
pol1.append(float(input("X7: ")))
pol1.append(float(input("X8: ")))
pol1.append(float(input("X9: ")))
pol1.append(float(input("X10: ")))
pol1.append(float(input("X11 ")))
print()
print(" INGRESA LOS DATOS DEL SEGUNDO POLINOMIO EN ORDEN ASCENDENTE:")
print("--------------------------------------------------------------")
print()
pol2 = []
pol2.append(float(input("XTI: ")))
pol2.append(float(input("X1: ")))
pol2.append(float(input("X2: ")))
pol2.append(float(input("X3: ")))
pol2.append(float(input("X4: ")))
pol2.append(float(input("X5: ")))
pol2.append(float(input("X6: ")))
pol2.append(float(input("X7: ")))
pol2.append(float(input("X8: ")))
pol2.append(float(input("X9: ")))
pol2.append(float(input("X10: ")))
pol2.append(float(input("X11 ")))
print()
print()
print()
print()
print()
# Sean dos polinomios
p1 = Polynomial(coef=pol1) + 0
p2 = Polynomial(coef=pol2) + 0
# Polinomio
print()
print()
print("             Estos son los dos polinomios:")
print("           ---------------------------------")
print()
print(p1)
print("Grado del Polinomio 1: ",p1.degree())
print()
print(p2)
print("Grado del Polinomio 2: ",p2.degree())
print()
print()
print()
print()
print()
# SUMA DE POLINOMIOS
revisar = False
while revisar == False:
    print("")
    confirmacion = input("Oprime +, para sumarlos: ")
    if confirmacion =="+":
        revisar = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un +, vuelve a intentarlo")
#CÁLCULO DE LA SUMA DE DOS POLINOMIOS:
print()
print()
print()
print()
print()
print()
print()
print("             Esta es la SUMA de los polinomios:")
print("           -------------------------------------")
print(p1)
print()
print(p2)
print("        -----------------------------------------------------")
suma = p1+p2
print(suma)
print()
print("Grado de la Suma: ",suma.degree())
print()
print()
print()
print()
print()
print()
# RESTA DE POLINOMIOS
revisar2 = False
while revisar2 == False:
    print("")
    confirmacion = input("Oprime -, para restarlos: ")
    if confirmacion =="-":
        revisar2 = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un -, vuelve a intentarlo")
# CÁLCULO DE LA RESTA DE DOS PLINOMIOS:
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print("             Esta es la RESTA de los polinomios:")
print("           -------------------------------------")
print(p1)
print()
print(p2)
print("        -----------------------------------------------------")
resta = p1-p2
print(resta)
print()
print("Grado de la Resta: ",resta.degree())
print()
print()
print()
print()
print()
# MULTIPLICACIÓN DE POLINOMIOS
revisar3 = False
while revisar3 == False:
    print("")
    confirmacion = input("Oprime *, para multiplicarlos: ")
    if confirmacion =="*":
        revisar3 = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un *, vuelve a intentarlo")
# CÁLCULO DE LA MULTIPLICACIÓN DE DOS PLINOMIOS:
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print("        Esta es la MULTIPLICACIÓN de los polinomios:")
print("       ----------------------------------------------")
print(p1)
print()
print(p2)
print("        -----------------------------------------------------")
print("")
mult = p1*p2
print(mult)
print()
print("Grado de la Multiplicación: ",mult.degree())
print()
print()
print()
print()
# DIVISIÓN DE POLINOMIOS
revisar4 = False
while revisar4 == False:
    print("")
    confirmacion = input("Oprime /, para hacer una división de polinomios: ")
    if confirmacion =="/":
        revisar4 = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un /, vuelve a intentarlo")
# CÁLCULO DE LA DIVISIÓN DE DOS PLINOMIOS:
print()
print()
print("") 
print("") 
print("")
print("        Esta es la DIVISIÓN de los polinomios:")
print("       ----------------------------------------------")
print("") 
print(p1)
print("        -----------------------------------------------------")
print(p2)
print("")
print("                 Resultado de la División: ")
print("             ----------------------------------")
print("")
C = p1//p2
print("COCIENTE:", C)
print("---------")
print("")
print("Grado del Cociente: ",C.degree())
print("")
R = p1%p2
print("RESIDUO:", R)
print("--------")
print("")
print("Grado del Residuo: ",R.degree())
# RAÍCES DE LOS POLINOMIOS
revisar5 = False
while revisar5 == False:
    print("")
    confirmacion = input("Oprime r, para ver las RAÍCES de los polinomios: ")
    if confirmacion =="r":
        revisar5 = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un r, vuelve a intentarlo")
print()
print()
print()
print()
print()
print("")        
print("Raices del polinomio 1:")
print("-----------------------")
print("")
print(p1.roots())
print()
print()
print("")
print("Raices del polinomio 2:")
print("-----------------------")
print("")
print(p2.roots())
print("")
print()
print()
revisar6 = False
while revisar6 == False:
    print("")
    confirmacion = input("Oprime ENTER, para CONTINUAR: ")
    if confirmacion =="":
        revisar6 = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un ENTER, vuelve a intentarlo")
print()
print()
print()
print()
print("")
print("Raices de la SUMA:")
print("------------------")
print("")
print(suma.roots())
print("")
print()
print()
print("Raices de la RESTA:")
print("-------------------")
print("")
print(resta.roots())
print("")
print()
print()
print()
print()
revisar7 = False
while revisar7 == False:
    print("")
    confirmacion = input("Oprime ENTER, para CONTINUAR: ")
    if confirmacion =="":
        revisar7 = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un ENTER, vuelve a intentarlo")
print()
print()
print()
print()
print()
print()
print()
print()
print("")
print("Raices de la MULTIPLICACIÓN:")
print("")
print(mult.roots())
print("")
print()
print()
print()
print()
print()
print()
print()
print()
revisar8 = False
while revisar8 == False:
    print("")
    confirmacion = input("Oprime ENTER, para CONTINUAR: ")
    if confirmacion =="":
        revisar8 = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un ENTER, vuelve a intentarlo")
print()
print()
print()
print()
print()
print()
print()
print()
print("")
print("Raices de la DIVISIÓN:")
print("-----------------------")
print("")
print("Raices del COCIENTE:")
print("--------------------")
print("")
print(C.roots())
print("")
print("Raices del RESIDUO:")
print("-------------------")
print("")
print(R.roots)
print("")
print()
print()
print()
print()
# -----------------------------------------------------------
#                     POLINOMIO 1
revisar9 = False
while revisar9 == False:
    print("")
    confirmacion = input("Oprime ENTER, para CONTINUAR: ")
    if confirmacion =="":
        revisar9 = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un ENTER, vuelve a intentarlo")
print()
print()
print()
print()
print()
print()
print("          Función del Polinomio 1:")
print("         -------------------------")
print()
print()
print("Polinomio 1: ",p1)
print()
print()
pd1 = p1.deriv()
print("Derivada 1: ",pd1)
print()
print("            Punto Crítico: Mínimo y Máximo:")
print("           --------------------------------")  
print()
Xmax = max(pd1.roots())
Xmin = min(pd1.roots())
raices = pd1.roots()
evaluaciones = p1(pd1.roots())
print("X: ",raices)
print("Y: ",evaluaciones)
Y1 = p1(Xmax)
Y2 = p1(Xmin)
Y3 = max(p1(pd1.roots()))
Y4 = min(p1(pd1.roots()))
print()
print("Punto Crítico MÁXIMO: ",Y3)
print("Punto Crítico MÍNIMO: ",Y4)
revisar10 = False
while revisar10 == False:
    print("")
    confirmacion = input("Oprime ENTER, para GRAFICAR Polinomio 1: ")
    if confirmacion =="":
        revisar10 = True
    else:
        print("")       
        print("Ese no es un ENTER, vuelve a intentarlo")
x = np.linspace(start=Xmin,stop=Xmax,num=70)
plt.plot(x,p1(x),"r-",label="Polinomio 1")
plt.plot(x,pd1(x),"b.",label="Derivada")
plt.xlabel("X")
plt.ylabel("Y")
#  TÍTULO PRINCIPAL
plt.title("Polinomio 1")
plt.legend(loc=2)
plt.text(Xmax,Y1,"pc1")
plt.text(Xmin,Y2,"pc2")
plt.grid()
plt.show()
"""
# -----------------------------------------------------------
#                     POLINOMIO 2

revisar9 = False
while revisar9 == False:
    print("")
    confirmacion = input("Oprime ENTER, para CONTINUAR: ")
    if confirmacion =="":
        revisar9 = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un ENTER, vuelve a intentarlo")
print()
print()
print()
print()
print()
print()
print("          Función del Polinomio 2:")
print("         -------------------------")
print()
print()
print("Polinomio 2: ",p2)
print()
print()
pd2 = p2.deriv()
print("Derivada 2: ",pd2)
print()
print("            Punto Crítico: Mínimo y Máximo:")
print("           --------------------------------")  
print()
Xmax = max(pd2.roots())
Xmin = min(pd2.roots())
raices = pd2.roots()
evaluaciones = p2(pd2.roots())
print("X: ",raices)
print("Y: ",evaluaciones)
Y1 = p2(Xmax)
Y2 = p2(Xmin)
Y3 = max(p2(pd2.roots()))
Y4 = min(p2(pd2.roots()))
print()
print("Punto Crítico MÁXIMO: ",Y3)
print("Punto Crítico MÍNIMO: ",Y4)
revisar10 = False
while revisar10 == False:
    print("")
    confirmacion = input("Oprime ENTER, para GRAFICAR Polinomio 2: ")
    if confirmacion =="":
        revisar10 = True
    else:
        print("")       
        print("Ese no es un ENTER, vuelve a intentarlo")
x = np.linspace(start=Xmin,stop=Xmax,num=70)
plt.plot(x,p2(x),"r-",label="Polinomio 2")
plt.plot(x,pd2(x),"b.",label="Derivada 2")
plt.xlabel("X")
plt.ylabel("Y")
#  TÍTULO PRINCIPAL
plt.title("Polinomio 2")
plt.legend(loc=3)
plt.text(Xmax,Y1,"pc1")
plt.text(Xmin,Y2,"pc2")
plt.grid()
plt.show()

"""
"""
# -----------------------------------------------------------
#                           SUMA

revisar9 = False
while revisar9 == False:
    print("")
    confirmacion = input("Oprime ENTER, para CONTINUAR: ")
    if confirmacion =="":
        revisar9 = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un ENTER, vuelve a intentarlo")
print()
print()
print()
print()
print()
print()
print("          Función de la Suma:")
print("         -------------------------")
print()
print()
print("Suma: ",suma)
print()
print()
dsuma = suma.deriv()
print("Derivada: ",dsuma)
print()
print("            Punto Crítico: Mínimo y Máximo:")
print("           --------------------------------")  
print()
Xmax = max(dsuma.roots())
Xmin = min(dsuma.roots())
raices = dsuma.roots()
evaluaciones = suma(dsuma.roots())
print("X: ",raices)
print("Y: ",evaluaciones)
Y1 = suma(Xmax)
Y2 = suma(Xmin)
Y3 = max(suma(dsuma.roots()))
Y4 = min(suma(dsuma.roots()))
print()
print("Punto Crítico MÁXIMO: ",Y3)
print("Punto Crítico MÍNIMO: ",Y4)
revisar10 = False
while revisar10 == False:
    print("")
    confirmacion = input("Oprime ENTER, para GRAFICAR la Suma: ")
    if confirmacion =="":
        revisar10 = True
    else:
        print("")       
        print("Ese no es un ENTER, vuelve a intentarlo")
x = np.linspace(start=Xmin,stop=Xmax,num=70)
plt.plot(x,suma(x),"r-",label="Suma")
plt.plot(x,dsuma(x),"b.",label="Derivada Suma")
plt.xlabel("X")
plt.ylabel("Y")
#  TÍTULO PRINCIPAL
plt.title("Suma")
plt.legend(loc=3)
plt.text(Xmax,Y1,"pc1")
plt.text(Xmin,Y2,"pc2")
plt.grid()
plt.show()
"""
"""
# -----------------------------------------------------------
#                           RESTA
revisar9 = False
while revisar9 == False:
    print("")
    confirmacion = input("Oprime ENTER, para CONTINUAR: ")
    if confirmacion =="":
        revisar9 = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un ENTER, vuelve a intentarlo")
print()
print()
print()
print()
print()
print()
print("          Función de la Resta:")
print("         -------------------------")
print()
print()
print("Resta: ",resta)
print()
print()
dresta = resta.deriv()
print("Derivada: ",dresta)
print()
print("            Punto Crítico: Mínimo y Máximo:")
print("           --------------------------------")  
print()
Xmax = max(dresta.roots())
Xmin = min(dresta.roots())
raices = dresta.roots()
evaluaciones = resta(dresta.roots())
print("X: ",raices)
print("Y: ",evaluaciones)
Y1 = resta(Xmax)
Y2 = resta(Xmin)
Y3 = max(resta(dresta.roots()))
Y4 = min(resta(dresta.roots()))
print()
print("Punto Crítico MÁXIMO: ",Y3)
print("Punto Crítico MÍNIMO: ",Y4)
revisar10 = False
while revisar10 == False:
    print("")
    confirmacion = input("Oprime ENTER, para GRAFICAR la Resta: ")
    if confirmacion =="":
        revisar10 = True
    else:
        print("")       
        print("Ese no es un ENTER, vuelve a intentarlo")
x = np.linspace(start=Xmin,stop=Xmax,num=70)
plt.plot(x,resta(x),"r-",label="Resta")
plt.plot(x,dresta(x),"b.",label="Derivada Resta")
plt.xlabel("X")
plt.ylabel("Y")
#  TÍTULO PRINCIPAL
plt.title("Resta")
plt.legend(loc=4)
plt.text(Xmax,Y1,"pc1")
plt.text(Xmin,Y2,"pc2")
plt.grid()
plt.show()

"""
"""
# -----------------------------------------------------------
#                           MULTIPLICACIÓN

revisar9 = False
while revisar9 == False:
    print("")
    confirmacion = input("Oprime ENTER, para CONTINUAR: ")
    if confirmacion =="":
        revisar9 = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un ENTER, vuelve a intentarlo")
print()
print()
print()
print()
print()
print()
print("          Función de la Multiplicación:")
print("         -------------------------")
print()
print()
print("Multiplicación: ",mult)
print()
print()
dmult = mult.deriv()
print("Derivada: ",dmult)
print()
print("            Punto Crítico: Mínimo y Máximo:")
print("           --------------------------------")  
print()
Xmax = max(dmult.roots())
Xmin = min(dmult.roots())
raices = dmult.roots()
evaluaciones = mult(dmult.roots())
print("X: ",raices)
print("Y: ",evaluaciones)
Y1 = mult(Xmax)
Y2 = mult(Xmin)
Y3 = max(mult(dmult.roots()))
Y4 = min(mult(dmult.roots()))
print()
print("Punto Crítico MÁXIMO: ",Y3)
print("Punto Crítico MÍNIMO: ",Y4)
revisar10 = False
while revisar10 == False:
    print("")
    confirmacion = input("Oprime ENTER, para GRAFICAR la Multiplicación: ")
    if confirmacion =="":
        revisar10 = True
    else:
        print("")       
        print("Ese no es un ENTER, vuelve a intentarlo")
x = np.linspace(start=Xmin,stop=Xmax,num=70)
plt.plot(x,mult(x),"r-",label="Multiplicación")
plt.plot(x,dmult(x),"b.",label="Derivada Multiplicación")
plt.xlabel("X")
plt.ylabel("Y")
#  TÍTULO PRINCIPAL
plt.title("Multiplicación")
plt.legend(loc=3)
plt.text(Xmax,Y1,"pc1")
plt.text(Xmin,Y2,"pc2")
plt.grid()
plt.show()

"""
"""
# -----------------------------------------------------------
#                           División: COCIENTE
revisar9 = False
while revisar9 == False:
    print("")
    confirmacion = input("Oprime ENTER, para CONTINUAR: ")
    if confirmacion =="":
        revisar9 = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un ENTER, vuelve a intentarlo")
print()
print()
print()
print()
print()
print()
print("          Función del COCIENTE:")
print("         -------------------------")
print()
print()
print("COCIENTE: ",C)
print()
print()
dC = C.deriv()
print("Derivada: ",dC)
print()
print("            Punto Crítico: Mínimo y Máximo:")
print("           --------------------------------")  
print()
Xmax = max(dC.roots())
Xmin = min(dC.roots())
raices = dC.roots()
evaluaciones = C(dC.roots())
print("X: ",raices)
print("Y: ",evaluaciones)
Y1 = C(Xmax)
Y2 = C(Xmin)
Y3 = max(C(dC.roots()))
Y4 = min(C(dC.roots()))
print()
print("Punto Crítico MÁXIMO: ",Y3)
print("Punto Crítico MÍNIMO: ",Y4)
revisar10 = False
while revisar10 == False:
    print("")
    confirmacion = input("Oprime ENTER, para GRAFICAR el COCIENTE: ")
    if confirmacion =="":
        revisar10 = True
    else:
        print("")       
        print("Ese no es un ENTER, vuelve a intentarlo")
x = np.linspace(start=Xmin,stop=Xmax,num=70)
plt.plot(x,C(x),"r-",label="COCIENTE")
plt.plot(x,dC(x),"b.",label="Derivada COCIENTE")
plt.xlabel("X")
plt.ylabel("Y")
#  TÍTULO PRINCIPAL
plt.title("COCIENTE")
plt.legend(loc=3)
plt.text(Xmax,Y1,"pc1")
plt.text(Xmin,Y2,"pc2")
plt.grid()
plt.show()
"""
"""
# -----------------------------------------------------------
#                           División: RESIDUO
revisar9 = False
while revisar9 == False:
    print("")
    confirmacion = input("Oprime ENTER, para CONTINUAR: ")
    if confirmacion =="":
        revisar9 = True
    else:
        print("")
        print("")
        print("")
        print("Ese no es un ENTER, vuelve a intentarlo")
print()
print()
print()
print()
print()
print()
print("          Función del RESIDUO:")
print("         -------------------------")
print()
print()
print("RESIDUO: ",R)
print()
print()
dR = R.deriv()
print("Derivada: ",dR)
print()
print("            Punto Crítico: Mínimo y Máximo:")
print("           --------------------------------")  
print()
Xmax = max(dR.roots())
Xmin = min(dR.roots())
raices = dR.roots()
evaluaciones = R(dR.roots())
print("X: ",raices)
print("Y: ",evaluaciones)
Y1 = R(Xmax)
Y2 = R(Xmin)
Y3 = max(R(dR.roots()))
Y4 = min(R(dR.roots()))
print()
print("Punto Crítico MÁXIMO: ",Y3)
print("Punto Crítico MÍNIMO: ",Y4)
revisar10 = False
while revisar10 == False:
    print("")
    confirmacion = input("Oprime ENTER, para GRAFICAR el RESIDUO: ")
    if confirmacion =="":
        revisar10 = True
    else:
        print("")       
        print("Ese no es un ENTER, vuelve a intentarlo")
x = np.linspace(start=Xmin,stop=Xmax,num=70)
plt.plot(x,R(x),"r-",label="RESIDUO")
plt.plot(x,dR(x),"b.",label="Derivada RESIDUO")
plt.xlabel("X")
plt.ylabel("Y")
#  TÍTULO PRINCIPAL
plt.title("RESIDUO")
plt.legend(loc=3)
plt.text(Xmax,Y1,"pc1")
plt.text(Xmin,Y2,"pc2")
plt.grid()
plt.show()
"""