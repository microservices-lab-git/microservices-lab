Video  Fundamentos + Docker + Git
https://www.youtube.com/watch?v=wj766sxHZrM&t=20s
🎯 Objetivo: entender qué son los microservicios, instalar y configurar Docker y Git.
 🕐 Duración del bloque a visualizar:
 ➡️ Desde minuto 0:00 hasta minuto 26:00 del video.
________________________________________
📹 Detalle minuto a minuto
Minutos	Tema	Estado	Instrucción
0:00 – 5:00	Introducción general y objetivos del curso. Qué son los microservicios.	✅ Obligatorio	Escuchar completo. Conceptos base que usarán toda la semana.
5:00 – 10:00	Principios: autonomía, acoplamiento, escalabilidad, observabilidad.	✅ Obligatorio	Tomar notas — base teórica para arquitectura modular.
10:00 – 20:00	Instalación y configuración de Docker Desktop y Docker Compose (WSL2).	✅ Obligatorio	Repetir los pasos y dejar Docker funcionando localmente.
20:00 – 24:00	Configuración de Git y GitHub (ramas Main / Staging).	✅ Obligatorio	Crear repo propio del equipo.
24:00 – 26:00	Inicio de explicación de Kafka / Confluent Cloud.	⚠️ Opcional — saltar o ver solo como referencia.	No aplicable para esta semana (Kafka se ve en la demo final).

🧭 DÍA 1 — Fundamentos + Entorno Docker / Git
🎯 Objetivo general
Comprender qué es una arquitectura de microservicios y preparar el entorno de trabajo para los siguientes días.
 El grupo debe terminar el día con una base funcional en Docker Compose, donde cada servicio puede ser levantado de forma independiente.
________________________________________
🧩 Conceptos que deben dominar
●	Diferencia entre monolito y microservicios

●	Principios básicos: autonomía, responsabilidad única, acoplamiento flexible, escalabilidad y observabilidad

●	Estructura de proyecto “multi-servicio”

●	Uso de Docker + Docker Compose para levantar contenedores

●	Control de versiones en Git (ramas Main y Staging)

________________________________________
🛠️ Tareas prácticas paso a paso
1️⃣ Crear la estructura base del proyecto
mkdir microservices-lab
cd microservices-lab
mkdir auth-service blog-service email-service frontend reverse-proxy

Dentro de cada carpeta, crear un README.md vacío describiendo qué contendrá.
________________________________________
2️⃣ Inicializar Git y GitHub
git init
git branch -M main
git add .
git commit -m "Estructura inicial del laboratorio de microservicios"

Luego crear el repo remoto y vincularlo:
git remote add origin https://github.com/<tu-org>/microservices-lab.git
git push -u origin main

________________________________________
3️⃣ Preparar el entorno Docker Compose
Crea en la raíz un archivo docker-compose.yml:
version: "3.9"
services:
  postgres:
    image: postgres:15
    container_name: db_postgres
    restart: always
    environment:
      POSTGRES_USER: devuser
      POSTGRES_PASSWORD: devpass
      POSTGRES_DB: main_db
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  redis:
    image: redis:7
    container_name: cache_redis
    restart: always
    ports:
      - "6379:6379"

volumes:
  pgdata:

Ejecutar:
docker compose up -d
docker ps

✅ Si ves los contenedores db_postgres y cache_redis activos, el entorno base está listo.
________________________________________
4️⃣ Crear archivos de entorno
En la raíz:
.env.example
POSTGRES_USER=devuser
POSTGRES_PASSWORD=devpass
POSTGRES_DB=main_db
REDIS_HOST=redis
REDIS_PORT=6379

Cada equipo debe copiarlo a .env local.
________________________________________
5️⃣ Registrar en README el diseño inicial
En README.md (raíz):
# Laboratorio de Microservicios (Django + React)

