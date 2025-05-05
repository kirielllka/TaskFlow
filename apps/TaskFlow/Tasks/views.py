from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permission import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

from .models import Categories, Group, Tasks, UserProfile
from .paginations import (
    CategoryPagination,
    GroupPagination,
    TasksPagination,
    UserProfilePagination,
)
from .serializer import (
    CategoriesSerializer,
    GroupSerializer,
    TasksSerializer,
    UserProfileSerializer,
)

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


class BasePermissionViewSet(ModelViewSet):

    def get_permissions(self):
        if self.action in ('create',):
            permission_classes = (IsAuthenticated,)
        elif self.action in ('update', 'partial_update',):
            permission_classes = (IsAuthorOrReadOnly,)
        elif self.action in ('delete',):
            permission_classes = (IsAdminUser, IsAuthorOrReadOnly)
        else:
            permission_classes = (IsAuthenticatedOrReadOnly,)

        return [permission() for permission in permission_classes]


class TasksViewSet(BasePermissionViewSet):
    queryset = Tasks.objects.prefetch_related("category").select_related("author").all()
    serializer_class = TasksSerializer
    filter_backends = [OrderingFilter,SearchFilter]
    search_fields = ["title", "content", "time", "repeats_days", "category"]
    ordering_fields = ["time", "status", "category"]
    ordering = ["time"]
    pagination_class = TasksPagination

    @action(detail=False, url_path="user_me", methods=["GET"])
    def get_by_user(self, request):
        tasks = cache.get(f"tasks{request.user.id}")
        if not tasks:
            tasks = Tasks.objects.filter(author=request.user.id)
            cache.set(f"tasks{request.user.id}",tasks,DEFAULT_TIMEOUT)
        result = [TasksSerializer(task).data for task in tasks]
        return Response(data=result, status=status.HTTP_200_OK)

    @action(detail=True,url_path="complete", methods=["POST"])
    def complete_task(self, request, pk):
        task = self.get_object()
        task.status = True
        task.save()
        return Response(data=TasksSerializer(task).data,status=status.HTTP_200_OK)

    @action(detail=True, url_path="uncomplete", methods=["POST"])
    def uncomplete_task(self, request, pk):
        task = self.get_object()
        task.status = False
        task.save()
        return Response(data=TasksSerializer(task).data,status=status.HTTP_200_OK)


class CategoryViewSet(BasePermissionViewSet):
    queryset = Categories.objects.select_related("created_user").all()
    serializer_class = CategoriesSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ["category_name","created_user"]
    pagination_class = CategoryPagination


class UserProfileViewSet(BasePermissionViewSet):
    queryset = UserProfile.objects.select_related("user").all()
    serializer_class = UserProfileSerializer
    pagination_class = UserProfilePagination


class GroupViewSet(BasePermissionViewSet):
    queryset = Group.objects.select_related("creater").all()
    serializer_class = GroupSerializer
    pagination_class = GroupPagination

    @action(detail=True, url_path="join",methods=["POST"])
    def join(self, request, pk):
        profile = UserProfile.objects.get(id=request.user.id)
        profile.group_id = self.get_object()
        profile.save()
        return Response(status=status.HTTP_200_OK,data=UserProfileSerializer(profile).data)

    @action(detail=True, url_path="exit", methods=["POST"])
    def exit(self, request, pk):
        profile = UserProfile.objects.get(id=request.user.id)
        profile.group_id = None
        profile.save()
        return Response(status=status.HTTP_200_OK,data=UserProfileSerializer(profile).data)


