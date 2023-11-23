import os

from .base import *

from dotenv import load_dotenv
import dj_database_url


# Load environment variables from .env file
load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ["DEBUG"]

# ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"].split(",")

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# DATABASES = {
#     "default": dj_database_url.parse(os.environ.get("DATABASE_URL"), conn_max_age=600),
# }

# importing logger settings
try:
    from .logger_settings import *
except Exception as e:
    pass

MIDDLEWARE += [
    # Django Debug Toolbar
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]


MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
