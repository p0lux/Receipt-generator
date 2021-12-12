from django.contrib.auth.urls import views as auth_views
from django.urls import path, include
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home')
]
