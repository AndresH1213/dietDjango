from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('register/', views.registerUser, name='register')
]