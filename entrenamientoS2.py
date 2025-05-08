
#pedimos nota al usuario y usamos un if elif else para validar la calificacion y ver si aprobó

nota = float(input("Ingrese su nota (0-100): "))
if nota < 0 or nota > 100:
            print("Solo se permiten valores entre 0 y 100.")
elif nota == 100:
            print("¡Aprobaste con la nota maxima!")
elif nota >=60:
      print("Aprobaste")           
else:
    print(" No aprobaste.")

#creamos una funcion para usar el while true que nos permita no tener errores innesperados

def ingresar_calificaciones():
    while True:
        try:
            entrada = input("Ingrese las calificaciones separadas por comas: ")
            if not entrada.strip():
                print("Error, solo numeros separados por comas")
                continue

            #quitamos los espacios con el metodo .strip y le decimos al sistema cn el metodo.split que lo separe por comas
            calificaciones = [float(cali.strip()) for cali in entrada.split(",")]
            
            if not all(0 <= cali <= 100 for cali in calificaciones):
                print("Solo calificaciones de 0 a 100: ")
            else:
                return calificaciones
        except ValueError:
            print("Error, solo numeros separados por comas")

calificaciones = ingresar_calificaciones()

# sumamos las calificaciones y dividimos entre el numero de calificaciones con len

promedio = sum(calificaciones) / len(calificaciones)

print(f"El promedio de las {len(calificaciones)} calificaciones es: {promedio}")

while True:
        valor = float(input("Ingrese un valor para contar cuántas calificaciones son mayores: "))
        
        mayores = sum(1 for cali in calificaciones if cali > valor)
        
        print(f"Hay {mayores} calificaciones mayores que {valor}.")
        break

# ingresan las calificaciones de nuevo y usamos los mismos metodos que se utilizaron arriba
entrada1 = input("Ingrese las calificaciones separadas por comas (0-100): ")
calificaciones1 = [float(cali.strip()) for cali in entrada1.split(",")]

especifica = float(input("Ingrese una calificación específica a buscar: "))

# si la calificacion es mayor a 100 o menor a 0 volvemos a pedir una cantidad valida

if especifica >100 or especifica <0:
      print("cantidad invalida")
      float(input("ingrese una calificacion valida"))

#usamos el metodo .count para que imprima un 1 por cada vez que encuentre una calificación igual a la que el usuario ingresó

contador = calificaciones.count(especifica)
if contador > 0:
    print(f"La calificación {especifica} aparece {contador} veces.")
else:
    print(f"La calificación {especifica} no aparece en la lista.")

