from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "published_at")
    search_fields = ("title", "slug", "body")
    list_filter = ("status",)