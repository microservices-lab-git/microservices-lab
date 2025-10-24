from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
import random
from authors.models import Author
from categories.models import Category
from posts.models import Post


class Command(BaseCommand):
    help = 'Seed the database with sample blog data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting blog data seeding...'))
        
        # Crear categorías
        categories_data = [
            {'name': 'Tecnología', 'is_active': True},
            {'name': 'Programación', 'is_active': True},
            {'name': 'Inteligencia Artificial', 'is_active': True},
            {'name': 'Desarrollo Web', 'is_active': True},
            {'name': 'DevOps', 'is_active': True},
        ]
        
        categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults=cat_data
            )
            categories.append(category)
            if created:
                self.stdout.write(f'Created category: {category.name}')
        
        # Crear autores
        authors_data = [
            {'display_name': 'Ana García', 'email': 'ana.garcia@blog.com'},
            {'display_name': 'Carlos Rodríguez', 'email': 'carlos.rodriguez@blog.com'},
            {'display_name': 'María López', 'email': 'maria.lopez@blog.com'},
        ]
        
        authors = []
        for author_data in authors_data:
            author, created = Author.objects.get_or_create(
                email=author_data['email'],
                defaults=author_data
            )
            authors.append(author)
            if created:
                self.stdout.write(f'Created author: {author.display_name}')
        
        # Crear posts
        posts_data = [
            {
                'title': 'Introducción a los Microservicios',
                'body': 'Los microservicios son una arquitectura de software que estructura una aplicación como una colección de servicios débilmente acoplados. Esta arquitectura permite que los equipos desarrollen, desplieguen y escalen servicios de forma independiente...',
                'status': 'published'
            },
            {
                'title': 'Django REST Framework: Guía Completa',
                'body': 'Django REST Framework (DRF) es un toolkit poderoso y flexible para construir APIs web. Proporciona serialización, autenticación, permisos y muchas otras características útiles para el desarrollo de APIs REST...',
                'status': 'published'
            },
            {
                'title': 'Docker para Desarrolladores',
                'body': 'Docker ha revolucionado la forma en que desarrollamos y desplegamos aplicaciones. Con Docker, podemos empaquetar nuestras aplicaciones junto con todas sus dependencias en contenedores ligeros y portables...',
                'status': 'published'
            },
            {
                'title': 'JWT: Autenticación Moderna',
                'body': 'JSON Web Tokens (JWT) es un estándar abierto que define una forma compacta y autónoma de transmitir información de forma segura entre partes como un objeto JSON...',
                'status': 'published'
            },
            {
                'title': 'Redis como Sistema de Caché',
                'body': 'Redis es una estructura de datos en memoria que se utiliza como base de datos, caché y broker de mensajes. Su velocidad y flexibilidad lo convierten en una excelente opción para sistemas de alto rendimiento...',
                'status': 'published'
            },
            {
                'title': 'Patrones de Diseño en Python',
                'body': 'Los patrones de diseño son soluciones reutilizables a problemas comunes en el diseño de software. En Python, podemos implementar estos patrones de manera elegante y pythónica...',
                'status': 'draft'
            },
            {
                'title': 'Testing en Django',
                'body': 'Las pruebas son fundamentales para mantener la calidad del código. Django proporciona un framework robusto para escribir y ejecutar pruebas unitarias e de integración...',
                'status': 'published'
            },
            {
                'title': 'Optimización de Consultas en Django ORM',
                'body': 'El ORM de Django es poderoso, pero puede generar consultas ineficientes si no se usa correctamente. Aprende técnicas para optimizar tus consultas y mejorar el rendimiento...',
                'status': 'published'
            },
            {
                'title': 'Deployment con Docker Compose',
                'body': 'Docker Compose permite definir y ejecutar aplicaciones multi-contenedor. Es perfecto para entornos de desarrollo y despliegues simples de microservicios...',
                'status': 'published'
            },
            {
                'title': 'Monitoreo de Aplicaciones',
                'body': 'El monitoreo es crucial para mantener aplicaciones saludables en producción. Explora herramientas y técnicas para monitorear tus microservicios...',
                'status': 'draft'
            }
        ]
        
        # Extender la lista con más posts variados
        additional_posts = []
        for i in range(20):
            additional_posts.append({
                'title': f'Post de Ejemplo {i+11}',
                'body': f'Este es el contenido del post número {i+11}. Contiene información relevante sobre desarrollo de software, mejores prácticas y tecnologías modernas. El contenido es lo suficientemente largo para probar la funcionalidad de extractos y búsqueda en el sistema.',
                'status': random.choice(['published', 'draft'])
            })
        
        posts_data.extend(additional_posts)
        
        # Crear posts
        for i, post_data in enumerate(posts_data):
            if not Post.objects.filter(title=post_data['title']).exists():
                published_at = None
                if post_data['status'] == 'published':
                    # Fechas aleatorias en los últimos 30 días
                    days_ago = random.randint(1, 30)
                    published_at = timezone.now() - timedelta(days=days_ago)
                
                post = Post.objects.create(
                    title=post_data['title'],
                    body=post_data['body'],
                    author=random.choice(authors),
                    category=random.choice(categories),
                    status=post_data['status'],
                    published_at=published_at,
                    views=random.randint(0, 1000)
                )
                self.stdout.write(f'Created post: {post.title}')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully seeded database with:\n'
                f'- {len(categories)} categories\n'
                f'- {len(authors)} authors\n'
                f'- {len(posts_data)} posts'
            )
        )