from django.urls import path, include
from rest_framework import routers

from .api import BlogViewSet


router = routers.DefaultRouter()
router.register(r"", BlogViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
