## **Video  Fundamentos \+ Docker \+ Git**

https://www.youtube.com/watch?v=wj766sxHZrM\&t=20s

🎯 **Objetivo:** entender qué son los microservicios, instalar y configurar Docker y Git.  
 🕐 **Duración del bloque a visualizar:**  
 ➡️ **Desde minuto 0:00 hasta minuto 26:00** del video.

---

### **📹 Detalle minuto a minuto**

| Minutos | Tema | Estado | Instrucción |
| ----- | ----- | ----- | ----- |
| **0:00 – 5:00** | Introducción general y objetivos del curso. Qué son los microservicios. | ✅ **Obligatorio** | Escuchar completo. Conceptos base que usarán toda la semana. |
| **5:00 – 10:00** | Principios: autonomía, acoplamiento, escalabilidad, observabilidad. | ✅ **Obligatorio** | Tomar notas — base teórica para arquitectura modular. |
| **10:00 – 20:00** | Instalación y configuración de Docker Desktop y Docker Compose (WSL2). | ✅ **Obligatorio** | Repetir los pasos y dejar Docker funcionando localmente. |
| **20:00 – 24:00** | Configuración de Git y GitHub (ramas Main / Staging). | ✅ **Obligatorio** | Crear repo propio del equipo. |
| **24:00 – 26:00** | Inicio de explicación de Kafka / Confluent Cloud. | ⚠️ **Opcional — saltar o ver solo como referencia.** | No aplicable para esta semana (Kafka se ve en la demo final). |

# **🧭 DÍA 1 — Fundamentos \+ Entorno Docker / Git**

## **🎯 Objetivo general**

Comprender qué es una arquitectura de microservicios y preparar el entorno de trabajo para los siguientes días.  
 El grupo debe terminar el día con una base funcional en **Docker Compose**, donde cada servicio puede ser levantado de forma independiente.

---

## **🧩 Conceptos que deben dominar**

* Diferencia entre monolito y microservicios

* Principios básicos: **autonomía, responsabilidad única, acoplamiento flexible, escalabilidad y observabilidad**

* Estructura de proyecto “multi-servicio”

* Uso de Docker \+ Docker Compose para levantar contenedores

* Control de versiones en Git (ramas Main y Staging)

---

## **🛠️ Tareas prácticas paso a paso**

### **1️⃣ Crear la estructura base del proyecto**

`mkdir microservices-lab`  
`cd microservices-lab`  
`mkdir auth-service blog-service email-service frontend reverse-proxy`

Dentro de cada carpeta, crear un `README.md` vacío describiendo qué contendrá.

---

### **2️⃣ Inicializar Git y GitHub**

`git init`  
`git branch -M main`  
`git add .`  
`git commit -m "Estructura inicial del laboratorio de microservicios"`

Luego crear el repo remoto y vincularlo:

`git remote add origin https://github.com/<tu-org>/microservices-lab.git`  
`git push -u origin main`

---

### **3️⃣ Preparar el entorno Docker Compose**

Crea en la raíz un archivo `docker-compose.yml`:

`version: "3.9"`  
`services:`  
  `postgres:`  
    `image: postgres:15`  
    `container_name: db_postgres`  
    `restart: always`  
    `environment:`  
      `POSTGRES_USER: devuser`  
      `POSTGRES_PASSWORD: devpass`  
      `POSTGRES_DB: main_db`  
    `ports:`  
      `- "5432:5432"`  
    `volumes:`  
      `- pgdata:/var/lib/postgresql/data`

  `redis:`  
    `image: redis:7`  
    `container_name: cache_redis`  
    `restart: always`  
    `ports:`  
      `- "6379:6379"`

`volumes:`  
  `pgdata:`

Ejecutar:

`docker compose up -d`  
`docker ps`

✅ Si ves los contenedores `db_postgres` y `cache_redis` activos, el entorno base está listo.

---

### **4️⃣ Crear archivos de entorno**

En la raíz:

`.env.example`

`POSTGRES_USER=devuser`  
`POSTGRES_PASSWORD=devpass`  
`POSTGRES_DB=main_db`  
`REDIS_HOST=redis`  
`REDIS_PORT=6379`

Cada equipo debe copiarlo a `.env` local.

---

### **5️⃣ Registrar en README el diseño inicial**

En `README.md` (raíz):

`# Laboratorio de Microservicios (Django + React)`

`## Arquitectura inicial`  
`- auth-service/      → Autenticación y tokens JWT`  
`- blog-service/      → Publicaciones, autores y categorías`  
`- email-service/     → Notificaciones y formularios`  
`- frontend/          → Interfaz React`  
`- reverse-proxy/     → Balanceo / Gateway local`

`Servicios base:`  
`- PostgreSQL (5432)`  
`- Redis (6379)`

