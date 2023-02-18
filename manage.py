#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def check_prod_settings():
    prod_settings = ["SECRET_KEY"]
    for setting in prod_settings:
        try:
            os.environ[setting]
        except KeyError:
            print(f"{setting} is not set in the ENVIRONMENT !!")


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    try:
        os.environ["AUTHKEY"]
    except KeyError:
        print('AUTHKEY has to be set')
    check_prod_settings()
    main()
