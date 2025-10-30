# TPI - Gestión de Datos de Países con Flask y Docker

**Universidad Tecnológica Nacional (UTN) | Tecnicatura Universitaria en Programación | Programación 1**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-000000.svg?style=flat&logo=flask)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-24.0-2496ED.svg?style=flat&logo=docker)](https://www.docker.com/)

---

## Integrantes

| Nombre y Apellido                 |
| :-------------------------------- |
| **Jorge Ramiro Lorenzo Casanova** |
| **Gustavo Adolfo Cortés**         |

---

## Demo en Vivo

**Puedes probar la aplicación desplegada en Render aquí:**

### [tpi-paises-app.onrender.com]([Agregar URL]) 👈

_(Nota: El plan gratuito de Render puede tener un "arranque en frío", por lo que la primera carga puede tardar unos segundos)._

---

## Descripción del Proyecto

Este proyecto es una aplicación web interactiva desarrollada con **Python y Flask** que permite visualizar, buscar, filtrar y ordenar datos de países. La información se obtiene dinámicamente de la API pública [RestCountries](https://restcountries.com/) cada vez que la aplicación se inicia, asegurando un conjunto de datos fresco en cada ejecución.

El proyecto está completamente **"dockerizado"**, lo que garantiza su portabilidad y un despliegue sencillo y consistente en cualquier entorno.

### ✨ Funcionalidades Clave

- **Carga Dinámica desde API:** Obtiene una selección aleatoria de 20 países en cada inicio.
- **Lista y Ordenamiento:** Visualiza la lista completa de países y la ordena por nombre, población o superficie de forma ascendente o descendente.
- **Búsqueda Parcial:** Busca países por nombre de forma insensible a mayúsculas y minúsculas.
- **Filtros Combinados:** Aplica filtros por continente, rango de población y rango de superficie de manera simultánea.
- **Estadísticas Globales:** Muestra datos calculados como los países más/menos poblados, promedios y conteo por continente.
- **Diseño Responsivo:** La interfaz se adapta a dispositivos de escritorio y móviles.

---

## Stack de Tecnologías

- **Backend:** Python 3.11, Flask
- **Frontend:** HTML5, CSS3 (sin frameworks)
- **Fuente de Datos:** [RestCountries API](https://restcountries.com/)
- **Contenerización:** Docker
- **Despliegue:** Render
- **Gestión de tareas:** Trello

---

## Estructura del Proyecto

El código está organizado siguiendo una arquitectura modular para separar la lógica de negocio de la presentación.

---

## Instalación y Ejecución Local

### Requisitos Previos

- Python 3.8+
- Docker Desktop (Recomendado)

### 1. Ejecución con Docker (Método Recomendado)

Este método garantiza que la aplicación se ejecute en un entorno idéntico al de producción.

1.  **Construir la imagen Docker:**

    ```bash
    docker build -t tpi-web-app .
    ```

2.  **Ejecutar el contenedor:**

    ```bash
    docker run -it --rm -p 5000:5000 tpi-web-app
    ```

3.  **Acceder a la aplicación:**
    Abre tu navegador y ve a `http://localhost:5000`.

### 2. Ejecución Local (Sin Docker)

1.  **Clonar el repositorio:**

    ```bash
    git clone [URL-DE-TU-REPOSITORIO]
    cd [NOMBRE-DEL-REPOSITORIO]
    ```

2.  **Crear y activar un entorno virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instalar las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar la aplicación:**

    ```bash
    python app.py
    ```

5.  **Acceder a la aplicación:**
    Abre tu navegador y ve a `http://localhost:5000`.

---

## Video Tutorial

En el siguiente video se explica el problema planteado, la estructura de datos, y se realiza una demostración de la aplicación funcionando.

[![Ver Video Tutorial](https://img.youtube.com/vi/ID_DEL_VIDEO/0.jpg)](https://www.youtube.com/watch?v=ID_DEL_VIDEO)
** [Ver Video Tutorial en YouTube]([URL-DEL-VIDEO-AQUI])**
_(Reemplaza `[URL-DEL-VIDEO-AQUI]` por el enlace a tu video. Si lo subes a YouTube, puedes obtener el ID del video y la miniatura funcionará)._

---

## Documento del Proyecto (Informe Teórico)

El informe completo del proyecto, incluyendo el marco teórico, diagrama de flujo, conclusiones y bibliografía, se encuentra disponible en el siguiente enlace.

** [Acceder al Informe en Google Drive](https://docs.google.com/document/d/1cThdIUpqeXxhHu30nzRwIxvcHwOLfMBXBacSvGYxEsE/edit?usp=sharing)**

---