---

## **🧪 Mini-reto de cierre del día**

* Levantar los contenedores (`docker compose up -d`).

* Crear un archivo `test_connection.py` en `auth-service/` que pruebe la conexión a PostgreSQL y Redis usando variables de entorno.

* Ejecutarlo con `docker exec -it` dentro del contenedor.

---

## **📦 Entregables del Día 1**

| Entregable | Descripción |
| ----- | ----- |
| **Repo Git** | Subido a GitHub con estructura base y `.env.example` |
| **Docker Compose funcional** | Levanta PostgreSQL y Redis sin errores |
| **README documentado** | Incluye arquitectura y checklist |
| **Captura o video corto** | Mostrando los contenedores en ejecución (`docker ps`) |

---

## **🧠 Evaluación**

| Criterio | Peso |
| ----- | ----- |
| Entorno Docker funcionando | 40 % |
| Organización y limpieza del repo | 25 % |
| README claro y completo | 20 % |
| Comunicación y trabajo en equipo (Scrum Daily) | 15 % |

# **🧭 Evaluación — Día 1: Fundamentos \+ Entorno Docker / Git**

## **🎯 Objetivo**

Comprobar que cada practicante:

* Entiende los principios y beneficios de los microservicios.

* Maneja los comandos básicos de Git y Docker.

* Puede explicar cómo se relaciona la teoría con la práctica configurada.

---

## **🧠 Preguntas teóricas (10 preguntas × 2 pts \= 20 pts)**

| Nº | Pregunta | Ponderación |
| ----- | ----- | ----- |
| **1** | ¿Qué diferencia principal existe entre una arquitectura **monolítica** y una **de microservicios**? | 2 pts |
| **2** | Menciona **dos ventajas** y **dos desventajas** de usar microservicios. | 2 pts |
| **3** | Explica con tus palabras qué significa el principio de **responsabilidad única** en un microservicio. | 2 pts |
| **4** | ¿Qué implica tener un **acoplamiento flexible** entre servicios y cómo se logra en Django REST? | 2 pts |
| **5** | ¿Qué función cumple **Docker Compose** dentro de una arquitectura de microservicios? | 2 pts |
| **6** | ¿Para qué sirve el archivo **.env** y por qué no debe subirse al repositorio? | 2 pts |
| **7** | Indica los comandos para **crear una nueva rama**, **hacer un commit** y **subirlo al remoto**. | 2 pts |
| **8** | ¿Qué papel cumple **Redis** dentro del ecosistema de microservicios? | 2 pts |
| **9** | ¿Qué buenas prácticas del modelo **12 Factor App** aplicaste hoy al crear tu entorno Dockerizado? | 2 pts |
| **10** | Si un contenedor no arranca, ¿qué comando usarías para **inspeccionar logs o errores** y cómo lo resolverías? | 2 pts |

# **🧭 DÍA 2 — Ejercicio 2: BACKEND Microservicio Backend Auth (Django \+ DRF \+ JWT \+ PostgreSQL \+ Redis)**

🎯 **Objetivo general:**  
 Construir un microservicio de autenticación completamente independiente, que maneje usuarios, login y tokens JWT, corriendo en su propio contenedor Docker y conectado a PostgreSQL y Redis.

---

## **🧩 Conceptos clave**

* Autenticación basada en **JWT (JSON Web Tokens)**

* Estructura de un **servicio Django aislado**

* Configuración de variables de entorno y dependencias

* Cacheo y sesiones con Redis

* Comunicación segura entre servicios vía API

---

## **🕐 Video de referencia:**

