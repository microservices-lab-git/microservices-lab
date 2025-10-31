# Endpoints Día 3 - Blog Service (Postman)

Base URL: `http://localhost:8001`

Todos los endpoints devuelven JSON. Usa el header `Accept: application/json`.

## Health Check
- Método: `GET`
- URL: `/healthz` (sin barra final)
- Descripción: Estado de conectividad a base de datos y Redis.
- Esperado: `200 OK` con `{ "db": true, "redis": true }`.

## Categorías (Listado)
- Método: `GET`
- URL: `/api/categories/`
- Descripción: Lista categorías activas. Cache TTL ~90s.
- Parámetros: `page` (opcional)
- Esperado: `200 OK` con estructura paginada `{ count, next, previous, results: [...] }`.

## Posts (Listado publicado)
- Método: `GET`
- URL: `/api/posts/`
- Descripción: Lista posts con estado `published` ordenados por `published_at` descendente.
- Parámetros: `search` (opcional, busca en `title` y `body`), `page` (opcional)
- Esperado: `200 OK` con estructura paginada `{ count, next, previous, results: [...] }`.

## Post (Detalle por slug)
- Método: `GET`
- URL: `/api/posts/<slug>` (sin barra final)
- Ejemplo: `/api/posts/hola-mundo`
- Descripción: Devuelve detalle del post publicado. Cache TTL ~120s.
- Esperado: `200 OK` con campos `{ id, title, slug, body, status, published_at, views, author, category }`.

## Swagger UI
- Método: `GET`
- URL: `/api/docs/`
- Descripción: Documentación interactiva para probar y visualizar el API.
- Esperado: `200 OK` (HTML de Swagger UI).

## OpenAPI Schema
- Método: `GET`
- URL: `/api/schema/`
- Descripción: Esquema OpenAPI 3 en JSON, útil para importar en herramientas.
- Esperado: `200 OK` (JSON del esquema).

## Ejemplos de uso (PowerShell)
- `Invoke-RestMethod -Uri http://localhost:8001/healthz`
- `Invoke-RestMethod -Uri http://localhost:8001/api/categories/`
- `Invoke-RestMethod -Uri "http://localhost:8001/api/posts/?search=hola"`
- `Invoke-RestMethod -Uri http://localhost:8001/api/posts/hola-mundo`

## Notas
- Coincidir exactamente las rutas: `healthz` y el detalle de post sin barra final.
- La paginación de DRF retorna `count`, `next`, `previous` y `results`.
- Si cambias el puerto o host, ajusta la `Base URL` en Postman.