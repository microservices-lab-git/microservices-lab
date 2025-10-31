# Laboratorio de Microservicios (Django + React)

## Arquitectura inicial

- auth-service/      → Autenticación y tokens JWT
- blog-service/      → Publicaciones, autores y categorías
- email-service/     → Notificaciones y formularios
- frontend/          → Interfaz React
- reverse-proxy/     → Balanceo / Gateway local

### Servicios base:
- PostgreSQL (5432)
- Redis (6379)
## Checklist Día 1
- Estructura de carpetas creada (auth-service, blog-service, email-service, frontend, reverse-proxy)
- docker-compose.yml con PostgreSQL y Redis configurados
- Archivo `.env.example` creado en la raíz (copiar a `.env`)
- Contenedores ejecutándose con `docker compose up -d` y verificados con `docker ps`

## Cómo levantar el entorno base
- `docker compose up -d`
- `docker ps` debe mostrar `db_postgres` y `cache_redis` activos
- Para revisar logs: `docker compose logs postgres --tail=100` y `docker compose logs redis --tail=100`

## Notas
- No subir `.env` al repositorio. Usar `.env.example` como referencia.
- En caso de errores de arranque, inspeccionar logs y validar puertos libres.
## Guía Día 3 (Blog Service)

La guía detallada para la implementación del servicio de Blog está disponible en `docs/Guia_Dia3.md`. Incluye preparación de entorno, estructura del proyecto, Docker, configuración (Django/DRF/PostgreSQL/Redis), endpoints públicos con cache, health checks, Swagger/OpenAPI y pasos de validación.