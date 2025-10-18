def calcular_y_mostrar_estadisticas(lista_paises):
    if not lista_paises:
        print('No hay una lista para mostrar los países')
        return
    
    print('Estadísticas globales')

    #1) Paises con mayor densidad de población
    paises_con_mayor_densidad = []
    for pais in lista_paises:
        if pais['superficie'] > 0:
            densidad = pais['poblacion'] / pais['superficie']
            nuevo_pais = pais.copy()
            nuevo_pais['densidad'] = densidad
            paises_con_mayor_densidad.append(nuevo_pais)

    paises_ordenados = sorted(paises_con_mayor_densidad, key=lambda p: p['densidad'], reverse=True)

    print('Paises con mayor densidad: ')
    for i, pais in enumerate(paises_ordenados[:5], 1):
        print(f' {i}, {pais['nombre']} : {pais['densidad']:.2f} Hab/km²')

    print('------------------------------------------')
    
    #2. Resumen por Continente
    resumen_continentes = {}
    for pais in lista_paises:
        continente = pais['continente']
        if continente not in resumen_continentes:
            resumen_continentes[continente] = {'conteo_paises': 0, 'poblacion_total': 0}
        
        resumen_continentes[continente]['conteo_paises'] += 1
        resumen_continentes[continente]['poblacion_total'] += pais['poblacion']
    
    print("Resumen por Continente:")
    print(f"  {'Continente':<15} | {'Nº de Países':>15} | {'Población Total':>20}")
    print("-" * 60)
    for continente, datos in resumen_continentes.items():
        conteo = datos['conteo_paises']
        poblacion = f"{datos['poblacion_total']:,}"
        print(f"  {continente:<15} | {conteo:>15} | {poblacion:>20}")

    print('------------------------------------------')

    #Países con menos y más población y superficie
    print('Mínimos y máximos:')
    pais_mas_poblado = max(lista_paises, key=lambda p: p['poblacion'])
    pais_menos_poblado = min(lista_paises, key=lambda p: p['poblacion'])
    
    pais_mas_extenso = max(lista_paises, key=lambda p: p['superficie'])
    pais_menos_extenso = min(lista_paises, key=lambda p: p['superficie'])

    print("Extremos Globales:")
    print(f"  País más poblado: {pais_mas_poblado['nombre']} ({pais_mas_poblado['poblacion']:,})")
    print(f"  País menos poblado: {pais_menos_poblado['nombre']} ({pais_menos_poblado['poblacion']:,})")
    print(f"  País más extenso: {pais_mas_extenso['nombre']} ({pais_mas_extenso['superficie']:,} km²)")
    print(f"  País menos extenso: {pais_menos_extenso['nombre']} ({pais_menos_extenso['superficie']:,} km²)")
