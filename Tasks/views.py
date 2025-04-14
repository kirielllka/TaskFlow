from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Categories, Tasks
from .serializer import (
    CategoriesSerializer,
    TasksSerializer,
    UserSerializer,
)


class TasksViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


