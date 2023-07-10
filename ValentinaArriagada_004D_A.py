import datetime

# Variables globales
entradas_platinum = [False] * 20
entradas_gold = [False] * 30
entradas_silver = [False] * 50
asistentes = []
ganancias = {'Platinum': 0, 'Gold': 0, 'Silver': 0}


def mostrar_menu():
    print("---- MENÚ ----")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")


def comprar_entradas():
    cantidad = int(input("Ingrese la cantidad de entradas a comprar (1-3): "))
    if cantidad < 1 or cantidad > 3:
        print("Cantidad inválida. Intente nuevamente.")
        return

    print("Ubicaciones disponibles:")
    mostrar_ubicaciones_disponibles()

    for _ in range(cantidad):
        ubicacion = int(input("Ingrese la ubicación deseada: "))
        if ubicacion < 1 or ubicacion > 100:
            print("Ubicación inválida. Intente nuevamente.")
            continue

        if ubicacion <= 20 and not entradas_platinum[ubicacion - 1]:
            entradas_platinum[ubicacion - 1] = True
            asistente = input("Ingrese el RUN del asistente: ")
            asistentes.append((ubicacion, asistente, 'Platinum'))
            ganancias['Platinum'] += 120000
            print("Compra realizada correctamente.")
        elif ubicacion <= 50 and not entradas_gold[ubicacion - 21]:
            entradas_gold[ubicacion - 21] = True
            asistente = input("Ingrese el RUN del asistente: ")
            asistentes.append((ubicacion, asistente, 'Gold'))
            ganancias['Gold'] += 80000
            print("Compra realizada correctamente.")
        elif ubicacion <= 100 and not entradas_silver[ubicacion - 51]:
            entradas_silver[ubicacion - 51] = True
            asistente = input("Ingrese el RUN del asistente: ")
            asistentes.append((ubicacion, asistente, 'Silver'))
            ganancias['Silver'] += 50000
            print("Compra realizada correctamente.")
        else:
            print("Ubicación no disponible. Intente nuevamente.")


def mostrar_ubicaciones_disponibles():
   print("***********************ESCENARIO**************************")
   print(" |Fila |1| |2| |3| |4| |5| |6| |7| |8| |9| |10| :")
   print(" |Fila |11| |12| |13| |14| |15| |16| |17| |18| |19| |20| :")
   print(" |Fila |21| |22| |23| |24| |25| |26| |27| |28| |29| |30| :")
   print(" |Fila |31| |32| |33| |34| |35| |36| |37| |38| |39| |40| :")
   print(" |Fila |41| |42| |43| |44| |45| |46| |47| |48| |49| |50| :")
   print(" |Fila |51| |52| |53| |54| |55| |56| |57| |58| |59| |60| :")
   print(" |Fila |61| |62| |63| |64| |65| |66| |67| |68| |69| |70| :")
   print(" |Fila |71| |72| |73| |74| |75| |76| |77| |78| |79| |80| :")
   print(" |Fila |81| |82| |83| |84| |85| |86| |87| |88| |89| |90| :")
   print(" |Fila |91| |92| |93| |94| |95| |96| |97| |98| |99| |100| :")
   print("\n Entradas Disponibles")

   


def ver_listado_asistentes():
    if len(asistentes) == 0:
        print("No hay asistentes registrados.")
    else:
        print("Listado de asistentes:")
        for asistente in sorted(asistentes, key=lambda x: x[1]):
            print(f"RUN: {asistente[1]}, Ubicación: {asistente[0]}, Tipo: {asistente[2]}")


def mostrar_ganancias_totales():
    print("Tipo entrada\tcantidad\ttotal")
    total = 0
    for tipo, cantidad in ganancias.items():
        precio = 120000 if tipo == 'Platinum' else (80000 if tipo == 'Gold' else 50000)
        print(f"{tipo}\t\t{cantidad}\t\t${cantidad * precio}")
        total += cantidad * precio
    print(f"Total\t\t\t{sum(ganancias.values())}\t\t${total}")


# Función principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            comprar_entradas()
        elif opcion == '2':
            mostrar_ubicaciones_disponibles()
        elif opcion == '3':
            ver_listado_asistentes()
        elif opcion == '4':
            mostrar_ganancias_totales()
        elif opcion == '5':
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            fecha_actual = datetime.date.today().strftime("%d/%m/%Y")
            print(f"\nGracias por utilizar el sistema, {nombre} {apellido}.")
            print(f"Fecha de salida: {fecha_actual}")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == '__main__':
    main()
