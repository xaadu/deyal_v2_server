from django.db.models import Q
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Blog
from .serializers import BlogSerializer


class BlogPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = "page_size"
    max_page_size = 30


class BlogViewSet(viewsets.ModelViewSet):
    queryset = (
        Blog.objects.filter(is_active=True).select_related("therapist").order_by("id")
    )
    serializer_class = BlogSerializer
    pagination_class = BlogPagination

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.query_params.get("q", "")
        qs = qs.filter(Q(title__icontains=q) | Q(des__icontains=q))
        return qs
