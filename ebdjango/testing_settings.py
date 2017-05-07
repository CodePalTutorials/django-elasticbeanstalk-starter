# coding=utf-8

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
import os


# Add all your test or QA Settings here.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT'],
    }
}

# Celery broker Url
BROKER_URL = os.environ['BROKER_URL']
