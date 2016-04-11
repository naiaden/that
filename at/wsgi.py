"""
WSGI config for at project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/scratch2/www/that/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "at.settings")

application = get_wsgi_application()
