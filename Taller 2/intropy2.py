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

#Ciclos copntrolados po rel valor de una variable
import random
a=0

while a !=5:
    a=random.randint(1,10)
    print(a)
    
print("Se acabó")