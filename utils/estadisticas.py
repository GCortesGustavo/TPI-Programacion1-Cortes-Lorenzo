def mostrar_menu_estadisticas():
    """Imprime en la consola el sub-menú de opciones de estadísticas."""
    print("\n--- SUB-MENÚ DE ESTADÍSTICAS ---")
    print("1. País con Mayor y Menor Población")
    print("2. Promedio de Población y Superficie")
    print("3. Cantidad de Países por Continente")
    print("4. Volver al Menú Principal")
    print("----------------------------------")


def mostrar_extremos_poblacion(lista_paises):
    pais_mas_poblado = max(lista_paises, key=lambda p: p['poblacion'])
    pais_menos_poblado = min(lista_paises, key=lambda p: p['poblacion'])

    print("\nExtremos de Población:")
    print(f"  País más poblado  : {pais_mas_poblado['nombre']:<10} ({pais_mas_poblado['poblacion']:,})")
    print(f"  País menos poblado: {pais_menos_poblado['nombre']:<10} ({pais_menos_poblado['poblacion']:,})")

def mostrar_promedios(lista_paises):
    total_paises = len(lista_paises)
    
    total_poblacion = sum(pais['poblacion'] for pais in lista_paises)
    total_superficie = sum(pais['superficie'] for pais in lista_paises)

    promedio_poblacion = total_poblacion / total_paises if total_paises > 0 else 0
    promedio_superficie = total_superficie / total_paises if total_paises > 0 else 0

    print("\nPromedios Globales:")
    print(f"  Población promedio  : {promedio_poblacion:,.0f} habitantes")
    print(f"  Superficie promedio: {promedio_superficie:,.0f} km²")

def mostrar_conteo_por_continente(lista_paises):
    conteo_continentes = {}
    for pais in lista_paises:
        continente = pais['continente']
        conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1
    
    print("\nCantidad de Países por Continente:")
    print(f"  {'Continente':<10} | {'Nº de Países':>10}")
    print("-" * 35)
    for continente, conteo in sorted(conteo_continentes.items()):
        print(f"  {continente:<15} | {conteo:>15}")

def gestionar_estadisticas(lista_paises):
    if not lista_paises:
        print("No hay datos de países para calcular estadísticas.")
        return

    while True:
        mostrar_menu_estadisticas()
        opcion = input("Seleccione una opción de estadística: ")

        if opcion == '1':
            mostrar_extremos_poblacion(lista_paises)
        elif opcion == '2':
            mostrar_promedios(lista_paises)
        elif opcion == '3':
            mostrar_conteo_por_continente(lista_paises)
        elif opcion == '4':
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")