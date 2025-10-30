import requests
import csv      
import random   

def obtener_paises_de_api(): #obtiene datos de paises desde la API
    url_api = "https://restcountries.com/v3.1/all?fields=name,population,area,continents"
    paises_formateados = [] #lista para almacenar los paises obtenidos

    print("Obteniendo datos de la API de restcountries.com...")
    try:
        respuesta = requests.get(url_api) #realiza la solicitud a la API
        respuesta.raise_for_status() #verifica si la solicitud fue exitosa
        datos_api = respuesta.json()  #convierte la respuesta a formato JSON
        
        paises_seleccionados = random.sample(datos_api, 50) #selecciona 50 paises aleatoriamente
        
        for pais_data in paises_seleccionados: #itera sobre los datos de cada pais
            nombre = pais_data.get('name', {}).get('common', 'N/A')
            poblacion = pais_data.get('population', 0)
            superficie = pais_data.get('area', 0)
            
            continentes = pais_data.get('continents', ['N/A'])
            continente = continentes[0] if continentes else 'N/A'
            
            paises_formateados.append({
                'nombre': nombre,
                'poblacion': int(poblacion),
                'superficie': int(superficie),
                'continente': continente
            })
            
        print(f"¡Éxito! Se obtuvieron {len(paises_formateados)} países de la API.")
        return paises_formateados

    except requests.exceptions.RequestException as error: 
        print(f"Error al conectar con la API: {error}") 
        return [] 

def guardar_paises_en_csv(lista_paises, ruta_archivo): #guarda la lista de paises en un archivo csv
    if not lista_paises:
        print("No hay datos de países para guardar en el CSV.") 
        return False

    encabezados = ['nombre', 'poblacion', 'superficie', 'continente']
    
    try:
        with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv: #abre el archivo en modo escritura
            escritor_csv = csv.DictWriter(archivo_csv, fieldnames=encabezados)
            
            escritor_csv.writeheader()  
            escritor_csv.writerows(lista_paises) 
        
        print(f"Datos guardados exitosamente en '{ruta_archivo}'.")
        return True
    except IOError as e:
        print(f"Error al escribir en el archivo CSV: {e}")
        return False

def cargar_paises_desde_csv(ruta_archivo): #carga la lista de paises desde un archivo csv
    lista_paises = []
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo_csv: #abre el archivo en modo lectura
            lector_csv = csv.DictReader(archivo_csv)
            for fila in lector_csv:
                try:
                    lista_paises.append({
                        'nombre': fila['nombre'],
                        'poblacion': int(fila['poblacion']),
                        'superficie': int(fila['superficie']),
                        'continente': fila['continente']
                    })
                except (ValueError, KeyError):
                    print(f"Advertencia: Se omitió una fila con datos inválidos en el CSV: {fila}")

    except FileNotFoundError:
        print(f"Error: El archivo CSV '{ruta_archivo}' no fue encontrado después de intentar generarlo.")
    
    return lista_paises #devuelve la lista de paises cargados