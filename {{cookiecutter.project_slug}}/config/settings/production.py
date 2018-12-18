from .base import *
from .base import env


# GENERAL
# ------------------------------------------------------------------------------
SECRET_KEY = env('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['{{ cookiecutter.domain_name }}'])
