from rest_framework import viewsets

from .models import Service
from .serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.prefetch_related("symptom_set")
    serializer_class = ServiceSerializer
