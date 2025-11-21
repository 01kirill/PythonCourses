from rest_framework.permissions import BasePermission

class IsInGroup(BasePermission):
    group_name = None

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return request.user.groups.filter(name=self.group_name).exists()
        return False

class IsManager(IsInGroup):
    group_name = 'manager'
