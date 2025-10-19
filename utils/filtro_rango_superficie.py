def filtrar_por_rango_superficie(lista_paises):
    bandera_rango :bool = True

    while bandera_rango:
        try:
            opcion_menu = input("Ingrese 1 para filtrar por superficie, 2 para salir:")
            if opcion_menu == "1":
                try:
                    superficie_min = int(input("Ingrese la superficie mínima: "))
                    superficie_max = int(input("Ingrese la superficie máxima: "))
                except ValueError:
                    print("Error: Por favor, ingrese valores numéricos válidos para la superficie.")
                if superficie_min < 0 or superficie_max < 0:
                    print("Error: La superficie no puede ser negativa.")
                elif superficie_min > superficie_max:
                    print("Error: La superficie mínima no puede ser mayor que la máxima.")
                else:
                    paises_filtrados = [pais for pais in lista_paises if superficie_min <= pais['poblacion'] <= superficie_max]
                    if paises_filtrados:
                        print(f"\nPaíses con superficie entre {superficie_min} y {superficie_max}:")
                        for pais in paises_filtrados:
                            print(f"- {pais['nombre']}: {pais['superficie']} superficie km²")
                    else:
                        print(f"No se encontraron países con superficie entre {superficie_min} y {superficie_max}.")
            elif opcion_menu == "2":
                print("Saliendo del filtro de superficie.")
                bandera_rango = False
        except ValueError:
            print("Error: Opción no válida. Por favor, ingrese 1 o 2.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    return
            