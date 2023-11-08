from django.urls import path, include
from rest_framework import routers

from .api import RestrictedBlogViewSet


router = routers.DefaultRouter()
router.register(r"", RestrictedBlogViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
