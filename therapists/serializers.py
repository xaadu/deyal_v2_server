from rest_framework import serializers

from .models import Therapist


class ThreapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = [
            "name",
            "img",
            "expyear",
            "description",
            "user",
        ]
