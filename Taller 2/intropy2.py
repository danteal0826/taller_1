# While
# while<condicion_Verdadera>:
#   cuerpo del ciclo
#Condiciones son: expresiones booleanas (or, and) y operaciones de comparacion
#Ciclos controlados por un contador enteros
i=0

while i<10:
    print("ciclo")
    #Importante modificar el valor del contador
    i=i+1 #i+=1<-equivalente; i++ en python no existe

#Ciclos copntrolados por el valor de una variable
import random
a=0

while a !=5:
    a=random.randint(1,10)
    print(a)
    
print("Se acabó")

#Ciclos controlados por un evento

a=0
'''while 1==1:
    a=int(input("Ingrese un número: "))
    
    if a==10:
        break''' #Rompe el ciclo en donde se encuentra a donde ocurre un evento determinado

#for: se utiliza para recorrer un "iterable"(cualquier cosa que se pueda recorrer: listas, tuplas, diccionarios...)

#Lista: conjunto de variables organizadas en espacios consecutivos de memoria
# A las que se les asigna un unico nombre. se diferencian por la posicion que ocupan respecto al primer elemento de la lista

miLista=[1, True, "Textos", 3.89]
miLista2=[] #Puede ir vacia

print (miLista)
print (miLista2)

#En python todos son objetos
#Operador "." es para acceder a los comportamientos de una lista 
#agrega un objeto al final de la lista
print(miLista)
miLista.append(45)
print(miLista)
#antes del indice que yo le diga
#print(miLista)
#miLista.insert("Hola")
#print(miLista)
#Remueve el item en el indice que yo le diga, por defecto remueve el ultimo elemento
print(miLista)
miLista.pop(2)
print(miLista)
#Lo ordena de mayor a menor
miLista1=[5,45,89,6,7]
print(miLista1)
miLista.sort()
print(miLista1)
#Cantidad de elementos que tiene una lista
print(len(miLista))

#Tupla: lista inmutable. No se puede modificar
miTupla=(2,45,6,8,9,10)

#For: ciclo para recorrer iterables. el cuerpo del for se repite tantas veces como elementos tenga el iterable
#En cada ciclo se guarda el valor del elemento del indice correspondiente en una variable definida
miLista1=[5,45,89,6,7]
#Estructura del for en python
#for <Variable_dodn_guardo_el_elemento in iterable:

for x in miLista1:
    print(x)
    #break
    
for x in miLista1:
    if x>50:
       print("Grande")
       
#Si solo utilizo el iterable para definir la cantidad de repticiones
#entonces no es necesario la variable

for _ in miLista1: #"_" sirve para omitir la variable, para saber cuantas veces se repite el ciclo for
    print("Ciclo")
    
#Si no tengo un iterable puedo usar la funcion renge() para generar una secuencia de numeros
for x in range(-10,10): #Incluye el primer valor, excluye el ultimo
    print (x)
    
#Taller crear un programma que pida un numero al usuario y:
#1. imprima los numeros impares entre -numero y numero
#2. imprima los numeros primos entre 0 y numero*100
#El programa debe garantizar que el usuario ingrese un numero positivo >0