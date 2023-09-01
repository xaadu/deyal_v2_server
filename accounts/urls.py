from django.urls import path, include
from rest_framework import routers

from .api import SiteUserViewSet


router = routers.DefaultRouter()
router.register(r"users", SiteUserViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
