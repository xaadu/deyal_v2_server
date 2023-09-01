from django.db import models
from django.contrib.auth import get_user_model

from config.models import BaseModel


class Therapist(BaseModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField()
    img = models.URLField()
    expyear = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
