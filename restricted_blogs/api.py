from rest_framework.permissions import IsAuthenticated

from blogs.api import BlogViewSet


class RestrictedBlogViewSet(BlogViewSet):
    permission_classes = (IsAuthenticated,)
