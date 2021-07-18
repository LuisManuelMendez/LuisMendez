# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 07:21:48 2021

@author: Luis Manuel Méndez
"""

# Descomposición en producto de factores primos
print()
print("NÚMERO AL QUE DESEA DESCOMPONER EN FACTORES PRIMOS:")
print("===================================================")
contador2 = 0
contador3 = 0
contador5 = 0
contador7 = 0
f = int(input("f = "))
n00 = f
while f%2 == 0:
    f = int(f/2)
    print(f)
    contador2 += 1
while f%3 == 0:
    f = int(f/3)
    print(f)
    contador3 += 1
while f%5 == 0:
    f = int(f/5)
    print(f)
    contador5 += 1
while f%7 == 0:
    f = int(f/7)
    print(f)
    contador7 += 1
# print("El 2 se repite",contador1,"veces")
# print("El 3 se repite",contador2,"veces")
# print("El 5 se repite",contador3,"veces")
# print("El 7 se repite",contador4,"veces")
mult2 = 1
new_cont2 = 0
while new_cont2 < contador2:
    mult2 = mult2*2
    print(mult2)
    new_cont2 += 1

mult3 = 1
new_cont3 = 0
while new_cont3 < contador3:
    mult3 = mult3*3
    print(mult3)
    new_cont3 += 1
    
mult5 = 1
new_cont5 = 0
while new_cont5 < contador5:
    mult5 = mult5*5
    print(mult5)
    new_cont5 += 1

mult7 = 1
new_cont7 = 0
while new_cont7 < contador7:
    mult7 = mult7*7
    print(mult7)
    new_cont7 += 1
print()
print("FIN")