from artists.models import Artist
from rest_framework import permissions

class IsArtistPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return Artist.objects.filter(user_id = request.user.id).exists()