import os

from .settings import *
from .settings import BASE_DIR

# Azure deployment settings
SECRET_KEY = os.environ['SECRET']
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://'+os.environ['WEBSITE_HOSTNAME']]
DEBUG = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Database

connection_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
print(connection_string)
parameters = {pair.split('=')[0]: pair.split('=')[1] for pair in connection_string.split(' ')}
print(parameters['dbname'])
print(parameters['host'])
print(parameters['user'])
print(parameters['password'])
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django-zono-database',
        'HOST': 'django-zono-server.postgres.database.azure.com',
        'USER': 'haylsfjysv',
        'PASSWORD': 'JzI6sc72o$hUiot1',
        'PORT': '5432',
    }
}