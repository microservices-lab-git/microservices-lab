from rest_framework.generics import ListAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Category
from .serializers import CategorySerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.filter(is_active=True).order_by("name")
    serializer_class = CategorySerializer

    @method_decorator(cache_page(90))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)