from rest_framework.permissions import BasePermission


class AuthenticatedCanGet(BasePermission):
    """
    Only logged in users (which should only be staff) can GET the view, everyone can PUT, POST, or
    DELETE. Useful when you want to allow anonymous people to submit a form, but not see all of the
    other forms that have been submitted.
    """

    SAFE_METHODS = ['POST', 'PUT', 'PATCH' 'DELETE', 'HEAD', 'OPTIONS']

    def has_permission(self, request, view):
        return request.method in self.SAFE_METHODS or request.user.is_authenticated
