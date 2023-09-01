from rest_framework import viewsets

from .models import (
    Therapist,
    AppointmentTime,
    AppointmentBooking,
)
from .serializers import (
    ThreapistSerializer,
    AppointmentTimeSerializer,
    AppointmentBookingSerializer,
)


class TherapistViewSet(viewsets.ModelViewSet):
    queryset = Therapist.objects.all().select_related("speciality")
    serializer_class = ThreapistSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        speciality = self.request.query_params.get("speciality_id")
        if speciality:
            qs = qs.filter(speciality_id=speciality)
        return qs


class AppointmentTimeViewSet(viewsets.ModelViewSet):
    queryset = AppointmentTime.objects.all()
    serializer_class = AppointmentTimeSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        therapist_id = self.request.query_params.get("therapist_id")
        appointment_type = self.request.query_params.get("appointment_type")

        if not therapist_id or not appointment_type:
            return AppointmentTime.objects.none()

        qs = qs.filter(therapist_id=therapist_id, appointment_type=appointment_type)

        return qs


class AppointmentBookingViewSet(viewsets.ModelViewSet):
    queryset = AppointmentBooking.objects.none()
    serializer_class = AppointmentBookingSerializer
