def calcular_extremos_poblacion(lista_paises): #calcula el pais mas y menos poblado
    if not lista_paises:
        return None, None #maneja el caso de lista vacia
        
    pais_mas_poblado = max(lista_paises, key=lambda p: p['poblacion']) #encuentra el pais con mayor poblacion
    pais_menos_poblado = min(lista_paises, key=lambda p: p['poblacion']) #encuentra el pais con menor poblacion
    return pais_mas_poblado, pais_menos_poblado #devuelve ambos paises

def calcular_promedios(lista_paises): #calcula los promedios de poblacion y superficie
    if not lista_paises:
        return 0, 0 #maneja el caso de lista vacia
        
    total_paises = len(lista_paises)
    total_poblacion = sum(p['poblacion'] for p in lista_paises) #suma la poblacion total
    total_superficie = sum(p['superficie'] for p in lista_paises) #suma la superficie total

    promedio_poblacion = total_poblacion / total_paises #calcula el promedio de poblacion
    promedio_superficie = total_superficie / total_paises #calcula los promedios
    
    return promedio_poblacion, promedio_superficie #devuelve los promedios

def calcular_conteo_por_continente(lista_paises): #calcula el conteo de paises por continente
    conteo_continentes = {}
    for pais in lista_paises:
        continente = pais['continente'] #obtiene el continente del pais
        conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1 #incrementa el conteo para el continente
    
    return dict(sorted(conteo_continentes.items())) #devuelve el conteo ordenado por continente
 