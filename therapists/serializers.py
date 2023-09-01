from rest_framework import serializers

from .models import (
    Therapist,
    AppointmentTime,
    AppointmentBooking,
)


class ThreapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = [
            "id",
            "name",
            "speciality",
            "img",
            "expyear",
            "description",
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["speciality"] = instance.speciality.title
        return rep


class AppointmentTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentTime
        fields = [
            "id",
            "appointment_type",
            "details",
            "therapist",
        ]


class AppointmentBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentBooking
        fields = [
            "id",
            "full_name",
            "email",
            "current_age",
            "phone_no",
            "gender",
            "site_user",
            "appointment_time",
        ]
