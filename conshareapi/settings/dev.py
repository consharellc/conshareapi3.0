from .base import *
import os
# override base.py settings

DEBUG = bool(os.environ.get("DEBUG", default=0))
SECRET_KEY = os.environ.get("SECRET_KEY")

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        'ENGINE': os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        'USER': os.environ.get("SQL_USER", "user"),
        'PASSWORD': os.environ.get("SQL_PASSWORD", "password"),
        'HOST': os.environ.get("SQL_HOST", "localhost"),
        'PORT': '5432',
        
    },
    'message': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'messages.sqlite3',
    }
}


DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage' 