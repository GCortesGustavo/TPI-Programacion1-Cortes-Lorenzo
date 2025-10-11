def filtrar_por_continente(lista_paises, continente):
    paises_filtrados = []
    continente_lower = continente.strip().lower()

    for pais in lista_paises:
        if pais['continente'].lower() == continente_lower:
            paises_filtrados.append(pais)

    return paises_filtrados

def gestionar_filtro_continente(lista_paises):
    continente_buscado = input('Ingresa el continente buscado: ')

    if not continente_buscado.strip():
        print('Error: El nombre del continente no puede estar vacío.')
        return
    
    resultados = filtrar_por_continente(lista_paises, continente_buscado)

    if not resultados:
        print(f'No se encuentran países en continente: {continente_buscado}')
        return

    print(f"\n--- Países encontrados en: {continente_buscado.capitalize()} ---")
    print(f"{'Nombre':<30} | {'Población':>15} | {'Superficie (km²)':>18} | {'Continente':<15}")
    print("-" * 85)

    for pais in resultados:
        poblacion_formateada = f"{pais['poblacion']:,}"
        superficie_formateada = f"{pais['superficie']:,}"
        
        print(f"{pais['nombre']:<30} | {poblacion_formateada:>15} | {superficie_formateada:>18} | {pais['continente']:<15}")
        print("-" * 85)
