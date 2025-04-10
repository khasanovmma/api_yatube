from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """
    Разрешает изменение и удаление объекта только его автору.
    Для остальных пользователей доступен только просмотр.
    """

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.owner == request.usergi
