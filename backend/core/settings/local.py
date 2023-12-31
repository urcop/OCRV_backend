from .base import *
import dj_database_url

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['http://localhost']
CORS_ALLOW_ALL_ORIGINS = True

DB_USER = environ.get('POSTGRES_USER')
DB_NAME = environ.get('POSTGRES_DB')
DB_PASSWORD = environ.get('POSTGRES_PASSWORD')
DB_HOST = environ.get('POSTGRES_HOST')
DB_PORT = 5432

ALL_DB = all([
    DB_PORT,
    DB_USER,
    DB_HOST,
    DB_PASSWORD,
    DB_NAME
])

if ALL_DB:
    DATABASES['default'] = dj_database_url.parse(f'postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

THIRD_PARTY = [
    'rest_framework',
    'ckeditor',
]

LOCAL_APPS = [
    'api',
    'news',
    'questions',
]


INSTALLED_APPS += THIRD_PARTY + LOCAL_APPS

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'core.renderers.UTF8CharsetJSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
}
