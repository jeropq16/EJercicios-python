#2. Tipos de datos en Python

#1

entero = 20
decimal= 1.4
booleano = True
cadena= "tipos de datos en python"
cadenaconnum= 16

entero= int(cadenaconnum)

num2= 29

resultado=(entero + num2)
print("el resultado de la suma de entero y cadena es: ")
print(resultado)



#2

texto= input("introduce un numero decimal")

Nfloat= float(texto)

multiplicacion= Nfloat * 2
print("el resultado multiplicado por 2 es:")
print(float(multiplicacion))


#3

texto1= input("escribe algio")
X= False
try:
    valor=float(texto1)
    X= True
except ValueError:
      X= False

    
if X == True:
    print("el numero se puede convertir")
else:
     print("no se puede convertir")