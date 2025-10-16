def ordenar_paises(lista_paises):

    paises_ordenados = sorted(lista_paises, key=lambda pais: pais['nombre'])
    print("\nPaíses ordenados alfabéticamente por nombre:")
    
    for pais in paises_ordenados:
        print(f"- {pais['nombre']}: Población {pais['poblacion']}, Superficie {pais['superficie']} km² ")
    return
