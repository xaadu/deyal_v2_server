from django.db import models

from config.models import BaseModel


class Blog(BaseModel):
    title = models.CharField()
    des = models.TextField()

    therapist = models.ForeignKey(
        "therapists.therapist",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.title}"
