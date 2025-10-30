# TPI - Gestión de Datos de Países con Flask y Docker

**Universidad Tecnológica Nacional (UTN) | Tecnicatura Universitaria en Programación | Programación 1**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-000000.svg?style=flat&logo=flask)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-24.0-2496ED.svg?style=flat&logo=docker)](https://www.docker.com/)
[![Render](https://img.shields.io/badge/Render-46E3B7.svg?style=flat&logo=render)](https://render.com/)

---

## Integrantes

| Nombre y Apellido                 |
| :-------------------------------- |
| **Jorge Ramiro Lorenzo Casanova** |
| **Gustavo Adolfo Cortés**         |

---

## Demo en Vivo

**Podés probar la aplicación desplegada en Render aquí:**

### [tpi-paises-app.onrender.com](https://tpi-paises-cortes-lorenzo.onrender.com/)

---

## Descripción del Proyecto

Este proyecto es una aplicación web interactiva desarrollada con **Python y Flask** que permite visualizar, buscar, filtrar y ordenar datos de países. La información se obtiene dinámicamente de la API pública [RestCountries](https://restcountries.com/) cada vez que la aplicación se inicia, asegurando un conjunto de datos fresco en cada ejecución.

El proyecto está completamente **"dockerizado"**, lo que garantiza su portabilidad y un despliegue sencillo y consistente en cualquier entorno.

### Funcionalidades Clave

- **Carga Dinámica desde API:** Obtiene una selección aleatoria de 50 países en cada inicio.
- **Lista:** Visualiza la lista completa de países.
- **Ordenamiento** Ordena la lista por nombre, población de forma ascendente o descendente.
- **Búsqueda Parcial:** Busca países por nombre de forma insensible a mayúsculas y minúsculas.
- **Filtros Combinados:** Aplica filtros por continente, rango de población y rango de superficie de manera simultánea.
- **Estadísticas Globales:** Muestra datos calculados como los países más/menos poblados, promedios y conteo por continente.
- **Diseño Responsivo:** La interfaz se adapta a dispositivos de escritorio y móviles en su parcialidad.

---

## Stack de Tecnologías

- **Backend:** Python 3.11, Flask, Gunicorn
- **Frontend:** HTML5, CSS3 (sin frameworks)
- **Fuente de Datos:** [RestCountries API](https://restcountries.com/)
- **Contenerización:** Docker
- **Despliegue:** Render
- **Gestión de tareas:** Trello

---

## Estructura del Proyecto

El código está organizado siguiendo una arquitectura modular para separar la lógica de negocio de la presentación.

---

## 🚀 Cómo Ejecutar Este Proyecto

Existen dos métodos para ejecutar la aplicación: a través de Docker (recomendado para simular el entorno de producción) o de forma manual en un entorno local.

### 🐳 Vía Docker (Método Recomendado)

Este método es el más sencillo y garantiza que la aplicación funcione correctamente sin necesidad de instalar Python o dependencias manualmente en tu sistema.

**Requisitos:**

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y en ejecución.

**Pasos:**

1.  **Clona el repositorio:**

    ```bash
    git clone https://github.com/GCortesGustavo/TPI-Programacion1-Cortes-Lorenzo.git
    cd TPI-Programacion1-Cortes-Lorenzo
    ```

2.  **Construye la imagen Docker:**
    Este comando lee el `Dockerfile` y empaqueta la aplicación.

    ```bash
    docker build -t tpi-web-final .
    ```

3.  **Ejecuta el contenedor:**
    Este comando inicia la aplicación y la hace accesible en tu máquina.

    ```bash
    docker run -it --rm -p 5000:5000 tpi-web-final
    ```

4.  **Accede a la aplicación:**
    Abre tu navegador y ve a `http://localhost:5000`.

### Vía Local (Método Manual)

Este método es útil si deseas modificar el código y ver los cambios al instante sin usar Docker.

**Requisitos:**

- Python 3.8 o superior.

**Pasos:**

1.  **Clona el repositorio:**

    ```bash
    git clone https://github.com/GCortesGustavo/TPI-Programacion1-Cortes-Lorenzo.git
    cd TPI-Programacion1-Cortes-Lorenzo
    ```

2.  **Crea y activa un entorno virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    Este comando instalará `Flask`, `requests` y `gunicorn` desde el archivo `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta la aplicación:**
    Flask iniciará su servidor de desarrollo.

    ```bash
    python app.py
    ```

5.  **Accede a la aplicación:**
    Abre tu navegador y ve a `http://localhost:5000`.

6.  **Desactivar el entorno virtual:**
    Este comando finalizará el entorno virtual y volverá a la consola normal.

    ```bash
    deactivate
    ```

---

## Video Tutorial

En el siguiente video se explica el problema planteado, la estructura de datos, y se realiza una demostración de la aplicación funcionando.

[![Ver Video Tutorial](https://img.youtube.com/vi/ID_DEL_VIDEO/0.jpg)](https://www.youtube.com/watch?v=ID_DEL_VIDEO)
** [Ver Video Tutorial en YouTube]([URL-DEL-VIDEO-AQUI])**

---

## Documento del Proyecto (Informe Teórico)

El informe completo del proyecto, incluyendo el marco teórico, diagrama de flujo, conclusiones y bibliografía, se encuentra disponible en el siguiente enlace.

** [Acceder al Informe en Google Drive](https://docs.google.com/document/d/1cThdIUpqeXxhHu30nzRwIxvcHwOLfMBXBacSvGYxEsE/edit?usp=sharing)**

---
