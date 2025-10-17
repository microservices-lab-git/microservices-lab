# Email Service
Servicio responsable del envío de correos automáticos.
## Funcionalidades
- Envío de correos de confirmación o recuperación
- Notificaciones automáticas
- Plantillas HTML de correo
## Tecnologías
- Node.js / Express
- Nodemailer
- Docker
## Estructura
email-service/
■■■ src/
■■■ Dockerfile
■■■ package.json
## Ejecución
docker compose up email-service
## Endpoints
- POST /api/email/send
