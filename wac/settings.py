"""
Django settings for wac project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""



import os
import dj_database_url
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# to generate a secret key, do:
# import random
# ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', False) == 'true'

ALLOWED_HOSTS = [
    'api.womenandcolor.com',
    'womenandcolor-api-production.herokuapp.com',
    'womenandcolor-api-staging.herokuapp.com',
    'localhost',
]

if DEBUG == False:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',

    # Third Party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'corsheaders',
    'mailchimp3',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'storages',

    # App
    'wac.apps.core',
    'wac.apps.accounts',
    'wac.apps.contact_speaker'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'
]

ROOT_URLCONF = 'wac.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "wac", "templates")
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]


WSGI_APPLICATION = 'wac.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}

if DEBUG == True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB'),
            'USER': os.getenv('POSTGRES_USER'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
            'HOST': os.getenv('POSTGRES_HOST'),
            'PORT': os.getenv('POSTGRES_PORT', 5432)

        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# ====================== ROLLBAR ====================== #
ROLLBAR = {
    'access_token': '485f0f5f09334d179c696ac338009215',
    'environment': 'development' if DEBUG else 'production',
    'root': BASE_DIR,
}
import rollbar
rollbar.init(**ROLLBAR)
# ============================================================ #


# ====================== REST FRAMEWORK ====================== #
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    )
}

REST_USE_JWT = True
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=1),
}
USER_DETAILS_SERIALIZER = 'wac.apps.accounts.api.serializers.UserSerializer'
SITE_ID = 1
# ============================================================ #

# ====================== ALLAUTH ====================== #
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION  = "none"
ACCOUNT_AUTHENTICATION_METHOD = 'email'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[Women and Color] '
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

# ============================================================ #

# REST AUTH

OLD_PASSWORD_FIELD_ENABLED = True

# CORS

CORS_ORIGIN_WHITELIST = (
    'womenandcolor.com',
    'www.womenandcolor.com',
    'womenandcolor-staging.herokuapp.com',
    'womenandcolor-production.herokuapp.com',
    'localhost:8080',
    'localhost:8085',
    '127.0.0.1:8080',
    'localhost:9000',
    'women-and-color-staging.herokuapp.com',
    'women-and-color-production.herokuapp.com',
    'staging.modernleaders.com',
    'modernleaders.com',
    'www.modernleaders.com'
)

CSRF_TRUSTED_ORIGINS = (
    'womenandcolor.com',
    'api.womenandcolor.com',
    'www.womenandcolor.com',
    'womenandcolor-staging.herokuapp.com',
    'womenandcolor-production.herokuapp.com',
    'womenandcolor-api-staging.herokuapp.com',
    'womenandcolor-api-production.herokuapp.com',
    'localhost:8080',
    'localhost:8000',
    'staging.modernleaders.com',
    'modernleaders.com',
    'www.modernleaders.com'
)

# Email
if DEBUG == True:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Sendgrid

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('SENDGRID_ACCOUNT')
EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'hello@womenandcolor.com'
MESSAGE_EMAIL = 'messages@womenandcolor.com'

# Mailchimp

MAILCHIMP_API_KEY = os.environ.get('MAILCHIMP_API_KEY', '')
SPEAKER_LIST_ID = "c420f5416a"

# AWS

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_KEY', '')
AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_BUCKET', '')
AWS_REGION = 'ca-central-1'
AWS_S3_CUSTOM_DOMAIN = "s3.%s.amazonaws.com/%s" % (AWS_REGION, AWS_STORAGE_BUCKET_NAME)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=31536000',
}
CLOUDFRONT_DOMAIN = os.environ.get('CLOUDFRONT_DOMAIN', '')

AWS_MEDIA_LOCATION = 'media'
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_MEDIA_LOCATION)
DEFAULT_FILE_STORAGE = 'wac.storage_backends.MediaStorage'

AWS_STATIC_LOCATION = 'static'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
STATICFILES_STORAGE = 'wac.storage_backends.StaticStorage'

# Heroku API

## access to women-and-color-static app
HEROKU_PLATFORM_API_KEY = os.environ.get('HEROKU_PLATFORM_API_KEY')

## configuration for triggering front-end build
FRONTEND_APP_TARBALL = os.environ.get('FRONTEND_APP_TARBALL')
FRONTEND_APP_NAME = os.environ.get('FRONTEND_APP_NAME')

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}
