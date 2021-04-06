# coding: utf-8
# Django settings for transportes project.
from os.path import abspath, basename, dirname, join, normpath
from django.contrib.messages import constants as message_constants
import os
BASE_PATH = dirname(dirname(abspath(__file__)))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
LOCAL = True

INTERNAL_IPS = ('192.168.100.128',) ###'127.0.0.1' o 0.0.0.0
 
ADMINS = (
   (u'Anu', '@codefire.mx'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'demasys_vitesse_new', # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'logvitesse',### lofgvitesse (local)
        'PASSWORD': 'demasys45',
        'HOST': '127.0.0.1',##'mysql1.demasys-vitesse.com', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',  # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['demasys-vitesse.com',]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Mexico_City'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-mx'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

DATE_INPUT_FORMATS = ('%d-%m-%Y', '%d/%m/%Y', '%Y-%m-%d')

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True
#SITE_ROOT = os.path.dirname(__file__)
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
#test con site root
MEDIA_ROOT = BASE_PATH + '/media/'
#MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
#STATIC_ROOT = BASE_PATH + '/media/static/'
STATIC_ROOT = os.path.dirname(BASE_PATH)+'/media/static/'
# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/media/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 's+!7$^arve3hqj%vwv!^71*=h*1p-=gc-p^&7!fj%=85n*e=ar'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
)

ROOT_URLCONF = 'transportes.urls'


# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'transportes.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_PATH + '/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'grappelli',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'bootstrap_pagination',
    'django_extensions',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'south',
 #   'debug_toolbar',
    'easy_pdf',
    #'menu',
    #'sorl.thumbnail',
    'sepomex',
    'dashboards',
    'cuentas',
    'catalogos',
    'clientes',
    'workflow',
    'viajes',
    'solicitudes',
    'beneficiarios',
    'contable',
    'inventario',
    'empleados',
    'externo',
    'reporte',
)

MESSAGE_TAGS = {
    message_constants.DEBUG: 'alert-info',
    message_constants.INFO: 'alert-info',
    message_constants.SUCCESS: 'alert-success',
    message_constants.WARNING: 'alert-warning',
    message_constants.ERROR: 'alert-danger',
}

GRAPPELLI_ADMIN_TITLE = 'Vitesse'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/cuentas/login/'
LOGOUT_URL = '/cuentas/logout/'
SESSION_COOKIE_NAME = 'transportes'
AUTH_PROFILE_MODULE = 'cuentas.Perfil'


EMAIL_HOST = 'webmail.logisticavitesse.com.mx'
EMAIL_HOST_USER = 'controladministrativo@logisticavitesse.com.mx'#'contacto@logisticavitesse.com.mx'
EMAIL_HOST_PASSWORD = 'db286g1+-'##'Vitesse2015'
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = 'controladministrativo@logisticavitesse.com.mx'  #'contacto@logisticavitesse.com.mx'
#SERVER_EMAIL = 'contacto@logisticavitesse.com.mx''

#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'Ofarias0424@gmail.com'
#EMAIL_HOST_PASSWORD = 'elPaso35+'
#DEFAULT_FROM_EMAIL = 'Ofarias0424@gmail.com'
#DEFAULT_TO_EMAIL = 'Ofarias0424@gmail.com'


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from local_settings import *
except ImportError:
    pass
