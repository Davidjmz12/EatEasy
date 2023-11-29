# Usa la imagen base de Python
FROM python:3.11

# Establece el directorio de trabajo en /app
WORKDIR /app

# Configura las variables de entorno para la conexión PostgreSQL
ENV POSTGRES_DB EatEasyDB
ENV POSTGRES_USER admin
ENV POSTGRES_PASSWORD admin
ENV POSTGRES_HOST postgres
ENV POSTGRES_PORT 5432

# Copia el archivo de requerimientos para instalar dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido de la aplicación al contenedor
COPY . .

RUN python manage.py migrate

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación cuando el contenedor se inicia
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
