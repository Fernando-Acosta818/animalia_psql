"""
WSGI config for animalia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.contrib.auth.models import User
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animalia.settings')

application = get_wsgi_application()

users = User.objects.all()
if not users:
    User.objects.create_superuser(username="admin", email="user@example.com", password="admin", is_active=True, is_staff=True)