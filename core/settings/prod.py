import os
from .base import *
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = (
    [os.environ["WEBSITE_HOSTNAME"]] if "WEBSITE_HOSTNAME" in os.environ else []
)

CSRF_TRUSTED_ORIGINS = (
    ["https://" + os.environ["WEBSITE_HOSTNAME"]]
    if "WEBSITE_HOSTNAME" in os.environ
    else []
)

DEBUG = False

# If you are using a database other than sqlite, uncomment the following lines.

DATABASES = {
    "default": dj_database_url.parse(os.environ.get("DATABASE_URL"), conn_max_age=600),
}


INSTALLED_APPS += [
    # Media Cloudinary
    "cloudinary",
    "cloudinary_storage",
]

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.environ["CLOUDINARY_CLOUD_NAME"],
    "API_KEY": os.environ["CLOUDINARY_API_KEY"],
    "API_SECRET": os.environ["CLOUDINARY_API_SECRET"],
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
