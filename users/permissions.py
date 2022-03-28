from . import models, serializers
from rest_framework import viewsets, status, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_teacher is True:
            return True
        else:
            return False


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser is True:
            return True
        else:
            return False