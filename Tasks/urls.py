from config.yasg import urlpatterns as doc_url
from django.urls import include, path
from rest_framework import routers

from .views import CategoryViewSet, TasksViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TasksViewSet, basename='tasks')
router.register(r'category', CategoryViewSet, basename='categories')
urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns+= doc_url