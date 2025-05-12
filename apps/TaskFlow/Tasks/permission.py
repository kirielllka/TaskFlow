from rest_framework import permissions

from Tasks.models import Group


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if isinstance(obj, (Group)):
            return obj.user==requests.user
        return obj.author == request.user