## Arquitectura inicial
- auth-service/      → Autenticación y tokens JWT
- blog-service/      → Publicaciones, autores y categorías
- email-service/     → Notificaciones y formularios
- frontend/          → Interfaz React
- reverse-proxy/     → Balanceo / Gateway local

Servicios base:
- PostgreSQL (5432)
- Redis (6379)

________________________________________
🧪 Mini-reto de cierre del día
●	Levantar los contenedores (docker compose up -d).

●	Crear un archivo test_connection.py en auth-service/ que pruebe la conexión a PostgreSQL y Redis usando variables de entorno.

●	Ejecutarlo con docker exec -it dentro del contenedor.

________________________________________
📦 Entregables del Día 1
Entregable	Descripción
Repo Git	Subido a GitHub con estructura base y .env.example
Docker Compose funcional	Levanta PostgreSQL y Redis sin errores
README documentado	Incluye arquitectura y checklist
Captura o video corto	Mostrando los contenedores en ejecución (docker ps)
________________________________________
🧠 Evaluación
Criterio	Peso
Entorno Docker funcionando	40 %
Organización y limpieza del repo	25 %
README claro y completo	20 %
Comunicación y trabajo en equipo (Scrum Daily)	15 %
	
🧭 Evaluación — Día 1: Fundamentos + Entorno Docker / Git
🎯 Objetivo
Comprobar que cada practicante:
●	Entiende los principios y beneficios de los microservicios.

●	Maneja los comandos básicos de Git y Docker.

●	Puede explicar cómo se relaciona la teoría con la práctica configurada.

________________________________________
🧠 Preguntas teóricas (10 preguntas × 2 pts = 20 pts)
Nº	Pregunta	Ponderación
1	¿Qué diferencia principal existe entre una arquitectura monolítica y una de microservicios?	2 pts
2	Menciona dos ventajas y dos desventajas de usar microservicios.	2 pts
3	Explica con tus palabras qué significa el principio de responsabilidad única en un microservicio.	2 pts
4	¿Qué implica tener un acoplamiento flexible entre servicios y cómo se logra en Django REST?	2 pts
5	¿Qué función cumple Docker Compose dentro de una arquitectura de microservicios?	2 pts
6	¿Para qué sirve el archivo .env y por qué no debe subirse al repositorio?	2 pts
7	Indica los comandos para crear una nueva rama, hacer un commit y subirlo al remoto.	2 pts
8	¿Qué papel cumple Redis dentro del ecosistema de microservicios?	2 pts
9	¿Qué buenas prácticas del modelo 12 Factor App aplicaste hoy al crear tu entorno Dockerizado?	2 pts
10	Si un contenedor no arranca, ¿qué comando usarías para inspeccionar logs o errores y cómo lo resolverías?	2 pts
	
🧭 DÍA 2 — Ejercicio 2: Microservicio Auth (Django + DRF + JWT + PostgreSQL + Redis)
🎯 Objetivo general:
 Construir un microservicio de autenticación completamente independiente, que maneje usuarios, login y tokens JWT, corriendo en su propio contenedor Docker y conectado a PostgreSQL y Redis.
________________________________________
🧩 Conceptos clave
●	Autenticación basada en JWT (JSON Web Tokens)

●	Estructura de un servicio Django aislado

●	Configuración de variables de entorno y dependencias

●	Cacheo y sesiones con Redis

●	Comunicación segura entre servicios vía API

________________________________________
🕐 Video de referencia:
🎥 “Microservicios con Django REST Framework, Next.js y Apache Kafka”
 👉 https://www.youtube.com/watch?v=wj766sxHZrM
📍 Ver desde: minuto 26:13 hasta 2:54:00
(No ver ni implementar la parte de Kafka Producer — solo REST y Redis)
________________________________________
⚙️ Pasos del ejercicio
1️⃣ Crear el proyecto Django y app users
cd auth-service
django-admin startproject auth_service .
python manage.py startapp users

