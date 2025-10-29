# Blog Service

Microservicio de blog desarrollado con Django que permite gestionar publicaciones, categorías y autores.

## 🚀 Características

- ✅ API RESTful con Django REST Framework
- 🔍 Búsqueda y paginación en endpoints
- 🚀 Cache con Redis para mejorar el rendimiento
- 📄 Documentación OpenAPI
- 🐳 Dockerizado para fácil despliegue

## 🛠️ Requisitos previos

- Docker y Docker Compose
- Python 3.11+ (solo para desarrollo local)

## 🚀 Instalación

1. Clona el repositorio:
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd blog-service
   ```

2. Copia el archivo de variables de entorno:
   ```bash
   cp .env.example .env
   ```

3. Inicia los servicios con Docker:
   ```bash
   docker compose up -d --build
   ```

4. Ejecuta las migraciones:
   ```bash
   docker compose exec blog_service python manage.py migrate
   ```

5. (Opcional) Carga datos de prueba:
   ```bash
   docker compose exec blog_service python manage.py seed_blog
   ```

## 🌐 Endpoints disponibles

### Health Check
```bash
curl -X 'GET' 'http://localhost:8001/api/healthz/'
```

### Categorías
- **Listar categorías**:
  ```bash
  curl -X 'GET' 'http://localhost:8001/api/categories/'
  ```

### Publicaciones
- **Listar publicaciones** (con paginación):
  ```bash
  # Página 1
  curl -X 'GET' 'http://localhost:8001/api/posts/?page=1'
  ```

- **Buscar publicaciones**:
  ```bash
  curl -X 'GET' 'http://localhost:8001/api/posts/?search=python'
  ```

- **Obtener detalle de publicación**:
  ```bash
  curl -X 'GET' 'http://localhost:8001/api/posts/1/'
  ```

## 🔄 Caché

El servicio utiliza Redis para cachear:
- Listado de categorías
- Detalle de publicaciones

La caché se invalida automáticamente cuando se actualizan los datos.

## 📚 Documentación API

La documentación completa de la API está disponible en formato OpenAPI:
- [openapi.yaml](openapi.yaml)

Puedes visualizarla usando herramientas como:
- [Swagger UI](https://petstore.swagger.io/)
- [ReDoc](https://redocly.github.io/redoc/)

## 🐛 Solución de problemas

Si encuentras algún problema:
1. Verifica que todos los contenedores estén en ejecución:
   ```bash
   docker ps
   ```

2. Revisa los logs del servicio:
   ```bash
   docker logs blog_service
   ```

3. Si necesitas reiniciar el servicio:
   ```bash
   docker compose down
   docker compose up -d
   ```

## 📝 Notas adicionales

- El servicio está configurado para ejecutarse en el puerto 8001
- Los datos se persisten en un volumen de Docker
- Redis se ejecuta en el puerto 6379
- MySQL se ejecuta en el puerto 3306 (mapeado al 3307 en el host)
