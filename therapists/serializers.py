from rest_framework import serializers

from .models import Therapist


class ThreapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = [
            "id",
            "name",
            "img",
            "expyear",
            "description",
            "user",
        ]