2️⃣ Configurar el Dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "auth_service.wsgi:application", "--bind", "0.0.0.0:8000"]

3️⃣ Extender docker-compose.yml
auth:
  build: ./auth-service
  container_name: auth_service
  restart: always
  environment:
    - DEBUG=1
    - DB_HOST=postgres
    - DB_NAME=main_db
    - DB_USER=devuser
    - DB_PASS=devpass
    - REDIS_HOST=redis
    - REDIS_PORT=6379
  depends_on:
    - postgres
    - redis
  ports:
    - "8000:8000"

________________________________________
4️⃣ Instalar dependencias (en requirements.txt)
django==5.0
djangorestframework==3.15
djangorestframework-simplejwt==5.3
psycopg2-binary
redis
django-cors-headers

________________________________________
5️⃣ Configurar settings.py
●	Añadir rest_framework, corsheaders, users

●	Configurar DATABASES con variables de entorno

●	Configurar CACHES (Redis)

●	Añadir middleware corsheaders.middleware.CorsMiddleware

●	Definir REST_FRAMEWORK con JWTAuthentication

________________________________________
6️⃣ Modelo de usuario personalizado
En users/models.py:
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email obligatorio")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

Registrar en settings.py:
AUTH_USER_MODEL = 'users.User'

________________________________________
7️⃣ Endpoints con JWT
En users/views.py o rutas de API:
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

Configura rutas:
path('api/token/', TokenObtainPairView.as_view()),
path('api/token/refresh/', TokenRefreshView.as_view()),

Crea también un endpoint /api/register/ que permita crear usuarios.
________________________________________
8️⃣ Probar con Postman
●	POST /api/register/ → crea usuario

●	POST /api/token/ → genera access/refresh token

●	POST /api/token/refresh/ → renueva token

Verificar conexión con base de datos y Redis:
docker exec -it auth_service python manage.py shell

________________________________________
🧪 Reto adicional (opcional)
Implementar endpoint /api/me/ que devuelva la información del usuario autenticado.
________________________________________
📦 Entregables del Día 2
Entregable	Descripción
Código funcional del microservicio auth-service/	Proyecto Django con JWT, PostgreSQL y Redis
Dockerfile y docker-compose.yml actualizados	Contenedor funcionando en puerto 8000
Captura Postman	Evidencia de login, refresh y verify exitosos
README actualizado	Descripción del servicio y endpoints
________________________________________
🧠 Evaluación (0 – 20 pts)
Criterio	Peso
Estructura y configuración del servicio	5 pts
Modelos y endpoints funcionales	8 pts
JWT implementado correctamente	5 pts
Documentación y commits limpios	2 pts
🧭 Evaluación teórica — Día 2: Microservicio Auth (Django + JWT + Redis)
🎯 Objetivo
Verificar que el practicante comprende cómo se construye y protege un microservicio de autenticación, cómo se gestiona la persistencia y el cache, y cómo se integran los conceptos de seguridad, desacoplamiento y despliegue.
________________________________________
Nº	Pregunta	Valor
1	¿Cuál es el propósito de crear un microservicio de autenticación separado en una arquitectura distribuida?	2 pts
2	¿Qué diferencia existe entre la autenticación basada en sesiones y la autenticación basada en tokens JWT?	2 pts
3	Explica brevemente cómo se estructura un token JWT (qué contiene el header, payload y signature).	2 pts
4	¿Qué ventaja ofrece usar Redis dentro del microservicio Auth? Da un ejemplo práctico.	2 pts
5	¿Qué es el archivo Dockerfile y cuál es su función en el microservicio Auth?	2 pts
6	¿Por qué es recomendable definir las variables sensibles en un archivo .env y no directamente en el código fuente?	2 pts
7	¿Qué librería de Django se utiliza para implementar JWT y cómo se integra en settings.py?	2 pts
8	¿Qué comando de Django se usa para crear migraciones y cuál para aplicarlas dentro del contenedor Docker?	2 pts
9	Explica el flujo completo de login con JWT: desde que el usuario envía sus credenciales hasta que accede a un recurso protegido.	2 pts
10	Menciona dos buenas prácticas para asegurar un microservicio Auth en producción (por ejemplo: manejo de tokens, CORS, HTTPS, etc.).	2 pts
________________________________________
📊 Escala de evaluación
Puntaje	Nivel	Descripción
18 – 20	⭐ Avanzado	Explica conceptos de seguridad y configuración con precisión.
15 – 17	✅ Competente	Entiende el flujo JWT y maneja Redis/Docker correctamente.
12 – 14	⚠️ Básico	Conoce la teoría pero no puede aplicarla sin guía.
< 12	❌ Insuficiente	No distingue JWT, Redis o configuración de entorno.

