def ordenar_paises(lista_paises, criterio='nombre', orden='asc'): #ordena la lista de paises segun el criterio y orden especificados
    if criterio not in ['nombre', 'poblacion', 'superficie']:
        criterio = 'nombre' # criterio por defecto si el ingresado no es valido

    reverse_flag = (orden == 'desc') 
    
    try:
        paises_ordenados = sorted(lista_paises, key=lambda pais: pais[criterio], reverse=reverse_flag) #ordena la lista segun el criterio y orden
        return paises_ordenados
    except KeyError:
        print(f"Advertencia: No se pudo ordenar por el criterio '{criterio}' debido a datos faltantes.")
        return lista_paises