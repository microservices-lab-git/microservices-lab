# Reverse Proxy
Servicio encargado del enrutamiento y balanceo de peticiones entre microservicios.
## Funcionalidades
- Redirección de rutas
- Balanceo de carga
- Configuración de CORS
## Tecnologías
- Nginx
- Docker
## Estructura
reverse-proxy/
■■■ nginx.conf
■■■ Dockerfile
## Ejecución
docker compose up reverse-proxy
## Rutas configuradas
- /api/auth → auth-service
- /api/blog → blog-service
- /api/email → email-service
- / → frontend