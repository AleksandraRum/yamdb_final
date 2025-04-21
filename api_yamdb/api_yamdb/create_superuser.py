import os

import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_yamdb.settings')
django.setup()

User = get_user_model()

if not User.objects.filter(
    username=os.environ.get('DJANGO_SUPERUSER_USERNAME')).exists():
        User.objects.create_superuser(
            username=os.environ.get('DJANGO_SUPERUSER_USERNAME'),
            email=os.environ.get('DJANGO_SUPERUSER_EMAIL'),
            password=os.environ.get('DJANGO_SUPERUSER_PASSWORD')
    )
