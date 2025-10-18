from utils.buscar_pais import buscar_pais_por_nombre
from utils.carga_datos import cargar_paises_desde_csv
from utils.filtro_continente import gestionar_filtro_continente
from utils.filtro_rango_poblacion import filtrar_por_rango_poblacion
from utils.menu import mostrar_menu
from utils.estadisticas import calcular_y_mostrar_estadisticas

def main():
    NOMBRE_ARCHIVO_CSV = "paises.csv"

    lista_paises = cargar_paises_desde_csv(NOMBRE_ARCHIVO_CSV)
    
    if not lista_paises:
        print("No se cargaron los datos o el archivo está vacío. El programa se cerrará")
        return

    print(f"\n¡Carga de datos exitosa! Se cargaron {len(lista_paises)} países.")
    print("Ejemplo de datos del primer país:", lista_paises[5])
    
    print("Bienvenido al sistema de gestión de países")

    bandera_menu_princial :bool = True

    while bandera_menu_princial:
        mostrar_menu()

        opcion_menu :str = input("Selecciona una opción del menú: ")

        if opcion_menu == "1":
            print("\nHas elegido la opción 1: Buscar país por nombre")
            buscar_pais_por_nombre(lista_paises)
            pass
        elif opcion_menu == "2":
            print("\nHas elegido la opción 2: Filtrar países por continente")
            gestionar_filtro_continente(lista_paises)
            pass
        elif opcion_menu == "3":
            print("\nHas elegido la opción 3: Filtrar países por población")
            filtrar_por_rango_poblacion(lista_paises)
        elif opcion_menu == "4":
            print("\nHas elegido la opción 4: Filtrar países por superficie")
            pass
        elif opcion_menu == "5":
            print("\nHas elegido la opción 5: Ordenar países")
            pass
        elif opcion_menu == "6":
            print("\nHas elegido la opción 6: Mostrar estadísticas")
            calcular_y_mostrar_estadisticas(lista_paises)
            pass
        elif opcion_menu == "7":
            print("\nGracias por utilizar el programa")
            bandera_menu_princial = False
        else:
            print("\nOpción no válida. Ingresa un número del menú.")


if __name__ == "__main__":
    main()