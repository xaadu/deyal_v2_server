from django.contrib import admin

from .models import (
    Service,
    Symptom,
)

admin.site.register(Service)
admin.site.register(Symptom)
