from django.urls import path

from . import views

app_name = '{{cookiecutter.project_slug.lower()}}'
urlpatterns = [
    path('', views.cover, name='cover'),
    path('home/', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
]
