FROM python:3.7-slim-stretch

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y build-essential gcc python3-dev musl-dev

{% if cookiecutter.production_sgbd.lower() == 'mssql' %}

##
## Necessario para instalar os drivers para o SQL Server
##

RUN apt-get update \
    && apt-get install -y apt-utils curl apt-transport-https wget gnupg \
    # Pacote para o django-pyodbc-azure
    && apt-get install -y unixodbc unixodbc-dev

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update \
    && ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql17 unixodbc-dev \
    && ACCEPT_EULA=Y apt-get install -y --no-install-recommends mssql-tools


RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile \
    && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc \
    && /bin/bash -c "source ~/.bashrc"


{% elif cookiecutter.production_sgbd.lower() == 'postgres' %}

##
## Necessario para suporte ao Postgres
## https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
##

RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main' > /etc/apt/sources.list.d/pgdg.list \
    && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt-get update \
    && apt-get install -y postgresql-client-10 \
    # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
    && apt-get install -y libpq-dev

{% endif %}

RUN apt-get update \
    # psycopg2 dependencies
    && apt-get install -y build-essential gcc python3-dev musl-dev \
    # Git
    && apt-get install -y git \
    # Pillow dependencies
    && apt-get install -y libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libtiff-dev tk-dev tcl-dev \
    # CFFI dependencies
    && apt-get install -y libffi-dev \
    # Translations dependencies
    && apt-get install -y gettext \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN addgroup --system django
RUN adduser --system --group django

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/production.txt \
    && rm -rf /requirements


COPY --chown=django:django ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY --chown=django:django ./compose/production/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start


{% if cookiecutter.use_celery.lower() == 'y' %}
COPY --chown=django:django ./compose/production/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY --chown=django:django ./compose/production/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/production/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower
{% endif %}

COPY --chown=django:django . /app

USER django

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
