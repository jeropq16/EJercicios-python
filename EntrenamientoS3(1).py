#iniciamos creando un diccionario el cual definimos como inventario 
inventario = {}
#creamos varias funciones para mas adelante llamarlas en un menu de opciones
def añadirp():
    nombre = input("Ingrese el nombre del producto: ")
    while not nombre.replace(" ", "").isalpha():  # Permitir espacios en nombres
        print("Caracteres invalidos")
        print("Por favor ingrese solo letras y espacios")
        nombre = input()

    while True:
        precio = input("¿Cuál es el precio del producto?: ")
        try:
            precio = float(precio)
            if precio > 0:
                break
            else:
                print("El valor debe ser superior a 0.")
        except ValueError:
            print("Ingresa un precio válido.")

    while True:
        cantidad = input("¿Cuántas cantidades hay disponibles?: ")
        try:
            cantidad = int(cantidad)
            if cantidad > 0:
                break
            else:
                print("El valor debe ser superior a 0.")
        except ValueError:
            print("Ingresa una cantidad válida.")

    inventario[nombre] = {'precio': precio, 'cantidad': cantidad}
    print(f"Producto {nombre} añadido correctamente.")
#usamos un .replace y un .isalpha para validar que solo se ingresen letras el .replace es para permitir la entrada de espacios en el input del usuario 
def consultarp():
    nombre = input("Ingrese el nombre del producto: ")
    while not nombre.replace(" ", "").isalpha():  # Permitir espacios en nombres
        print("Caracteres invalidos")
        print("Por favor ingrese solo letras y espacios")
        nombre = input()
    if nombre in inventario:
        producto = inventario[nombre]
        print(f"Producto: {nombre}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print(f"El producto {nombre} no está en el inventario.")

def actualizarp():
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    while not nombre.replace(" ", "").isalpha():  # Permitir espacios en nombres
        print("Caracteres invalidos")
        print("Por favor ingrese solo letras y espacios")
        nombre = input()
    
    if nombre in inventario:
        while True:
            try:
                nuevoprecio = float(input("¿Cuál es el nuevo precio del producto? "))
                if nuevoprecio > 0:
                    break
                else:
                    print("El valor debe ser superior a 0.")
            except ValueError:
                print("Ingresa un precio válido.")

        inventario[nombre]['precio'] = nuevoprecio
        print(f"El precio del producto {nombre} ha sido actualizado.")
    else:
        print(f"El producto {nombre} no existe en el inventario.")

def eliminarp():
    nombre = input("Ingrese el nombre del producto que quiere eliminar: ")
    while not nombre.replace(" ", "").isalpha(): 
        print("Caracteres invalidos")
        print("Por favor ingrese solo letras y espacios")
        nombre = input()
    
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto {nombre} eliminado correctamente.")
    else:
        print(f"El producto {nombre} no está en el inventario.")
#usamos lambda para sumar y despues multiplicar el total de inventario 
def calcularvalor():
    total = sum(map(lambda producto: float(producto['precio']) * int(producto['cantidad']), inventario.values()))
    print(f"El valor total del inventario es: {total}")

def menu():
    print("Menú de gestión de inventario")
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar precio")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("6. Salir")
#funcion para ejecutar el menú
def gestionari():
    while True:
        menu()
        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Por favor ingrese un número válido.")
            continue
        
        if opcion == 1:
            añadirp()
        elif opcion == 2:
            consultarp()
        elif opcion == 3:
            actualizarp()
        elif opcion == 4:
            eliminarp()
        elif opcion == 5:
            calcularvalor()
        elif opcion == 6:
            print("Gracias por usar el programa")
            break
        else:
            print("Por favor ingrese una opción válida.")

gestionari()
