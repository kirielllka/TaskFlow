from django.urls import include, path
from rest_framework import routers

from config.yasg import urlpatterns as doc_url

from .views import CategoryViewSet, TasksViewSet, UserProfileViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r"tasks", TasksViewSet, basename="tasks")
router.register(r"category", CategoryViewSet, basename="categories")
router.register(r"profile", UserProfileViewSet, basename="profiles")
router.register(r"groups", GroupViewSet, basename="groups")
urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns+= doc_url
