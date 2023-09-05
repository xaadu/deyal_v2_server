from rest_framework import serializers

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    sym = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = [
            "id",
            "title",
            "duration",
            "img",
            "description",
            "what",
            "sym",
            "cure",
        ]

    def get_sym(self, obj) -> list[str]:
        return [symptom.details for symptom in obj.symptom_set.all()]
