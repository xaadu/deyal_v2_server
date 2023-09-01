from django.urls import path, include
from rest_framework import routers

from .api import ServiceViewSet


router = routers.DefaultRouter()
router.register(r"", ServiceViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
