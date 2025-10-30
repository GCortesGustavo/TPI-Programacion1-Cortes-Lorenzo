def filtrar_por_superficie(lista_paises, min_sup=0, max_sup=float('inf')): #filtra los paises por rango de superficie
    return [
        pais for pais in lista_paises 
        if min_sup <= pais['superficie'] <= max_sup #filtra por superficie
    ]