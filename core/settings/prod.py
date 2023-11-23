from .base import *
import dj_database_url
from dotenv import load_dotenv
import os

try:
    load_dotenv()
    print("Loaded environment variables from .env file")
except Exception as e:
    print("Failed to load environment variables from .env file")

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
