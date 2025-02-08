"""
WSGI config for HelloDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os, sys
site_user_root_dir = '/home/a/annadi43/anna-didenko.ru/public_html'
sys.path.insert(0, site_user_root_dir + '/anadid')
sys.path.insert(1, site_user_root_dir + '/venv/lib/python3.11/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'anadid.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
