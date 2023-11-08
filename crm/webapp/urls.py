"""WebApp URL Configuration"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('register', views.register, name='register'),
    path('login', views.my_login, name='my-login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.user_logout, name='user-logout'),
]
