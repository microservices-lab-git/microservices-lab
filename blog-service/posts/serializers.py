from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "body",
            "status",
            "published_at",
            "views",
            "author",
            "category",
        ]