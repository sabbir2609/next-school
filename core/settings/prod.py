from .base import *

import os

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = (
    [os.environ["WEBSITE_HOSTNAME"]] if "WEBSITE_HOSTNAME" in os.environ else []
)

CSRF_TRUSTED_ORIGINS = (
    ["https://" + os.environ["WEBSITE_HOSTNAME"]]
    if "WEBSITE_HOSTNAME" in os.environ
    else []
)

DEBUG = os.environ["DEBUG"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "HOST": os.environ["DB_HOST"],
        "PORT": os.environ["DB_PORT"],
        "ATOMIC_REQUESTS": True,
    }
}


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Set SECURE_HSTS_SECONDS to the desired duration, for example, 1 year
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds
