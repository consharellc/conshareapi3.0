import os
import django_heroku
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from .base import *  # noqa: F403

DEBUG = bool(os.environ.get("DEBUG", default=0))
SECRET_KEY = os.environ.get("SECRET_KEY")



sentry_sdk.init(
    dsn="https://de808f6f605c4fd79120ddb21f073904@o599875.ingest.sentry.io/5743882",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['SQL_DATABASE'],
        'USER': os.environ['SQL_USER'],
        'PASSWORD': os.environ['SQL_PASSWORD'],
        'HOST': os.environ['SQL_HOST'],
        'PORT': os.environ['PORT'],
        
    },
    'message': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'messages.sqlite3',
    }
}
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.mailgun.org'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = True


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

django_heroku.settings(locals(), test_runner=False)