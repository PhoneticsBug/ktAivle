# blog/urls.py
from django.urls import path
from . import views

app_name = 'alphabet_to_video'
urlpatterns = [
    path('', views.index, name='index'),
]
