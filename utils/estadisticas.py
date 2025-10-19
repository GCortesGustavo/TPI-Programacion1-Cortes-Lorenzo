# Dentro de utils/estadisticas.py

def calcular_extremos_poblacion(lista_paises):
    """
    Encuentra los países con la mayor y menor población.
    Retorna dos diccionarios: (pais_mas_poblado, pais_menos_poblado).
    """
    if not lista_paises:
        return None, None
        
    pais_mas_poblado = max(lista_paises, key=lambda p: p['poblacion'])
    pais_menos_poblado = min(lista_paises, key=lambda p: p['poblacion'])
    return pais_mas_poblado, pais_menos_poblado

def calcular_promedios(lista_paises):
    """
    Calcula la población y superficie promedio de todos los países.
    Retorna dos números: (promedio_poblacion, promedio_superficie).
    """
    if not lista_paises:
        return 0, 0
        
    total_paises = len(lista_paises)
    total_poblacion = sum(p['poblacion'] for p in lista_paises)
    total_superficie = sum(p['superficie'] for p in lista_paises)

    promedio_poblacion = total_poblacion / total_paises
    promedio_superficie = total_superficie / total_paises
    
    return promedio_poblacion, promedio_superficie

def calcular_conteo_por_continente(lista_paises):
    """
    Cuenta la cantidad de países por cada continente.
    Retorna un diccionario: {'Continente': conteo, ...}.
    """
    conteo_continentes = {}
    for pais in lista_paises:
        continente = pais['continente']
        conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1
    
    # Retornamos el diccionario ordenado por nombre de continente para una presentación consistente
    return dict(sorted(conteo_continentes.items()))

# Las funciones de consola (gestionar_estadisticas, mostrar_menu_estadisticas)
# ya no son necesarias para la aplicación web, por lo que las hemos eliminado de este archivo.
# Si quieres mantener la app de consola, deberías moverlas a otro archivo o dejarlas aquí
# sabiendo que app.py no las usará.