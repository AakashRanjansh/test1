import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta


load_dotenv()

DEBUG = True


BASE_DIR = Path(__file__).resolve().parent.parent

if DEBUG:
    ADMINS_EMAIL = ['sahaakashranjan@gmail.com']
else:
    ADMINS_EMAIL = ['subhakaarya77@gmail.com']

SECRET_KEY = "$fjka-secure-$6rbw73vq4&hiffkll7=7x&2#n%ew!z_!5mn=nv09bcz3!tfce"


if DEBUG:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.vercel.app']
else:
    ALLOWED_HOSTS = ['.subhakaarya.com', '.vercel.app']

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:5173',
    'http://localhost:5173',
]

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'subhakaarya777@gmail.com'
EMAIL_HOST_PASSWORD = 'hcphzbwueygxkktx'

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'subhakaarya_app',
    'account',
    'rest_framework',
    'corsheaders',
    "verify_email.apps.VerifyEmailConfig",
]
LOGIN_URL = "/subhakaarya/"
VERIFICATION_SUCCESS_TEMPLATE = None

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'subhakaarya.urls'

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

WSGI_APPLICATION = 'subhakaarya.wsgi.application'

DATABASES = {
    "default": {
        "CONN_MAX_AGE": 0,
        "ENGINE": "django.db.backends.sqlite3",
        "HOST": 'localhost',
        "NAME": 'db.sqlite3',
        "PASSWORD": '',
        "PORT": "",
        "USER": 'root',
    }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=2),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=5),
}

if DEBUG:
    STATIC_URL = 'static/'
else:
    STATIC_URL = "/static/"
    # STATICFILES_DIRS = [BASE_DIR/"static"]
    STATIC_ROOT = "/home/subhakaa/api/static"

    MEDIA_URL = "/media/"
    MEDIA_ROOT = "/home/subhakaa/api/media"

JAZZMIN_SETTINGS = {
    "site_title": "Subhakaarya.com",
    "site_brand": "Subhakaarya.com",
    # Add your own branding here
    "welcome_sign": "Welcome to Subhakaarya.com",
    # Copyright on the footer
    "copyright": "Subhakaarya.com",
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    # "topmenu_links": [
    #     # Url that gets reversed (Permissions can be added)
    #     {"name": "Subhakaarya.com", "url": "home", "permissions": ["auth.view_user"]},
    #     # model admin to link to (Permissions checked against model)
    #     {"model": "auth.User"},
    # ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    "hide_apps": ['auth'],
    "order_with_respect_to": ['subhakaarya_app.Event', 'subhakaarya_app.Service', 'subhakaarya_app.Plan'],
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "users.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "admin.LogEntry": "fas fa-file",
    },
    # # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-arrow-circle-right",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    # Uncomment this line once you create the bootstrap-dark.css file
    # "custom_css": "css/bootstrap-dark.css",
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
    ###############
    # Change view #
    ###############
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
}
