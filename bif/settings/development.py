# file for development
import datetime
from bif.settings.base import *
from decouple import config
from pathlib import Path

SECRET_KEY = config("SECRET_KEY")
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# DEBUG = config('DEBUG')
DEBUG = True
ALLOWED_HOSTS = ['*']


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}




CORS_ORIGIN_WRITELIST = (
    'http://localhost:3000',
    'http://localhost:',
)


# CORS_ORIGIN_WRITELIST= (
#     'http://localhost',
# )


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(hours=2),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "SIGNING_KEY": SECRET_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",),
}
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'
STATICFILES_DIRS = [BASE_DIR / "media/static"]


CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    'http://127.0.0.1:8000'
]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://127.0.0.1:8000'
]

CORS_ALLOW_HEADERS = (
    'content-disposition', 'accept-encoding',
    'content-type', 'accept', 'origin', 'Authorization', 'access-control-allow-methods',
    'Access-Control-Allow-Origin'
)

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)