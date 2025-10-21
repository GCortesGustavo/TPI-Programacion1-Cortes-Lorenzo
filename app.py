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

# Generamos un CSV cada vez que la aplicación se inicia
print("Iniciando carga de datos desde la API...")
paises_api = obtener_paises_de_api()
if paises_api:
    guardar_paises_en_csv(paises_api, 'paises.csv')
else:
    print("ADVERTENCIA: No se pudo obtener datos de la API. Se usará el último CSV guardado si existe.")

lista_paises = cargar_paises_desde_csv('paises.csv')
print(f"Carga completa. {len(lista_paises)} países listos para servir.")


@app.route('/')
def index():
    """Ruta principal que muestra la lista de países y permite ordenarla."""
    return render_template('index.html', paises=lista_paises)

@app.route('/buscar')
def buscar_web():
    query = request.args.get('query', '')
    paises_encontrados = buscar_pais(lista_paises, query) if query else []
    
    return render_template('buscar.html', 
        query=query, 
        paises_encontrados=paises_encontrados)

@app.route('/ordenar')
def ordenar_web():
    sort_by = request.args.get('sort_by', 'nombre')
    order = request.args.get('order', 'asc')
    
    paises_ordenados = ordenar_paises(lista_paises, sort_by, order)
    
    return render_template('ordenar.html', 
        paises_ordenados=paises_ordenados, 
        sort_by=sort_by, 
        order=order)

@app.route('/filtrar')
def filtrar_web():
    paises_filtrados = lista_paises
    
    filtro_continente = request.args.get('continente', '')
    filtro_pob_min = request.args.get('pob_min', type=int)
    filtro_pob_max = request.args.get('pob_max', type=int)
    filtro_sup_min = request.args.get('sup_min', type=int)
    filtro_sup_max = request.args.get('sup_max', type=int)

    if filtro_continente:
        paises_filtrados = filtrar_por_continente(paises_filtrados, filtro_continente)
    
    min_pob = filtro_pob_min if filtro_pob_min is not None else 0
    max_pob = filtro_pob_max if filtro_pob_max is not None else float('inf')
    if filtro_pob_min is not None or filtro_pob_max is not None:
        paises_filtrados = filtrar_por_poblacion(paises_filtrados, min_pob, max_pob)
    
    min_sup = filtro_sup_min if filtro_sup_min is not None else 0
    max_sup = filtro_sup_max if filtro_sup_max is not None else float('inf')
    if filtro_sup_min is not None or filtro_sup_max is not None:
        paises_filtrados = filtrar_por_superficie(paises_filtrados, min_sup, max_sup)
    
    continentes = sorted(list(set(p['continente'] for p in lista_paises)))
    filtros_actuales = {k: request.args.get(k, '') for k in ['continente', 'pob_min', 'pob_max', 'sup_min', 'sup_max']}

    return render_template('filtrar.html', 
        paises=paises_filtrados, 
        continentes=continentes, 
        filtros_actuales=filtros_actuales)

@app.route('/estadisticas')
def estadisticas_web():
    mas_poblado, menos_poblado = calcular_extremos_poblacion(lista_paises)
    prom_poblacion, prom_superficie = calcular_promedios(lista_paises)
    conteo_continentes = calcular_conteo_por_continente(lista_paises)
    
    return render_template('estadisticas.html', 
        mas_poblado=mas_poblado,
        menos_poblado=menos_poblado,
        prom_poblacion=prom_poblacion,
        prom_superficie=prom_superficie,
        conteo_continentes=conteo_continentes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)