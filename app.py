from flask import Flask, render_template, request
from utils.carga_datos import obtener_paises_de_api, guardar_paises_en_csv, cargar_paises_desde_csv
from utils.buscar_pais import buscar_pais
from utils.filtro_continente import filtrar_por_continente
from utils.filtro_rango_poblacion import filtrar_por_poblacion
from utils.filtro_rango_superficie import filtrar_por_superficie
from utils.ordenar_paises import ordenar_paises
from utils.estadisticas import calcular_extremos_poblacion, calcular_promedios, calcular_conteo_por_continente

# CONFIGURACIÓN INICIAL DE LA APP 
app = Flask(__name__)

NOMBRE_ARCHIVO_CSV = 'paises.csv'

# Generamos un CSV cada vez que la aplicación se inicia
print("Iniciando carga de datos desde la API...")
paises_api = obtener_paises_de_api()
if paises_api:
    guardar_paises_en_csv(paises_api, NOMBRE_ARCHIVO_CSV)
else:
    print("ADVERTENCIA: No se pudo obtener datos de la API. Se usará el último CSV guardado si existe.")

lista_paises = cargar_paises_desde_csv(NOMBRE_ARCHIVO_CSV) #guarda la lista de paises en una lista
print(f"Carga completa. {len(lista_paises)} países listos para servir.")


@app.route('/')
def index():
    """Ruta principal que muestra la lista de países y permite ordenarla."""
    return render_template('index.html', paises=lista_paises) #muestra la lista de paises en la pagina principal

@app.route('/buscar')
def buscar_web():
    query = request.args.get('query', '')
    paises_encontrados = buscar_pais(lista_paises, query) if query else [] #busca los paises que coincidan con la consulta ingresada
    
    return render_template('buscar.html', 
        query=query, 
        paises_encontrados=paises_encontrados) #muestra los paises encontrados en la pagina de busqueda

@app.route('/ordenar')
def ordenar_web(): #ruta para ordenar los paises
    sort_by = request.args.get('sort_by', 'nombre')
    order = request.args.get('order', 'asc')
    
    paises_ordenados = ordenar_paises(lista_paises, sort_by, order) #ordena los paises segun el criterio y orden seleccionado
    
    return render_template('ordenar.html',  
        paises_ordenados=paises_ordenados, 
        sort_by=sort_by, 
        order=order)

@app.route('/filtrar') 
def filtrar_web(): #ruta para filtrar los paises
    paises_filtrados = lista_paises #inicialmente todos los paises
    
    filtro_continente = request.args.get('continente', '') #obtiene los filtros ingresados por el usuario
    filtro_pob_min = request.args.get('pob_min', type=int) # obtiene el valor minimo de poblacion
    filtro_pob_max = request.args.get('pob_max', type=int) # obtiene el valor maximo de poblacion
    filtro_sup_min = request.args.get('sup_min', type=int) # obtiene el valor minimo de superficie
    filtro_sup_max = request.args.get('sup_max', type=int) # obtiene el valor maximo de superficie

    if filtro_continente:
        paises_filtrados = filtrar_por_continente(paises_filtrados, filtro_continente) #filtra por continente
    
    min_pob = filtro_pob_min if filtro_pob_min is not None else 0 
    max_pob = filtro_pob_max if filtro_pob_max is not None else float('inf')
    if filtro_pob_min is not None or filtro_pob_max is not None:
        paises_filtrados = filtrar_por_poblacion(paises_filtrados, min_pob, max_pob) #filtra por poblacion
    
    min_sup = filtro_sup_min if filtro_sup_min is not None else 0
    max_sup = filtro_sup_max if filtro_sup_max is not None else float('inf')
    if filtro_sup_min is not None or filtro_sup_max is not None:
        paises_filtrados = filtrar_por_superficie(paises_filtrados, min_sup, max_sup) #filtra por superficie
    
    continentes = sorted(list(set(p['continente'] for p in lista_paises))) #lista de continentes disponibles para el filtro
    filtros_actuales = {k: request.args.get(k, '') for k in ['continente', 'pob_min', 'pob_max', 'sup_min', 'sup_max']}

    return render_template('filtrar.html', 
        paises=paises_filtrados, 
        continentes=continentes, 
        filtros_actuales=filtros_actuales)

@app.route('/estadisticas')
def estadisticas_web(): #ruta para mostrar las estadisticas de los paises
    mas_poblado, menos_poblado = calcular_extremos_poblacion(lista_paises) #calcula el pais mas y menos poblado
    prom_poblacion, prom_superficie = calcular_promedios(lista_paises) #calcula los promedios de poblacion y superficie
    conteo_continentes = calcular_conteo_por_continente(lista_paises) #calcula el conteo de paises por continente

    return render_template('estadisticas.html', # muestra las estadisticas en la pagina de estadisticas 
        mas_poblado=mas_poblado,
        menos_poblado=menos_poblado,
        prom_poblacion=prom_poblacion,
        prom_superficie=prom_superficie,
        conteo_continentes=conteo_continentes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)