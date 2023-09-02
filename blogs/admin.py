from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "title",
        "therapist",
        "is_active",
    )
    search_fields = (
        "title",
        "des",
        "therapist__name",
    )
    list_filter = (
        "is_active",
        "therapist",
    )
    ordering = ("is_active",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(therapist_id=request.user.therapist.id)
        return qs
