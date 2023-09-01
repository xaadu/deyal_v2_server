from django.db import models

from config.models import BaseModel


class Post(BaseModel):
    details = models.TextField()

    site_user = models.ForeignKey(
        "accounts.siteuser",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.details[:30]}"
