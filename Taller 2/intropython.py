#Comentario de una linea 
#Todo lo que va despues es ignorado por el interprete de python
#interprete de python

#Variable: espacios de memoria, con nombre, donde guardo valores
#Los nombres de variables deben ser cortos, descriptivos, NO TENER ESPACIOS
#EN BLANCO ni caracteres especiales, no deben empezar por un numero

#Descriptivo significa que representa la categoria del dato que quiero guardar 
#En python las variables pueden contener cualquier dato de tipo primitivo
#numeros(entero, reales), cadenas de caracteres (string), booleanos(true, false)
#caracteres (letras)

variable=1

variable='Juventud divino tesoro, te vas para no volver'

variable=True

variable='a'

variable=3.1415926535

#Para asignar un valor a la variable se usa el operador =

#Operadores: mecanismo para obtener un dato a partir de otros datos
#Los datos que intervienen se llaman operandos
#Aritmeticos: + - * / %
#De comparacion: retorna True o False <= >= < > == !=
#Logica booleana: OR AND, retornan True o False de acuerdo a la tabla de verdad
#Los operandos siempre son booleanos(True o False)

a=True
b=False

print(a and b)

#Los operadores booleanos y de conmparacion con muy utilizados al definir condiciones

#Sentencias de control de codigo: en general un programa se ejecuta linea por linea de manera secuecncial
#Se puede romper esa secuencialidad empleando un conjunto de sentencias (expresiones) que permite:
#1. Seleccionar la ejecucion de un bloque de codigo
#2. Repetir la ejecucion de un bloque de codigo
#3. Seleccionar entre ejecutar un bloque de codigo u otro bloque de codigo
#De esa manera podemos "romper" la secuencialidad
#Principios del paradigma de programacion estructurado

#Sentencia if. si se cumple una condicion (se evalua como True) se ejcuta un bloque de codigo

entrada= int(input("Cuantos años tiene? "))

if entrada<18:
    print("Es menor de edad.")
else:
    print("Ya es mayor de edad.")
    
#Taller, crear un programa que genere un numero aleatorio entre 1 y 12, si el numero es 7 imprimir gano, sino imprimir deje el juego

