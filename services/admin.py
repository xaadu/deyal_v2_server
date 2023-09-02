from django.contrib import admin

from .models import (
    Service,
    Symptom,
)


class SymptomInlineAdmin(admin.TabularInline):
    model = Symptom
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "title",
        "is_active",
    )
    search_fields = (
        "title",
        "description",
        "what",
        "cure",
    )
    inlines = (SymptomInlineAdmin,)
    list_filter = ("is_active",)
    ordering = (
        "is_active",
        "id",
    )


@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "service",
        "get_details",
        "is_active",
    )
    search_fields = (
        "details",
        "service__title",
    )
    list_filter = (
        "is_active",
        "service",
    )
    ordering = (
        "is_active",
        "id",
    )

    @admin.display(description="Details", ordering="details")
    def get_details(self, obj):
        return f"{obj.details[:30]}"
