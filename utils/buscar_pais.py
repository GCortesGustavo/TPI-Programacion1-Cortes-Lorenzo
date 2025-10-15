def buscar_pais_por_nombre(lista_paises):
    bandera_busqueda :bool = True
    pais = None
    while bandera_busqueda:
            opcion = input("Ingresa 1 para buscar un país o 2 para salir: ")
            try:
                if opcion == "1":
                    pais_buscado = input("Ingresa el nombre del país o las siglas a buscar: ")
                    pais_buscado = pais_buscado.lower()
                    for pais in lista_paises:
                        try:
                            if pais['nombre'].lower().startswith(pais_buscado):
                                print(f"País encontrado: {pais['nombre']} - Población: {pais['poblacion']} - Superficie: {pais['superficie']} km² - Continente: {pais['continente']}")
                        except ValueError:
                            print(f"el pais no se encontro")
                        except pais == "":
                            print("valor vacio")
                if opcion == "2":
                    bandera_busqueda = False
                    print("Saliendo de la búsqueda.")
            except ValueError:
                print("Opción inválida. Por favor, ingresa 1 o 2.")