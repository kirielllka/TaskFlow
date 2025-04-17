from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from django.views.generic import ListView


from .models import Categories, Tasks, UserProfile
from .serializer import (
    CategoriesSerializer,
    TasksSerializer,
    UserSerializer,
    UserProfileSerializer,
)

from .paginations import TasksPaginations,CategoryPaginations


class TasksViewSet(ModelViewSet):
    queryset = Tasks.objects.prefetch_related('category').select_related('author').all()
    serializer_class = TasksSerializer
    filter_backends = [OrderingFilter,SearchFilter]
    search_fields = ['title', 'content', 'time', 'repeats_days', 'category']
    ordering_fields = ['time', 'status', 'category']
    ordering = ['time']
    pagination_class = TasksPaginations

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
    queryset = Categories.objects.select_related('created_user').all()
    serializer_class = CategoriesSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['category_name','created_user']
    pagination_class = CategoryPaginations

class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer



