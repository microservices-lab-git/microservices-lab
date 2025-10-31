# Guía paso a paso — Día 3

Esta guía detalla la implementación del Día 3 del laboratorio de microservicios. Sigue las indicaciones del documento de ejercicios ("BACKEND Microservicios EJERCICIOS.md") y está lista para ejecutarse y probarse fuera de VSCode (Postman, cURL).

---
## Objetivos
- Construir el microservicio Blog (Django + DRF + PostgreSQL + Redis) con endpoints públicos y caché.
- Alternativa Sala 4: estructurar un servicio Loans con arquitectura hexagonal, puertos/adaptadores y pruebas.
- Documentar endpoints con OpenAPI/Swagger y preparar ambiente de tests.
- Dejar todo listo para validar con Postman/cURL.

---
## 1) Preparación del entorno

### Verificar configuración de Días 1 y 2
- `docker compose ps` debe mostrar `db_postgres` y `cache_redis` (y `auth_service` si ya lo tienes).
- Variables `.env` presentes en la raíz (o `docker-compose.yml` con env en el servicio).
- Docker Desktop en modo Linux y WSL2 activo:
  - Cambiar a “Linux containers” y `docker context use desktop-linux`.
  - Reiniciar WSL si hay dudas: `wsl --shutdown`.

### Dependencias necesarias (Blog)
- Django 5, DRF, `psycopg2-binary`, `django-redis`, `django-filter`, `python-slugify`, `gunicorn`.
- Para documentación: `drf-spectacular` y `drf-spectacular[sidecar]` (Swagger UI integrada).

### Confirmación del entorno
- Ejecuta `docker compose up -d` para bases (Postgres/Redis).
- Si vas a correr comandos de Django localmente: usa un `venv` en `blog-service/` y ajusta `DB_HOST=localhost`. Para contenedor: `DB_HOST=postgres`.

---
## 2) Implementación — Blog Service

El Blog Service expone categorías y posts con paginación, búsqueda y caché. Corre en `8001`.

### Estructura del proyecto
1. Crear proyecto Django dentro de `blog-service/`:
   - `cd blog-service`
   - `python -m venv .venv` (opcional, si deseas correr local)
   - `source .venv/Scripts/activate` en Windows PowerShell: `.venv\Scripts\Activate.ps1`
   - `pip install Django djangorestframework psycopg2-binary django-redis django-filter python-slugify gunicorn drf-spectacular "drf-spectacular[sidecar]"`
   - `django-admin startproject blog_service .`
   - `python manage.py startapp categories`
   - `python manage.py startapp authors`
   - `python manage.py startapp posts`

2. `requirements.txt` (en `blog-service/`):
   ```
   Django==5.0
   djangorestframework==3.15
   psycopg2-binary
   django-redis
   django-filter
   python-slugify
   gunicorn
   drf-spectacular
   drf-spectacular[sidecar]
   ```

3. `Dockerfile` (en `blog-service/`):
   ```
   FROM python:3.11
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["gunicorn", "blog_service.wsgi:application", "--bind", "0.0.0.0:8001"]
   ```

4. Extender `docker-compose.yml` (en raíz):
   ```
   blog:
     build: ./blog-service
     container_name: blog_service
     environment:
       - DB_HOST=postgres
       - DB_NAME=main_db
       - DB_USER=devuser
       - DB_PASS=devpass
       - REDIS_HOST=redis
       - REDIS_PORT=6379
       - DEBUG=1
     depends_on:
       - postgres
       - redis
     ports:
       - "8001:8001"
   ```

### Configuración (`blog_service/settings.py`)
- `INSTALLED_APPS`: `rest_framework`, `django_filters`, `drf_spectacular`, `categories`, `authors`, `posts`.
- `DATABASES` (PostgreSQL):
  ```python
  import os
  DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.postgresql",
          "NAME": os.getenv("DB_NAME", "main_db"),
          "USER": os.getenv("DB_USER", "devuser"),
          "PASSWORD": os.getenv("DB_PASS", "devpass"),
          "HOST": os.getenv("DB_HOST", "localhost"),  # "postgres" en contenedor
          "PORT": os.getenv("DB_PORT", "5432"),
      }
    }
  ```
- `CACHES` (Redis):
  ```python
  CACHES = {
      "default": {
          "BACKEND": "django_redis.cache.RedisCache",
          "LOCATION": f"redis://{os.getenv('REDIS_HOST','localhost')}:{os.getenv('REDIS_PORT','6379')}/1",
          "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
          "KEY_PREFIX": "blog",
      }
  }
  ```
