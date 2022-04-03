import os
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application


def before_all(context):
    application = get_wsgi_application()
    call_command('runserver', '127.0.0.1:8000')
