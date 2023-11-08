"""
URL configuration for deyal_v2_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


API_URLS = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("account/", include("accounts.urls")),
    path("services/", include("services.urls")),
    path("therapists/", include("therapists.urls")),
    path("blogs/", include("blogs.urls")),
    path("restricted-blogs/", include("restricted_blogs.urls")),
    path("posts/", include("posts.urls")),
    path(
        route="schema/",
        view=SpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        route="docs/",
        view=SpectacularSwaggerView.as_view(),
        name="docs",
    ),
    path(
        route="redoc/",
        view=SpectacularRedocView.as_view(),
        name="redoc",
    ),
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(API_URLS)),
]

# Admin Config
admin.site.site_header = "Dashboard | Deyal"
admin.site.site_title = "Dashboard | Deyal"
admin.site.index_title = "Home"
