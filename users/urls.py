from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('profile-information/', views.editProfile, name='profile-information'),
    path('profile/', views.profile, name='profile')
]