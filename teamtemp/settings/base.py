# Django settings for teamtemp project.
import os

from csp.constants import SELF, UNSAFE_INLINE
from django.urls import reverse_lazy

DEBUG = os.environ.get('DJANGO_DEBUG', False)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)

STATIC_BASE_DIR = os.environ.get('STATIC_BASE_DIR', BASE_DIR)
MEDIA_BASE_DIR = os.environ.get('MEDIA_BASE_DIR', BASE_DIR)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Australia/Brisbane'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(MEDIA_BASE_DIR, 'mediafiles')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(STATIC_BASE_DIR, 'staticfiles')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
#    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'teamtemp.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'teamtemp.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django_filters',
    'teamtemp.responses',
    'bootstrap3',
    'rest_framework',
    'crispy_forms',
    'crispy_bootstrap3',
    'csp',
    'csvexport',
    'drf_spectacular',
    'drf_spectacular_sidecar',
)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

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

# Do not require Authentication to render BVC when IGNORE_BVC_AUTH == True
IGNORE_BVC_AUTH = True

CRON_PIN = os.environ.get('TEAM_TEMP_CRON_PIN', '0000')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates').replace('\\', '/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Settings for django-bootstrap3
BOOTSTRAP3 = {
    'javascript_in_head': True,
    'jquery_url': '/static/jquery-3.6.3.min.js',
}

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_FRAME_DENY = True
X_FRAME_OPTIONS = 'DENY'

CONTENT_SECURITY_POLICY = {
    "EXCLUDE_URL_PREFIXES": ["/djadmin"],
    "DIRECTIVES": {
        "report-uri": 'https://1s0c2tfx-subdomain.uriports.com/reports/report',
        "default-src": [SELF],
        "script-src": [
            SELF,
            UNSAFE_INLINE,
            'code.jquery.com',
            'stackpath.bootstrapcdn.com',
            'cdnjs.cloudflare.com',
            'www.gstatic.com',
            'ssl.gstatic.com',
            'cdn.jsdelivr.net',
        ],
        "script-src-elmm": [
            SELF,
            UNSAFE_INLINE,
            'code.jquery.com',
            'www.gstatic.com',
            'ssl.gstatic.com',
            'www.google.com',
            'stackpath.bootstrapcdn.com',
        ],
        "connect-src": [SELF, 'stackpath.bootstrapcdn.com'],
        "style-src": [
            SELF,
            UNSAFE_INLINE,
            'code.jquery.com',
            'stackpath.bootstrapcdn.com',
            'www.gstatic.com',
            'ssl.gstatic.com',
            'cdn.jsdelivr.net',
            'fonts.googleapis.com',
        ],
        "style-src-elem": [
            SELF,
            UNSAFE_INLINE,
            'www.gstatic.com',
            'stackpath.bootstrapcdn.com',
        ],
        "img-src": [SELF, "data:", 'blob:', 'www.gstatic.com', 'ssl.gstatic.com'],
        "font-src": [
            SELF,
            "data:",
            'stackpath.bootstrapcdn.com',
            'fonts.gstatic.com',
            'fonts.googleapis.com',
            'cdnjs.cloudflare.com',
        ],
        "worker-src": [SELF, 'blob:'],
    },
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'PAGE_SIZE': 25,
}

LOGIN_URL = "/djadmin/login/"
LOGOUT_URL = "/djadmin/logout/"

WORDCLOUD_HEIGHT = 400
WORDCLOUD_WIDTH = 400

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap3"

CRISPY_TEMPLATE_PACK = "bootstrap3"

SPECTACULAR_SETTINGS = {
    'TITLE': 'Team Temperature API',
    'DESCRIPTION': 'Team Temperature API',
    'VERSION': '0.0.1',
    'SERVE_INCLUDE_SCHEMA': True,
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
}
