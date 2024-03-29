"""
Django settings for CRM project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from . import keys

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-opf2^cubtoesvi^ro17612z2uybet5%v0a!a%brw_4n$%=d^6!"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django_filters",
    "accounts.apps.AccountsConfig",
    "storages",
    
    
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "kolo.middleware.KoloMiddleware",


    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "CRM.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "CRM.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

USE_POSTGRESQL_DB=True
USE_AWS_RDS = False

if USE_POSTGRESQL_DB:
    if USE_AWS_RDS:

        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": "demo_1",
                "USER": os.getenv("AWS_USER"),
                "PASSWORD": os.getenv("AWS_PASS"),
                "HOST": os.getenv("AWS_HOST_ENDPOINT"),
                "PORT": "5432",
            }

        
        }
    else:

        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": "DEMO_TEST",
                "USER": "postgres",
                "PASSWORD": os.getenv("LOCAL_HOST_PASS"),
                "HOST": "localhost",
                "PORT": "5432",
            }
        }

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

    


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/London"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
USE_S3 = True

if USE_S3:
    AWS_ACCESS_KEY_ID = keys.AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY = keys.AWS_SECRET_ACCESS_KEY
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = os.getenv("AWS_LOCATION")

    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'

    AWS_S3_FILE_OVERWRITE = True

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
else:

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]

    MEDIA_ROOT = os.path.join(BASE_DIR, 'static/imgs/userProfiles')
    MEDIA_URL = '/imgs/'

STATIC_URL = '/static/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"







