# Guía paso a paso — Día 1 y Día 2

Esta guía concentra las instrucciones prácticas para completar las tareas del Día 1 (entorno base con Docker/Git) y del Día 2 (microservicio de autenticación con Django + DRF + JWT + PostgreSQL + Redis).

## Requisitos previos
- Windows con Docker Desktop instalado y en modo Linux (WSL2).
- Git instalado y repositorio clonado localmente.
- Virtualización habilitada (VT-x/AMD-V) y WSL2 activo.

---
## Día 1 — Fundamentos + Entorno Docker / Git

### Objetivo
Dejar funcionando los servicios base (PostgreSQL y Redis) vía Docker Compose y tener el repo con estructura inicial.

### Pasos
1. Estructura del proyecto
   - Crear carpetas: `auth-service`, `blog-service`, `email-service`, `frontend`, `reverse-proxy`.
   - Añadir un `README.md` en cada servicio describiendo su propósito.

2. Variables de entorno
   - En la raíz crear `.env.example` con:
     - `POSTGRES_USER=devuser`
     - `POSTGRES_PASSWORD=devpass`
     - `POSTGRES_DB=main_db`
     - `REDIS_HOST=redis`
     - `REDIS_PORT=6379`
   - Copiar a `.env` para uso local (no subir `.env` al repo).

3. Docker Compose base
   - Verificar `docker-compose.yml` con servicios `postgres` y `redis` y volumen `pgdata`.
   - Comandos:
     - `docker compose up -d`
     - `docker ps` (debe mostrar `db_postgres` y `cache_redis`)
     - Logs: `docker compose logs postgres --tail=100`, `docker compose logs redis --tail=100`

4. Mini-reto: test de conexiones
   - En `auth-service/test_connection.py` probar conexión a PostgreSQL y Redis usando variables de entorno.
   - Ejecutar dentro del contenedor `auth` (más fiable):
     - `docker compose exec auth python test_connection.py`

### Validación
- Contenedores base arriba y estables.
- Script de prueba devuelve `PostgreSQL OK: True` y `Redis OK: True`.

---
## Día 2 — Microservicio Auth (Django + DRF + JWT)

### Objetivo
Crear `auth-service` con login JWT y endpoints básicos, conectado a PostgreSQL y Redis.

### Estructura y dependencias
- `auth-service/requirements.txt`:
  - `django==5.0`
  - `djangorestframework==3.15`
  - `djangorestframework-simplejwt==5.3`
  - `psycopg2-binary`
  - `redis`
  - `django-cors-headers`
  - `gunicorn`
- `auth-service/Dockerfile` (ejecución con gunicorn):
  - `FROM python:3.11`
  - `WORKDIR /app`
  - `COPY requirements.txt .` y `RUN pip install -r requirements.txt`
  - `COPY . .`
  - `CMD ["gunicorn", "auth_service.wsgi:application", "--bind", "0.0.0.0:8000"]`
- `docker-compose.yml` añadir servicio `auth` con env (`DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASS`, `REDIS_HOST`, `REDIS_PORT`).

### Proyecto Django
1. Inicialización
   - En `auth-service/`: `django-admin startproject auth_service .`
   - `python manage.py startapp users`

2. Configuración (`auth_service/settings.py`)
   - `INSTALLED_APPS`: `rest_framework`, `corsheaders`, `users`.
   - `DATABASES`: leer `DB_*` desde entorno (motor `postgresql`).
   - `CACHES`: Redis via `REDIS_HOST` y `REDIS_PORT`.
   - `AUTH_USER_MODEL = 'users.User'`.
   - `REST_FRAMEWORK` con `JWTAuthentication`.
   - `CORS_ALLOW_ALL_ORIGINS = True` (solo desarrollo).

3. Rutas (`auth_service/urls.py`)
   - `admin/`
   - `api/token/` y `api/token/refresh/` (SimpleJWT)
   - `api/` incluir `users.urls`

4. Modelo y API (`users/`)
   - `models.py`: usuario con `email` como identificador y manager (`create_user`, `create_superuser`).
   - `serializers.py`: `RegisterSerializer` para crear usuarios.
   - `views.py`: `RegisterView` (AllowAny) y `MeView` (IsAuthenticated).
   - `urls.py`: `register/` y `me/`.
   - `admin.py`: registrar `User` (opcional).

### Build, arranque y migraciones
- ``
- `docker compose up -d`
- Migraciones dentro del contenedor:
  - `docker exec -it auth_service python manage.py makemigrations`
  - `docker exec -it auth_service python manage.py migrate`
- Superusuario (opcional):
  - `docker exec -it auth_service python manage.py createsuperuser`

### Pruebas de endpoints
- Registrar: `POST /api/register/` body `{ "email": "dev@example.com", "password": "12345678" }`
- Login: `POST /api/token/` body `{ "email": "dev@example.com", "password": "12345678" }`
- Perfil: `GET /api/me` con `Authorization: Bearer <access_token>`

### Notas de calidad y seguridad
- No subir `.env` (usar `.env.example`).
- Restringir CORS y configurar `ALLOWED_HOSTS` en staging/prod.
- Usar HTTPS y revisar expiración/rotación de tokens.

---
## Solución de problemas comunes
- Advertencia Compose: `version` obsoleta
  - Eliminar `version: "3.9"` del `docker-compose.yml` para evitar el warning (Compose v2).
- Error de motor Docker en Windows
  - Asegurar Docker Desktop corriendo y contexto Linux/WSL:
    - Cambiar a “Linux containers”.
    - `docker context use desktop-linux`
    - Reiniciar WSL: `wsl --shutdown` y reiniciar Docker Desktop.
- Ejecución de tests
  - Preferir `docker compose exec auth python test_connection.py` para usar dependencias y env del contenedor.