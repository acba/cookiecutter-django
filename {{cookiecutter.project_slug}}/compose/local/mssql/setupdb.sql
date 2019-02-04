IF db_id(N'BD_{{cookiecutter.project_slug.upper()}}') IS NULL
    CREATE DATABASE BD_{{cookiecutter.project_slug.upper()}};
GO
