from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Therapist
from .serializers import ThreapistSerializer


class TherapistViewSet(viewsets.ModelViewSet):
    queryset = Therapist.objects.all().select_related("speciality")
    serializer_class = ThreapistSerializer
