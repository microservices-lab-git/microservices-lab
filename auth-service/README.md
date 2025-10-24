# Auth Service

Microservicio de autenticación completamente independiente con Django REST Framework.

## 🚀 Funcionalidades
- ✅ Registro de usuarios con validación
- ✅ Autenticación JWT (access/refresh tokens)
- ✅ Gestión de perfiles de usuario
- ✅ Modelo de usuario personalizado
- ✅ Integración con Redis para caché
- ✅ Conexión a MySQL

## 🛠️ Tecnologías
- Django 5.0
- Django REST Framework 3.15
- Simple JWT 5.3
- MySQL (mysqlclient)
- Redis
- Gunicorn
- Docker

## 📡 Endpoints disponibles

### Autenticación
- `POST /api/register/` - Registro de nuevos usuarios
- `POST /api/token/` - Obtener tokens JWT (login)
- `POST /api/token/refresh/` - Renovar access token
- `POST /api/token/verify/` - Verificar validez del token

### Perfil de usuario
- `GET /api/me/` - Obtener información del usuario autenticado
- `PUT /api/me/update/` - Actualizar perfil del usuario

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
docker compose build auth

# Levantar servicios
docker compose up -d

# Ejecutar migraciones
docker exec -it auth_service python manage.py makemigrations
docker exec -it auth_service python manage.py migrate

# Crear superusuario (opcional)
docker exec -it auth_service python manage.py createsuperuser
```

## 🧪 Pruebas

### Ejemplo de registro
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword123",
    "password_confirm": "securepassword123",
    "first_name": "John",
    "last_name": "Doe"
  }'
```

### Ejemplo de login
```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword123"
  }'
```

### Ejemplo de acceso a perfil
```bash
curl -X GET http://localhost:8000/api/me/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 📊 Estado del servicio
- ✅ Contenedor funcionando en puerto 8000
- ✅ Conexión a MySQL establecida
- ✅ Conexión a Redis establecida
- ✅ Migraciones aplicadas
- ✅ Endpoints probados y funcionando