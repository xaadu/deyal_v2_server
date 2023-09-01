from django.contrib import admin

from .models import (
    Therapist,
    AppointmentTime,
    AppointmentBooking,
)

admin.site.register(Therapist)
admin.site.register(AppointmentTime)
admin.site.register(AppointmentBooking)
