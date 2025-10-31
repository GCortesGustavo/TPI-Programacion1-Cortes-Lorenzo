# ESTE ARCHIVO YA NO TIENE USO POR EL CAMBIO HACIA FLASK- SE MANEJA LA INFORMACIÓN EN APP.PY

from utils.carga_datos import obtener_paises_de_api, guardar_paises_en_csv, cargar_paises_desde_csv
from utils.buscar_pais import buscar_pais
from utils.filtro_continente import filtrar_por_continente
from utils.filtro_rango_poblacion import filtrar_por_poblacion
from utils.filtro_rango_superficie import filtrar_por_superficie
from utils.ordenar_paises import ordenar_paises
from utils.estadisticas import (
    calcular_extremos_poblacion,
    calcular_promedios,
    calcular_conteo_por_continente
)
from utils.menu import mostrar_menu


def mostrar_tabla_paises(lista_paises, titulo="Resultados"): #Muestra una tabla simple de los paises en el csv
    """Función reutilizable para imprimir una lista de países en formato tabla."""
    if not lista_paises: 
        print(f"\n>> No se encontraron países para mostrar.") 
        return

    print(f"\n--- {titulo} ---")
    print(f"{'Nombre':<30} | {'Población':>15} | {'Superficie (km²)':>18} | {'Continente':<15}")
    print("-" * 85)
    for pais in lista_paises:
        poblacion = f"{pais['poblacion']:,}"
        superficie = f"{pais['superficie']:,}"
        print(f"{pais['nombre']:<30} | {poblacion:>15} | {superficie:>18} | {pais['continente']:<15}")
    print("-" * 85)

def mostrar_menu_estadisticas():  #muestra el menu de estadisticas
    """Imprime en la consola el sub-menú de opciones de estadísticas."""
    print("\n--- SUB-MENÚ DE ESTADÍSTICAS ---")
    print("1. País con Mayor y Menor Población")
    print("2. Promedio de Población y Superficie")
    print("3. Cantidad de Países por Continente")
    print("4. Volver al Menú Principal")
    print("----------------------------------")


def gestionar_busqueda_consola(lista_paises): #gestiona la busqueda de paises ingresando el nombre
    query = input("Ingrese el nombre (o parte del nombre) del país a buscar: ")
    resultados = buscar_pais(lista_paises, query)
    mostrar_tabla_paises(resultados, f"Resultados para '{query}'")

def gestionar_filtros_consola(lista_paises): #gestiona los filtros de paises por contiente
    print("Filtro por continente:")
    continente = input("Ingrese el nombre del continente: ")
    resultados = filtrar_por_continente(lista_paises, continente)
    mostrar_tabla_paises(resultados, f"Países en {continente.capitalize()}")
    # Se podrían añadir aquí las peticiones para los otros filtros...

def gestionar_ordenamiento_consola(lista_paises): #gestiona el ordenamiento de paises por nombre, poblacion o superficie en el csv
    criterio = input("Ordenar por (nombre, poblacion, superficie): ").lower()
    orden = input("Orden (asc, desc): ").lower()
    
    resultados = ordenar_paises(lista_paises, criterio, orden)
    mostrar_tabla_paises(resultados, f"Países ordenados por {criterio} ({orden})")

def gestionar_estadisticas_consola(lista_paises): #gestiona las estadisticas de los paises en el csv
    while True:
        mostrar_menu_estadisticas()
        opcion = input("Seleccione una opción de estadística: ")
        if opcion == '1':
            mas, menos = calcular_extremos_poblacion(lista_paises)
            if mas and menos:
                print(f"\nPaís más poblado: {mas['nombre']} ({mas['poblacion']:,})")
                print(f"País menos poblado: {menos['nombre']} ({menos['poblacion']:,})")
        elif opcion == '2':
            prom_pob, prom_sup = calcular_promedios(lista_paises)
            print(f"\nPoblación promedio: {prom_pob:,.0f} hab.")
            print(f"Superficie promedio: {prom_sup:,.0f} km²")
        elif opcion == '3':
            conteo = calcular_conteo_por_continente(lista_paises)
            print("\nConteo de países por continente:")
            for cont, num in conteo.items():
                print(f"  - {cont}: {num} países")
        elif opcion == '4':
            break
        else:
            print("Opción no válida.")

def main(): #funcion principal que ejecuta el programa
    NOMBRE_ARCHIVO_CSV = "paises.csv"
    
    paises_de_api = obtener_paises_de_api()
    if paises_de_api:
        guardar_paises_en_csv(paises_de_api, NOMBRE_ARCHIVO_CSV)
    
    lista_paises = cargar_paises_desde_csv(NOMBRE_ARCHIVO_CSV)
    if not lista_paises:
        print("No se pudieron cargar datos para iniciar el programa. Cerrando.")
        return

    print(f"\n¡Carga de datos exitosa! Se cargaron {len(lista_paises)} países.")
    print("Bienvenido al sistema de gestión de países")

    while True:
        mostrar_menu()
        opcion_menu = input("Selecciona una opción del menú: ")

        if opcion_menu == "1":
            gestionar_busqueda_consola(lista_paises) 
        elif opcion_menu == "2":
            gestionar_filtros_consola(lista_paises)
        elif opcion_menu == "3":
            print("Opción no implementada en esta versión de consola. (Filtro Población)")
        elif opcion_menu == "4":
            print("Opción no implementada en esta versión de consola. (Filtro Superficie)")
        elif opcion_menu == "5":
            gestionar_ordenamiento_consola(lista_paises)
        elif opcion_menu == "6":
            gestionar_estadisticas_consola(lista_paises)
        elif opcion_menu == "7":
            print("\nGracias por utilizar el programa")
            break
        else:
            print("\nOpción no válida. Ingresa un número del menú.")

if __name__ == "__main__":
    main()