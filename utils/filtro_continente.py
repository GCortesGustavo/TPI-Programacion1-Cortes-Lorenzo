def filtrar_por_continente(lista_paises, continente):
    paises_filtrados = []
    continente_lower = continente.strip().lower()
    for pais in lista_paises:
        if pais['continente'].lower() == continente_lower:
            paises_filtrados.append(pais)
    return paises_filtrados