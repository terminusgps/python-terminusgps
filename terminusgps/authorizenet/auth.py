from authorizenet.apicontractsv1 import merchantAuthenticationType
from authorizenet.constants import constants

from django.conf import ImproperlyConfigured, settings


def settings_required(settings_list: list[str]):
    def decorator(func):
        def wrapped(*args, **kwargs):
            for setting_name in settings_list:
                if not hasattr(settings, setting_name):
                    raise ImproperlyConfigured(f"'{setting_name}' setting is required.")
            return func(*args, **kwargs)

        return wrapped

    return decorator


@settings_required(["MERCHANT_AUTH_LOGIN_ID", "MERCHANT_AUTH_TRANSACTION_KEY"])
def get_merchant_auth() -> merchantAuthenticationType:
    return merchantAuthenticationType(
        name=str(settings.MERCHANT_AUTH_LOGIN_ID),
        transactionKey=str(settings.MERCHANT_AUTH_TRANSACTION_KEY),
    )


@settings_required(["DEBUG"])
def get_environment() -> str:
    return constants.SANDBOX if settings.DEBUG else constants.PRODUCTION


@settings_required(["DEBUG"])
def get_validation_mode() -> str:
    return "testMode" if settings.DEBUG else "liveMode"
