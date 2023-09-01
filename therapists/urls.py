from django.urls import path, include
from rest_framework import routers

from .api import TherapistViewSet


router = routers.DefaultRouter()
router.register(r"", TherapistViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
