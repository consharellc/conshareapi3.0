from .base import *  # noqa: F403
import os
# override base.py settings

DEBUG = bool(os.environ.get("DEBUG", default=0))

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


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


DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage' 