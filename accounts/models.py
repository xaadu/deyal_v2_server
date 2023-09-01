from django.db import models

from config.models import BaseModel


class SiteUser(BaseModel):
    email = models.CharField(unique=True)
    full_name = models.CharField()
    photo_url = models.URLField()
