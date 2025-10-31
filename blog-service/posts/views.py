from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Post
from .serializers import PostSerializer


class PostListView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = Post.objects.filter(status=Post.STATUS_PUBLISHED).order_by("-published_at")
        search = self.request.query_params.get("search")
        if search:
            qs = qs.filter(Q(title__icontains=search) | Q(body__icontains=search))
        return qs


class PostDetailView(RetrieveAPIView):
    serializer_class = PostSerializer
    lookup_field = "slug"
    queryset = Post.objects.filter(status=Post.STATUS_PUBLISHED)

    @method_decorator(cache_page(120))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)