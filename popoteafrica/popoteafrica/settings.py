"""
Django settings for popoteafrica project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from django.conf import global_settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR  = os.path.dirname(__file__)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v7sva@#kr317_uq361tor5%owo+ns_d206mxyz3wl@ie0(hyt-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'popoteafrica',
    'live_support',
    'cropper'
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



ROOT_URLCONF = 'popoteafrica.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            'C:\\Users\\AfricaTechSolutions\\Envs\\africatechsolutions\\popoteafrica\\templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
        #        'django.template.context_processors.debug',
        #        'django.template.context_processors.request',
        #        'django.contrib.auth.context_processors.auth',
        #        'django.contrib.messages.context_processors.messages',

                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEMPLATES_DIRS = (
#    '/home/africatechsolutions/djangoivan/mainproject/templates'
    os.path.join(BASE_DIR, 'templates')
)

WSGI_APPLICATION = 'popoteafrica.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.popoteafrica'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

STATIC_ROOT = os.path.join(PROJECT_DIR)

#AVATAR_ROOT = 'home/africatechsolutions/djangoivan/mainproject/mainproject/static'
#AVATAR_ROOT= os.path.join(PROJECT_ROOT, 'profile_pictures')

STATIC_URL = '/static/'

STATICFILES_DIRS=(
#('assets', os.path.join(PROJECT_DIR, '../static'))
#(os.path.join(BASE_DIR, '../static'),)
#(os.path.join(PROJECT_DIR, 'static')),
(os.path.join(BASE_DIR, 'static')),
)

#MEDIA_ROOT=(os.path.join(PROJECT_DIR, 'static'))
MEDIA_ROOT = ('C:\\Users\\AfricaTechSolutions\\Envs\\africatechsolutions\\popoteafrica\\static')

#MEDIA_ROOT='/home/africatechsolutions/djangoivan/mainproject/mainproject/static'


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Dar_es_Salaam'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'