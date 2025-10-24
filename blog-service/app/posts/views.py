from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.db.models import Q, F
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer


class PostViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    ViewSet para posts con búsqueda, paginación y caché
    """
    queryset = Post.objects.filter(status='published').select_related('author', 'category')
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'body']
    ordering_fields = ['published_at', 'views', 'title']
    ordering = ['-published_at']
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        return PostListSerializer
    
    @method_decorator(cache_page(60))  # Cache detalle por 1 minuto
    def retrieve(self, request, *args, **kwargs):
        # Incrementar views al obtener detalle
        instance = self.get_object()
        Post.objects.filter(pk=instance.pk).update(views=F('views') + 1)
        return super().retrieve(request, *args, **kwargs)