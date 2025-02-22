from django.urls import path
from django.contrib import admin
from .views import (register_view, logout_view, login_view)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
