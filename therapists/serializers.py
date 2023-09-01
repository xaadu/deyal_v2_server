from rest_framework import serializers

from .models import Therapist


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
