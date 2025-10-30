FROM python:3.11-slim

# Establecemos el directorio de trabajo.
WORKDIR /app

# Primero, copiamos SOLO el archivo de requerimientos.
COPY requirements.txt .

# Luego, instalamos las dependencias. Docker guardará en caché esta capa.
# Si no cambiamos requirements.txt, este paso no se volverá a ejecutar,
# haciendo las futuras construcciones (builds) mucho más rápidas.
RUN pip install --no-cache-dir -r requirements.txt


# Ahora que las dependencias están instaladas, copiamos el resto del código.
COPY . .

# Le informamos a Docker que el contenedor escuchará en el puerto 5000.
# Esto es más bien una documentación, el mapeo real se hace en 'docker run'.
EXPOSE 5000


# Ejecutamos la aplicación web usando el archivo app.py.
CMD ["python", "app.py"]