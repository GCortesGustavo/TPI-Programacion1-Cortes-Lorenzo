from utils.menu import mostrar_menu

def main():
    # lista_paises = cargar_datos_csv('paises.csv')

    print('Bienvenido al sistema de gestión de países')

    bandera_menu_princial :bool = True

    while bandera_menu_princial:
        mostrar_menu()

        opcion_menu :str = input('Selecciona una opción del menú: ')

        if opcion_menu == "1":
            print("\nHas elegido la opción 1: Buscar país por nombre")
            pass
        elif opcion_menu == "2":
            print("\nHas elegido la opción 2: Filtrar países por continente")
            pass
        elif opcion_menu == "3":
            print("\nHas elegido la opción 3: Filtrar países por población")
            pass
        elif opcion_menu == "4":
            print("\nHas elegido la opción 4: Filtrar países por superficie")
            pass
        elif opcion_menu == "5":
            print("\nHas elegido la opción 5: Ordenar países")
            pass
        elif opcion_menu == "6":
            print("\nHas elegido la opción 6: Mostrar estadísticas")
            pass
        elif opcion_menu == "7":
            print("\nGracias por utilizar el programa")
            bandera_menu_princial = False
        else:
            print("\nOpción no válida. Ingresa un número del menú.")


if __name__ == "__main__":
    main()