- DRF y Spectacular:
  ```python
  REST_FRAMEWORK = {
      "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
      "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
      "PAGE_SIZE": 10,
      "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
  }
  SPECTACULAR_SETTINGS = {
      "TITLE": "Blog Service API",
      "DESCRIPTION": "Endpoints públicos para categorías y posts.",
      "VERSION": "1.0.0",
  }
  ```
- Logging (simple estructurado):
  ```python
  LOGGING = {
      "version": 1,
      "disable_existing_loggers": False,
      "formatters": {
          "json": {
              "format": '{"time":"%(asctime)s","level":"%(levelname)s","name":"%(name)s","message":"%(message)s"}'
          }
      },
      "handlers": {
          "console": {"class": "logging.StreamHandler", "formatter": "json"}
      },
      "root": {"handlers": ["console"], "level": "INFO"},
  }
  ```
- `ALLOWED_HOSTS = ["*"]` y `DEBUG=os.getenv("DEBUG") == "1"` durante desarrollo.

### Modelos
- `categories/models.py`:
  ```python
  from django.db import models
  class Category(models.Model):
      name = models.CharField(max_length=120, unique=True)
      slug = models.SlugField(max_length=140, unique=True)
      is_active = models.BooleanField(default=True)
      def __str__(self): return self.name
  ```
- `authors/models.py`:
  ```python
  from django.db import models
  class Author(models.Model):
      display_name = models.CharField(max_length=120)
      email = models.EmailField(unique=True)
      def __str__(self): return self.display_name
  ```
- `posts/models.py`:
  ```python
  from django.db import models
  from django.utils import timezone
  from slugify import slugify
  from authors.models import Author
  from categories.models import Category
  class Post(models.Model):
      STATUS_CHOICES = [("published","published"),("draft","draft")]
      title = models.CharField(max_length=200)
      slug = models.SlugField(maxlength=220, unique=True)
      body = models.TextField()
      author = models.ForeignKey(Author, on_delete=models.PROTECT)
      category = models.ForeignKey(Category, on_delete=models.PROTECT)
      status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
      published_at = models.DateTimeField(null=True, blank=True)
      views = models.PositiveIntegerField(default=0)
      def save(self, *args, **kwargs):
          if not self.slug:
              self.slug = slugify(self.title)
          if self.status == "published" and not self.published_at:
              self.published_at = timezone.now()
          super().save(*args, **kwargs)
      def __str__(self): return self.title
  ```

- Registrar en `admin.py` (opcional) y realizar migraciones:
  - `python manage.py makemigrations`
  - `python manage.py migrate`
  - En contenedor: `docker compose exec blog python manage.py migrate`

### Serializers
- `categories/serializers.py`:
  ```python
  from rest_framework import serializers
  from .models import Category
  class CategorySerializer(serializers.ModelSerializer):
      class Meta:
          model = Category
          fields = ["id","name","slug","is_active"]
  ```
- `posts/serializers.py`:
  ```python
  from rest_framework import serializers
  from .models import Post
  class PostSerializer(serializers.ModelSerializer):
      class Meta:
          model = Post
          fields = ["id","title","slug","body","status","published_at","views","author","category"]
  ```

### Vistas (DRF) y caché
- `categories/views.py`:
  ```python
  from rest_framework.generics import ListAPIView
  from django.utils.decorators import method_decorator
  from django.views.decorators.cache import cache_page
  from .models import Category
  from .serializers import CategorySerializer
  class CategoryListView(ListAPIView):
      queryset = Category.objects.filter(is_active=True).order_by("name")
      serializer_class = CategorySerializer
      @method_decorator(cache_page(90))  # TTL 90s
      def dispatch(self, *args, **kwargs):
          return super().dispatch(*args, **kwargs)
  ```
