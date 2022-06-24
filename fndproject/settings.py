
import os
import  django.contrib.gis
import cloudinary
import osgeo


import cloudinary

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pw(0k@eoji1&7=gwtvo78=1&wgub&i^m0vqrma+&@ae(uy45!j'

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
    'services',
    'rest_framework',
    'portfolio',
    'ratings',
    'authapp',
    'profiles',
    'cloudinary',
    'rest_framework.authtoken',
]
cloudinary.config(
  cloud_name = "oyesa",
  api_key = "749352579693875",
  api_secret = "W6qFNFY_0mRnS6YbzrzWwegcfCY",
)


cloudinary.config(
  cloud_name = "moringa-kipkemoi",
  api_key = "583484295129265",
  api_secret = "iUp89baICJSY--PpsiI7aOIuGOg",
)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fndproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'fndproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'fnd',
        'USER': 'postgres',
        'HOST':'localhost',
        'PASSWORD': 'SEMBERUA',
        'PORT': '5432',
    'default':
     {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fnd',
        'USER': 'rachel',
    'PASSWORD':'hotspurs',
    }
  
}

# FOR GEODJANGO
POSTGIS_VERSION = (2, 4, 3)


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS =(
    os.path.join(BASE_DIR,'static'),
)

LEAFLET_CONFIG ={
    'DEFAULT_CENTER': (-0.23, 36.87), #KENYA
    'DEFAULT_ZOOM': 5,# ZOOM
    'MAX_ZOOM': 20,
    'MIN_ZOOM': 3,
    'SCALE': 'both', #imperial/metric
    'ATTRIBUTION_PREFIX':'Inspired By Life in Moringa School'
}


if os.name == 'nt':
    VENV_BASE = os.environ['VIRTUAL_ENV']
    os.environ['PATH'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo') + ';' + os.environ['PATH']
    os.environ['PROJ_LIB'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo\\data\\proj') + ';' + os.environ['PATH']



DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

cloudinary.config(
  cloud_name = "oyesa",
  api_key = "749352579693875",
  api_secret = "W6qFNFY_0mRnS6YbzrzWwegcfCY",
)

REST_FRAMEWORK = {
   'DEFAULT_AUTHENTICATION_CLASSES': (
       'rest_framework.authentication.TokenAuthentication',
   ),
   'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser'
   ),
}


