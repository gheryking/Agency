from dotenv import load_dotenv
import os

from agency.loggin import *
from agency.settings.base import *

load_dotenv(Path.joinpath(BASE_DIR,'.env'))

#TODO -> 
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#TODO -> 
DEBUG = False

#TODO -> 
ALLOWED_HOSTS = ['*']

#TODO -> 
# DOCKER ->
#DATABASES = {
#    'default':{
#        'ENGINE':'django.db.backends.postgresql',
#        'NAME':'postgres',
#        'USER':'postgres',
#        'PASSWORD':'Sistemas123',
#        'HOST':'localhost',
#        'PORT':'5432',
#    }
#}

DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.postgresql',
        'NAME':os.environ.get('DB_NAME'),
        'USER':os.environ.get('DB_USER'),
        'PASSWORD':os.environ.get('DB_PASSWORD'),
        'HOST':os.environ.get('DB_HOST'),
        'PORT':os.environ.get('DB_PORT'),
    }
}

STATIC_ROOT = Path.joinpath(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"