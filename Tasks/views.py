from django.shortcuts import render

from .models import Tasks, Categories
from .serializer import UserSerializer,CategoriesSerializer,TasksSerializer

from rest_framework.viewsets import ModelViewSet


class TasksViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


