""" Production Settings """
# default: use settings from main settings.py if not overwritten
from .settings import *
import config

import django_heroku

# DEBUG = config('DEBUG')

DEBUG =  config('DEBUG')
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', SECRET_KEY)
# adjust to the URL of your Heroku app
ALLOWED_HOSTS = ['django-hello-world-app.herokuapp.com']

# Activate Django-Heroku.
django_heroku.settings(locals())