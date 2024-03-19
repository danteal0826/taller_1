#para generar un numero aleatorio en python

import random

#la funcion input() captura un dato desde el teclado, como si fuera una cadena de texto
a=input("Limite inferior: ")
b=input("Limite superior: ")

#Convertir a y b a un entero
a=int(a)
b=int(b)
respuesta= random.randint(a,b)
print("numero:",respuesta)