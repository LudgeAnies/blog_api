from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission): # Для иного запроса разрешено только чтение.
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Запись разрешена только автору поста
        return obj.author == request.user