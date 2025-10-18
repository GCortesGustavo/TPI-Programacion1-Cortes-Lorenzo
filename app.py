from flask import Flask, render_template
from utils.carga_datos import cargar_paises_desde_csv 

# 1. Creamos la aplicación Flask
app = Flask(__name__)

# 2. Cargamos los datos UNA SOLA VEZ cuando la app inicia
lista_de_paises = cargar_paises_desde_csv('paises.csv')

# 3. Definimos una "ruta" (una URL)
# El decorador @app.route('/') significa "cuando alguien visite la página principal..."
@app.route('/')
def inicio():
    """
    Esta función se ejecuta cuando se accede a la URL principal.
    """
    return render_template('index.html', paises=lista_de_paises)

# Esto es para poder ejecutarlo directamente con 'python app.py' para pruebas
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)