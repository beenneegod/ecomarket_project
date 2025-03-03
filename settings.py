import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '5_wz)t^b#9b3)dbhf2yrg3iz(5-mxribcwrtylj)9s&brrwudu'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main_app',
    'payments',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecomarket_project.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecomarket_db',
        'USER': 'postgres',
        'PASSWORD': 'PolinakA288001$',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}

LANGUAGE_CODE = 'pl'

LANGUAGES = [
    ('pl', 'Polski'),
    ('en', 'English'),
]

LOCALE_PATHS = [BASE_DIR / 'main_app/translations']
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "main_app/static"]