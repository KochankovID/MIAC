import os
from datetime import timedelta
from pathlib import Path

import environ

env = environ.Env()
environ.Env.read_env(".env")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")

ALLOWED_HOSTS = []

INTERNAL_IPS = [
    '127.0.0.1',
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    'django_extensions',
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "allauth",
    "allauth.account",
    "dj_rest_auth.registration",
    "rest_framework_simplejwt.token_blacklist",
    "phonenumber_field",
    "drf_yasg",
    "corsheaders",
    "debug_toolbar",
    "users",
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "miac.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "miac.wsgi.application"

DATABASES = {
    "default": env.db(),
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME":
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME":
            "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME":
            "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME":
            "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

PHONENUMBER_DB_FORMAT = "NATIONAL"
PHONENUMBER_DEFAULT_REGION = "RU"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES":
        ("rest_framework_simplejwt.authentication.JWTAuthentication",)
}

AUTH_USER_MODEL = "users.User"
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "users.serializers.RegisterSerializer"
}

REST_USE_JWT = True
JWT_AUTH_COOKIE = "miac-auth"
JWT_AUTH_REFRESH_COOKIE = "miac-refresh"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE":
        "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

CACHES = {
    "default": env.cache("REDIS_URL"),
    "sessions": env.cache("REDIS_SESSION_URL")
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "sessions"

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

CORS_ORIGIN_ALLOW_ALL = True
