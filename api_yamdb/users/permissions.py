from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Разрешает доступ к ресурсу, если пользователь аутентифицирован и является
    администратором или суперпользователем.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_admin or request.user.is_superuser
        )