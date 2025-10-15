def filtrar_por_rango_poblacion(lista_paises):
    bandera_rango :bool = True

    while bandera_rango:
        try:
            opcion_menu = input("Ingrese 1 para filtrar por poblacion, 2 para salir:")
            if opcion_menu == "1":
                try:
                    poblacion_min = int(input("Ingrese la población mínima: "))
                    poblacion_max = int(input("Ingrese la población máxima: "))
                except ValueError:
                    print("Error: Por favor, ingrese valores numéricos válidos para la población.")
                if poblacion_min < 0 or poblacion_max < 0:
                    print("Error: La población no puede ser negativa.")
                elif poblacion_min > poblacion_max:
                    print("Error: La población mínima no puede ser mayor que la máxima.")
                else:
                    paises_filtrados = [pais for pais in lista_paises if poblacion_min <= pais['poblacion'] <= poblacion_max]
                    if paises_filtrados:
                        print(f"\nPaíses con población entre {poblacion_min} y {poblacion_max}:")
                        for pais in paises_filtrados:
                            print(f"- {pais['nombre']}: {pais['poblacion']} habitantes")
                    else:
                        print(f"No se encontraron países con población entre {poblacion_min} y {poblacion_max}.")
            elif opcion_menu == "2":
                print("Saliendo del filtro de población.")
                bandera_rango = False
        except ValueError:
            print("Error: Opción no válida. Por favor, ingrese 1 o 2.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    return
            

