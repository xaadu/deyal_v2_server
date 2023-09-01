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
        return self.name
