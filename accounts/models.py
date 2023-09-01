from django.db import models

from config.models import BaseModel


class SiteUser(BaseModel):
    email = models.CharField(primary_key=True)
    full_name = models.CharField()
    photo_url = models.URLField()

    def __str__(self) -> str:
        return self.full_name
