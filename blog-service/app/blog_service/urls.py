"""
URL configuration for blog_service project.
"""
from django.contrib import admin
from django.urls import path, include

# En tu archivo local: blog-service/app/blog_service/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('categories.urls')),
    path('api/', include('posts.urls')),
    path('api/healthz/', include('core.urls')),  # Asegúrate de que esta línea esté presente
]