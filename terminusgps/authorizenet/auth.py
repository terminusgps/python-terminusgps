from authorizenet.apicontractsv1 import merchantAuthenticationType
from authorizenet.constants import constants

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

if not hasattr(settings, "DEBUG"):
    raise ImproperlyConfigured("'DEBUG' setting is required.")
if not hasattr(settings, "MERCHANT_AUTH_LOGIN_ID"):
    raise ImproperlyConfigured("'MERCHANT_AUTH_LOGIN_ID' setting is required.")
if not hasattr(settings, "MERCHANT_AUTH_TRANSACTION_KEY"):
    raise ImproperlyConfigured("'MERCHANT_AUTH_TRANSACTION_KEY' setting is required.")


def get_merchant_auth() -> merchantAuthenticationType:
    return merchantAuthenticationType(
        name=str(settings.MERCHANT_AUTH_LOGIN_ID),
        transactionKey=str(settings.MERCHANT_AUTH_TRANSACTION_KEY),
    )


def get_environment() -> str:
    return constants.SANDBOX if settings.DEBUG else constants.PRODUCTION


def get_validation_mode() -> str:
    return "testMode" if settings.DEBUG else "liveMode"
