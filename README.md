# Laboratorio de Microservicios (Django + React)

## Arquitectura inicial

- **auth-service/**      → Autenticación y tokens JWT
- **blog-service/**      → Publicaciones, autores y categorías  
- **email-service/**     → Notificaciones y formularios
- **frontend/**          → Interfaz React
- **reverse-proxy/**     → Balanceo / Gateway local

## Servicios base

- PostgreSQL (5432)
- Redis (6379)

## Configuración inicial

1. Copiar variables de entorno:
   ```bash
   cp .env.example .env
   ```

2. Levantar servicios base:
   ```bash
   docker compose up -d
   ```

3. Verificar contenedores:
   ```bash
   docker ps
   ```

## Checklist Día 1

- [x] Estructura de proyecto creada
- [x] Git inicializado
- [x] Docker Compose configurado
- [x] Variables de entorno preparadas
- [x] README documentado
- [ ] Conexión a BD probada
- [ ] Repo subido a GitHub