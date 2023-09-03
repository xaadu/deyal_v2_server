from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "get_details",
        "site_user",
        "is_active",
    )
    search_fields = (
        "details",
        "site_user__email",
    )
    list_filter = (
        "is_active",
        "site_user",
    )
    ordering = (
        "is_active",
        "-id",
    )

    def get_details(self, instance):
        return instance.details[:30]