- `posts/views.py`:
  ```python
  from rest_framework.generics import ListAPIView, RetrieveAPIView
  from django.db.models import Q
  from django.utils.decorators import method_decorator
  from django.views.decorators.cache import cache_page
  from .models import Post
  from .serializers import PostSerializer
  class PostListView(ListAPIView):
      serializer_class = PostSerializer
      def get_queryset(self):
          qs = Post.objects.filter(status="published").order_by("-published_at")
          search = self.request.query_params.get("search")
          if search:
              qs = qs.filter(Q(title__icontains=search) | Q(body__icontains=search))
          return qs
  class PostDetailView(RetrieveAPIView):
      serializer_class = PostSerializer
      lookup_field = "slug"
      queryset = Post.objects.filter(status="published")
      @method_decorator(cache_page(120))  # TTL 120s
      def dispatch(self, *args, **kwargs):
          return super().dispatch(*args, **kwargs)
  ```

### Salud y logging
- `core/views.py` (crear app `core` opcional o añadir a `blog_service/views.py`):
  ```python
  from django.db import connection
  from django.core.cache import cache
  from django.http import JsonResponse
  def healthz(request):
      db_ok = True
      try:
          with connection.cursor() as cur:
              cur.execute("SELECT 1")
      except Exception:
          db_ok = False
      cache_ok = True
      try:
          cache.set("healthz", "ok", timeout=10)
          cache_ok = cache.get("healthz") == "ok"
      except Exception:
          cache_ok = False
      return JsonResponse({"db": db_ok, "redis": cache_ok})
  ```

### URLs y documentación
- `blog_service/urls.py`:
  ```python
  from django.contrib import admin
  from django.urls import path, include
  from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
  from core.views import healthz
  urlpatterns = [
      path("admin/", admin.site.urls),
      path("api/categories/", include("categories.urls")),
      path("api/posts/", include("posts.urls")),
      path("healthz", healthz),
      path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
      path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
  ]
  ```
- `categories/urls.py`:
  ```python
  from django.urls import path
  from .views import CategoryListView
  urlpatterns = [path("", CategoryListView.as_view(), name="categories-list")]
  ```
- `posts/urls.py`:
  ```python
  from django.urls import path
  from .views import PostListView, PostDetailView
  urlpatterns = [
      path("", PostListView.as_view(), name="posts-list"),
      path("<slug:slug>", PostDetailView.as_view(), name="posts-detail"),
  ]
  ```

### Build y arranque
- Construir y levantar:
  - `docker compose build blog`
  - `docker compose up -d blog`
- Migraciones dentro del contenedor:
  - `docker compose exec blog python manage.py makemigrations`
  - `docker compose exec blog python manage.py migrate`
- Semilla rápida (opcional):
  ```bash
  docker compose exec blog python manage.py shell <<'PY'
  from categories.models import Category
  from authors.models import Author
  from posts.models import Post
  cat = Category.objects.create(name="General", slug="general", is_active=True)
  auth = Author.objects.create(display_name="Equipo", email="equipo@example.com")
  Post.objects.create(title="Hola Mundo", body="Contenido...", author=auth, category=cat, status="published")
  print("Seed listo")
  PY
  ```

### Endpoints y ejemplos
- Listar categorías:
  - `GET http://localhost:8001/api/categories/`
- Listar posts con búsqueda:
  - `GET http://localhost:8001/api/posts/?search=hola&page=1`
- Detalle por slug:
  - `GET http://localhost:8001/api/posts/hola-mundo`
- Salud:
  - `GET http://localhost:8001/healthz`
- OpenAPI/Swagger:
  - `GET http://localhost:8001/api/schema/` (JSON)
  - `GET http://localhost:8001/api/docs/` (UI)
- cURL de ejemplo:
  ```
  curl http://localhost:8001/api/categories/
  curl "http://localhost:8001/api/posts/?search=hola&page=1"
  curl http://localhost:8001/api/posts/hola-mundo
  curl http://localhost:8001/healthz
  ```

### Manejo de errores y validaciones
- `Category.name` y `Category.slug` únicos; responder `400` si se violan.
- En creación/actualización de `Post`, validar `status` y consistencia de `published_at`.
- Manejo básico de errores:
  ```python
  from rest_framework.exceptions import ValidationError
  # Ejemplo: raise ValidationError({"field": "mensaje"})
  ```
- Logs JSON en consola facilitan rastreo (`LOGGING` arriba).

---
## 3) Documentación del código
- Añade comentarios explicativos en modelos/vistas donde haya lógica (por ejemplo, generación de `slug` y `published_at`).
- Documenta endpoints con `drf-spectacular` mediante docstrings:
  ```python
  from drf_spectacular.utils import extend_schema
  @extend_schema(summary="Lista categorías activas", tags=["Categories"])
  class CategoryListView(ListAPIView):
      ...
  ```
