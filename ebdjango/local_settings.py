# coding=utf-8


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': '<username>',
        'PASSWORD': '<password>',
    }
}

# Celery broker Url
BROKER_URL = 'amqp://guest:guest@localhost'
