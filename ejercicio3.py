#3. Operadores en Python

#1
base= input("ingresa la base del rectangulo: ")
altura= input ("ingresa la altura: ")
resultado= int(base) * int(altura) /2
print("el area del rectangulo es")
print (int(resultado))

#2 Dado un precio y un porcentaje de descuento, muestra el valor final a pagar.

precio = int(input("Ingresa el precio: "))
descuento= int(input("Cual es el porcentaje de descuento: "))

descuentot = precio * (descuento/100)
descuentoF = precio - descuentot

print("el precio con el descuento es de " + str(descuentoF))

#3 Calcula el residuo de dividir dos números dados por el usuario.

dividendo=float(input("Ingresa el primer numero: "))
divisor=float(input("ingresa el numero por el que se va a dividir"))

resultado1= dividendo % divisor
print("el residuo de la division es: ")
print (float(resultado1))

#4Escribe una fórmula que use al menos tres operadores diferentes y muestre el resultado.

suma= int(input("ingresa un numero: "))
multiplicacion= int(input("ingresa por el numero que lo quieres multiplicar"))
division= int(input("ingresa por la cantidad q lo quieres dividir: "))
resultado2= suma * multiplicacion / division
print ("este es el resultado: " + str(resultado2))