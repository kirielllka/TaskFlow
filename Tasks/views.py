from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action


from .models import Categories, Tasks
from .serializer import (
    CategoriesSerializer,
    TasksSerializer,
    UserSerializer,
)


class TasksViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


    @action(detail=True,url_path='complete', methods=['POST'])
    def complete_task(self, request, pk):
        task = self.get_object()
        task.status = True
        task.save()
        return Response(data=TasksSerializer(task).data,status=status.HTTP_200_OK)


    @action(detail=True, url_path='uncomplete', methods=['POST'])
    def uncomplete_task(self, request, pk):
        task = self.get_object()
        task.status = False
        task.save()
        return Response(data=TasksSerializer(task).data,status=status.HTTP_200_OK)



class CategoryViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


