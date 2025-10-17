# Auth Service
Este servicio gestiona la autenticación y autorización de usuarios dentro del sistema de
microservicios.
## Funcionalidades
- Registro de usuarios
- Inicio de sesión con JWT
- Encriptación de contraseñas
- Verificación de tokens
## Tecnologías
- Node.js / Express
- MongoDB o PostgreSQL
- JWT
- Docker
## Estructura
auth-service/
■■■ src/
■■■ Dockerfile
■■■ package.json
## Ejecución
docker compose up auth-service
## Endpoints
- POST /api/auth/register
- POST /api/auth/login
- GET /api/auth/verify
