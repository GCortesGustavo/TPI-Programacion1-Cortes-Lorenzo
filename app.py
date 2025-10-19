# Dentro de app.py
from flask import Flask, render_template, request
from utils.carga_datos import cargar_paises_desde_csv
# Importa las funciones "puras" que refactorizamos
from utils.buscar_pais import buscar_pais
from utils.filtro_continente import filtrar_por_continente
from utils.estadisticas import calcular_extremos_poblacion, calcular_promedios, calcular_conteo_por_continente
from utils.filtro_continente import filtrar_por_continente
from utils.filtro_rango_poblacion import filtrar_por_poblacion
from utils.filtro_rango_superficie import filtrar_por_superficie

app = Flask(__name__)
lista_paises = cargar_paises_desde_csv('paises.csv')

# --- RUTA 1: PÁGINA DE INICIO ---
@app.route('/')
def index():
    return render_template('index.html', paises=lista_paises)

# --- RUTA 2: PÁGINA DE BÚSQUEDA ---
@app.route('/buscar')
def buscar():
    query = request.args.get('query', '')
    paises_encontrados = None
    if query:
        paises_encontrados = buscar_pais(lista_paises, query)
    return render_template('buscar.html', query=query, paises_encontrados=paises_encontrados)

# --- RUTA 3: PÁGINA DE FILTROS ---
@app.route('/filtrar')
def filtrar():
    # 1. Empezamos con la lista completa de países
    paises_filtrados = lista_paises

    # 2. Leemos todos los posibles valores de los filtros desde la URL
    filtro_continente = request.args.get('continente', '')
    
    # Leemos los rangos, convirtiéndolos a 'int' si existen, si no, quedan como None
    filtro_pob_min = request.args.get('pob_min', type=int)
    filtro_pob_max = request.args.get('pob_max', type=int)
    filtro_sup_min = request.args.get('sup_min', type=int)
    filtro_sup_max = request.args.get('sup_max', type=int)

    # 3. Aplicamos los filtros secuencialmente
    if filtro_continente:
        paises_filtrados = filtrar_por_continente(paises_filtrados, filtro_continente)
    
    # Para los rangos, usamos los valores por defecto que definimos en las funciones
    min_pob = filtro_pob_min if filtro_pob_min is not None else 0
    max_pob = filtro_pob_max if filtro_pob_max is not None else float('inf')
    if filtro_pob_min is not None or filtro_pob_max is not None:
         paises_filtrados = filtrar_por_poblacion(paises_filtrados, min_pob, max_pob)
    
    min_sup = filtro_sup_min if filtro_sup_min is not None else 0
    max_sup = filtro_sup_max if filtro_sup_max is not None else float('inf')
    if filtro_sup_min is not None or filtro_sup_max is not None:
        paises_filtrados = filtrar_por_superficie(paises_filtrados, min_sup, max_sup)
    
    # 4. Preparamos datos extra para la plantilla
    # Lista única de continentes para el menú desplegable
    continentes = sorted(list(set(p['continente'] for p in lista_paises)))
    
    # Diccionario con los filtros actuales para rellenar el formulario
    filtros_actuales = {
        'continente': filtro_continente,
        'pob_min': request.args.get('pob_min', ''), # Pasamos el string para el 'value'
        'pob_max': request.args.get('pob_max', ''),
        'sup_min': request.args.get('sup_min', ''),
        'sup_max': request.args.get('sup_max', ''),
    }

    # 5. Renderizamos la plantilla con todos los datos
    return render_template('filtrar.html', 
                           paises=paises_filtrados, 
                           continentes=continentes, 
                           filtros_actuales=filtros_actuales)

# --- RUTA 4: PÁGINA DE ESTADÍSTICAS ---
@app.route('/estadisticas')
def estadisticas():
    # Esta llamada ahora encontrará las funciones correctas
    mas_poblado, menos_poblado = calcular_extremos_poblacion(lista_paises)
    prom_poblacion, prom_superficie = calcular_promedios(lista_paises)
    conteo_continentes = calcular_conteo_por_continente(lista_paises)
    
    # Pasamos los datos calculados a la plantilla HTML
    return render_template(
        'estadisticas.html', 
        mas_poblado=mas_poblado,
        menos_poblado=menos_poblado,
        prom_poblacion=prom_poblacion,
        prom_superficie=prom_superficie,
        conteo_continentes=conteo_continentes
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)