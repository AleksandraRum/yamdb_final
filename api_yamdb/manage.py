#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_yamdb.settings')
    try:
        from django.core.management import execute_from_command_line
        from django.contrib.auth import get_user_model
        User = get_user_model()

        username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

        if username and email and password:
            if not User.objects.filter(username=username).exists():
                print("⚙️ Creating superuser...")
                User.objects.create_superuser(username=username, email=email, password=password)
            else:
                print("Superuser already exists.")
        else:
            print("No superuser info in env — skipping create_superuser.")

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
