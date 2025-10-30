def filtrar_por_poblacion(lista_paises, min_pob=0, max_pob=float('inf')): #filtra los paises por rango de poblacion
    return [
        pais for pais in lista_paises  # itera sobre la lista de paises
        if min_pob <= pais['poblacion'] <= max_pob 
    ]