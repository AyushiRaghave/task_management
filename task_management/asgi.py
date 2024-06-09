"""
ASGI config for task_management project.

This module contains the ASGI application used for serving the project.
It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Set the default settings module for the 'asgi' application.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_management.settings")

# Create the ASGI application instance.
application = get_asgi_application()
