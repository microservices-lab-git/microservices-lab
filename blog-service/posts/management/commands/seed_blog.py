from django.core.management.base import BaseCommand
from categories.models import Category
from authors.models import Author
from posts.models import Post


class Command(BaseCommand):
    help = "Crea datos de ejemplo para el Blog Service"

    def handle(self, *args, **options):
        cat, _ = Category.objects.get_or_create(name="General", slug="general", is_active=True)
        auth, _ = Author.objects.get_or_create(display_name="Equipo", email="equipo@example.com")
        Post.objects.get_or_create(
            title="Hola Mundo",
            slug="hola-mundo",
            body="Contenido de ejemplo...",
            author=auth,
            category=cat,
            status=Post.STATUS_PUBLISHED,
        )
        self.stdout.write(self.style.SUCCESS("Seed del blog completado"))