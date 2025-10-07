import csv

def cargar_paises_desde_csv(ruta_archivo):
    #Se cargan los datos de los países desde el archivo paises.csv
    #y se devuelven como una lista de diccionarios

    # Se utiliza un manejo de errores por si no se encuentra el archivo
    # o si el formato de los datos son incorrectos en las filas.

    lista_paises :list = []

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo_csv:
            # DictReader se utiliza para tratar a cada fila como diccionario.
            lector_csv = csv.DictReader(archivo_csv)

            for fila in lector_csv:
                try:
                    población = int(fila["poblacion"])
                    superficie = int(fila["superficie"])

                    lista_paises.append({
                        "nombre" : fila["nombre"],
                        "poblacion" : población,
                        "superficie" : superficie,
                        "continente" : fila["continente"],
                    })
                except ValueError:
                    print(f"Advertencia: Se omitió una fila por falta de claves esperadas (nombre, poblacion, etc.).")
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no fue encontrado.")
    except Exception as error:
        print(f"Ocurrió un error inesperado al leer el archivo: {error}")

    return lista_paises