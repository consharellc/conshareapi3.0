from conshareapi.settings.base import *
from .base import *
import os
# override base.py settings

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'd8153ta0utvn67',
        # 'USER': 'tfikjzwhrosoxy',
        # 'PASSWORD': '8409a753e4ef9a66b01bdd0544211538179ed057cb58405c221964080b807098',
        # 'HOST': 'ec2-54-166-120-40.compute-1.amazonaws.com',
        # 'PORT': '5432',
        
    },
    'message': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'messages.sqlite3',
    }
}


DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage' 