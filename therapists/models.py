from django.db import models
from django.contrib.auth import get_user_model

from config.models import BaseModel


class Therapist(BaseModel):
    name = models.CharField()
    img = models.URLField()
    expyear = models.IntegerField()
    description = models.TextField()

    speciality = models.ForeignKey(
        "services.service",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.name}"


class AppointmentTime(BaseModel):
    APPOINTMENT_ONLINE = "online"
    APPOINTMENT_OFFLINE = "offline"
    APPOINTMENT_TYPE_CHOICES = (
        (APPOINTMENT_ONLINE, "Online Appointment"),
        (APPOINTMENT_OFFLINE, "Offline Appointment"),
    )

    appointment_type = models.CharField(choices=APPOINTMENT_TYPE_CHOICES)
    details = models.CharField()

    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.details[:30]}"


class AppointmentBooking(BaseModel):
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    )

    full_name = models.CharField()
    email = models.EmailField()
    current_age = models.PositiveSmallIntegerField()
    phone_no = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES)

    site_user = models.ForeignKey(
        "accounts.siteuser",
        on_delete=models.CASCADE,
    )
    appointment_time = models.ForeignKey(
        AppointmentTime,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )

    def __str__(self) -> str:
        return f"{self.email}"
