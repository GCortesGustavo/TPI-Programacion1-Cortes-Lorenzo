def buscar_pais(lista_paises, nombre_buscado):
    if not nombre_buscado.strip():
        return []

    nombre_buscado_lower = nombre_buscado.lower()
    
    paises_encontrados = [
        pais for pais in lista_paises 
        if nombre_buscado_lower in pais['nombre'].lower()
    ]
    
    return paises_encontrados