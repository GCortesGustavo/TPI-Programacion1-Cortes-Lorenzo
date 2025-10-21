def calcular_extremos_poblacion(lista_paises):
    if not lista_paises:
        return None, None
        
    pais_mas_poblado = max(lista_paises, key=lambda p: p['poblacion'])
    pais_menos_poblado = min(lista_paises, key=lambda p: p['poblacion'])
    return pais_mas_poblado, pais_menos_poblado

def calcular_promedios(lista_paises):
    if not lista_paises:
        return 0, 0
        
    total_paises = len(lista_paises)
    total_poblacion = sum(p['poblacion'] for p in lista_paises)
    total_superficie = sum(p['superficie'] for p in lista_paises)

    promedio_poblacion = total_poblacion / total_paises
    promedio_superficie = total_superficie / total_paises
    
    return promedio_poblacion, promedio_superficie

def calcular_conteo_por_continente(lista_paises):
    conteo_continentes = {}
    for pais in lista_paises:
        continente = pais['continente']
        conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1
    
    return dict(sorted(conteo_continentes.items()))
