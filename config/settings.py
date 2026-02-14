from pathlib import Path
import os
import dj_database_url

ALLOWED_HOSTS = [
    "mysite-production-0e1f2.up.railway.app",
    "web-createsuperuser-true.up.railway.app",
]

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-fallback-key"
)

DEBUG = True
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'users',          # ← ★これでOK（apps指定しない）
    'blog',

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,
    )
}

STATIC_URL = "/static/"
STATICFILES_DIRS = []
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

print("=== Django settings loaded ===")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = "no-reply@yourdomain.com"

# ==============================
# Stripe settings (FORCE LOAD)
# ==============================
import os

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_PRICE_ID = os.getenv("STRIPE_PRICE_ID", "")
STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY", "")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "")

STRIPE_ENABLED = bool(STRIPE_SECRET_KEY and STRIPE_PRICE_ID)

print(">>> STRIPE SETTINGS LOADED <<<")
print("PRICE =", repr(STRIPE_PRICE_ID))
print("ENABLED =", STRIPE_ENABLED)
# FORCE_GIT_CHANGE

LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/premium/"
LOGOUT_REDIRECT_URL = "/accounts/login/"

CSRF_TRUSTED_ORIGINS = [
    "https://mysite-production-0e1f2.up.railway.app",
    "https://web-createsuperuser-true.up.railway.app",
]

MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

import os

if os.environ.get("RAILWAY_ENVIRONMENT"):
    os.environ.setdefault("DJANGO_SUPERUSER_USERNAME", "adminrail")
    os.environ.setdefault("DJANGO_SUPERUSER_PASSWORD", "Admin12345")
    os.environ.setdefault("DJANGO_SUPERUSER_EMAIL", "adminrail@example.com")
