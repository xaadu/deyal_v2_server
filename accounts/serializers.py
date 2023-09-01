from rest_framework import serializers

from .models import SiteUser


class SiteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteUser
        fields = [
            "email",
            "full_name",
            "photo_url",
        ]
