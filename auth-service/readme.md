# Auth Service

Servicio de autenticación basado en Django + DRF con JWT (SimpleJWT).

- Base de datos por defecto: SQLite .
- Opcional en `docker-compose.yml`: PostgreSQL y Redis para entornos más completos.
- Expuesto en `http://localhost:8000` dentro del contenedor `auth_service`.

## Requisitos

- Docker y Docker Compose (recomendado) o
- Python 3.11+ y `pip` (ejecución local sin Docker)

## Arranque rápido (Docker)

1. Construir y levantar solo el servicio de auth (usando SQLite y cache en memoria):
   ```bash
   docker-compose up -d --no-deps auth
   ```
2. Aplicar migraciones dentro del contenedor:
   ```bash
   docker exec auth_service python manage.py migrate
   ```
3. (Opcional) Crear un usuario de prueba:
   ```bash
   docker exec auth_service python -c "import os; os.environ['DJANGO_SETTINGS_MODULE']='auth_service.settings'; import django; django.setup(); from users.models import User; User.objects.create_user('usuario@ejemplo.com','contrasena123')"
   ```
4. Ver logs:
   ```bash
   docker logs --tail 100 auth_service
   ```

## Ejecución local (sin Docker)

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Migraciones:
   ```bash
   python manage.py migrate
   ```
3. Levantar servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Endpoints disponibles

- Obtener token (POST): `http://localhost:8000/api/token/`
  - Body JSON:
    ```json
    {
      "email": "usuario@ejemplo.com",
      "password": "contrasena123"
    }
    ```
  - Respuesta:
    ```json
    {
      "refresh": "<refresh_token>",
      "access": "<access_token>"
    }
    ```

- Refrescar token (POST): `http://localhost:8000/api/token/refresh/`
  - Body JSON:
    ```json
    {
      "refresh": "<refresh_token>"
    }
    ```

> Nota: Este proyecto NO incluye `/api/register/` actualmente. Para crear usuarios, usa el comando del contenedor o solicita agregar un endpoint de registro.

## Probar con Postman o curl

- Postman: crea una petición `POST` a `http://localhost:8000/api/token/` con el Body JSON anterior.
- curl:
  ```bash
  curl -X POST http://localhost:8000/api/token/ \
    -H "Content-Type: application/json" \
    -d '{"email":"usuario@ejemplo.com","password":"contrasena123"}'
  ```

## Configuración

- Archivo: `auth_service/settings.py`
- Base de datos: configurada a SQLite:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
      }
  }
  ```
- Cache: memoria local (sin Redis) para desarrollo:
  ```python
  CACHES = {
      'default': {
          'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
          'LOCATION': 'unique-snowflake',
      }
  }
  ```

Para usar PostgreSQL y Redis, ajusta `settings.py` y levanta todo con:
```bash
docker-compose up -d
```

## Problemas comunes

- `ProgrammingError: relation "users_user" does not exist` → Ejecuta migraciones.
- `ModuleNotFoundError: No module named 'corsheaders'` → `pip install -r requirements.txt` dentro de tu entorno/imagen.
- `Method Not Allowed: /api/token/` → Este endpoint acepta solo `POST`.

## Estructura del proyecto

```
Fundamentos-Entorno-Docker-Git/auth-service/
├── auth_service/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/
│   ├── migrations/
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── Dockerfile
├── manage.py
├── requirements.txt
└── readme.md
```
