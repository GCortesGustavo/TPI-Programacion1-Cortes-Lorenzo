def ordenar_paises(lista_paises, criterio='nombre', orden='asc'):
    if criterio not in ['nombre', 'poblacion', 'superficie']:
        criterio = 'nombre'

    reverse_flag = (orden == 'desc')
    
    try:
        paises_ordenados = sorted(lista_paises, key=lambda pais: pais[criterio], reverse=reverse_flag)
        return paises_ordenados
    except KeyError:
        print(f"Advertencia: No se pudo ordenar por el criterio '{criterio}' debido a datos faltantes.")
        return lista_paises