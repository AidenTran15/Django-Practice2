"""
WSGI config for codedaddies project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys


path = '/codedaddies/templates/base.html'
if path not in sys.path:
    sys.path.append(path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codedaddies.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
