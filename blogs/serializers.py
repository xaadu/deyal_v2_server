from rest_framework import serializers

from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "date",
            "des",
            "therapist",
        ]

    def get_date(self, instance) -> str:
        return instance.created_at.strftime("%B %d, %Y")

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["therapist"] = instance.therapist.name
        return rep
