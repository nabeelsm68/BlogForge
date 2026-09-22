import django_filters
from .models import BlogPost


class BlogPostFilter(django_filters.FilterSet):

    class Meta:

        model = BlogPost

        fields = [
            "created_at"
        ]