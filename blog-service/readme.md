# Blog Service
Servicio encargado de la gestión de publicaciones y contenido.
## Funcionalidades
- CRUD de publicaciones
- Asociación con usuarios autenticados
- Comentarios y likes (opcional)
## Tecnologías
- Node.js / Express
- MongoDB / Mongoose
- Docker
## Estructura
blog-service/
■■■ src/
■■■ Dockerfile
■■■ package.json
## Ejecución
docker compose up blog-service
## Endpoints
- GET /api/posts
- POST /api/posts
- PUT /api/posts/:id
- DELETE /api/posts/:id