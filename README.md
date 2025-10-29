# Trabajo Práctico Integrador (TPI) - Gestión de Datos de Países

**Universidad Tecnológica Nacional (UTN)**
**Tecnicatura Universitaria en Programación**
**Materia:** Programación 1

---

## Descripción del Proyecto:

Este proyecto consiste en una aplicación de consola desarrollada en **Python 3.x** para gestionar información sobre países. El sistema lee un dataset desde un archivo CSV y permite al usuario realizar consultas, aplicar filtros, ordenar los datos y generar estadísticas clave.

El objetivo principal es consolidar los conocimientos adquiridos en la materia, demostrando un uso correcto de:

- Estructuras de datos (Listas de diccionarios).
- Modularización con funciones.
- Manejo de archivos CSV.
- Lógica de programación (filtros, ordenamientos, bucles).
- Buenas prácticas de codificación y documentación.

## Integrantes del Equipo:

| Nombre y Apellido                 |
| :-------------------------------- |
| **Jorge Ramiro Lorenzo Casanova** |
| **Gustavo Adolfo Cortés**         |

## Requisitos Previos:

Para ejecutar este proyecto necesitas tener instalado:

- **Python 3.6** o superior.

## Instalación y Configuración:

Sigue estos pasos para configurar el proyecto en tu entorno local:

1.  **Clonar el repositorio:**
    Abre tu terminal y ejecuta el siguiente comando:

    ```bash
    git clone https://github.com/GCortesGustavo/TPI-Programacion1-Cortes-Lorenzo.git
    ```

2.  **Acceder al directorio del proyecto:**

    ```bash
    cd TPI-Programacion1-Cortes-Lorenzo
    ```

3.  **Verificar el archivo de datos:**
    El archivo `paises.csv` se encuentra en la raíz del proyecto. Este archivo contiene el dataset base necesario para que el programa funcione.

## Instrucciones de Uso:

Para iniciar la aplicación, ejecuta el archivo principal `main.py` desde la terminal estando en la raíz del proyecto:

```bash
python main.py
```

1. Ejecución principal
El archivo main.py es el punto de entrada del programa.

    Al ejecutarse, muestra el menú principal en la terminal y permite al usuario seleccionar las distintas opciones disponibles.

2. Interacción con el usuario
    La lógica del menú se gestiona en el archivo menu.py, donde el usuario puede elegir las distintas operaciones sobre los datos del archivo paises.csv.

3. Búsqueda de país — buscar_pais.py

    Permite buscar un país por su nombre.

    Si el país existe, se muestran sus datos.

    Si no se encuentra, retorna un mensaje o valor indicando que no existe.

4. Filtro por continente — filtro_continente.py

    Filtra los países según el continente ingresado por el usuario.

    Retorna una lista con todos los países pertenecientes a dicho continente.

5. Filtro poblacional — filtro_rango_poblacion.py

    El usuario ingresa un valor mínimo y máximo de población.

    Se muestran los países cuya población se encuentra dentro de ese rango.

6. Filtro por superficie — filtro_rango_superficie.py

    Funciona de forma similar al filtro poblacional.

    El usuario define los valores mínimo y máximo de superficie (en km²).

    Se retornan los países que se encuentren dentro de los límites establecidos.

7. Ordenar países alfabéticamente — ordenar_paises.py

    Reorganiza los datos del archivo CSV en orden ascendente (A–Z) según el nombre de los países.

    El resultado puede guardarse o visualizarse dependiendo de la implementación.

8. Cálculo de estadísticas — estadisticas.py

    Calcula y muestra distintos valores estadísticos sobre los países:

    Promedio de los países más poblados.

    Promedio de los países menos poblados.

    Promedio general de superficie.

9. Carga de datos — carga_datos.py

    Se encarga de la lectura del archivo paises.csv y la conversión de los datos a estructuras utilizables dentro del programa (por ejemplo, listas o diccionarios).