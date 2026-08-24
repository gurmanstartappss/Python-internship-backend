from rest_framework.permissions import BasePermission,SAFE_METHODS


#authenticated users can read,only staff/admin user can modify"
class IsAdminOrReadOnly(BasePermission):
  def has_permission(self, request, view):
     if request.method in SAFE_METHODS:
        return request.user.is_authenticated
     return (request.user.is_authenticated and request.user.is_staff)