________________________________________
🟢 Estado de avance — Día 1 (Completado)
- Estructura base creada (carpetas y README por servicio).
- docker-compose.yml configurado con PostgreSQL y Redis.
- Archivo `.env.example` creado en la raíz.
- Contenedores levantados y verificados: `db_postgres`, `cache_redis`.

Comandos útiles:
```
docker compose up -d
docker ps
docker compose logs postgres --tail=100
docker compose logs redis --tail=100
```

________________________________________
✅ Implementación — Día 2 (Completado)
Arquitectura del servicio `auth-service/`:
- `requirements.txt`, `Dockerfile`, `manage.py`
- `auth_service/` (settings, urls, wsgi, asgi)
- `users/` (models, serializers, views, urls, admin, migrations)

Configuraciones clave (settings.py):
- `DATABASES` con variables de entorno (`DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASS`).
- `CACHES` Redis (`REDIS_HOST`, `REDIS_PORT`).
- `REST_FRAMEWORK` con `JWTAuthentication`.
- `AUTH_USER_MODEL = 'users.User'`.
- `CORS_ALLOW_ALL_ORIGINS = True` (solo dev).

Rutas expuestas (urls):
- `POST /api/register/` → registro (AllowAny)
- `GET /api/me/` → usuario autenticado (IsAuthenticated)
- `POST /api/token/` → JWT access/refresh
- `POST /api/token/refresh/` → renovar token

Modelo de usuario (`users/models.py`):
- `email` único, `is_active`, `is_admin`.
- `UserManager` con `create_user` y `create_superuser`.

Script de prueba de conexiones:
- `auth-service/test_connection.py` (PostgreSQL y Redis via env).

Ejecución y migraciones:
```
docker compose build
docker compose up -d
# Dentro del contenedor auth_service:
docker exec -it auth_service python manage.py makemigrations
docker exec -it auth_service python manage.py migrate
# (Opcional) Crear superusuario para /admin
docker exec -it auth_service python manage.py createsuperuser
```

Pruebas rápidas con Postman:
- Registrar: `POST /api/register/` body `{ "email": "dev@example.com", "password": "12345678" }`
- Login: `POST /api/token/` body `{ "email": "dev@example.com", "password": "12345678" }`
- Perfil: `GET /api/me/` con `Authorization: Bearer <access_token>`

Notas de calidad y seguridad:
- No subir `.env` (usar `.env.example`).
- Restringir CORS en producción; usar HTTPS.
- Revisar rotación/expiración de tokens según necesidad.

________________________________________
📋 Guía de finalización priorizada
Alta prioridad:
- Construir imágenes y levantar contenedores (`docker compose build && docker compose up -d`).
- Generar y aplicar migraciones en `auth-service`.
- Validar endpoints `/api/register`, `/api/token`, `/api/me`.

Media prioridad:
- Ajustar CORS y `ALLOWED_HOSTS` para entornos de staging/producción.
- Documentar endpoints en `auth-service/README.md`.

Baja prioridad:
- Crear datos seed o fixtures para pruebas.
- Configurar variables avanzadas de JWT (rotación, lifetimes).