🎥 *“Microservicios con Django REST Framework, Next.js y Apache Kafka”*  
 👉 [https://www.youtube.com/watch?v=wj766sxHZrM](https://www.youtube.com/watch?v=wj766sxHZrM&utm_source=chatgpt.com)

📍 **Ver desde:** **minuto 26:13 hasta 2:54:00**

(No ver ni implementar la parte de Kafka Producer — solo REST y Redis)

---

## **⚙️ Pasos del ejercicio**

### **1️⃣ Crear el proyecto Django y app `users`**

`cd auth-service`  
`django-admin startproject auth_service .`  
`python manage.py startapp users`

### **2️⃣ Configurar el `Dockerfile`**

`FROM python:3.11`  
`WORKDIR /app`  
`COPY requirements.txt .`  
`RUN pip install -r requirements.txt`  
`COPY . .`  
`CMD ["gunicorn", "auth_service.wsgi:application", "--bind", "0.0.0.0:8000"]`

### **3️⃣ Extender `docker-compose.yml`**

`auth:`  
  `build: ./auth-service`  
  `container_name: auth_service`  
  `restart: always`  
  `environment:`  
    `- DEBUG=1`  
    `- DB_HOST=postgres`  
    `- DB_NAME=main_db`  
    `- DB_USER=devuser`  
    `- DB_PASS=devpass`  
    `- REDIS_HOST=redis`  
    `- REDIS_PORT=6379`  
  `depends_on:`  
    `- postgres`  
    `- redis`  
  `ports:`  
    `- "8000:8000"`

---

### **4️⃣ Instalar dependencias (en `requirements.txt`)**

`django==5.0`  
`djangorestframework==3.15`  
`djangorestframework-simplejwt==5.3`  
`psycopg2-binary`  
`redis`  
`django-cors-headers`

---

### **5️⃣ Configurar `settings.py`**

* Añadir `rest_framework`, `corsheaders`, `users`

* Configurar **DATABASES** con variables de entorno

* Configurar **CACHES** (Redis)

* Añadir middleware `corsheaders.middleware.CorsMiddleware`

* Definir `REST_FRAMEWORK` con `JWTAuthentication`

---

### **6️⃣ Modelo de usuario personalizado**

En `users/models.py`:

`from django.contrib.auth.models import AbstractBaseUser, BaseUserManager`  
`from django.db import models`

`class UserManager(BaseUserManager):`  
    `def create_user(self, email, password=None):`  
        `if not email:`  
            `raise ValueError("Email obligatorio")`  
        `user = self.model(email=self.normalize_email(email))`  
        `user.set_password(password)`  
        `user.save(using=self._db)`  
        `return user`

`class User(AbstractBaseUser):`  
    `email = models.EmailField(unique=True)`  
    `is_active = models.BooleanField(default=True)`  
    `is_admin = models.BooleanField(default=False)`  
    `USERNAME_FIELD = 'email'`  
    `objects = UserManager()`

    `def __str__(self):`  
        `return self.email`

Registrar en `settings.py`:

`AUTH_USER_MODEL = 'users.User'`

---

### **7️⃣ Endpoints con JWT**

En `users/views.py` o rutas de API:

`from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView`

Configura rutas:

`path('api/token/', TokenObtainPairView.as_view()),`  
`path('api/token/refresh/', TokenRefreshView.as_view()),`

Crea también un endpoint `/api/register/` que permita crear usuarios.

---

### **8️⃣ Probar con Postman**

* **POST /api/register/** → crea usuario

* **POST /api/token/** → genera access/refresh token

* **POST /api/token/refresh/** → renueva token

Verificar conexión con base de datos y Redis:

`docker exec -it auth_service python manage.py shell`

---

## **🧪 Reto adicional (opcional)**

Implementar endpoint `/api/me/` que devuelva la información del usuario autenticado.

---

## **📦 Entregables del Día 2**

| Entregable | Descripción |
| ----- | ----- |
| Código funcional del microservicio `auth-service/` | Proyecto Django con JWT, PostgreSQL y Redis |
| `Dockerfile` y `docker-compose.yml` actualizados | Contenedor funcionando en puerto 8000 |
| Captura Postman | Evidencia de login, refresh y verify exitosos |
| README actualizado | Descripción del servicio y endpoints |

---

## **🧠 Evaluación (0 – 20 pts)**

| Criterio | Peso |
| ----- | ----- |
| Estructura y configuración del servicio | 5 pts |
| Modelos y endpoints funcionales | 8 pts |
| JWT implementado correctamente | 5 pts |
| Documentación y commits limpios | 2 pts |

# **🧭 Evaluación teórica — Día 2: Microservicio Auth (Django \+ JWT \+ Redis)**

## **🎯 Objetivo**

Verificar que el practicante comprende **cómo se construye y protege un microservicio de autenticación**, cómo se gestiona la **persistencia y el cache**, y cómo se integran los conceptos de **seguridad, desacoplamiento y despliegue**.

---

| Nº | Pregunta | Valor |
| ----- | ----- | ----- |
| **1** | ¿Cuál es el propósito de crear un microservicio de autenticación separado en una arquitectura distribuida? | 2 pts |
| **2** | ¿Qué diferencia existe entre la autenticación basada en **sesiones** y la autenticación basada en **tokens JWT**? | 2 pts |
| **3** | Explica brevemente cómo se estructura un **token JWT** (qué contiene el *header*, *payload* y *signature*). | 2 pts |
| **4** | ¿Qué ventaja ofrece usar **Redis** dentro del microservicio Auth? Da un ejemplo práctico. | 2 pts |
| **5** | ¿Qué es el archivo **Dockerfile** y cuál es su función en el microservicio Auth? | 2 pts |
| **6** | ¿Por qué es recomendable definir las variables sensibles en un archivo **.env** y no directamente en el código fuente? | 2 pts |
| **7** | ¿Qué librería de Django se utiliza para implementar JWT y cómo se integra en `settings.py`? | 2 pts |
| **8** | ¿Qué comando de Django se usa para **crear migraciones** y cuál para **aplicarlas** dentro del contenedor Docker? | 2 pts |
| **9** | Explica el flujo completo de login con JWT: desde que el usuario envía sus credenciales hasta que accede a un recurso protegido. | 2 pts |
| **10** | Menciona dos buenas prácticas para asegurar un microservicio Auth en producción (por ejemplo: manejo de tokens, CORS, HTTPS, etc.). | 2 pts |

---

## **📊 Escala de evaluación**

| Puntaje | Nivel | Descripción |
| ----- | ----- | ----- |
| **18 – 20** | ⭐ Avanzado | Explica conceptos de seguridad y configuración con precisión. |
| **15 – 17** | ✅ Competente | Entiende el flujo JWT y maneja Redis/Docker correctamente. |
| **12 – 14** | ⚠️ Básico | Conoce la teoría pero no puede aplicarla sin guía. |
| **\< 12** | ❌ Insuficiente | No distingue JWT, Redis o configuración de entorno. |

# **🧭 DÍA 3 — Ejercicio 3: SALA 4 BACKEND (Hexagonal \+ Microservicios)**

# **El resto de los grupos el ejercicios está en la página 17**

## **Alcance (mismo dominio “Biblioteca Digital”)**

Microservicios:

* **Loans** (préstamos) — foco hexagonal

* **Books** (libros) — CRUD simple

* **Users** (usuarios) — verificación de estado

## **Estructura recomendada (Django)**

`loans_service/`  
  `src/`  
    `domain/`  
      `entities/loan.py`  
      `rules/validators.py`  
      `ports/{users_repo.py, books_repo.py, clock.py, uuid_gen.py}`  
      `services/loan_service.py`  
    `application/`  
      `use_cases/{create_loan_uc.py, return_loan_uc.py}`  
      `dtos/{loan_request_dto.py, loan_response_dto.py}`  
    `infrastructure/`  
      `repositories/{users_repo_http.py, books_repo_http.py, loans_repo_django.py}`  
      `services/{clock_system.py, uuid_native.py}`  
      `configs/container.py   # wiring sencillo (DI light)`  
    `interfaces/api/{serializers.py, views.py, urls.py}`  
  `tests/{unit/, integration/}`

## **Reglas (dominio Loans)**

* Máximo **3 préstamos activos** por usuario.

* Duración **≤ 15 días**.

* Usuario **activo** y **no suspendido**.

* Libro **disponible** (no eliminado, no “prestado”).

## **Contratos (para integrarse sin bloquearse)**

### **Users (puerto 9000\)**

* `GET /api/users/{id}` → `{ id, email, status: "active"|"suspended" }`

* `GET /api/users/{id}/loans/count?status=active` → `{ count: number }`

### **Books (puerto 9001\)**

* `GET /api/books/{id}` → `{ id, title, status: "available"|"loaned"|"deleted" }`

* `POST /api/books/{id}/mark-loaned` → `204`

* `POST /api/books/{id}/mark-returned` → `204`

### **Loans (puerto 9002\)**

* `POST /api/loans`  
   **request**: `{ user_id, book_id, start_date (ISO), days }`  
   **response**: `{ loan_id, due_date, status: "active" }`

* `POST /api/loans/{loan_id}/return` → `{ status: "returned" }`

* `GET /api/loans/{loan_id}` → `{ loan_id, user_id, book_id, start_date, due_date, status }`

**Nota:** Sala 4 puede usar **REST** (no Kafka). Añadir **timeouts \+ retries** (httpx/requests), y logging estructurado (json) en adaptadores HTTP.

## **DoD (Definition of Done)**

* Dominio sin dependencias de framework (reglas testeadas).

* Puertos \+ adaptadores con **timeouts (≤3s)**, **retry (máx. 2\)** y manejo de errores.

* **Tests**: ≥6 unit (dominio) \+ ≥3 integración (HTTP/ORM).

* **OpenAPI** mínimo para Loans.

* Docker Compose con `users`, `books`, `loans` (DB por servicio).

* README con arquitectura, cómo correr y ejemplos de cURL.

# **🧭 Evaluación teórica — Sala 4 (Hexagonal \+ MS Biblioteca Digital)**

| Nº | Pregunta | Valor |
| ----- | ----- | ----- |
| **1** | Explica con tus palabras qué es **Arquitectura Hexagonal** y cuál es su objetivo principal. | 2 pts |
| **2** | ¿Qué son los **puertos** y los **adaptadores** en Hexagonal? Da un ejemplo concreto del **UsersRepository** o **BooksRepository**. | 2 pts |
| **3** | ¿Por qué el **dominio** (reglas de negocio) debe estar **libre de dependencias** de framework (Django/DRF/ORM)? ¿Qué beneficio aporta? | 2 pts |
| **4** | Describe el **flujo para crear un préstamo** en Loans (use case `create_loan`): validaciones y llamadas a otros servicios. | 2 pts |
| **5** | Enumera las **reglas de negocio** obligatorias del dominio Loans (límite de 3 préstamos, ≤15 días, usuario activo, libro disponible) y explica **dónde** deben implementarse. | 2 pts |
| **6** | ¿Cómo implementarías **timeouts y retries** en los adaptadores HTTP hacia Users/Books y por qué son necesarios en microservicios? | 2 pts |
| **7** | ¿Qué diferencia hay entre un **test de unidad** del dominio y un **test de integración** (por ejemplo, contra el adaptador HTTP u ORM)? | 2 pts |
| **8** | ¿Qué debe incluir el **contrato OpenAPI** mínimo del servicio Loans y cómo ayuda al Frontend y a otros equipos? | 2 pts |
| **9** | Explica el principio de **base de datos por microservicio**. ¿Por qué no se comparten tablas entre Loans, Users y Books? | 2 pts |
| **10** | Propón dos **buenas prácticas de observabilidad** aplicables aquí (logs estructurados, healthchecks, métricas) y qué información registrarías. |  |

# **🧭 DÍA 3 — Backend (todas las salas excepto Sala 4\)**

## **Ejercicio: Blog Service** 

## **Stack:** Django \+ DRF \+ PostgreSQL \+ Redis \+ Docker  **Puerto:** `8001`  **Objetivo:** construir un microservicio **independiente** que exponga posts y categorías con **paginación, búsqueda y caché**, y que **esté listo** para, más adelante, consumir Auth por REST (JWT) **sin bloquearse hoy**.

---

## **1\) Alcance funcional (MVP)**

* **Modelos**

  * `Category(id, name, slug, is_active)`

  * `Author(id, display_name, email)` *(por hoy: seed local; mañana se enlaza a Auth)*

  * `Post(id, title, slug, body, author(FK), category(FK), status[published|draft], published_at, views)`

* **Endpoints (públicos hoy; privados mañana)**

  * `GET /api/categories` → lista categorías activas

  * `GET /api/posts?search=&page=` → lista con búsqueda (título/body) \+ paginación

  * `GET /api/posts/{id|slug}` → detalle

* **Caché (Redis)**

  * Cachear `GET /api/categories` y `GET /api/posts/{id|slug}` (TTL 60–120s)

* **Observabilidad**

  * `GET /healthz` (DB \+ Redis OK)

  * Logging estructurado (JSON) por request

**Opcional hoy (dejar esqueleto):** middleware que lea `Authorization: Bearer ...` y **no valide** todavía (solo loguea el header). Mañana se conecta al Auth real.

---

## **2\) Estructura del proyecto**

`blog-service/`

  `app/`

    `blog_service/            # proyecto Django`

    `core/                    # utilidades (cache helpers, pagination)`

    `categories/              # app`

    `authors/                 # app`

    `posts/                   # app`

  `Dockerfile`

  `requirements.txt`

  `manage.py`

  `openapi.yaml               # contrato mínimo`

### **`requirements.txt`**

`Django==5.0`

`djangorestframework==3.15`

`psycopg2-binary`

`django-redis`

`django-filter`

`python-slugify`

---

## **3\) Docker (servicio y compose)**

**Dockerfile**

`FROM python:3.11`

`WORKDIR /app`

`COPY requirements.txt .`

`RUN pip install -r requirements.txt`

`COPY . .`

`CMD ["gunicorn", "blog_service.wsgi:application", "--bind", "0.0.0.0:8001"]`

**docker-compose.yml** (extiende el que ya tienen)

`blog:`

  `build: ./blog-service`

  `container_name: blog_service`

  `environment:`

    `- DB_HOST=postgres`

    `- DB_NAME=main_db`

    `- DB_USER=devuser`

    `- DB_PASS=devpass`

    `- REDIS_HOST=redis`

    `- REDIS_PORT=6379`

    `- DEBUG=1`

  `depends_on:`

    `- postgres`

    `- redis`

  `ports:`

    `- "8001:8001"`

---

## **4\) DRF rápido (paginación, filtro, caché)**

* **Paginación:** DRF `PAGE_SIZE=10`

* **Búsqueda:** `django-filter` o `?search=` simple sobre `title`/`body`

* **Caché Redis:** `django-redis` \+ decorador `cache_page` en `categories` y `post detail`

Ejemplo `views.py (posts)`

`from django.views.decorators.cache import cache_page`

`from django.utils.decorators import method_decorator`

`from rest_framework import viewsets, mixins`

`from .models import Post`

`from .serializers import PostListSerializer, PostDetailSerializer`

`@method_decorator(cache_page(60), name="retrieve")   # detalle cacheado 60s`

`class PostViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):`

    `queryset = Post.objects.filter(status="published").select_related("author", "category")`

    `def get_serializer_class(self):`

        `return PostDetailSerializer if self.action == "retrieve" else PostListSerializer`

---

## **5\) Datos de ejemplo (seed)**

Crear `management/commands/seed_blog.py` para cargar:

* 5 categorías

* 3 autores

* 30 posts variados (algunos draft)

---

## **6\) Healthcheck y logging**

* `GET /healthz` verifica conexión a DB y ping a Redis.

* Logging JSON por request (método, path, status, tiempo).

---

## **7\) Contrato OpenAPI mínimo (front puede trabajar ya)**

* `GET /api/categories` → `[{id, name, slug}]`

* `GET /api/posts?search=&page=` → `results:[{id, title, slug, excerpt, author:{id,display_name}, category:{id,name}, published_at}]`

* `GET /api/posts/{id|slug}` → `{id, title, body, author:{...}, category:{...}, published_at, views}`

*(Guárdalo en `openapi.yaml` y compártelo con Front.)*

---

## **8\) Entregables del día**

* Servicio corriendo en `:8001` (Docker)

* Endpoints funcionando \+ paginación \+ búsqueda

* Cache Redis en `categories` y `post detail`

* `seed_blog` ejecutado y documentado

* `openapi.yaml` publicado

* README con cómo correr, seeds y ejemplos cURL

---

## **9\) Evaluación (0–20 pts)**

| Criterio | Pts |
| ----- | ----- |
| Modelos \+ migraciones limpias | 4 |
| Endpoints (lista, detalle, categorías) | 6 |
| Paginación \+ búsqueda | 3 |
| Caché Redis en endpoints clave | 3 |
| Healthcheck \+ logging básico | 2 |
| README \+ OpenAPI mínimo | 2 |

---

## **10\) Preguntas teóricas (10 × 2 \= 20 pts)**

1. ¿Por qué **blog** debe tener su **propia base de datos** en microservicios?

2. Diferencia entre **caché de página** y **caché de fragmento** (y cuándo usar cada una).

3. ¿Qué riesgo hay al **no invalidar** caché y cómo mitigarlo en este ejercicio?

4. ¿Qué aporta la **paginación** y qué métricas de rendimiento observarías?

5. ¿Por qué preferimos **búsqueda server-side** en listados grandes?

6. ¿Qué ventajas ofrece `select_related/prefetch_related`?

7. Explica el rol de un **healthcheck** en entornos orquestados.

8. ¿Qué campos de **logging** son útiles para depurar latencia?

9. ¿Cómo prepararías el servicio para exigir **JWT** más adelante sin romper al frontend?

10. ¿Qué estrategias usarías para evitar **N+1 queries** en endpoints de lista?

# **🧭 DÍA 4 — \- 28/10/ 2025 Backend: Email / Notifications Service**

📦 **Puerto sugerido:** `8002`  
 📚 **Nivel:** Intermedio (enfocado en integración y comunicación entre servicios)

---

## **🎯 Objetivo general**

Construir un **microservicio independiente de notificaciones (Email Service)** que:

* Reciba mensajes o formularios desde otros microservicios (p. ej. Blog o Auth).

* Envíe correos simulados (o reales si se tiene configuración SMTP).

* Ejemplifique **comunicación entre microservicios** por **HTTP** y **colas** (opcional).

* Refuerce conceptos de **idempotencia**, **reintentos** y **observabilidad**.

---

## **⚙️ Requisitos técnicos**

* **Stack:** Django \+ DRF \+ Redis \+ Docker \+ (opcional Celery)

* **Base de datos:** independiente (PostgreSQL o SQLite local)

* **Servicios relacionados:** Auth (8000) y Blog (8001) solo como emisores; Email recibe.

---

## **🧩 Requisitos funcionales**

### **1️⃣ Endpoint principal**

`POST /api/contact/`

`{`  
  `"name": "Carlos Rivas",`  
  `"email": "carlos@mail.com",`  
  `"message": "Me interesa una colaboración"`  
`}`

**Respuesta**

`{ "status": "queued" }`

* Valida campos requeridos.

* Persiste la solicitud en la BD (`ContactMessage`).

* Envía una notificación (simulada por consola o archivo log).

### **2️⃣ Endpoint interno (opcional)**

`POST /api/notify/`

`{`  
  `"to": "user@mail.com",`  
  `"subject": "Nuevo post publicado",`  
  `"body": "..."`  
`}`

→ Simula un evento recibido desde Blog u otro servicio.

---

## **🏗️ Estructura recomendada**

`email-service/`  
 `├── app/`  
 `│   ├── notifications/`  
 `│   │    ├── models.py      # ContactMessage, NotificationLog`  
 `│   │    ├── serializers.py`  
 `│   │    ├── views.py       # ContactViewSet, NotifyViewSet`  
 `│   │    └── tasks.py       # (si usan Celery)`  
 `│   └── utils/`  
 `│        ├── mailer.py      # función send_email()`  
 `│        └── logger.py`  
 `├── Dockerfile`  
 `├── requirements.txt`  
 `├── manage.py`  
 `├── openapi.yaml`

---

## **⚙️ Configuración mínima**

**Dependencias**

`Django==5.0`  
`djangorestframework==3.15`  
`django-cors-headers`  
`psycopg2-binary`  
`redis`  
`celery==5.4  # opcional`

**Correo simulado (settings.py)**

`EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"`

(O bien `filebased.EmailBackend` para guardar en carpeta `/sent_emails`.)

---

## **🔁 Opcional: Celery \+ Redis (worker asíncrono)**

* Definir cola `emails`.

* Encolar las tareas de envío en segundo plano.

* Configurar retry máx. 3, delay 5 s.

---

## **🔍 Observabilidad y resiliencia**

* Healthcheck `/healthz` (DB \+ Redis).

* Logs estructurados (JSON): entrada, salida, tiempo de procesamiento.

* Reintento con backoff si fallan llamadas HTTP entrantes.

* Idempotencia (basada en UUID del mensaje).

---

## **📦 Entregables**

| Entregable | Descripción |
| ----- | ----- |
| Microservicio Email funcional | `POST /api/contact` almacena y simula envío |
| Healthcheck \+ logging | `/healthz` y logs estructurados |
| OpenAPI documentado | Endpoints contact/notify |
| (Opcional) Celery \+ Redis | Reintentos asíncronos |
| README | Cómo correr \+ ejemplos cURL \+ docker-compose |

---

## **🧠 Evaluación (0–20 pts)**

| Criterio | Pts |
| ----- | ----- |
| Endpoints funcionales / validaciones | 5 |
| Persistencia de mensajes | 3 |
| Simulación de envío o worker Celery | 4 |
| Logs \+ healthcheck | 3 |
| Docker / README / OpenAPI | 3 |
| (Bonus) Retry / Idempotencia | 2 |

---

## **💬 Preguntas teóricas (10 × 2 \= 20 pts)**

1️⃣ ¿Qué ventaja aporta separar las notificaciones en un microservicio independiente?  
 2️⃣ Explica la diferencia entre **envío síncrono** y **asíncrono** de correos.  
 3️⃣ ¿Qué es una **cola de mensajes** y cuándo conviene usarla en este caso?  
 4️⃣ ¿Qué problemas resuelve Celery en arquitecturas distribuidas?  
 5️⃣ ¿Cómo podrías asegurar la **idempotencia** de un envío de correo?  
 6️⃣ ¿Por qué es útil tener un endpoint interno (`/notify`) para otros servicios?  
 7️⃣ ¿Qué debería verificar un **healthcheck** en este servicio?  
 8️⃣ ¿Qué campos incluirías en un **log estructurado** de notificación?  
 9️⃣ ¿Cómo manejarías un **error de SMTP** sin bloquear el servicio?  
 🔟 ¿Qué estrategias usarías para **probar asíncronamente** el envío de correos?

Para la **SALA 4 – BACKEND (Hexagonal \+ Microservicios)** el siguiente paso es **cerrar el flujo de “Préstamo end-to-end”** con arquitectura hexagonal en `Loans`, usando `Users` y `Books` mínimos (REST), sin Kafka.

# **Siguiente ejercicio — Sala 4 \- 28/10/ 2025 (Hexagonal)**

## **🎯 Objetivo**

Entregar el **MVP completo de Loans** con dominio puro (reglas), puertos/adaptadores, tests y **comunicación real** con `Users` y `Books` por HTTP. Todo dockerizado y documentado.

## **🪜 Tareas (orden sugerido)**

1. **Dominio (Loans) listo**

   * Reglas: `≤3` préstamos activos / usuario, duración `≤15` días, usuario activo, libro disponible.

   * Casos de uso: `create_loan` y `return_loan`.

   * Entidades/DTOs: `Loan`, `LoanRequestDTO`, `LoanResponseDTO`.

2. **Puertos y Adaptadores**

   * Puertos: `UsersRepository`, `BooksRepository`, `Clock`, `UUIDGen`, `LoansRepository`.

   * Adaptadores:

     * HTTP `users_repo_http` (GET `/api/users/{id}`, GET `/api/users/{id}/loans/count?status=active`).

     * HTTP `books_repo_http` (GET `/api/books/{id}`, POST `/mark-loaned`, `/mark-returned`).

     * ORM `loans_repo_django`.

3. **Resiliencia obligatoria**

   * **Timeout ≤3s** y **retry x2** en adaptadores HTTP (requests/httpx).

   * Manejo de errores (time-out, 4xx/5xx) → mapear a errores de dominio.

   * Logging estructurado (JSON) con latencia y outcome.

4. **Interfaces (DRF)**

   * `POST /api/loans` → `{loan_id, due_date, status:"active"}`

   * `POST /api/loans/{loan_id}/return` → `{status:"returned"}`

   * `GET /api/loans/{loan_id}` → detalle

5. **Servicios auxiliares mínimos**

   * **Users** y **Books** como servicios simples (o mocks HTTP con seed) que respeten los **contratos acordados**.

   * Cada servicio con su **DB propia**.

6. **OpenAPI \+ Compose**

   * `openapi.yaml` de **Loans** publicado.

   * `docker-compose` con `users`, `books`, `loans`, `postgres` (por servicio) y `redis` (si lo usan para cache/counter).

7. **Tests**

   * **Unidad (dominio):** ≥6 (reglas y casos de uso).

   * **Integración:** ≥3 (HTTP a Users/Books con timeouts/retry \+ ORM Loans).

## **📦 Entregables**

* Repos de `loans_service`, `users_service`, `books_service`.

* `openapi.yaml` de Loans.

* `docker-compose.yml` para levantar todo.

* README con: arquitectura, cómo correr, ejemplos `curl`, y tabla de errores (mapeo HTTP→dominio).

## **🧠 Evaluación (0–20)**

| Criterio | Pts |
| ----- | ----- |
| Dominio (reglas \+ casos de uso) aislado de framework | 5 |
| Puertos/adaptadores con timeout \+ retry \+ manejo de errores | 5 |
| Endpoints DRF funcionales | 4 |
| Tests (unidad \+ integración) | 4 |
| OpenAPI \+ Compose \+ README | 2 |

Nota: **No Kafka aún.** Si terminan antes, bonus: **idempotencia** en `create_loan` (evitar doble préstamo ante reintentos) y **métricas simples** (contadores por outcome).

# **Evaluación teórica – Sala 4: Arquitectura Hexagonal \+ Microservicios**

| Nº | Pregunta | Valor |
| ----- | ----- | ----- |
| **1** | ¿Cuál es la diferencia principal entre una arquitectura **en capas tradicional** y la **arquitectura hexagonal**? | 2 pts |
| **2** | ¿Qué son los **puertos** y los **adaptadores**, y cómo ayudan a mantener el código desacoplado del framework? | 2 pts |
| **3** | En el microservicio Loans, ¿por qué el dominio no debe importar Django ni DRF? ¿Qué ventaja ofrece esta independencia? | 2 pts |
| **4** | Describe paso a paso qué ocurre en el caso de uso **create\_loan**: desde que llega la solicitud hasta que se registra el préstamo. | 2 pts |
| **5** | ¿Qué reglas de negocio deben cumplirse antes de crear un préstamo? ¿Dónde se validan dentro de la arquitectura hexagonal? | 2 pts |
| **6** | Explica cómo se manejan los **errores de comunicación HTTP** entre Loans y Users/Books (timeouts, reintentos, mapeo de errores). | 2 pts |
| **7** | ¿Qué diferencia hay entre un **test de unidad** en el dominio y un **test de integración** de los adaptadores HTTP u ORM? | 2 pts |
| **8** | ¿Por qué cada microservicio (Loans, Users, Books) debe tener su **propia base de datos**? ¿Qué problemas evita esta separación? | 2 pts |
| **9** | ¿Qué información incluirías en los **logs estructurados** para mejorar la observabilidad y depuración del sistema? | 2 pts |
| **10** | ¿Qué beneficios obtiene el equipo al documentar los endpoints en **OpenAPI**, y cómo ayuda esto al frontend o a otros servicios? | 2 pts |

---

## **📊 Escala de calificación**

| Puntaje | Nivel | Descripción |
| ----- | ----- | ----- |
| **18–20** | ⭐ Avanzado | Comprende a fondo el patrón hexagonal y su aplicación en Loans. |
| **15–17** | ✅ Competente | Entiende la estructura y sabe ubicar reglas y adaptadores. |
| **12–14** | ⚠️ Básico | Identifica los elementos pero confunde responsabilidades. |
| **\< 12** | ❌ Insuficiente | No distingue dominio, infraestructura ni puertos. |

---

¿Deseas que te prepare también los **ítems prácticos (5 evaluables)** para esta Sala 4 —por ejemplo: validación de reglas, timeout \+ retry, tests, logs y OpenAPI— con rúbrica de 0 a 20?

