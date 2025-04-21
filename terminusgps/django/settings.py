import os
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent
DEBUG = True
SECRET_KEY = "xem*6no%8d9%^qzt2f3x3ar-uq4_+7h9myc$t0!+4%bj5us6f)"
USE_TZ = False

# Secrets
CONNECT_SECRET = os.getenv("CONNECT_SECRET")
MERCHANT_AUTH_LOGIN_ID = os.getenv("MERCHANT_AUTH_LOGIN_ID")
MERCHANT_AUTH_TRANSACTION_KEY = os.getenv("MERCHANT_AUTH_TRANSACTION_KEY")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")
TWILIO_MESSAGING_SID = os.getenv("TWILIO_MESSAGING_SID")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
WIALON_ADMIN_ID = os.getenv("WIALON_ADMIN_ID")
WIALON_TOKEN = os.getenv("WIALON_TOKEN")
