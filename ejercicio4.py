#operadores relacionales

#1Pide dos números e indica cuál es mayor o si son iguales.

num1=int(input("escribe 1 numero"))
num2=int(input("escribe otro numero"))
if num1>num2:
    print(str(num1) + "es mayor")
else:
    print(str(num2) + "es mayor")



#2 Solicita una edad y determina si la persona es menor de edad (menor a 18).

edad= int(input("cual es tu edad: "))
if edad>=18:
    print("Bienvenido")
else:
    print("no puedes entrar eres menor de edad")


#3 

texto1= input("ingresa una palabra")
texto2= input("por favor ingresa una palabra")
if texto1 == texto2:
    print("los textos son iguales") 
else:
    print("el texto es diferente.")

