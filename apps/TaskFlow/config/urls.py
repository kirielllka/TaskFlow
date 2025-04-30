
from django.contrib import admin
from django.urls import include, path, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("Tasks.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/auth/", include("djoser.urls")),
    re_path("api/auth/", include("djoser.urls.authtoken")),
    path("__debug__/", include("debug_toolbar.urls")),
]
