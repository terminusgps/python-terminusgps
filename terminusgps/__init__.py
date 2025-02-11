from django.conf import settings, ImproperlyConfigured

if not hasattr(settings, "DEBUG"):
    raise ImproperlyConfigured("'DEBUG' setting is required.")
if not hasattr(settings, "MERCHANT_AUTH_LOGIN_ID"):
    raise ImproperlyConfigured("'MERCHANT_AUTH_LOGIN_ID' setting is required.")
if not hasattr(settings, "MERCHANT_AUTH_TRANSACTION_KEY"):
    raise ImproperlyConfigured("'MERCHANT_AUTH_TRANSACTION_KEY' setting is required.")
if not hasattr(settings, "TWILIO_FROM_NUMBER"):
    raise ImproperlyConfigured("'TWILIO_FROM_NUMBER' setting is required.")
if not hasattr(settings, "TWILIO_MESSAGING_SID"):
    raise ImproperlyConfigured("'TWILIO_MESSAGING_SID' setting is required.")
if not hasattr(settings, "TWILIO_SID"):
    raise ImproperlyConfigured("'TWILIO_SID' setting is required.")
if not hasattr(settings, "TWILIO_TOKEN"):
    raise ImproperlyConfigured("'TWILIO_TOKEN' setting is required.")
if not hasattr(settings, "WIALON_TOKEN"):
    raise ImproperlyConfigured("'WIALON_TOKEN' setting is required.")
if not hasattr(settings, "WIALON_ADMIN_ID"):
    raise ImproperlyConfigured("'WIALON_ADMIN_ID' setting is required.")
