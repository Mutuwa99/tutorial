from django.urls import path
from . import views


urlpatterns = [
    path('auth/login', views.welcome, name="auth/login"),
    path('dashboard', views.dashboard, name="dashboard"),
]
