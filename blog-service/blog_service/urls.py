from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from core.views import healthz

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/categories/", include("categories.urls")),
    path("api/posts/", include("posts.urls")),
    path("healthz", healthz),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]