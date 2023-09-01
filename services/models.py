from django.db import models
from django.contrib.auth import get_user_model

from config.models import BaseModel


class Service(BaseModel):
    title = models.CharField()
    duration = models.FloatField()
    img = models.URLField()
    description = models.TextField()
    what = models.TextField()
    cure = models.TextField()

    def __str__(self) -> str:
        return self.title


class Symptom(BaseModel):
    details = models.TextField()

    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.details[:30]}"
