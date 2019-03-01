import datetime
import django_heroku
import os
from decouple import config
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '^0$(x=d-+oxnacx$*#o&@pf2+od$zz30&ug%+*7qw$$t453=1y'

TOKEN_EXPIRE_TIME = datetime.timedelta(days=120)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = config(‘SECRET_KEY’)
# SECURITY WARNING: don’t run with debug turned on in production!
DEBUG = config(‘DEBUG’, default=False, cast=bool)
ALLOWED_HOSTS = [‘*’]
# Recommended setting is [ ‘.herokuapp.com’ ]

#ALLOWED_HOSTS = ['127.0.0.1']

AUTH_USER_MODEL = 'user.CustomUser'

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'rest_framework',
	'rest_framework.authtoken',
	'weather_data',
	'user',
	'raw'
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

ROOT_URLCONF = 'pbApi.urls'

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

WSGI_APPLICATION = 'pbApi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
"""
DATABASES = {
    'default': {

		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'pbdb',
		'USER': 'pbuser',
		'PASSWORD': 'pb123',
		'HOST': 'localhost',
		'PORT': '',
	}
}
"""
DATABASES = {
 ‘default’: dj_database_url.config(
 default=config(‘DATABASE_URL’)
 )}

REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'user.authentication.ExpiringTokenAuthentication',
	),
	'DEFAULT_RENDERER_CLASSES': (
		'rest_framework.renderers.JSONRenderer',
	),
	'DEFAULT_PERMISSION_CLASSES': (
		'rest_framework.permissions.IsAuthenticated',
		#'rest_framework.permissions.AllowAny',
	)
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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'





# Activate Django-Heroku.
django_heroku.settings(locals())