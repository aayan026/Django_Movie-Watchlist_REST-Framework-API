from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    İstifadəçi yalnız öz filmlərinə giriş əldə edə bilər:
    başqasının filmini görmək, redaktə etmək və ya silmək qadağandır.
    """

    message = "Siz yalnız öz filmlərinizlə işləyə bilərsiniz"

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
