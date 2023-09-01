from rest_framework import viewsets

from config.utils import paginators
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = (
        Post.objects.filter(is_active=True).select_related("site_user").order_by("-id")
    )
    serializer_class = PostSerializer
    pagination_class = paginators.BasicPagination

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.query_params.get("q", "")
        qs = qs.filter(details__icontains=q)
        return qs
