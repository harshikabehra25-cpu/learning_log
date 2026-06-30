"""Defines URL pattern for users"""

from django.urls import path 
from django.contrib.auth import views as auth_views 
from .import views

app_name = 'users'

urlpatterns = [
    # login
    path ('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    #logout
    path('logout/', views.logout_view, name='logout'),

    #registration
    path('register/', views.register, name='register'),
]