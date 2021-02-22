from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print('OBJ', obj)
        print('R', request)
        return obj.id == request.user.id