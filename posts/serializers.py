from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "details",
            "site_user",
            "created_at",
        ]
        extra_kwargs = {
            "site_user": {"write_only": True},
        }
