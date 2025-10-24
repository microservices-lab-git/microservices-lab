# Blog Service

Microservicio de blog completamente independiente con Django REST Framework.

## 🚀 Funcionalidades implementadas
- ✅ Gestión de categorías activas
- ✅ Gestión de autores
- ✅ CRUD de publicaciones (posts)
- ✅ Búsqueda en título y contenido
- ✅ Paginación automática (10 posts por página)
- ✅ Caché Redis en categorías y detalles de posts
- ✅ Health check con verificación de DB y Redis
- ✅ Logging estructurado JSON
- ✅ Middleware de autorización (preparado para JWT)
- ✅ Datos de ejemplo (seed)

## 🛠️ Tecnologías
- Django 5.0
- Django REST Framework 3.15
- MySQL (mysqlclient)
- Redis para caché
- django-filter para búsqueda
- python-slugify para URLs amigables
- Gunicorn como servidor WSGI
- Docker

## 📊 Modelos de datos

### Category
- `id` - ID único
- `name` - Nombre de la categoría
- `slug` - URL amigable
- `is_active` - Estado activo/inactivo

### Author
- `id` - ID único
- `display_name` - Nombre para mostrar
- `email` - Email único

### Post
- `id` - ID único
- `title` - Título del post
- `slug` - URL amigable
- `body` - Contenido completo
- `author` - Relación con Author
- `category` - Relación con Category
- `status` - Estado (draft/published)
- `published_at` - Fecha de publicación
- `views` - Contador de visualizaciones

## 📡 Endpoints disponibles

### Health Check
- `GET /healthz/` - Verificar estado del servicio

### Categorías
- `GET /api/categories/` - Listar categorías activas (con caché)

### Posts
- `GET /api/posts/` - Listar posts publicados con paginación
- `GET /api/posts/?search=término` - Buscar en título y contenido
- `GET /api/posts/?page=2` - Paginación
- `GET /api/posts/?ordering=-views` - Ordenar por views, fecha, etc.
- `GET /api/posts/{slug}/` - Detalle de post (con caché e incremento de views)

## 🔧 Configuración

### Variables de entorno
```
DEBUG=1
DB_HOST=mysql
DB_NAME=main_db
DB_USER=devuser
DB_PASS=devpass
REDIS_HOST=redis
REDIS_PORT=6379
```

### Ejecutar localmente
```bash
# Construir el contenedor
docker compose build blog

# Levantar servicios
docker compose up -d

# Ejecutar migraciones
docker exec -it blog_service python manage.py makemigrations
docker exec -it blog_service python manage.py migrate

# Cargar datos de ejemplo
docker exec -it blog_service python manage.py seed_blog

# Crear superusuario (opcional)
docker exec -it blog_service python manage.py createsuperuser
```

## 🧪 Pruebas

### Ejemplos con cURL

**Health check:**
```bash
curl http://localhost:8001/healthz/
```

**Listar categorías:**
```bash
curl http://localhost:8001/api/categories/
```

**Listar posts:**
```bash
curl http://localhost:8001/api/posts/
```

**Buscar posts:**
```bash
curl "http://localhost:8001/api/posts/?search=Django"
```

**Detalle de post:**
```bash
curl http://localhost:8001/api/posts/introduccion-a-los-microservicios/
```

**Paginación:**
```bash
curl "http://localhost:8001/api/posts/?page=2"
```

## ⚡ Características de rendimiento

### Caché Redis
- **Categorías**: Cache de 2 minutos (120s)
- **Detalle de posts**: Cache de 1 minuto (60s)
- **Base de datos**: Cache de conexiones

### Optimizaciones
- `select_related()` para evitar N+1 queries
- Índices en campos de búsqueda frecuente
- Paginación automática para listas grandes

## 📋 Datos de ejemplo incluidos

El comando `seed_blog` carga:
- **5 categorías**: Tecnología, Programación, IA, Desarrollo Web, DevOps
- **3 autores**: Ana García, Carlos Rodríguez, María López  
- **30 posts**: Variados entre publicados y borradores

## 🔮 Preparado para el futuro

### Middleware de autorización
- Captura headers `Authorization: Bearer ...`
- Listo para integrar con auth-service
- Logging de intentos de autenticación

### Logging estructurado
- Formato JSON para facilitar análisis
- Métricas de tiempo de respuesta
- Información de requests por endpoint

## 📊 Estado del servicio
- ✅ Contenedor funcionando en puerto 8001
- ✅ Conexión a MySQL establecida
- ✅ Conexión a Redis establecida
- ✅ Migraciones aplicadas
- ✅ Datos de ejemplo cargados
- ✅ Todos los endpoints funcionando
- ✅ Caché funcionando
- ✅ Búsqueda y paginación operativas