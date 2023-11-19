#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv


def main():
    """Run administrative tasks."""
    print("WEBSITE_HOSTNAME" in os.environ)
    # Only for Local Development - Load environment variables from the .env file
    if "WEBSITE_HOSTNAME" not in os.environ:
        print("Loading environment variables for .env file")
        env_path = os.path.join(BASE_DIR, ".env")
        load_dotenv(env_path)

    settings_module = (
        "core.settings.prod"
        if "WEBSITE_HOSTNAME" in os.environ
        else "core.settings.dev"
    )
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
