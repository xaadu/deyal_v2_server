from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Therapist
from .serializers import ThreapistSerializer


class TherapistViewSet(viewsets.ModelViewSet):
    queryset = Therapist.objects.all().select_related("speciality")
    serializer_class = ThreapistSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        speciality = self.request.query_params.get("speciality_id")
        if speciality:
            qs = qs.filter(speciality_id=speciality)
        return qs
