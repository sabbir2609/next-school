import os

# Directory path where logs will be stored
log_directory = "logs"

# Ensure the log directory exists, create it if it doesn't
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# fmt: off
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(levelname)s %(asctime)s %(message)s",
        },
        "custom_format_debug": {
            "()": "django.utils.log.ServerFormatter",
            "format": "\033[92mDEBUG\033[0m %(asctime)s %(message)s",
        },
        "custom_format_info": {
            "()": "django.utils.log.ServerFormatter",
            "format": "\033[94mINFO\033[0m %(asctime)s %(message)s",
        },
        "custom_format_success": {
            "()": "django.utils.log.ServerFormatter",
            "format": "\033[92mSUCCESS\033[0m %(asctime)s %(message)s",
        },
        "custom_format_warning": {
            "()": "django.utils.log.ServerFormatter",
            "format": "\033[93mWARNING\033[0m %(asctime)s %(message)s",
        },
        "custom_format_error": {
            "()": "django.utils.log.ServerFormatter",
            "format": "\033[91mERROR\033[0m %(asctime)s %(message)s",
        },
    },
    "handlers": {

        "error_log": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": os.path.join(log_directory, "error.log"),
            "formatter": "standard",
        },

        "server_log": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(log_directory, "server.log"),
            "formatter": "standard",
        },

        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    
    "loggers": {
        "": {
            "handlers": ["error_log", "server_log", "console"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
