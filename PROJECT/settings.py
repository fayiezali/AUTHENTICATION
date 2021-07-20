"""
Django settings for PROJECT project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-naq&()wl+tjwb9z9xpd(mk@c!sbdg9uuqm650#c$viqtnjn($n'

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
# -------------------------------------------------------------------------------
    # تسجيل التطبيقات التي أنشأتها في المشروع
    'widget_tweaks', # 01 جميلة - التطبيق رقم  "Login.html"  هذا التطبيق وظيفته يجعل شكل صفحة
    'public_pages', # التطبيق رقم 02
    'accounts', # التطبيق رقم 03
    # 'django_countries',# تطبيق معد مسبقاً يحتوي على جميع اسماء دول العالم
# -------------------------------------------------------------------------------

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

ROOT_URLCONF = 'PROJECT.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        # 'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'PROJECT.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / "static"]# تحديد مسار الملف وهو الموقع الذي سوف يحبث  في المشروع عن هذا الملف
# '/media/':  الوسائط المتعددة"Media" بإدارة ملفات الـ "static" يقوم مجلد 
# '/media/': التي يحتاجها المشروع "Documents ,Images , Audio , Video,"هو مجلد  يتحوي على جميع ملفات 
# '/media/': يتم إستدعائها عن طريق هذا المجلد . هذاالمجلد فيه جميع إعدادت وتنسيقات الصفحة  "app"في التطبيق  "html"أي صفحة 
MEDIA_URL = '/media/'
MEDIA_ROOT = (BASE_DIR /'media')#تحديد مسار الملف وهو الموقع الذي سوف يحبث  في المشروع عن هذا الملف


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#
LOGIN_REDIRECT_URL = 'Index_URL' # Go To Home Page HTML
LOGOUT_REDIRECT_URL = 'My_LogoutDone_URL' # Go To LogoutDone.html Page HTML



EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' # mail service smtp
EMAIL_HOST_USER = 'fayiez1@gmail.com' # email id
EMAIL_HOST_PASSWORD = 'F050a636h1' #password
EMAIL_PORT = 587
EMAIL_USE_TLS = True
#
#
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
