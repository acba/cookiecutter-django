from .base import *
from .base import env


# GENERAL
# ------------------------------------------------------------------------------
SECRET_KEY = env('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['{{ cookiecutter.domain_name }}'])


# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL regex.
ADMIN_URL = env('DJANGO_ADMIN_URL')


# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = env.bool('DJANGO_SECURE_SSL_REDIRECT', default=True)
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool('DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True)
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = env.bool('DJANGO_SECURE_HSTS_PRELOAD', default=True)
# https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = env.bool('DJANGO_SECURE_CONTENT_TYPE_NOSNIFF', default=True)


# Gunicorn
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['gunicorn']  # noqa F405


{% if cookiecutter.production_sgbd.lower() == 'mssql' -%}
##
## SQL SERVER
##

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': env('MSSQL_DB'),
        'USER': env('MSSQL_USER'),
        'PASSWORD': env('MSSQL_PASSWORD'),
        'HOST': env('MSSQL_HOST'),
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}

{%- endif %}


{% if cookiecutter.local_sgbd.lower() == 'postgres' -%}

DATABASES = {
    'default': env.db('DATABASE_URL'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

{%- endif %}
