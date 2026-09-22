from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import BlogPost
from .serializers import BlogPostSerializer
from .permissions import IsOwner
from .filters import BlogPostFilter
from .pagination import BlogPagination


class BlogPostViewSet(viewsets.ModelViewSet):

    serializer_class = BlogPostSerializer

    permission_classes = [IsAuthenticated, IsOwner]

    pagination_class = BlogPagination

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_class = BlogPostFilter

    search_fields = [
        "title",
        "content"
    ]

    ordering_fields = [
        "id"
    ]

    def get_queryset(self):
        return BlogPost.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)