# -*- coding: cp1252 -*-
"""

Tarea 1 Ayudantia Computación Paralela Segundo Semestre 2014. Problema 3:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Integrantes: Jonathan León S. (johnnysavior)
             Juan Cortez G. (juannmmaa)
             Christopher Salvatierra L. (Chris2141)
             Felipe Alvarez R. (fliseven)
"""
#declaramos nuestro primer numero divisor
x=int(2)
lista=[]  #lista para almacenar los factores primos
numero = 600851475143  #el numero en particular al cual queremos descomponer...

while (numero != 1):

    if(numero % x == 0): #divimos el numero por el numero x defido anteriormente, si        
        lista.append(x)  #la division da resto 0, quiere decir que x es un factor primo del numero,
        numero = numero / x;  # por ende lo almacenamos en la lista y dividimos el numero por x
    else:
        x = x + 1    #si al realizar las divisiones consecutivas da resto distinto de 0, aumentamos x en 1.
print lista[len(lista)-1]  #finalmente imprimimos el ultimo factor primo almacenado en la lista, que corresponde
                             #al mayor.
