def cargar_paises_desde_csv(ruta_archivo):

    lista_paises = []
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo_csv:
            next(archivo_csv)  # Lee y descarta la línea de encabezado

            for linea in archivo_csv:
                linea_limpia = linea.strip()
                
                if not linea_limpia:
                    continue
                
                objeto = linea_limpia.split(',')
                
                if len(objeto) == 4:
                    try:
                        nombre = objeto[0]
                        poblacion = int(objeto[1])
                        superficie = int(objeto[2])
                        continente = objeto[3]
                        
                        lista_paises.append({
                            'nombre': nombre,
                            'poblacion': poblacion,
                            'superficie': superficie,
                            'continente': continente
                        })
                    except ValueError:
                        print(f"Advertencia: Se omitió la fila para '{objeto[0]}' por datos numéricos inválidos.")
                else:
                    print(f"Advertencia: Se omitió una fila malformada: '{linea_limpia}'")

    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer el archivo: {e}")

    return lista_paises