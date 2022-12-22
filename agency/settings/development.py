from .base import *

#TODO -> 
SECRET_KEY = 'Sistemas123'

# SECURITY WARNING: don't run with debug turned on in production!
#TODO -> 
DEBUG = True

#TODO -> 
ALLOWED_HOSTS = ['*']

#TODO ->
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Email  SERVER (GMAIL)

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'gerardo.lunarcito@gmail.com'
EMAIL_HOST_PASSWORD = 'juigbjfvogxtqash'
EMAIL_USE_TLS = True