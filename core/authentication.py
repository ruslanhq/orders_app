from django.conf import settings
from django.core.signing import constant_time_compare
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from core.settings.base import STORE_API_KEY, WAREHOUSE_API_KEY


class AuthToken(BaseAuthentication):
    API_KEYS = {
        "apps.store": STORE_API_KEY,
        "apps.warehouse": WAREHOUSE_API_KEY,
    }

    def authenticate(self, request):
        request_token = request.headers.get("X-API-Key")
        for app, token in self.API_KEYS.items():
            if app in settings.INSTALLED_APPS and constant_time_compare(
                request_token, token
            ):
                return
        raise AuthenticationFailed("Invalid token for any of the installed apps")
