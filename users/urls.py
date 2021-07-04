from django.urls import path
from django.contrib.auth import logout

from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', logout, name="logout"),
]
