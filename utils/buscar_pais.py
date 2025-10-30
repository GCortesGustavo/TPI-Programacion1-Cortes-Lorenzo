def buscar_pais(lista_paises, nombre_buscado): #busca paises cuyo nombre contenga el texto ingresado
    if not nombre_buscado.strip():
        return [] #retorna lista vacia si el nombre buscado esta vacio

    nombre_buscado_lower = nombre_buscado.lower() #convierte el nombre buscado a minusculas
    
    paises_encontrados = [ #busca en la lista de paises
        pais for pais in lista_paises  
        if nombre_buscado_lower in pais['nombre'].lower() #compara en minusculas
    ]
    
    return paises_encontrados