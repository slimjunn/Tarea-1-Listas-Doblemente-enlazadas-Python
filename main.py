from lista_doble import ListaDoblementeEnlazada

def menu():
    lista = ListaDoblementeEnlazada()

    while True:
        print("\n----- MENÚ LISTA DOBLEMENTE ENLAZADA -----")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Eliminar por carnet")
        print("4. Mostrar lista")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")
            lista.insertar_al_principio(nombre, apellido, carnet)

        elif opcion == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")
            lista.insertar_al_final(nombre, apellido, carnet)

        elif opcion == "3":
            carnet = input("Ingrese el carnet a eliminar: ")
            lista.eliminar_por_valor(carnet)

        elif opcion == "4":
            lista.mostrar_lista()

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
