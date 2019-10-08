from rest_framework.permissions import BasePermission

class IsBarber(BasePermission):
    message = "You must be the creator of this appointment."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.barber.user == request.user):
            return True
        else:
            return False
