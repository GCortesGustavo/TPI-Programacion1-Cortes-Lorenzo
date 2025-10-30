def filtrar_por_continente(lista_paises, continente): #filtra los paises por continente
    paises_filtrados = []
    continente_lower = continente.strip().lower() #convierte el continente a minusculas y elimina espacios
    for pais in lista_paises:
        if pais['continente'].lower() == continente_lower: #compara el continente en minusculas
            paises_filtrados.append(pais) #agrega el pais a la lista filtrada
    return paises_filtrados