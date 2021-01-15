import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import re

DJANGO_ENV = os.getenv('DJANGO_ENV', 'LOCAL')
with open(f'/etc/default/env.{DJANGO_ENV}', 'r') as f:
    matches = re.findall(r'^(.+)=(.*)$', f.read(), flags=re.M)
    env = dict(matches)

SECRET_KEY = env['DJANGO_SECRET']
DEBUG = env['DJANGO_DEBUG'] in (True, "True")

ALLOWED_HOSTS = [ '127.0.0.1', '.cloud-init.ml' ]
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'https://contactmanager.dev.cloud-init.ml'
    'https://contactmanager.cloud-init.ml'
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'contactmanager',
    'snippets.apps.SnippetsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

if DJANGO_ENV == "LOCAL":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'USER': env['DATABASE_USER'],
            'PASSWORD': env['DATABASE_PASSWORD'],
            'HOST': env['DATABASE_HOST'],
            'NAME': env['DATABASE_NAME'],
            'OPTIONS': {
                'charset': 'utf8',
                'use_unicode': True,
                'sql_mode': 'traditional',
            },
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = [
]
