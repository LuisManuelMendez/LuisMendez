# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 09:50:14 2021

@author: Luis Manuel Méndez
"""
"""
            PROGRAMA PARA HALAR LA RAÍZ CUADRADA DE UN NÚMERO
"""
print()
print("Autor: Luis Manuel Méndez")
print()

respuesta = False
while respuesta==False:
    b = float(input("Raíz Cuadrada de = "))
    a = float(b**(1/2))
    print()
    print("Resultado de la Raíz de",b,"=",round(a,2))
    print()
    pregunta = input("¿Desea sacar la raíz a otro número, s ó n:? ")
    if pregunta =="n":
        respuesta = True
print()
print("FIN")