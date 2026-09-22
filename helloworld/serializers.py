from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost

        fields = [
            "id",
            "user",
            "title",
            "content",
            "created_at"
        ]

        read_only_fields = [
            "user",
            "created_at"
        ]