- Exportar contrato OpenAPI:
  - JSON: `curl http://localhost:8001/api/schema/ -o blog-openapi.json`
  - YAML: usar `pip install pyyaml` y convertir o configurar `SPECTACULAR_SETTINGS` para generar YAML.
- Incluye ejemplos de request/response en la documentación (Swagger UI permite probar).

---
## 4) Preparación para testing

### Ambiente de pruebas
- Usa el test runner de Django:
  - `docker compose exec blog python manage.py test`
- Opcional: `pytest` + `pytest-django`.

### Casos de prueba sugeridos
- Categorías:
  - Lista solo categorías activas; cache TTL respeta.
- Posts:
  - Paginación (10 por página) y parámetro `page`.
  - Búsqueda por `title`/`body` (`search`).
  - Detalle por `slug`; TTL cache y consistencia tras actualizar.
- Salud:
  - `db` y `redis` devuelven `True` cuando operativos.

### Datos de prueba
- Fixtures mínimos para `Category`, `Author`, `Post`.
- Usa `setUpTestData` en `TestCase` para preparar datos iniciales.

### Documentar escenarios
- Describe entradas, salidas esperadas, estados de caché y errores (`400/404/500`).

---
## 5) Errores comunes y soluciones
- Compose warning `version`: elimina `version: "3.9"` en Compose v2.
- Error conectando al daemon Docker en Windows:
  - Inicia Docker Desktop, usa Linux containers, `docker context use desktop-linux`, reinicia WSL.
- `psycopg2-binary`/compilación:
  - Asegúrate de instalar con `pip`; en contenedor está en `requirements.txt`.
- DB host incorrecto:
  - Dentro del contenedor usa `DB_HOST=postgres`; local usa `localhost`.
- Migraciones no aplicadas:
  - Ejecuta `makemigrations` y `migrate` dentro del contenedor `blog`.
- Redis sin conexión:
  - Revisa `REDIS_HOST`/`REDIS_PORT`; prueba `healthz`.
- Puerto ocupado `8001`:
  - Cambia el mapeo en Compose (por ejemplo, `8002:8001`).

---
## 6) Verificación final (Checklist)
- Servicio `blog_service` corriendo en `http://localhost:8001/`.
- Endpoints devuelven datos y respetan paginación/búsqueda.
- Cache activo (`categories` y `post detail` con TTL).
- `healthz` OK para DB y Redis.
- Swagger en `/api/docs/` funcional y esquema exportable.
- Guía clara, ejemplos probados con Postman/cURL.

---
## Anexo — Sala 4 (Hexagonal + Microservicios)

Esta alternativa guía el servicio Loans con arquitectura hexagonal.

### Estructura sugerida
```
loans_service/
  src/
    domain/
      entities/loan.py
      rules/validators.py
      ports/{users_repo.py, books_repo.py, clock.py, uuid_gen.py}
      services/loan_service.py
    application/
      use_cases/{create_loan_uc.py, return_loan_uc.py}
      dtos/{loan_request_dto.py, loan_response_dto.py}
    infrastructure/
      repositories/{users_repo_http.py, books_repo_http.py, loans_repo_django.py}
      services/{clock_system.py, uuid_native.py}
      configs/container.py
    interfaces/api/{serializers.py, views.py, urls.py}
  tests/{unit/, integration/}
```

### Reglas del dominio
- Máximo 3 préstamos activos por usuario.
- Duración ≤ 15 días.
- Usuario activo y no suspendido.
- Libro disponible.

### Ejemplo de dominio (`domain/services/loan_service.py`)
```python
from dataclasses import dataclass
from datetime import timedelta
@dataclass
class LoanRequest:
    user_id: str
    book_id: str
    days: int
class LoanService:
    def __init__(self, users_repo, books_repo, clock, uuid_gen):
        self.users_repo = users_repo
        self.books_repo = books_repo
        self.clock = clock
        self.uuid_gen = uuid_gen
    def create_loan(self, req: LoanRequest):
        if req.days < 1 or req.days > 15:
            raise ValueError("Duración inválida")
        user = self.users_repo.get_user(req.user_id)
        if user.status != "active":
            raise ValueError("Usuario no activo")
        count = self.users_repo.get_active_loans_count(req.user_id)
        if count >= 3:
            raise ValueError("Límite de préstamos alcanzado")
        book = self.books_repo.get_book(req.book_id)
        if book.status != "available":
            raise ValueError("Libro no disponible")
        loan_id = self.uuid_gen.new()
        due_date = self.clock.now() + timedelta(days=req.days)
        self.books_repo.mark_loaned(req.book_id)
        return {"loan_id": loan_id, "due_date": due_date.isoformat(), "status": "active"}
```

