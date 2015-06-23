from __future__ import absolute_import


# for rabbitMQ as broker

BROKER_URL = 'amqp://guest:guest@localhost//'



CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'








# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e-8v^y-rt&n3f&5c9a$*wuq7_x6nf4$i-zu2_61))zu)!h0s08'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'material.admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'material',
    'material.frontend',
    'easy_pjax',
    'djcelery',
    'adwords',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'material.frontend.middleware.SmoothNavigationMiddleware',
)

ROOT_URLCONF = 'medlane.urls'

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
                'material.frontend.context_processors.modules',
            ],
        },
    },
]

WSGI_APPLICATION = 'medlane.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'medlane',
        'USER': 'medlane',
        'PASSWORD': 'medl@ne$',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static/")


############################
###  Adwords Settings  #####
############################

GOOGLEADWORDS_CLIENT_ID = '548906345961-ginb4gn71g10908m0miujks0ufu3blj3.apps.googleusercontent.com'
GOOGLEADWORDS_CLIENT_SECRET = '39b33527f6053e9b43988f9ebfeabdd483bce418'
GOOGLEADWORDS_REFRESH_TOKEN = ''
GOOGLEADWORDS_DEVELOPER_TOKEN = 'EQ9Phq4ibYUT_rwZ4RZrIw'
GOOGLEADWORDS_CLIENT_CUSTOMER_ID = '522-789-0930'