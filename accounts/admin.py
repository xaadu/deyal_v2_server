from django.contrib import admin

from .models import SiteUser


@admin.register(SiteUser)
class SiteUserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "full_name",
        "is_active",
        "created_at",
    )
    search_fields = (
        "email",
        "full_name",
    )
    list_filter = ("is_active",)
    ordering = ("is_active",)
