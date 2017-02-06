"""
Django settings for air_quality_sensor project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

LOGIN_URL = '/sensor/login'
LOGIN_REDIRECT_URL = '/sensor/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#dl3etb%m=az)f17teo6(y79n31-1nt5h0!-3zy0-f4y*%)lya'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),)

STATICFILES_DIRS = (
    BASE_DIR + '/static/',
)


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TASK_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sensor',
    'django_crontab',
    'celery',
    'djcelery'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# use rabbitmq consifuration
BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_BACKEND = "amqp"
CELERY_IMPORTS = ('sensor.tasks.task',)

from kombu import Exchange, Queue

CELERY_DEFAULT_QUEUE = 'periodical'
CELERY_QUEUES = (
    Queue('periodical', Exchange('periodical'), routing_key='periodical'),
    Queue('user_tasks', Exchange('user_tasks'), routing_key='user_tasks'),
)
CELERY_DEFAULT_EXCHANGE = 'periodical'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_DEFAULT_ROUTING_KEY = 'periodical'

CELERYD_PREFETCH_MULTIPLIER = 50 # Make sure that tasks that are not executed immediately will always be reserved instead of being ignored

BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "myusername"
BROKER_PASSWORD = "mypassword"
C_FORCE_ROOT = True
# BROKER_VHOST = "myvhost"

import djcelery

djcelery.setup_loader()
# use this settings to run cron job
# No project name for cron job
CRONJOBS = [
    ('*/10 * * * *', 'testbed.cron.my_scheduled_job'),
    ('*/1 * * * *', 'testbed.cron.loginsight_update'),
    # ('*/1 * * * *', 'testbed.cron.test_job'),
    # ('*/30 * * * *', 'testbed.cron.ui_client_update'),
    # update build number every day
    # ('*/30 * * * *', 'testbed.cron.build_number_update'),
]


ROOT_URLCONF = 'air_quality_sensor.urls'

WSGI_APPLICATION = 'air_quality_sensor.wsgi.application'


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
