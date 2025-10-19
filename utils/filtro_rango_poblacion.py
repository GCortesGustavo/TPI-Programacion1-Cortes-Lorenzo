def filtrar_por_poblacion(lista_paises, min_pob=0, max_pob=float('inf')):
    paises_filtrados = [
        pais for pais in lista_paises 
        if min_pob <= pais['poblacion'] <= max_pob
    ]
    return paises_filtrados