from typing import Any, List, Optional, Tuple, Union
from django.contrib import admin
from django.http.request import HttpRequest

from .models import (
    Therapist,
    AppointmentTime,
    AppointmentBooking,
)


class AppointmentTimeInline(admin.TabularInline):
    model = AppointmentTime
    extra = 1


@admin.register(Therapist)
class TherapistAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "speciality",
        "expyear",
        "is_active",
    )
    search_fields = (
        "name",
        "user__username",
        "user__email",
    )
    list_filter = (
        "is_active",
        "speciality",
    )
    ordering = (
        "is_active",
        "name",
    )
    readonly_fields = (
        "user",
        "speciality",
        "expyear",
        "is_active",
    )
    inlines = (AppointmentTimeInline,)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(id=request.user.therapist.id)
        return qs

    def get_readonly_fields(self, request, obj):
        ro_fields = super().get_readonly_fields(request, obj)
        if request.user.is_superuser:
            return tuple()
        return ro_fields


@admin.register(AppointmentTime)
class AppointmentTimeAdmin(admin.ModelAdmin):
    list_display = (
        "details",
        "appointment_type",
        "therapist",
        "is_active",
    )
    search_fields = ("details",)
    list_filter = (
        "is_active",
        "therapist",
    )
    ordering = (
        "is_active",
        "-id",
    )
    # readonly_fields = ("is_active",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(therapist_id=request.user.therapist.id)
        return qs

    def get_readonly_fields(self, request, obj):
        ro_fields = super().get_readonly_fields(request, obj)
        if request.user.is_superuser:
            return tuple()
        return ro_fields


@admin.register(AppointmentBooking)
class AppointmentBookingAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "full_name",
        "appointment_time",
        "email",
        "gender",
        "is_active",
    )
    search_fields = (
        "full_name",
        "appointment_time__details",
        "email",
    )
    list_filter = (
        "is_active",
        "gender",
    )
    ordering = (
        "is_active",
        "-id",
    )
    # readonly_fields = ("is_active",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(appointment_time__therapist_id=request.user.therapist.id)
        return qs

    def get_readonly_fields(self, request, obj):
        ro_fields = super().get_readonly_fields(request, obj)
        if request.user.is_superuser:
            return tuple()
        return ro_fields