### Adaptadores HTTP con timeout/retry (`infrastructure/repositories/users_repo_http.py`)
```python
import httpx
class UsersRepoHTTP:
    def __init__(self, base_url: str):
        self.base_url = base_url
    def get_user(self, user_id: str):
        with httpx.Client(timeout=3.0) as client:
            for _ in range(2):
                r = client.get(f"{self.base_url}/api/users/{user_id}")
                if r.status_code == 200: return r.json()
            raise RuntimeError("Users API no responde")
    def get_active_loans_count(self, user_id: str):
        with httpx.Client(timeout=3.0) as client:
            for _ in range(2):
                r = client.get(f"{self.base_url}/api/users/{user_id}/loans/count", params={"status":"active"})
                if r.status_code == 200: return r.json()["count"]
            raise RuntimeError("Users API no responde")
```

### Interfaces API (Loans)
- Endpoints:
  - `POST /api/loans` → crea préstamo
  - `POST /api/loans/{loan_id}/return` → devuelve préstamo
  - `GET /api/loans/{loan_id}` → detalle
- OpenAPI mínimo (exportable con `drf-spectacular` o archivo `openapi.yaml` manual).

### Tests
- Unitarios (dominio): validar reglas sin framework.
- Integración: adaptadores HTTP (mock), repositorio Django, endpoints.
- Ejecutar: `python manage.py test` o `pytest`.

---
## Cierre
Con esta guía puedes implementar el Blog Service (o el servicio Loans para Sala 4), documentarlo con OpenAPI, preparar pruebas y validar todo con Postman/cURL, respetando las reglas y el enfoque de microservicios del laboratorio.
## Estado actual en este repositorio (Blog Service)

Se ejecutó la implementación propuesta para el servicio de Blog (Django + DRF + PostgreSQL + Redis), con construcción y arranque de contenedores, migraciones, datos de ejemplo y verificación de endpoints.

### Pasos ejecutados
- Construcción de imagen: `docker compose build blog`
- Arranque de servicios: `docker compose up -d blog` (levanta `blog`, `db_postgres` y `cache_redis`).
- Creación de migraciones iniciales: `docker compose exec blog python manage.py makemigrations categories authors posts`
- Aplicación de migraciones: `docker compose exec blog python manage.py migrate`
- Carga de datos de ejemplo: `docker compose exec blog python manage.py seed_blog`

### Endpoints verificados
- Salud: `GET http://localhost:8001/healthz`
- Categorías (paginado, cache TTL 90s): `GET http://localhost:8001/api/categories/`
- Posts publicados (paginado, búsqueda por `search`): `GET http://localhost:8001/api/posts/`
- Detalle de post por `slug` (cache TTL 120s): `GET http://localhost:8001/api/posts/<slug>`

Notas:
- En este proyecto la ruta de salud es `healthz`.
- El detalle de post se expone sin barra final, por ejemplo: `http://localhost:8001/api/posts/hola-mundo`
- Swagger/OpenAPI está disponible en `http://localhost:8001/api/docs/`.

### Qué queda por hacer fuera de consola/VS Code
- Probar manualmente en Postman o navegador los endpoints anteriores (incluyendo parámetros de búsqueda `?search=...`).
- Navegar la documentación interactiva en `http://localhost:8001/api/docs/` y revisar el esquema en `http://localhost:8001/api/schema/`.
- (Opcional) Crear un superusuario para acceder al admin (`/admin/`) usando `python manage.py createsuperuser` de forma interactiva.

### Comprobación rápida (ejemplos)
- `GET http://localhost:8001/healthz` debe devolver `{"db": true, "redis": true}`.
- `GET http://localhost:8001/api/categories/` debe listar al menos la categoría `General`.
- `GET http://localhost:8001/api/posts/` debe listar el post `Hola Mundo`.
- `GET http://localhost:8001/api/posts/hola-mundo` debe devolver el detalle del post.

Si algo falla, revisa logs con `docker compose logs blog --tail=200` y valida variables de entorno en `blog-service/blog_service/settings.py` (DB y Redis).