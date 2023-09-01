from django.urls import path, include
from rest_framework import routers

from .api import (
    TherapistViewSet,
    AppointmentTimeViewSet,
)


router = routers.DefaultRouter()

router.register(r"appointment-times", AppointmentTimeViewSet)
# router.register(r"appointment-times", AppointmentTimeViewSet)
router.register(r"", TherapistViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
