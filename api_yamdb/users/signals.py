# users/signals.py
import os
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver

User = get_user_model()

@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    username = os.getenv('DJANGO_SUPERUSER_USERNAME')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

    if username and email and password:
        if not User.objects.filter(username=username).exists():
            print("\nCreating superuser...")
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
        else:
            print("\nSuperuser already exists.")