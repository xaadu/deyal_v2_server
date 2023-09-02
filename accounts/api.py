from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import SiteUser
from .serializers import SiteUserSerializer


class SiteUserViewSet(viewsets.ModelViewSet):
    queryset = SiteUser.objects.filter(is_active=True)
    serializer_class = SiteUserSerializer
    lookup_value_regex = "(?P<data>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})"
