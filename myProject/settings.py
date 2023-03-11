"""
Django settings for myProject project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
import environ
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
    SECRET_KEY = os.environ["SECRET_KEY"]
except KeyError:
    if not env.bool('DEBUG'):
        #  import sys
        #  sys.exit('SECRET_KEY not set!!!')
        raise SystemExit
    SECRET_KEY = 'django-insecure-%i5x*^%*%%ht)ko+^3@h&fm=37z^t*6u1+7(y1%bb6d@+7ji&r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")


# Application definition

INSTALLED_APPS = [
    'myApp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cleanup.apps.CleanupConfig',
    'corsheaders',
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
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'myProject.urls'

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

WSGI_APPLICATION = 'myProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if env("DATABASE_NAME") == "none":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': env("DATABASE_ENGINE"),
            'NAME': env("DATABASE_NAME"),
            'HOST': env("DATABASE_HOST"),
            'PORT': env("DATABASE_POST"),
            'USER': env("DATABASE_USER"),
            'PASSWORD': env("DATABASE_PASS"),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

"""
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
"""

LOGIN_URL = '/login'


# FileSystem Catching System
# https://docs.djangoproject.com/en/4.0/topics/cache/
CACHES = {
    'default': {
        'BACKEND': env("CACHE_BACKEND"),
        'LOCATION': env("CACHE_LOCATION"),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Prod settings (send cookies through https only)
CSRF_COOKIE_SECURE = env.bool("CSRF_COOKIE_SECURE")
CSRF_COOKIE_SAMESITE = env.str("CSRF_COOKIE_SAMESITE")

# Main Api settings
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")
CORS_ALLOW_CREDENTIALS = env.bool("CORS_ALLOW_CREDENTIALS")  # for allowing cors
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS")  # for allowing cors


# Cached type of session
# https://docs.djangoproject.com/en/4.0/topics/http/sessions/#cached-sessions-backend

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# Async tasks with celery using rabbitmq as broker
CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")
CELERY_IGNORE_RESULT = env.bool("CELERY_IGNORE_RESULT", default=False)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = env.str('STATIC_URL', default='static/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files folder
MEDIA_URL = env.str('MEDIA_URL', default='/media/')
MEDIA_ROOT = BASE_DIR / 'media'

# Logging properties and config
# https://docs.djangoproject.com/en/4.0/topics/logging/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{asctime} {levelname} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{asctime} {levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'WARNING',
        },
        'remote_network': {
            'class': 'logging.handlers.SocketHandler',
            'level': 'ERROR',
            'host': '127.0.0.1',
            'port': '7071'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'C:\\Users\\demilade.ayandele\\Documents\\project\\api\\back\\log\\cbeasylog.log',
            'maxBytes': 20240,
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'file1': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'C:\\Users\\demilade.ayandele\\Documents\\project\\api\\back\\log\\cbeasylog.server.log',
            'maxBytes': 20240,
            'backupCount': 5,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'myApp.views': {
            'handlers': ['file'],
            'level': env('DJANGO_LOG_LEVEL', default='INFO'),
        },
        'django.server': {
            'handlers': ['file1'],
            'level': env('DJANGO_LOG_LEVEL_SERVER', default='WARNING'),
        },
    },
}
