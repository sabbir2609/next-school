import os

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
        "colored_file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join("logs", "error.log"),
            "formatter": "standard",
        },
        "server_logs_file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join("logs", "server.log"),
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
            "handlers": ["colored_file", "server_logs_file", "console"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
