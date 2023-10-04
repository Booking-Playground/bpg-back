from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Разрешение на просмотр и редактирование только владельцу."""

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
