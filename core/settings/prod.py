from .base import *
import dj_database_url

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
    "default": dj_database_url.parse(os.environ.get("DATABASE_URL"), conn_max_age=600),
}


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Set SECURE_HSTS_SECONDS to the desired duration, for example, 1 year
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds
