from multiprocessing import cpu_count
from os import environ

PORT = environ.get('DJANGO_PORT')


def max_workers():
    return cpu_count()


command = '/usr/local/bin/gunicorn'
pythonpath = '/usr/local/bin/python'
bind = f'0.0.0.0:{PORT}'
workers = max_workers()
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=core.settings.local'
