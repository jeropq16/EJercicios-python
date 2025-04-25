

#5. Operadores lógicos

#1
edad= int(input("cual es tu edad: "))
licencia= input("tienes licencia?: ")
if edad >=18 and licencia == "si":
    print("puedes conducir")
else:
    print("no puedes conducir")


#2

experiencia = input("tienes experiencia laboral?: ")
titulo= input("tienes un titulo univeristario?: ")

if experiencia and titulo == "si":
    print("puedes aplicar")
else:
    print("no puedes aplicar")

#3 
numero=int(input("dame un numero: "))
if numero <50 and numero >10:
    print("eel numero esta dentro de el rango de 1 a 50")
else:
    print("el numero esta fuera de rango")


