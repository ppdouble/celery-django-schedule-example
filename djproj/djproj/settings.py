"""
Django settings for djproj project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from __future__ import absolute_import
from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6379/0'

from datetime import timedelta
CELERYBEAT_SCHEDULE = {
    'defaulttask1': {
        'task': 'djproj.celery.defaulttask1',
        'schedule': timedelta(seconds=3)
    }, 
    'hello': {
        'task': 'djproj.celery.hello',
        'schedule': timedelta(seconds=4)
    }, 
    'autodiscovertasks1': {
        'task': 'apps.app1.tasks.autotask1',
        'schedule': timedelta(seconds=5)
    },  
    'autodiscovertasks2': {
        'task': 'apps.app1.tasks.autotask2',
        'schedule': crontab(minute=55, hour=17)
    },
    'mytasks1': {
        'task': 'apps.app2.mytasks.mytask1',
        'schedule': timedelta(seconds=6)
    },  
    'mytasks2': {
        'task': 'apps.app2.mytasks.mytask2',
        'schedule': crontab(minute=55, hour=17)
    }
}

#import app2 manually
CELERY_IMPORTS = (
    'apps.app2.mytasks',
)

TIME_ZONE = 'Asia/Shanghai'

DATETIME_FORMAT = 'Y-m-d H:i:s'

TIME_FORMAT = 'Y-m-d H:i:s'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+df53@zaea16*pa%)kyta=ciam#$1c1&tjx-5!59f+nlo)n#!4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.app1',
    'apps.app2',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djproj.urls'

WSGI_APPLICATION = 'djproj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh_CN'

#TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
