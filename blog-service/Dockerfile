FROM python:3.11

# Instalar dependencias del sistema para MySQL
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Cambiar al directorio donde está el código Django
WORKDIR /app/app

EXPOSE 8001

CMD ["gunicorn", "blog_service.wsgi:application", "--bind", "0.0.0.0:8001"]