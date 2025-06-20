"""
Django settings for Blogproject project.

Generated by 'django-admin startproject' using Django 5.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""
import os
from pathlib import Path
import cloudinary_storage

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s32y#n@@t_k0cbmh4w_!n3+n+=!2t$tj^yc&gzxad*p$9vv3_y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*','localhost','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'tinymce',
    'home.apps.HomeConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
   
]

ROOT_URLCONF = 'Blogproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Blogproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

ROOT_URLCONF = 'Blogproject.urls'

MEDIA_URL='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# settings.py

# ... (your existing settings) ...

# TinyMCE configuration
TINYMCE_JS_URL = "https://cdn.tiny.cloud/1/hweiihzp6ripv6m0b5r8qz29a9bplj1qh2flqnrh3t8dnxjj/tinymce/7/tinymce.min.js" # MAKE SURE TO REPLACE YOUR_API_KEY

TINYMCE_DEFAULT_CONFIG = {
    "height": 500,
    "width": "100%",
    "menubar": "file edit insert view format tools table help",
    "plugins": (
        "advlist", "autolink", "lists", "link", "image", "charmap", "preview",
        "anchor", "searchreplace", "visualblocks", "codesample", "fullscreen",
        "insertdatetime", "media", "table", "code", "help", "wordcount", "emoticons"
    ),
    "toolbar": (
        "undo redo | blocks fontfamily fontsize | "
        "bold italic underline strikethrough forecolor backcolor | "
        "alignleft aligncenter alignright alignjustify | lineheight | "
        "numlist bullist indent outdent | "
        "link image media table | "
        "emoticons charmap codesample | "
        "anchor visualblocks | "
        "searchreplace fullscreen preview print | "
        "insertdatetime | help wordcount | removeformat code"
    ),
    "custom_undo_redo_levels": 10,
    "branding": False,
    "skin": "oxide-dark",
    "content_css": "dark",
}


CLOUDINARY_CLOUD_NAME = os.environ.get('MY_CLOUDINARY_CLOUD_NAME')
CLOUDINARY_API_KEY = os.environ.get('MY_CLOUDINARY_API_KEY')       
CLOUDINARY_API_SECRET = os.environ.get('MY_CLOUDINARY_API_SECRET')

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}