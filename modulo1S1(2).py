print("Bienvenido a la calculadora de costos")

#definimos variables y le preguntamos al usuario su nombre, nombre del producto y el precio de el
Nombre = input("Cual es tu nombre: ")
while not Nombre.isalpha():
    print("Caracteres invalidos")
    print("Por favor ingrese solo letras")
    Nombre=input()

Nombreproducto = input("Ingrese el nombre del prodoucto: ")
while not Nombreproducto.isalpha():
    print("Caracteres invalidos")
    print("Por favor ingrese solo letras")
    Nombreproducto=input()



while True:
    
    PrecioU=input("Cual es el precio unitario del producto?")
    if not  PrecioU.isalpha():
        if float(PrecioU) >0 :
            break
        else:
            print("el valor debe ser superior a 0 ")
            continue
    else:
        print("ngresa un cantidad valida")



#creamos un bucle que no permita al usuario poner un valor menor a 1 en precio y cantidad


cantidad = int(input("¿Què cantidad vas a comprar?: "))
while cantidad < 1:
    print("el valor debe ser superior a 0" + " " + (Nombreproducto))
    print("ingresa un cantidad valida")
    cantidad=int(input())

#calculamos el precio total de la compra sin el descuento y le mostramos el valor al usuario

PrecioT = cantidad * float(PrecioU)

print(Nombre + " "  "el precio total de " + Nombreproducto + " " "sin descuento es: " + str(PrecioT))

#Creamos una condicional para preguntarle que valor de descuento quieres agregarle a la compra,
#en caso de que sean menos de 15 unidades, el sistema le muestra al usuario que el descuento es de minimo 15 unidades

if cantidad >=15:
    descuento = int(input("Que porcentaje de descuento le vas a aplicar: "))
    while descuento < 1:
        print("el valor debe ser superior a 0")
        print("ingresa una cantidad mayor a 0")
        descuento = int(input())
    descuentot = PrecioT * (descuento/100)
    descuentoF = PrecioT - descuentot
    print(Nombre + " " "el precio con descuento de " + Nombreproducto + " " "es : " + str(descuentoF))

#calculamos que precio va a tener cada unidad despues de el descuento (si aplica) y le mostramos al usuario los datos finales de la compra

    unidadconD = descuentoF / cantidad

    print("Esta fue tu compra: ")
    print("Compraste" + " " + str(cantidad) + str(Nombreproducto))
    print("Cada unidad te salió en:" + str(unidadconD))
    print("Te ahorraste" + " " + str(descuentot))
    print("¡Gracias por tu compra!")

else:
    print("La compra minima para el descuento es de 20 unidades")  
    print("Esta fue tu compra: ")
    print("Compraste " + " " + str(cantidad) + str(Nombreproducto))
    print("¡Gracias por tu compra!")